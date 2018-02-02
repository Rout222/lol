import MySQLdb
f = open("querydump.csv")
db=MySQLdb.connect(passwd="",db="leagueoflegends", user="root")
c=db.cursor()
for x in f:
	c.execute("INSERT INTO `players`(`id`, `match_id`, `kills`, `deaths`, `assists`, `win`, `champ_id`, `lane`, `player_id`, `platform`, `type`) VALUES ({})".format(x))
db.commit()
db.close()