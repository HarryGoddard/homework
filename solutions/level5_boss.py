import csv

name = input("Which player? ")

file = open("matches.csv")
reader = csv.DictReader(file)

games = 0
wins = 0
total_kills = 0
total_gpm = 0
most_kills = 0
best_hero = ""

for row in reader:
    if row["player"] == name:
        games = games + 1
        if row["result"] == "Win":
            wins = wins + 1
        kills = int(row["kills"])
        total_kills = total_kills + kills
        total_gpm = total_gpm + int(row["gpm"])
        if kills > most_kills:
            most_kills = kills
            best_hero = row["hero"]

if games == 0:
    print("No player called", name)
else:
    print("=== Report card:", name, "===")
    print("Games:", games)
    print("Wins:", wins)
    print("Win rate:", round(wins / games * 100, 1), "%")
    print("Average kills:", round(total_kills / games, 1))
    print("Average GPM:", round(total_gpm / games))
    print("Best game:", most_kills, "kills on", best_hero)
