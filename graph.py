import click
import json
import time
import threading
import csv
import copy
from glob import glob
import MySQLdb
import champs
import os
tempototal = time.clock()
def getKey(item):
	return item['value']
line = {}
nodes = []
for x,y in champs.champs.items():
	line[x] = {'id' : x ,'name' : y[1], 'count' : 0, 'win' : 0}
	nodes.append({"id" : y[1], "group" : 1, 'url' : y[2], 'uid' : x})
matrix = copy.deepcopy(line)
for x,y in matrix.items():
	del matrix[x]['count']
	matrix[x]['list'] = copy.deepcopy(line)
db=MySQLdb.connect(passwd="",db="leagueoflegends", user="root")
c=db.cursor()
os.remove("querydump.csv")
c.execute("""
SELECT id, match_id, kills, deaths, assists, win, champ_id, lane, player_id, platform, type from players 
where type = 420
INTO OUTFILE 'E:/escola/lol/querydump.csv' 
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"' 
LINES TERMINATED BY '\n';
	""")
file = open('querydump.csv', newline='', encoding='utf-8')
reader = csv.reader(file)
line = []
for x in reader:
	line.append(x)
last = 0
with click.progressbar(line, label='Calculando dados brutos') as bar:
	for i,x in enumerate(bar):
		found = False
		for y in line[last:]:
			if(x[1] == y[1]):
				last = i
				found = True
				if(x[5] == y[5] and x[6] != y[6] ):
					if(int(x[5]) == 1):
						matrix[int(x[6])]['list'][matrix[int(y[6])]['id']]['win'] += 1	
						matrix[int(y[6])]['list'][matrix[int(x[6])]['id']]['win'] += 1
					matrix[int(x[6])]['list'][matrix[int(y[6])]['id']]['count'] += 1	
					matrix[int(y[6])]['list'][matrix[int(x[6])]['id']]['count'] += 1
			elif(found):
				break;

list_final = []
c.execute("TRUNCATE arcs;")
with click.progressbar(matrix.items(), label='Fazendo filtros, e ligações') as bar:
	for _,x in bar:
		for _, y in x['list'].items():
			if(y['count'] > 0 ):
				list_final.append({"source_id" : x['id'], "target_id" : y['id'] ,"source" : x['name'], "target" : y['name'], "win" : y['win']/y['count'],"value" : y['count']})
				c.execute("INSERT INTO `arcs`(`source_id`, `target_id`, `value`, `win`) VALUES (\"{}\",\"{}\",\"{}\",{})".format(x['id'],y['id'],y['count'],(y['win']/(y['count']+1))))
db.commit()
db.close()
list_final = sorted(list_final, key=getKey, reverse=True)
list_final = [num for num in list_final if (num['win'] > 0.6) and (num['value'] > 50)]
not_remove = []

for x in list_final:
	not_remove.append(x['source'])

filtered_nodes = []
with click.progressbar(nodes, label='Fazendo filtros, e removendo') as bar:
	for x in bar:
		if(not_remove.count(x['id']) > 0):
			filtered_nodes.append(x)


output = open('./static/output.json', 'w')
j = {"nodes" : filtered_nodes, "links" : list_final}
json.dump(j, output, ensure_ascii=False)

print("Algoritmo rodou em {}s".format(round((time.clock() - tempototal),2)))
