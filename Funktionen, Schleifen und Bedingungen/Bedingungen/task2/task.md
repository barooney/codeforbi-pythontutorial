# if, else, elif

Um den sogenannten Kontrollfluss in Python zu verändern, gibt es die Schlüsselwörter `if`, `else` und `elif`.
Sie helfen uns dabei, unseren Programmablauf zu verändern, indem wir weitere Schritte ausführen, wenn nötig oder andere
überspringen, wenn sie nicht notwendig sind.

Dabei müssen wir uns auf die Boolschen Ausdrücke konzentrieren, die wir im vorigen Abschnitt kennengelernt haben.
Wir können nur prüfen, ob eine bestimmte Bedingung zutrifft oder nicht.
"Ein bisschen zutreffen" oder "ein bisschen nicht zutreffen" gibt es in diesem Fall nicht!

Stellen wir uns vor, wir gehen wandern und kommen an eine Weggabelung.
Um uns zu entscheiden, in welche Richtung wir gehen (nach links oder rechts), wollen wir eine Münze werfen.
Zeigt die Münze Kopf, dann gehen wir nach links, zeigt sie Zahl, dann gehen wir nach rechts.

Wir nehmen an, dass wir öfter abbiegen müssen und uns öfters mittels Münzwurf für einen der beiden Weggabelungen
entscheiden.
Deswegen verwenden wir eine Funktion, der wir als Parameter das Ergebnis des Münzwurfs mitgeben.
Als Ergebnis wollen wir dann wissen, ob wir nach links oder nach rechts abbiegen:

```python
def abbiegen(seite):
    if seite == "kopf":
        return "links"
    else:
        return "rechts"
```

Hier siehst du schon wieder viele neue Konzepte:
`if` und `else` sind zwei der drei Schlüsselwörter, die oben bereits vorgestellt wurden.
Dabei erwartet `if` eine Bedingung, die überprüft wird (in diesem Fall ist das `seite == "kopf"`).
Hat der Parameter `seite` also den Wert `"kopf"`, dann ist der Vergleich an dieser Stelle wahr.
Auffällig ist hier das doppelte Gleichheitszeichen.
In der Mathematik schreibt man ein Gleichheitszeichen, um die Gleichheit auszudrücken, in Python und vielen anderen
Programmiersprachen verwendet man zwei davon, um Vergleiche kenntlich zu machen.
Würden wir in der Bedingung nur ein Gleichheitszeichen verwenden, dann würde Python `"kopf"` in `seite` speichern.

Wenn wir Zahlen miteinander vergleichen wollen, dann können wir nicht nur auf Gleichheit, sondern auch auf 
Verschiedenheit prüfen.
Vergleiche wie `<` und `>` erlauben es uns, Zahlen in Relation zu setzen.
Außerdem gibt es die Vergleiche `>=` und `<=`, die prüfen, ob eine Zahl größer oder gleich (oder kleiner oder gleich)
einer anderen Zahl ist.
Wenn wir uns nicht sicher sind, ob eine Zahl größer oder kleiner ist, wir aber wissen wollen, ob eine Zahl ungleich 
einer anderen Zahl ist, dann können wir `!=` verwenden.

`else` taucht – wenn überhaupt – immer mit einem zugehörigen `if` auf und kann niemals alleine stehen, es muss aber 
nicht auftauchen, wie wir gleich sehen werden.
In dem Beispiel oben prüfen wir, ob `seite` den Wert `"kopf"` hat – dann wollen wir nach links abbiegen.
Wenn wir aber nicht Kopf geworfen haben (das heißt nicht nur, dass wir Zahl geworfen haben, die Münze kann 
beispielsweise auch auf dem Rand stehengeblieben sein), dann wollen wir in jedem Fall nach rechts gehen.
Und das "in jedem Fall" ist hier wichtig, weil wir an das `else` keine Bedingung mehr knüpfen können.
Der Teil unterhalb von `else` wird immer dann ausgeführt, wenn kein anderer sogenannter Zweig (also keine Bedingung)
zutreffend war.

Doch was ist, wenn wir mehr als zwei Wege haben – angenommen, wir haben drei Wege.
Eine Münze hilft uns dabei nicht mehr weiter, weswegen wir jetzt zu einem Würfel greifen.
Würfeln wir eine 1 oder 2, dann gehen wir nach links, bei einer 3 oder 4 gehen wir geradeaus und bei einer 5 oder 6
biegen wir nach rechts ab:

