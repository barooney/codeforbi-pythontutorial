## Variablen

In dem letzten Abschnitt haben wir die Boxen kennengelernt.
Diese Boxen heißen in der Programmierung Variablen – ihr Inhalt ist variabel.

Variablen sind anhand ihres Namens eindeutig identifizierbar und haben einen bestimmten Inhalt.
Das kann ein Text, eine Zahl, eine Liste oder etwas ganz anderes sein.

Eine Variable `name` stört sich nicht an der Variablen `alter` und umgekehrt.
Beide können nebeneinander existieren und du kannst so viele Variablen definieren wie du willst.
Die einzige Beschränkung, die es gibt, ist dein Computer.
Denn obwohl er sich _sehr viel_ merken kann, so kann er sich nicht _unendlich viel_ merken.
Das liegt an dem Arbeitsspeicher, der in deinem Computer verbaut ist.

Die verschiedenen Typen von Variablen – darum kümmert sich Python selbst in den meisten Fällen – sind aber an einigen
Stellen nicht kompatibel.
So können Texte zum Beispiel in eckigen Boxen verpackt werden, Zahlen aber nur in runden Boxen.
Dafür gibt es verschiedene Funktionen, die den Wert, also einen Text oder eine Zahl aus einer Box herausnehmen und in
eine andere verpacken, sodass das Programm damit weiterarbeiten kann.
Im Endeffekt ist das ein Teil unseres Algorithmus.

Wenn wir der nutzenden Person mitteilen wollen, wie alt sie nächstes Jahr ist, dann müssen wir zuerst wissen, wie alt
sie im aktuellen Jahr ist.
Wenn wir die Person fragen, wie alt sie ist, dann gibt sie das mit der Tastatur ein.
Diese Eingabe liegt dann als Zeichenkette vor – beispielsweise also `"30"`.
Diese Zeichenkette hat dann die Länge zwei, das erste Zeichen ist dann die `3`, das zweite die `0`.
Nun müssen wir dem Computer vermitteln, dass wir aber aus dieser Zeichenkette eine Zahl machen wollen, damit wir damit
rechnen können.

## Text in eine Zahl umwandeln

Hierzu gibt es verschiedene Funktionen, die aus Zeichenketten Zahlen und umgekehrt aus Zahlen wieder Zeichenketten
machen.
Eine solche Funktion ist beispielsweise `int`:

```python
text = "23"
zahl = int(text)
```

Wenn wir also eine Zeichenkette haben, dann können wir sie mit der Funktion `int` in eine Zahl verwandeln und in einer
anderen Variablen speichern.
`int` steht hierbei für "Integer" und bedeutet im Englischen so viel wie "Ganzzahl", also eine Zahl ohne
Nachkommastellen.

Genauso gibt es auch die Funktion `float`, die Texte in Zahlen mit Nachkommastellen verwandeln kann, sodass wir damit
später rechnen können:

```python
text = "23.7"
kommazahl = float(text)
```

Wichtig an der Stelle ist, dass Kommazahlen in Python wie in fast allen anderen Programmiersprachen auch mit einem Punkt
getrennt werden.

## Zahl in einen Text umwandeln

Wenn wir nun eine Zahl ausgeben wollen, dann müssen wir die Zahl wieder aus der Box für eine Zahl herausnehmen und in
eine Box für eine Zeichenkette legen.
Auch hierfür gibt es eine Funktion: `str`.

Wenn wir jetzt eine Zahl wieder ausgeben wollen, dann müssen wir die Funktion `str` verwenden, damit wir einen Text 
zusammen mit einer Zahl ausgeben können:

```python
zahl = 23.7
zahl_als_text = str(zahl)
print("Meine Zahl ist " + zahl_als_text)
```

**Versuche nun, das vorliegende Programm aus der vorigen Aufgabe zu vervollständigen.**
Wir wollen die nutzende Person darum bitten, ihr Alter einzugeben, um dann auszurechnen, wie alt sie im nächsten Jahr 
sein wird.
Hierbei können dir die vorgegebenen Schritte helfen.

Die Ein- uns Ausgabe kann dann wie folgt aussehen:

```
Wie heißt du? Max
Hallo Max!
Wie alt bist du? 30
Dann bist du nächstes Jahr schon 31
```

**Falls du überprüfen willst, ob du alles richtig verstanden hast, dann kannst du versuchen, die nutzende Person nach
ihrer Größe in Meter zu fragen, um auch mit Kommazahlen zu arbeiten.**
Du kannst dann versuchen, einen Zentimeter dazuzurechnen oder abzuziehen.
Bedenke, dass Kommazahlen in Python immer mit einem Punkt getrennt werden.
Wenn du 1,70 Meter groß bist, dann musst du in Python `1.70` eingeben.
