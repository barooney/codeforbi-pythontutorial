import csv

def highscore_as_text(name, date, highscore):
    return name + " hat am " + date + " " + highscore + " Punkte erreicht!"

def load_csv(filename):
    with open(filename, "r") as file:
        data = csv.reader(file)
        for line in data:
            if line[0] != "name":
                print(highscore_as_text(line[0], line[1], line[2]))

load_csv("highscores.csv")
