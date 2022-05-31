# Todo: Hier implementierst du deine eigene greetings-Methode:
def greeting(name):
    return "Hallo " + name + "! Schön, dich kennenzulernen!"


# Hier ist ein bisschen Code, der es einfacher macht, deine Funktion zu testen.
# Davon solltest du dich nicht irritieren lassen.
# Willst du deinen Code ausführen, dann klicke oben links neben dem Editor auf den grünen Pfeil.
if __name__ == "__main__":
    # Den Namen der nutzenden Person einlesen
    mein_name = input("Hallo! Wie heißt du? ")

    # Die personalisierten Grüße speichern
    gruss = greeting(mein_name)

    # Die personalisierten Grüße ausgeben
    print(gruss)
