import click
import json
import time
import threading
import csv
import copy
from glob import glob

champs = {
	62: "MonkeyKing",
	24: "Jax",
	9: "Fiddlesticks",
	35: "Shaco",
	19: "Warwick",
	498: "Xayah",
	76: "Nidalee",
	143: "Zyra",
	240: "Kled",
	63: "Brand",
	33: "Rammus",
	420: "Illaoi",
	42: "Corki",
	201: "Braum",
	122: "Darius",
	23: "Tryndamere",
	21: "MissFortune",
	83: "Yorick",
	101: "Xerath",
	15: "Sivir",
	92: "Riven",
	61: "Orianna",
	41: "Gangplank",
	54: "Malphite",
	78: "Poppy",
	30: "Karthus",
	126: "Jayce",
	20: "Nunu",
	48: "Trundle",
	104: "Graves",
	142: "Zoe",
	150: "Gnar",
	99: "Lux",
	102: "Shyvana",
	58: "Renekton",
	114: "Fiora",
	222: "Jinx",
	429: "Kalista",
	105: "Fizz",
	38: "Kassadin",
	37: "Sona",
	39: "Irelia",
	112: "Viktor",
	497: "Rakan",
	203: "Kindred",
	69: "Cassiopeia",
	57: "Maokai",
	516: "Ornn",
	412: "Thresh",
	10: "Kayle",
	120: "Hecarim",
	121: "Khazix",
	2: "Olaf",
	115: "Ziggs",
	134: "Syndra",
	36: "DrMundo",
	43: "Karma",
	1: "Annie",
	84: "Akali",
	106: "Volibear",
	157: "Yasuo",
	85: "Kennen",
	107: "Rengar",
	13: "Ryze",
	98: "Shen",
	154: "Zac",
	91: "Talon",
	50: "Swain",
	432: "Bard",
	14: "Sion",
	67: "Vayne",
	75: "Nasus",
	141: "Kayn",
	4: "TwistedFate",
	31: "Chogath",
	77: "Udyr",
	236: "Lucian",
	427: "Ivern",
	89: "Leona",
	51: "Caitlyn",
	113: "Sejuani",
	56: "Nocturne",
	26: "Zilean",
	268: "Azir",
	68: "Rumble",
	25: "Morgana",
	163: "Taliyah",
	17: "Teemo",
	6: "Urgot",
	32: "Amumu",
	3: "Galio",
	74: "Heimerdinger",
	34: "Anivia",
	22: "Ashe",
	161: "Velkoz",
	27: "Singed",
	72: "Skarner",
	110: "Varus",
	29: "Twitch",
	86: "Garen",
	53: "Blitzcrank",
	11: "MasterYi",
	60: "Elise",
	12: "Alistar",
	55: "Katarina",
	245: "Ekko",
	82: "Mordekaiser",
	117: "Lulu",
	164: "Camille",
	266: "Aatrox",
	119: "Draven",
	223: "TahmKench",
	80: "Pantheon",
	5: "XinZhao",
	136: "AurelionSol",
	64: "LeeSin",
	44: "Taric",
	90: "Malzahar",
	127: "Lissandra",
	131: "Diana",
	18: "Tristana",
	421: "RekSai",
	8: "Vladimir",
	59: "JarvanIV",
	267: "Nami",
	202: "Jhin",
	16: "Soraka",
	45: "Veigar",
	40: "Janna",
	111: "Nautilus",
	28: "Evelynn",
	79: "Gragas",
	238: "Zed",
	254: "Vi",
	96: "KogMaw",
	103: "Ahri",
	133: "Quinn",
	7: "Leblanc",
	81: "Ezreal",}
tempototal = time.clock()
def getKey(item):
	return item['value']
line = {}
nodes = []
for x,y in champs.items():
	line[x] = {'id' : x ,'name' : y, 'count' : 0, 'win' : 0}
	nodes.append({"id" : y, "group" : 1})
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
list_com_no_minimo = [num for num in l if (num['win'] < 0.4) and (num['value'] > 50)]
output = open('E:/xampp/htdocs/laerte/output.json', 'w')
j = {"nodes" : nodes, "links" : list_com_no_minimo}
json.dump(j, output, ensure_ascii=False)
print("Algoritmo rodou em {}s".format(round((time.clock() - tempototal),2)))