```python
def abbiegen(augenzahl):
    if 1 <= augenzahl <= 2:
        return "links"
    elif 3 <= augenzahl <= 4:
        return "geradeaus"
    elif 5 <= augenzahl <= 6:
        return "rechts"
```

Python erlaubt es uns, Vergleiche von mehreren Zahlen etwas kompakter zu schreiben.
Wollen wir also sicherstellen, dass die `augenzahl` zwischen `1` und `2` liegt, dann können wir das wie folgt notieren:
`1 <= augenzahl <= 2`
Damit wird ausgedrückt, dass die 1 kleiner oder gleich `augenzahl` und zusätzlich dazu auch `augenzahl` kleiner oder
gleich 2 sein soll.

Diese Ausdrücke lassen sich auch komplexer beschreiben, insbesondere dann, wenn es nicht mehr ausschließlich um Zahlen
geht.
Statt `1 <= augenzahl <= 2` können wir auch `1 <= augenzahl and augenzahl <= 2` schreiben.
Hierbei prüfen wir dieselben Kriterien, allerdings in zwei Schritten und verlangen dann, dass beides zutreffen muss,
indem wir die Bedingungen mit dem Schlüsselwort `and` verbinden.
Erinnern wir uns nochmal an die letzte Aufgabe – hier haben wir auch mit "Und" und "Oder" gearbeitet.
Das Äquivalent für "Oder" ist entsprechend `or`.

Ein vereinfachtes Beispiel der Buchauswahl aus der letzten Aufgabe könnte wie folgt aussehen:

```python
def buchauswahl(genre, protagonistin, coverfarbe):
    if protagonistin and genre == "Horror":
        return True
    if coverfarbe == "blau-grün" and genre != "Fantasy":
        return True
    return False
```

Hierbei beachten wir nur die ersten beiden Fälle (es gibt eine Protagonistin und das Genre entspricht Horror
und das Buchcover ist blau-grün und das Genre ist nicht Fantasy).
Diese Funktion ist für uns lesbar und verständlich, jedoch lässt sich diese Auswahl noch knapper zusammenfassen.
Ich will niemanden motivieren, solchen Code zu schreiben, wenn man darüber stolpert, dann sollte man sich aber nicht
verunsichern lassen:

```python
def buchauswahl(genre, protagonistin, coverfarbe):
    return (protagonistin and genre == "Horror") or (coverfarbe == "blau-grün" and genre != "Fantasy")
```

Statt mit `if`, `elif` und `else` zu arbeiten, schreiben wir alles in eine Zeile und verzichten auf diese 
Schlüsselwörter.
Das können wir machen, weil das Schlüsselwort `or` uns gestattet, die beiden Bedingungen miteinander zu verbinden.
Wir prüfen also, ob entweder der erste Teil vor dem `or` oder der zweite Teil nach dem `or` wahr wird.
Es müssen nicht beide Teile wahr werden.

Anders ist es bei dem Schlüsselwort `and` in den Klammern:
Hier müssen beide (oder alle, wenn man mehrmals `and` notiert) Bedingungen erfüllt sein.
Zum Beispiel muss es eine Protagonistin geben und das Buch zum Genre "Horror" gehören.

## Aufgabe

Basierend auf dem Würfel-Beispiel oben sollst du nun eine Funktion schreiben, die deine Würfelwürfe "kommentiert".
Ein Wurf mit einer niedrigen Zahl (1 und 2) soll beispielsweise mit einem "Schade, nur eine 1" kommentiert werden.
Würfe mit einer 3 und 4 können als "Durchschnitt" bezeichnet werden.
Eine 5 kannst du mit einem "So knapp!" kommentieren und die 6 mit "Super! Weiter so!"
Achte darauf, die jeweilige Zahl auch immer im Text zu verwenden.

Eine Beispielausgabe des Programms könnte also wie folgt aussehen:

```
Schade, nur eine 1
Schade, nur eine 2
Eine durchschnittliche 3
Eine durchschnittliche 4
So knapp - leider nur eine 5
Super! Eine 6
```

Teste deine Ausgabe, indem du das Programm mit dem grünen Pfeil oben links neben dem Editorfenster startest.
Bist du mit deiner Lösung zufrieden, dann klicke unter der Aufgabe auf "Check".
