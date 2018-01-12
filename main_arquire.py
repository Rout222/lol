import json
import requests
import MySQLdb
import time
import threading
from glob import glob
start = 0
tentativas = 0
line_inserteds = 0
last_change = 0
api_usada = 0
api = threading.Lock()
match = threading.Lock()
debug = False
class getter(threading.Thread):
	"""docstring for threadin"""
	def __init__(self, id):
		threading.Thread.__init__(self)
		self.id = id
		self.sequence = False
	def run(self):
		global tentativas
		while True:
			url = 'https://br1.api.riotgames.com/lol/match/v3/matches/{}?api_key={}'.format(get_next_match_id(self.id),get_api_key())
			request = requests.get(url)
			tentativas += 1
			if request.status_code == 429:
				change_api_key(int(request.headers['Retry-After']), self.sequence)
				self.sequence = True
			elif (request.status_code == 404):
				self.sequence = False
				if debug:
					print("Match_id não existe, incrementando id ,{}".format(request.status_code))
				add_next_match_id(self.id)
			elif request.status_code == 200:
				self.sequence = False
				if debug:
					print("achou")
				data = json.loads(request.content)
				players = []
				for player in data['participants']:
					try:
						players.append((
							data['gameId'],
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
						if debug:
							print("{} tem algo de errado".format(self.id))
				add_next_match_id(self.id)
				save_data(players)
			else:
				if debug:
					print("Algo diferente aconteceu{}, verifique nesta url {}".format(request.status_code,'https://br1.api.riotgames.com/lol/match/v3/matches/{}?api_key={}'.format(get_next_match_id(self.id),get_api_key())))


def add_next_match_id(line):
	match.acquire()
	file = open('match_id.txt', 'r')
	matchs = file.readlines()
	file.close()
	file = open('match_id.txt', 'w')
	matchs[line] = str(int(matchs[line]) + 1) + '\n'
	for x in matchs:
		file.write(str(x))
	file.close()
	match.release()

def get_next_match_id(line):
	match.acquire()
	file = open('match_id.txt', 'r')
	matchs = file.readlines()
	match_id = int(matchs[line]) + 1
	file.close()
	match.release()
	return match_id

def save_data(data):
	db=MySQLdb.connect(passwd="",db="leagueoflegends", user="root")
	c=db.cursor()
	global line_inserteds
	line_inserteds += 1
	c.executemany("""INSERT INTO `players`(`match_id`, `kills`, `deaths`, `assists`, `win`, `champ_id`, `lane`, `player_id`, `platform`, `type`) VALUES  (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",data)
	db.commit()
	db.close()

def get_api_key():
	api.acquire()
	file = open('api.txt', 'r')
	apis = file.readlines()
	file.close()
	key = apis[api_usada%len(apis)]
	api.release()
	return key.rstrip()

def change_api_key(sleep, sequence):
	global api_usada
	global last_change
	if((time.clock() - last_change) > 15):
		print("Limite atingindo, trocando de API_KEY")
		api.acquire()
		last_change = time.clock()
		api_usada += 1
		api.release()
	elif(sequence):
		print("Limite atingindo, dormindo {}".format(sleep))
		time.sleep(sleep)

start = time.clock()
last_change = time.clock() - 100
threadG = []
for x in range(0,6):
	threadG.append(getter(x))

for x in threadG:
	x.start()

# for x in threadG:
# 	x.join()

while True:
	if((time.clock() - start) % 10 == 0):
		print("Rodando à {}s ,Média de inserções é de {}/s e Média de tentativas {}/s".format(round(time.clock() - start),round(line_inserteds/(time.clock() - start),2),round(tentativas/(time.clock() - start),2)))
