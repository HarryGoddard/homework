import csv

# Task 4
file = open("my_games.csv")
reader = csv.DictReader(file)
for row in reader:
    if row["result"] == "Win":
        print(row["hero"])

# Task 5
file = open("my_games.csv")
reader = csv.DictReader(file)
wins = 0
losses = 0
for row in reader:
    if row["result"] == "Win":
        wins = wins + 1
    else:
        losses = losses + 1
print("Wins:", wins)
print("Losses:", losses)

# Task 6
file = open("my_games.csv")
reader = csv.DictReader(file)
for row in reader:
    kills = int(row["kills"])
    if kills > 10:
        print(row["hero"], kills)

# Task 7
file = open("my_games.csv")
reader = csv.DictReader(file)
total_kills = 0
games = 0
for row in reader:
    total_kills = total_kills + int(row["kills"])
    games = games + 1
print("Total kills:", total_kills)
print("Average kills:", total_kills / games)
