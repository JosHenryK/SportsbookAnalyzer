import os
import csv
import json

def parsePlayerData(DataDir , parsedDataDir):
    os.makedirs(parsedDataDir , exist_ok = True)
    for file in os.listdir(DataDir):
        with open(os.path.join(DataDir, file), 'r') as readHead:
            dict = csv.DictReader(readHead)

            year = file.split("_")[2].split(".")[0]
            for entry in dict:
                week = entry['week']
                currentTeam = entry['recent_team']
                opponentTeam = entry['opponent_team']
                playerName = entry['player_display_name']

                path = os.path.join(parsedDataDir , year , week , currentTeam + "_v_" + opponentTeam , currentTeam)
                if year in os.listdir(parsedDataDir):
                    if week in os.listdir(os.path.join(parsedDataDir, year)):
                        if (opponentTeam + "_v_" + currentTeam) in os.listdir(os.path.join(parsedDataDir, year, week)):
                            path = os.path.join(parsedDataDir , year , week , opponentTeam + "_v_" + currentTeam , currentTeam)
                
                os.makedirs(path , exist_ok = True)
                with open(os.path.join(path , playerName + ".json") , 'w') as writeHead:
                    writeHead.write(json.dumps(entry))