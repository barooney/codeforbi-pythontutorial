def bankdruecken(gewicht):
    print("Das ist ganz schön schwer! Das sind bestimmt " + str(gewicht) + " Kilogramm!")
    return gewicht


def training(wiederholungen, gewicht):
    gesamtgewicht = 0
    for i in range(1, wiederholungen + 1):
        gesamtgewicht = gesamtgewicht + bankdruecken(gewicht)
    return gesamtgewicht


if __name__ == '__main__':
    gesamtgewicht = training(10, 25);
    print("Insgesamt hast du " + str(gesamtgewicht) + " Kilo gestemmt!")
