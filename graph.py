import click
import json
import time
import threading
import csv
import copy
from glob import glob
import champs
tempototal = time.clock()
def getKey(item):
	return item['value']
line = {}
nodes = []
for x,y in champs.champs.items():
	line[x] = {'id' : x ,'name' : y[1], 'count' : 0, 'win' : 0}
	nodes.append({"id" : y[1], "group" : 1, 'url' : y[2]})
matrix = copy.deepcopy(line)
for x,y in matrix.items():
	del matrix[x]['count']
	matrix[x]['list'] = copy.deepcopy(line)
file = open('querydump.csv', newline='', encoding='utf-8')
reader = csv.reader(file)
line = []
for x in reader:
	line.append(x)
last = 0
with click.progressbar(line, label='Progresso') as bar:
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
for _,x in matrix.items():
	for _, y in x['list'].items():
		if(y['count'] > 0 ):
			list_final.append({"source" : x['name'], "target" : y['name'], "win" : y['win']/y['count'],"value" : y['count']})

l = sorted(list_final, key=getKey, reverse=True)
list_com_no_minimo = [num for num in l if (num['win'] > 0.6) and (num['value'] > 50)]
output = open('./static/output.json', 'w')
j = {"nodes" : nodes, "links" : list_com_no_minimo}
json.dump(j, output, ensure_ascii=False)
print("Algoritmo rodou em {}s".format(round((time.clock() - tempototal),2)))
