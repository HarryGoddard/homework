import csv

# Task 8
file = open("matches.csv")
reader = csv.DictReader(file)
games = 0
for row in reader:
    games = games + 1
print("Games:", games)

# Task 9
file = open("matches.csv")
reader = csv.DictReader(file)
wins = 0
losses = 0
for row in reader:
    if row["result"] == "Win":
        wins = wins + 1
    else:
        losses = losses + 1
win_rate = wins / (wins + losses) * 100
print("Wins:", wins)
print("Losses:", losses)
print("Win rate:", round(win_rate, 1), "%")

# Task 10
hero = input("Which hero? ")
file = open("matches.csv")
reader = csv.DictReader(file)
found = 0
for row in reader:
    if row["hero"].lower() == hero.lower():
        print(row["player"], row["result"], row["kills"], "kills")
        found = found + 1
print(found, "games")

# Task 11
name = input("Which player? ")
file = open("matches.csv")
reader = csv.DictReader(file)
games = 0
wins = 0
for row in reader:
    if row["player"] == name:
        games = games + 1
        if row["result"] == "Win":
            wins = wins + 1
print("Games:", games)
print("Wins:", wins)
print("Win rate:", round(wins / games * 100, 1), "%")
