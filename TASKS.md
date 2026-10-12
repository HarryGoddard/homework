# Dota 2 Data Homework

How to work
- Make a new Python file for each task (`task1.py`, `task2.py`, ...) and save it in this folder, next to the `.csv` files.
- Run it and compare what it prints with the Check your answer box under the task.

---

## What's a CSV file?

A CSV is a spreadsheet saved as plain text. Each line is a row, and commas separate the columns. Imagine an excel workbook but instead of grids, each column is separated by a comma, and each new line is a new row. Open `my_games.csv` in VS Code and have a look:

```
game,hero,result,kills,deaths,assists,gpm
1,Pudge,Win,7,4,15,410
2,Crystal Maiden,Loss,2,9,11,260
...
```

The first line is the header, which holds the column names. Every line after that is data - one game each.

## The starter code

Every task starts with these lines, so copy them into each new file:

```python
import csv

file = open("my_games.csv")
reader = csv.DictReader(file)

for row in reader:
    print(row["hero"])
```

What each part does:
- `import csv` loads Python's tool for reading CSV files.
- `open("my_games.csv")` opens the file.
- `csv.DictReader(file)` passes the `file` into the csv reader, ready to be read one row at a time.
- The `for` loop goes round once for every game (every line/row). Each time round, `row` holds one game, and `row["hero"]` gets the value in that game's `hero` column.

---

## Level 1: Reading the file
Use `my_games.csv` for this level.

Task 1. Run the starter code. You should see 10 hero names. Then change it so it prints the `result` column instead.

Task 2. Print the hero and the result on the same line, like this:
```
Pudge Win
```
Hint: `print` can take more than one thing if you separate them with commas: `print(a, b)`.

Task 3. Print a line for each game, like this:
```
Game 1 - Pudge - Win - 7 kills
```

<details><summary>Hint</summary>

Text in quotes gets printed exactly as you typed it:

```python
print("Game", row["game"], "-", row["hero"], ...)
```

</details>

---

## Level 2: Asking questions with `if`
Still using `my_games.csv`.

Task 4. Print only the games you won. Put an `if` inside the loop:
```python
for row in reader:
    if row["result"] == "Win":
        print(row["hero"])
```
Then change it to print only the losses.

<details><summary>Check your answer</summary>

Losses: Crystal Maiden, Lion, Invoker, Pudge.

</details>

Task 5. Count the wins. Copy this and fill in the gap (`___`):
```python
wins = 0

for row in reader:
    if row["result"] == "Win":
        wins = ___

print("Wins:", wins)
```
Extra: count the losses as well, in the same loop. You'll need a second variable and an `else`.

<details><summary>Check your answer</summary>

6 wins and 4 losses

</details>

Task 6: the string trap. Print every game where you got more than 10 kills. Try this first:
```python
if row["kills"] > 10:
```
It crashes! Read the error message before you go on.

<details><summary>Why it crashes and how to fix it</summary>

Python reads everything in a CSV file as text. So `row["kills"]` is `"12"` (text), not `12` (a number), and Python can't check whether some text is bigger than a number.

Turn it into a number with `int()`:

```python
kills = int(row["kills"])
if kills > 10:
```

</details>

<details><summary>Check your answer</summary>

3 games: Juggernaut (12), Sven (14), Juggernaut (11)

</details>

Task 7. Work out your total kills and your average kills per game. This is like counting wins, except you add on the kills each time instead of adding 1:
```python
total_kills = 0
games = 0

for row in reader:
    total_kills = total_kills + int(row["kills"])
    games = games + 1
```
After the loop, print the total and the average (`total_kills / games`).

<details><summary>Check your answer</summary>

Total 73, average 7.3

</details>

---

## Level 3: The big file
From now on, use `matches.csv`. Change the open line to `open("matches.csv")`.

`my_games.csv` was small enough to check by eye. `matches.csv` has 101 games played by four friends, which is too many to count by hand.

