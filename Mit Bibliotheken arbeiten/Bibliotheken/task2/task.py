# Importiere den Counter
from collections import Counter


# Zähle, wie oft einzelne Worte in einem Satz vorkommen
def zaehle_wortvorkommen(satz):
    # Zerlege den Satz in einzelne Worte
    # satz.split() trennt den Text dabei immer bei einem Leerzeichen, Tab oder auch Zeilenumbrüchen!
    worte = satz.split()

    # Erzeuge einen Zähler, der ermittelt, welche Worte und wie oft diese in dem Satz vorkommen
    counter = Counter(worte)

    # Gib den Counter zurück, damit wir damit weiterarbeiten können
    return counter


# Zähle die Wortvorkommen in den beiden Sätzen und gib aus, wie oft welches Wort vorkommt:
print(zaehle_wortvorkommen("Das ist ein langer langer langer Satz mit vielen Wortvorkommen"))
print(zaehle_wortvorkommen("Das ist ein Satz mit wenigen Wortvorkommen"))
