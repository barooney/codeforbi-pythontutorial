def kommentar(augenzahl):
    if 1 <= augenzahl <= 2:
        return "Schade, nur eine " + str(augenzahl)
    elif 3 <= augenzahl <= 4:
        return "Eine durchschnittliche " + str(augenzahl)
    elif augenzahl == 5:
        return "So knapp - leider nur eine " + str(augenzahl)
    elif augenzahl == 6:
        return "Super! Eine " + str(augenzahl)


if __name__ == '__main__':
    print(kommentar(1))
    print(kommentar(2))
    print(kommentar(3))
    print(kommentar(4))
    print(kommentar(5))
    print(kommentar(6))

