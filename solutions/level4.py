import csv

# Task 12
file = open("matches.csv")
reader = csv.DictReader(file)
most_kills = 0
best_player = ""
best_hero = ""
for row in reader:
    kills = int(row["kills"])
    if kills > most_kills:
        most_kills = kills
        best_player = row["player"]
        best_hero = row["hero"]
print("Most kills:", most_kills, "by", best_player, "on", best_hero)

# Task 13
file = open("matches.csv")
reader = csv.DictReader(file)
longest = 0
longest_player = ""
longest_hero = ""
longest_result = ""
for row in reader:
    minutes = int(row["duration_mins"])
    if minutes > longest:
        longest = minutes
        longest_player = row["player"]
        longest_hero = row["hero"]
        longest_result = row["result"]
print("Longest game:", longest, "minutes -", longest_player, "on", longest_hero, "-", longest_result)

# Task 14
file = open("matches.csv")
reader = csv.DictReader(file)
best_kda = 0
best_player = ""
best_hero = ""
for row in reader:
    kills = int(row["kills"])
    deaths = int(row["deaths"])
    assists = int(row["assists"])
    if deaths == 0:
        deaths = 1
    kda = (kills + assists) / deaths
    print(row["hero"], round(kda, 2))
    if kda > best_kda:
        best_kda = kda
        best_player = row["player"]
        best_hero = row["hero"]
print("Best KDA:", round(best_kda, 2), "by", best_player, "on", best_hero)

# Task 15
file = open("matches.csv")
reader = csv.DictReader(file)
carry_gpm = 0
carry_games = 0
support_gpm = 0
support_games = 0
for row in reader:
    if row["role"] == "Carry":
        carry_gpm = carry_gpm + int(row["gpm"])
        carry_games = carry_games + 1
    elif row["role"] == "Hard Support":
        support_gpm = support_gpm + int(row["gpm"])
        support_games = support_games + 1
print("Carry average GPM:", round(carry_gpm / carry_games))
print("Hard Support average GPM:", round(support_gpm / support_games))
