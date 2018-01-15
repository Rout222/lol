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
	nodes.append({"id" : y[1], "group" : 1, 'url' : y[2], 'uid' : x})
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
with click.progressbar(matrix.items(), label='Fazendo filtros, e ligações') as bar:
	for _,x in bar:
		for _, y in x['list'].items():
			if(y['count'] > 0 ):
				list_final.append({"source_id" : x['id'], "target_id" : y['id'] ,"source" : x['name'], "target" : y['name'], "win" : y['win']/y['count'],"value" : y['count']})


l = sorted(list_final, key=getKey, reverse=True)
list_com_no_minimo = [num for num in l if (num['win'] > 0.6) and (num['value'] > 50)]

not_remove = []
paj_arcs = []
for x in list_com_no_minimo:
	not_remove.append(x['source'])
	paj_arcs.append([x['source_id'], x['target_id'], x['win']])

filtered_nodes = []
paj_nodes = []
with click.progressbar(nodes, label='Fazendo filtros, e removendo') as bar:
	for x in bar:
		if(not_remove.count(x['id']) > 0):
			filtered_nodes.append(x)
			paj_nodes.append([x['uid'], x['id']])
output = open('./static/output.json', 'w')
paj_output = open('./static/paj.paj', 'w')
paj_text = "*Vertices {}".format(len(filtered_nodes)+1)
for x in paj_nodes:
	paj_text += "\n\t{}\t\"{}\"".format(x[0],x[1])
paj_text += "\n*arcs"
for x in paj_arcs:
	paj_text += "\n\t{}\t{}\t{}".format(x[0],x[1],x[2])

paj_output.write(paj_text)
j = {"nodes" : filtered_nodes, "links" : list_com_no_minimo}
json.dump(j, output, ensure_ascii=False)
print("Algoritmo rodou em {}s".format(round((time.clock() - tempototal),2)))