Open it and have a look first. It has some extra columns:

| Column | Example | Meaning |
|---|---|---|
| `player` | `rubydota` | Who played (the four players are `rubydota`, `gron`, `hoxieloxie` and `gronaccount2`) |
| `role` | `Carry` | Carry, Mid, Offlane, Soft Support or Hard Support |
| `duration_mins` | `29` | How long the game lasted, in minutes |

Task 8. How many games are in the file? Count them with a variable, like you did in Task 5.

<details><summary>Check your answer</summary>

101

</details>

Task 9. Count the wins and losses, then work out the win rate:
```
win rate = wins / games * 100
```
Hint: `round(win_rate, 1)` rounds it to 1 decimal place.

<details><summary>Check your answer</summary>

55 wins, 46 losses, 54.5%

</details>

Task 10: hero search. Ask the user for a hero before the loop:
```python
hero = input("Which hero? ")
```
Inside the loop, print the player, result and kills of every game played on that hero. At the end, print how many games you found.

Extra: make it work even if someone types `pudge` or `PUDGE`.
Hint: `"PuDgE".lower()` gives `"pudge"`. Use `.lower()` on both sides of the `==`.

<details><summary>Check your answer</summary>

Pudge has 6 games.

</details>

Task 11: player search. Ask for a player's name, then print how many games they played, how many they won, and their win rate.
Hint: you'll need an `if` inside another `if`. First check it's the right player, then check whether they won.

<details><summary>Check your answer</summary>

rubydota: 28 games, 13 wins, 46.4%

</details>

---

## Level 4: Finding the best
Using `matches.csv`.

Task 12: most kills ever. Use a "record so far" variable. It starts at 0, and every time a game beats the record, that game becomes the new record:
```python
most_kills = 0

for row in reader:
    kills = int(row["kills"])
    if kills > most_kills:
        most_kills = kills

print("Most kills:", most_kills)
```
When that works, also print who got it and which hero they played.
Hint: make two more variables, `best_player` and `best_hero`, and update them inside the same `if`.

<details><summary>Check your answer</summary>

23 kills, by rubydota on Phantom Assassin

</details>

Task 13: longest game. Use the same trick to find the longest game (`duration_mins`). Who played it, on which hero, and did they win?

<details><summary>Check your answer</summary>

71 minutes. hoxieloxie on Tidehunter, and they won!

</details>

Task 14: KDA. KDA is a single score for how well someone played:
```
KDA = (kills + assists) / deaths
```
Print the hero and KDA of every game. Your program will crash partway through. Work out why from the error message.

<details><summary>Hint (open once you've seen the crash)</summary>

Someone played a perfect game with 0 deaths, and you can't divide by zero. In Dota, KDA counts 0 deaths as 1, so add this before you divide:

```python
if deaths == 0:
    deaths = 1
```

</details>

When that works, find the best KDA with the trick from Task 12.

<details><summary>Check your answer</summary>

36.0, by gron on Invoker (14 kills, 0 deaths, 22 assists)

</details>

Task 15: are supports poor? Work out the average GPM of Carry games and of Hard Support games.
You need four variables: `carry_gpm`, `carry_games`, `support_gpm` and `support_games`. Inside the loop, use `if` and `elif` to check `row["role"]`.

<details><summary>Check your answer</summary>

Carry is about 632 GPM and Hard Support about 276, so yes, supports are poor.

</details>

---

## Level 5: Boss fight, the player report card

Write one program that asks for a player's name and prints their report card:

```
=== Report card: rubydota ===
Games: 28
Wins: 13
Win rate: 46.4 %
Average kills: 8.8
Average GPM: 632
Best game: 23 kills on Phantom Assassin
```

This uses everything from Levels 1 to 4 in one program. Try it for all four players and see who's best.

Extra: if someone types a name that isn't in the file, print `No player called ...` instead of crashing.
Hint: what is `games` at the end if the name was never found?

---

Finished?
