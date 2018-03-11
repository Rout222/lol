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
import sys

tempototal = time.clock()
def getKey(item):
	return item['value']
line = {}
nodes = []
for x,y in champs.champs.items():
	line[x] = {'id' : x ,'name' : y[1], 'count' : 0, 'win' : 0, 'ganhoucontra' : 0, 'jogoucontra' : 0}
	nodes.append({"id" : y[1], "group" : 1, 'url' : y[2], 'uid' : x})
matrix = copy.deepcopy(line)
for x,y in matrix.items():
	del matrix[x]['count']
	matrix[x]['list'] = copy.deepcopy(line)
db=MySQLdb.connect(passwd="",db="leagueoflegends", user="root")
c=db.cursor()
filename = os.getcwd().replace("\\","/")+"/querydump.csv"
c.execute("""
	SELECT 
		id, match_id, kills, deaths, assists, win, champ_id, lane, player_id, platform, type 
	from 
		players 
	where 
		type in (420,440) 
	INTO OUTFILE '{}' 
	FIELDS TERMINATED BY ',' 
	OPTIONALLY ENCLOSED BY '\"' 
	LINES TERMINATED BY '\n';
	""".format(filename))
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
				if(x[6] != y[6]):
					if(x[5] == y[5]):
						if(int(x[5]) == 1):
							matrix[int(x[6])]['list'][matrix[int(y[6])]['id']]['win'] += 1	
							matrix[int(y[6])]['list'][matrix[int(x[6])]['id']]['win'] += 1
						matrix[int(x[6])]['list'][matrix[int(y[6])]['id']]['count'] += 1	
						matrix[int(y[6])]['list'][matrix[int(x[6])]['id']]['count'] += 1
					else:
						matrix[int(x[6])]['list'][matrix[int(y[6])]['id']]['jogoucontra'] += 1	
						matrix[int(y[6])]['list'][matrix[int(x[6])]['id']]['jogoucontra'] += 1
						if(int(x[5]) == 1):
							matrix[int(x[6])]['list'][matrix[int(y[6])]['id']]['ganhoucontra'] += 1
						else:
							matrix[int(y[6])]['list'][matrix[int(x[6])]['id']]['ganhoucontra'] += 1
			elif(found):
				break;

c.execute("TRUNCATE arcs;")
with click.progressbar(matrix.items(), label='Fazendo filtros, e ligações') as bar:
	for _,x in bar:
		for _, y in x['list'].items():
			if(y['count'] > 0 and y['jogoucontra'] > 0 and y['ganhoucontra'] > 0):
				c.execute("INSERT INTO `arcs`(`source_id`, `target_id`, `value`, `win`,`jogoucontra`,`ganhoucontra`) VALUES (\"{}\",\"{}\",\"{}\",{},\"{}\",\"{}\")".format(x['id'],y['id'],y['count'],(y['win']/(y['count']+1)),y['jogoucontra'],y['ganhoucontra']))
db.commit()
db.close()
file.close()
os.remove("querydump.csv")

print("Algoritmo rodou em {}s".format(round((time.clock() - tempototal),2)))
