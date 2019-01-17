import mysql.connector
import time
import threading

class predict(threading.Thread):
	"""docstring for threadin"""
	def __init__(self, ids, index, step):
		threading.Thread.__init__(self)
		self.ids = ids
		self.index = index
		self.step = step
		self.bd = mysql.connector.connect(passwd="",db="lol_kaggle", user="root")
		self.cursor = self.bd.cursor()

	def	cleanup_stop_thread(self):
		self.bd.close()
	
	def salva(self, dados, matchid):
		self.cursor.execute("INSERT INTO `predict`(`p1ep2`, `p1ep3`, `p1ep4`, `p1ep5`, `p1vp6`, `p1vp7`, `p1vp8`, `p1vp9`, `p1vp10`, `p2ep3`, `p2ep4`, `p2ep5`, `p2vp6`, `p2vp7`, `p2vp8`, `p2vp9`, `p2vp10`, `p3ep4`, `p3ep5`, `p3vp6`, `p3vp7`, `p3vp8`, `p3vp9`, `p3vp10`, `p4ep5`, `p4vp6`, `p4vp7`, `p4vp8`, `p4vp9`, `p4vp10`, `p5vp6`, `p5vp7`, `p5vp8`, `p5vp9`, `p5vp10`, `p6ep7`, `p6ep8`, `p6ep9`, `p6ep10`, `p7ep8`, `p7ep9`, `p7ep10`, `p8ep9`, `p8ep10`, `p9ep10`, `timevencedor`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", dados)
		self.cursor.execute("UPDATE `players` SET `processado`= 1 WHERE `match_id` = {}".format(matchid))
		self.bd.commit()

	def run(self):
		while True:
			for x in range(self.index, len(self.ids), self.step):
				matchid = self.ids[x][0]
				self.cursor.execute("SELECT `champ_id`, `win` FROM `players` WHERE `match_id` = {}".format(matchid))
				herois = self.cursor.fetchall()
				dados = []
				if (len(herois) == 10):
					for i, h1 in enumerate(herois):
						for h2 in herois[i:]:
							if (h1[0] != h2[0]):
								sql = "SELECT value, ganhoujunto, ganhoucontra, jogoucontra FROM `arcs` WHERE `source_id` = {} and `target_id` = {}".format(h1[0],h2[0])
								self.cursor.execute(sql)
								valores = self.cursor.fetchall()[0]
								if h1[1] == h2[1]:
									dados.append(valores[1]/valores[0])
								else:
									dados.append(valores[2]/valores[3])
				dados.append(int(herois[0][1] == 1))
				self.salva(dados, matchid)

db=mysql.connector.connect(passwd="",db="lol_kaggle", user="root")
c=db.cursor()
c.execute("SELECT DISTINCT(`match_id`) FROM `players` WHERE processado = 0")
quantidade = c.fetchall()

start = time.clock()
threadG = []
nThreads = 7
for x in range(0, nThreads):
	threadG.append(predict(quantidade, x, nThreads))
for x in threadG:
	x.start()
while True:
	if((time.clock() - start) % 10 == 0):
		c.execute("SELECT ((count(*)*100)/(SELECT count(*) FROM `players` WHERE 1)) FROM `players` WHERE `processado` = 1")
		concluido = c.fetchall()[0][0]
		print("Rodando à {}s, {} %  concluido".format(round(time.clock() - start),round(concluido)))