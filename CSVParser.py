import os
import csv
import json

def parsePlayerData(playerDataDir , parsedPlayerDataDir):
    for file in os.listdir(playerDataDir):
        with open(os.path.join(playerDataDir, file), 'r') as readHead:
            dict = csv.DictReader(readHead)
            for entry in dict:
                year = file.split("_")[2].split(".")[0]
                playerName = entry['player_name']
                currentTeam = entry['recent_team']
                opponentTeam = entry['opponent_team']

                path = os.path.join(parsedPlayerDataDir , year)
                os.makedirs(path , exist_ok = True)
                with open(os.path.join(path , playerName + "_" + currentTeam + "_v_" + opponentTeam + ".json") , 'w') as writeHead:
                    writeHead.write(json.dumps(entry))