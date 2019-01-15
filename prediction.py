import mysql.connector

import click

db=mysql.connector.connect(passwd="",db="lol_kaggle", user="root")
c=db.cursor()
c.execute("SELECT DISTINCT(`match_id`) FROM `players`")
quantidade = c.fetchall()
ids = []

print("p1ep2,p1ep3,p1ep4,p1ep5,p1vp6,p1vp7,p1vp8,p1vp9,p1vp10,p2ep3,p2ep4,p2ep5,p2vp6,p2vp7,p2vp8,p2vp9,p2vp10,p3ep4,p3ep5,p3vp6,p3vp7,p3vp8,p3vp9,p3vp10,p4ep5,p4vp6,p4vp7,p4vp8,p4vp9,p4vp10,p5vp6,p5vp7,p5vp8,p5vp9,p5vp10,p6ep7,p6ep8,p6ep9,p6ep10,p7ep8,p7ep9,p7ep10,p8ep9,p8ep10,p9ep10,timevencedor")
with click.progressbar(quantidade, label='Calculando dados brutos') as bar:
	for matchid in bar:
		c.execute("SELECT `champ_id`, `win` FROM `players` WHERE `match_id` = {}".format(matchid[0]))
		herois = c.fetchall()
		linha = ""
		if (len(herois) == 10):
			for i, h1 in enumerate(herois):
				for h2 in herois[i:]:
					if (h1[0] != h2[0]):
						sql = "SELECT value, ganhoujunto, ganhoucontra, jogoucontra FROM `arcs` WHERE `source_id` = {} and `target_id` = {}".format(h1[0],h2[0])
						c.execute(sql)
						valores = c.fetchall()[0]
						if h1[1] == h2[1]:
							linha += "{},".format(valores[1]/valores[0])
						else:
							linha += "{},".format(valores[2]/valores[3])
		linha += "{}".format(int(herois[0][1] == 1))
		print(linha)