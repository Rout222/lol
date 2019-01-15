import csv
import copy
import mysql.connector

data_matches = {}
data_match = {"participants_count": 0, "matchid": 0,
              "players": {}, "type": 0, "platform": 0, "creation": 0}
data_player = {"kills": 0, "deaths": 0,
               "assists": 0, "champion_id": 0, "win": 0,
               "role": 0, "position": 0}
data_player_match = {}


def save_match(match):

    c = db.cursor()
    for player in match['players']:
        c.execute("INSERT INTO `players`(`match_id`, `kills`, `deaths`, `assists`, `win`, `champ_id`, `lane`, `player_id`, `platform`, `type`, `data`) VALUES  (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                  [match['matchid'], match['players'][player]['kills'],match['players'][player]['deaths'], match['players'][player]['assists'], match['players'][player]['win'], match['players'][player]['champion_id'], match['players'][player]['position'], player, match['platform'], match['type'], match['creation']])
    db.commit()
    c.close()
    


with open("./dataset/matches.csv") as matches_file:
    with open("./dataset/participants.csv") as participants_file:
        with open("./dataset/stats1.csv") as stats1_file:
            with open("./dataset/stats2.csv") as stats2_file:
                matches = csv.DictReader(matches_file)
                participants = csv.DictReader(participants_file)
                stats1 = csv.DictReader(stats1_file)
                stats2 = csv.DictReader(stats2_file)

                print('Matches')
                for match in matches:
                    this_match = copy.deepcopy(data_match)
                    this_match['matchid'] = match['gameid']
                    this_match['platform'] = match['platformid']
                    this_match['type'] = match['queueid']
                    this_match['creation'] = match['creation']
                    data_matches[match['id']] = this_match

                print('Participant')
                for participant in participants:
                    this_player = copy.deepcopy(data_player)
                    data_player_match[participant['id']
                                      ] = participant['matchid']
                    this_player['role'] = participant['role']
                    this_player['position'] = participant['position']
                    this_player['champion_id'] = participant['championid']
                    data_matches[participant['matchid']
                                 ]['participants_count'] += 1
                    data_matches[participant['matchid']
                                 ]['players'][participant['id']] = this_player

                print('Stats1')
                for stats in stats1:
                    this_stats = data_matches[data_player_match[stats['id']]
                                              ]['players'][stats['id']]
                    this_stats['kills'] = stats['kills']
                    this_stats['deaths'] = stats['deaths']
                    this_stats['assists'] = stats['assists']
                    this_stats['win'] = stats['win']

                print('Stats2')
                for stats in stats2:
                    this_stats = data_matches[data_player_match[stats['id']]
                                              ]['players'][stats['id']]
                    this_stats['kills'] = stats['kills']
                    this_stats['deaths'] = stats['deaths']
                    this_stats['assists'] = stats['assists']
                    this_stats['win'] = stats['win']

                print('Saving')
                db = mysql.connector.connect(user='root', password='',
                                 host='127.0.0.1',
                                 database='lol_kaggle')
                for match in data_matches:
                    match = data_matches[match]
                    i = 0
                    if(match["participants_count"] == 10):
                        save_match(match)
                    else:
                    	i += 1
                db.close()

print(i + " deram erro")
