from flask import Flask, render_template, request,jsonify, Markup
import MySQLdb
import json
import sys
import re
import champs
import igraph
v = []
# print(len(request.form), file=sys.stderr)
app = Flask(__name__)
v=[2,3,4,8,9,14,17,22,24,31,32,39,41,46,51,52,54,56,58,61,63,71,72,80,89,92,96,101,106,109,111,114,117,120,121,123,125,126,133,136,139,1,12,16,20,30,34,37,53,75,76,81,91,105,107,113]
@app.route("/", methods = ['GET', 'POST'])
def hello():
	json_file = get_json(request.form) if len(request.form) > 0 else get_json([])
	if(len(json_file) > 1):
		init_igraph()
	return render_template('index.html', value=json_file, champs=champs.champs.items())

def init_igraph():
	g = igraph.read("pajekfile.net",format="pajek")
	cc = g.transitivity_local_undirected(vertices=v)
	grau = g.degree(v, mode="in", loops=True)
	excentricidade = g.eccentricity(vertices=v, mode="in")


def mk_int(s):
    s = s.strip()
    return int(s) if s else 0
def mk_float(s):
	s = s.strip()
	return float(s) if s else 0	
def get_json(args):
	default_min = 50
	default_win = 0.6

	query = "SELECT `value`,`win`, b.name as sname, c.name as tname, b.id as sid, c.id as tid FROM `arcs` a JOIN champs b ON (a.source_id = b.uid) JOIN champs c ON (a.target_id = c.uid)"
	if(len(args) > 0):
		minimo = mk_int(args['min'])
		query += " WHERE value >= {}".format(minimo)
		maximo = mk_int(args['max'])
		vitorias = mk_float(args['win'])
		if(maximo > 0):
			query += " AND value <= {}".format(maximo)

		picks = tuple(args.getlist('picks'))
		bans = tuple(args.getlist('bans'))
		if(len(picks) > 1):
			query += " AND source_id in {} AND target_id in {}".format(picks,picks)
		else:
			if(len(picks) == 1):
				query += " AND source_id in ({}) AND target_id in ({})".format(picks[0], picks[0])
		if(len(bans) > 1):
			query += " AND source_id not in {} AND target_id not in {}".format(bans,bans)
		else:
			if(len(bans) == 1):
				query += " AND source_id not in ({}) AND target_id not in ({})".format(bans[0], bans[0])	
		if (vitorias >= 0 and vitorias <= 1):
			query += " AND win > {}".format(vitorias) 
	else:
		query += " WHERE win >= {} AND value >= {}".format(default_win, default_min)

	db=MySQLdb.connect(passwd="",db="leagueoflegends", user="root")
	c=db.cursor()
	c.execute(query)
	db.close()
	return make_json(c.fetchall())

def make_json(data):
	links = []
	list_used = []
	global v
	paj_links = []
	paj_nodes = []
	for x in data:
		links.append({"source" : x[2], "target" : x[3], "win" : x[1], "value" :x[0]})
		paj_links.append({"sid" : x[4], "tid" : x[5], "value" :x[0]})
		if list_used.count(x[2]) == 0:
			list_used.append(x[2])
			v.append(x[4])
			paj_nodes.append({"sid" : x[4], "sname" : x[2]})

	make_paj(paj_nodes,paj_links)
	nodes = get_all_champs_in_node(links, list_used)
	
	output = Markup({"nodes" : nodes, "links" : links})
	return output

def make_paj(nodes, links):
	output = open('pajekfile.net', 'w')
	text = "*Vertices {}".format(140)
	for x in nodes:
		text += "\n\t{} \"{}\"".format(x["sid"],x["sname"])
	text += "\n*arcs"
	for x in links:
		text += "\n\t{} {} {}".format(x["sid"],x["tid"],x["value"])
	output.write(text)
	output.close()

def get_all_champs_in_node(links, list_used):
	db=MySQLdb.connect(passwd="",db="leagueoflegends", user="root")
	c=db.cursor()
	c.execute("SELECT uid, name, url FROM CHAMPS")
	data = c.fetchall()
	db.close()
	nodes = []
	tamanho_maximo = 0
	tam = {}
	for x in data:
		if(x[1] in list_used):
			value = 0
			for y in links:
				if(y['source'] == x[1] and y['target'] in list_used):
					value += y["value"]
			if(value > tamanho_maximo):
				tamanho_maximo = value
			tam[x[1]] = value
	for x in data:
		if(x[1] in list_used):
			nodes.append({"id" : x[1], "group" : 1, "url" : x[2], "uid" : x[0], "value" : tam[x[1]], "value_maximo" : tamanho_maximo})
	return nodes
if __name__ == "__main__":
	app.run()