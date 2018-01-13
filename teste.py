import json
import requests
import MySQLdb
import time
import threading
from glob import glob
inseridos = 0
key = 'RGAPI-daf9cd0c-51c8-481e-842c-97f3437ea0d3'
def get_match_id(id):
	global inseridos
	request = requests.get('https://br1.api.riotgames.com/lol/match/v3/matches/{}?api_key={}'.format(id,key))
	while(request.status_code == 429):
		print("Esperando {}s".format(request.headers['Retry-After']))
		print("\t Total de {} linhas inseridas".format(inseridos))
		time.sleep(int(request.headers['Retry-After']))
		request = requests.get('https://br1.api.riotgames.com/lol/match/v3/matches/{}?api_key={}'.format(id,key))
	if request.status_code == 200:
		data = json.loads(request.content)
		players = []
		for player in data['participants']:
			try:
				players.append((
					id,
					player['stats']['kills'],
					player['stats']['deaths'],
					player['stats']['assists'],
					player['stats']['win']*1,
					player['championId'],
					player['timeline']['lane'],
					data['participantIdentities'][player['participantId']-1]['player']['summonerId'],
					data['platformId'],
					data['queueId']
					))
			except Exception as e:
				print("{} tem algo de errado".format(id))
				# pass
		save_data(players)
		
	else:
		# pass
		print("{} nao existe".format(id))

def save_data(data):
	global inseridos
	db=MySQLdb.connect(passwd="",db="leagueoflegends", user="root")
	c=db.cursor()
	c.executemany("""INSERT INTO `players`(`match_id`, `kills`, `deaths`, `assists`, `win`, `champ_id`, `lane`, `player_id`, `platform`, `type`) VALUES  (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",data)
	db.commit()
	inseridos += 1
	db.close()

def initial():
	players = []
	for x in range(11,11):
		name = 'matches{}.json'.format(x)
		if(not glob(name)):
			print("{} não existe, baixando".format(name))
			request = requests.get('https://s3-us-west-1.amazonaws.com/riot-developer-portal/seed-data/{}'.format(name))
			if request.status_code == 200:
				f = open(name, 'w')
				f.write(request.text)
				f.close()
				print("{} baixado e salvo".format(name))
		print(name)
		f = open(name, 'r')
		data = json.loads(f.read())
		for matches in data['matches']:
			for player in matches['participants']:
				players.append((
					matches['gameId'],
					player['stats']['kills'],
					player['stats']['deaths'],
					player['stats']['assists'],
					player['stats']['win']*1,
					player['championId'],
					player['timeline']['lane'],
					matches['participantIdentities'][player['participantId']-1]['player']['summonerId'],
					matches['platformId'],
					matches['queueId']
					))
		save_data(players)
# initial()
ultimoLido = 0
def th1():
	while True:
		f1 = open('ultimolido1.txt', 'r')
		ultimoLido = int(f1.read()) + 1
		f1.close()
		get_match_id(ultimoLido)
		f1 = open('ultimolido1.txt', 'w')
		f1.write(str(ultimoLido))
		f1.close()
def th2():
	while True:
		f2 = open('ultimolido2.txt', 'r')
		ultimoLido = int(f2.read()) + 1
		f2.close()
		get_match_id(ultimoLido)
		f2 = open('ultimolido2.txt', 'w')
		f2.write(str(ultimoLido))
		f2.close()
def th3():
	while True:
		f3 = open('ultimolido3.txt', 'r')
		ultimoLido = int(f3.read()) + 1
		f3.close()
		get_match_id(ultimoLido)
		f3 = open('ultimolido3.txt', 'w')
		f3.write(str(ultimoLido))
		f3.close()
def th4():
	while True:
		f4 = open('ultimolido4.txt', 'r')
		ultimoLido = int(f4.read()) + 1
		f4.close()
		get_match_id(ultimoLido)
		f4 = open('ultimolido4.txt', 'w')
		f4.write(str(ultimoLido))
		f4.close()

t1 = threading.Thread(target=th1)
t2 = threading.Thread(target=th2)
t3 = threading.Thread(target=th3)
t4 = threading.Thread(target=th4)
init = threading.Thread(target=initial)
t1.start()
t2.start()
t3.start()
t4.start()
init.start()
t1.join()
t2.join()
t3.join()
t4.join()
init.join()