import csv

# Task 1
file = open("my_games.csv")
reader = csv.DictReader(file)
for row in reader:
    print(row["result"])

# Task 2
file = open("my_games.csv")
reader = csv.DictReader(file)
for row in reader:
    print(row["hero"], row["result"])

# Task 3
file = open("my_games.csv")
reader = csv.DictReader(file)
for row in reader:
    print("Game", row["game"], "-", row["hero"], "-", row["result"], "-", row["kills"], "kills")
