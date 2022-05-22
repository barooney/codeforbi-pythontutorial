name = input("Wie heißt du? ")

print("Hallo " + name + "!")

alter_text = input("Wie alt bist du? ")
alter = int(alter_text)
alter = alter + 1
alter_text = str(alter)
print("Dann bist du nächstes Jahr schon " + alter_text)
