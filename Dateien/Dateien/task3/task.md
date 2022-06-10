# CSV-Dateien einlesen

Während Nicht-Programmierer Excel verwenden, um Tabellen zu verwalten, greifen Programmierer zu sogenannten CSV-Dateien.
CSV steht dabei für "comma separated values" – Kommaseparierte Werte.
Eine Beispiel-Datei findest du in dieser Aufgabe – sie heißt `highscores.csv`.

In dieser Datei sind Highscore-Werte abgelegt.
Dazu gehört der Name der Person, die den Highscore erreicht hat, wann der Highscore erreicht wurde und wie hoch der
Highscore ist.

Hier ein Auszug aus der Datei:

```
name,datum,punkte
beetsauce,10.6.2022,9
eagleowl,9.5.2022,13
```

Was auffällt ist, dass alle Werte hintereinanderstehen und dazwischen jeweils nur ein Komma steht.
Diese Datei macht ihrem Namen alle Ehre – die Werte sind alle kommasepariert.

Wir können die Datei nun wie gehabt einlesen, dann haben wir aber das Problem, dass wir selbst herausfinden müssen, an 
welcher Stelle der Text geteilt werden muss.
Und was passiert, wenn wir zum Beispiel ein Datum haben, das "Montag, den 6.6.2022" lautet?
Die Zeile in der Datei sähe dann zum Beispiel wie folgt aus:

```
eagleowl,Montag, den 6.6.2022,9
```

In dem Fall könnten wir den Namen noch sehr sicher bestimmen, bei dem Datum wird es schon schwieriger – vermutlich
würden wir "Montag" als das Datum identifizieren und ` den 6.6.2022` als den Punktestand.
Die `9` wäre für uns nicht mehr relevant, weil wir ein Programm schreiben, das die ersten drei Spalten betrachtet und 
die `9` dementsprechend in der vierten Spalte landet.

Um all diesen Problemen vorzubeugen, liefert Python eine eigene sogenannte Bibliothek mit: `csv`
Du hast bereits einige Funktionalitäten von Python kennengelernt – unter anderem Bedingungen und Schleifen, die zum Kern
von Python gehören.
Andere Funktionen, die nicht so oft benötigt werden, sind in die sogenannten Libraries oder auch Bibliotheken
ausgelagert.
Das hat zum Vorteil, dass Python schnell gestartet werden kann, weil es nur die Teile lädt, die es wirklich braucht.
Und wenn du eine bestimmte Funktionalität brauchst (wie beispielsweise das Einlesen von CSV-Dateien), dann kannst du 
diese einfach verwenden, indem du sie importierst.
Damit sagst du Python "Pass auf, ich brauche Funktionen, die habe ich aber nicht selbst geschrieben, sondern die findest 
du in diesem und jenem Buch in der folgenden Bibliothek."

Ein Import ist nichts, wovor man sich fürchten müsste:

```python
import csv
```

Indem du das Schlüsselwort `import` verwendest, weiß Python an der Stelle, dass es jetzt loslaufen muss und in der 
passenden Bibliothek das richtige Buch aus dem Schrank zieht.
Den Namen der Bibliothek gibst du an dieser Stelle an.
Da wir hier nicht weiter spezifizieren, welches Buch wir gerne hätten, holt Python die gesamte Bibliothek.

Es gibt auch den Fall, dass du beispielsweise nur eine Funktion benötigst, dann kannst du das auch wie folgt notieren:

```python
from csv import reader
```

Das bedeutet soviel wie "Aus der Bibliothek `csv` brauche ich nur eine Funktion, und zwar `reader`".

Für unsere Übung können wir aber mit der ersten Variante arbeiten:

```python
import csv
```

Sinnvoll ist es, die Imports immer an den Anfang der Datei zu schreiben, also in den ersten Zeilen, bevor der 
eigentliche Code beginnt.
Damit behält man den Überblick, welche Funktionen aus anderen Bibliotheken man verwendet.

In der Funktion `load_csv` kannst du jetzt dein Können unter Beweis stellen und die Datei mit dem Namen öffnen, der über
den Parameter `filename` geliefert wird.
Der Variable, unter der diese Ressource zur Verfügung steht, kannst du einen beliebigen Namen geben, beispielsweise
also `file`.

Damit haben wir die Ressource geöffnet, können also Daten aus der Datei auslesen.
Anstatt dass wir die Daten nun mittels `readlines` selbst auslesen werden wir die Datei an `csv` übergeben.
Genauer bietet die Bibliothek einen sogenannten _Reader_ an, die die Daten aus der Datei einliest und uns in einem
Format zurückgibt, mit dem wir besser arbeiten können.
Unter anderem werden beispielsweise die "Spalten" in der Datei korrekt aufgeteilt.

Dafür verwenden wir die Methode `reader` aus der Bibliothek `csv`:

```python
lines = csv.reader(file)
```

Damit weisen wir den Computer an, die Datei als CSV-Datei einzulesen und deren Inhalt entsprechend aufzubereiten.

Und über diese Zeilen können wir nun ebenfalls mittels einer `for`-Schleife iterieren:

```python
for line in lines:
```

Statt der Zeile

```
beetsauce,10.6.2022,9
```

erhalten wir eine Liste mit den drei Elementen `beetsauce`, `10.6.2022` und `9`, auf die wir nun einzeln zugreifen
können.
Python kümmert sich also darum, dass die Daten korrekt in ihre einzelnen Bestandteile zerlegt werden.

Nun wollen wir mit diesen Daten arbeiten und sie an die Funktion `highscore_as_text` übergeben.

Die Funktion `highscore_as_text` akzeptiert drei Parameter:
- den Namen der spielenden Person
- das Datum, an dem der Highscore erreicht wurde
- der erreichte Highscore

Daraus generiert die Funktion beispielsweise den Text `beetsauce hat am 10.6.2022 9 Punkte erreicht!`

Doch wie greifen wir jetzt auf die einzelnen Elemente der Liste zu, die wir pro Zeile erhalten?
Dafür können wir sogenannte Indizes verwenden:

Eine Liste hat eine bestimmte Ordnung, die Elemente sind also sortiert.
Wir können beispielsweise auf das erste Element zugreifen, indem wir zum Beispiel

```python
erstes_element = line[0]
```

schreiben.
Dabei gibt man in eckigen Klammern den Index an, auf den man zugreifen will.
In der Informatik ist es üblich, bei dem "nullten" Element zu beginnen, das zweite Element hat dann also den Index `1`
und so weiter.

Jetzt wollen wir die Werte aus der eingelesenen Zeile an die Funktion übergeben.
Dazu müssen wir die drei Parameter `name`, `datum` und `highscore` mit entsprechenden Werten füllen.
Das können wir tun, indem wir die Funktion mit den Argumenten `line[0]`, `line[1]` und `line[2]` aufrufen:

```python
highscore_as_text(line[0], line[1], line[2])
```

Wenn wir diese Funktion aufrufen, dann würden wir ja erwarten, dass der Text auch ausgegeben wird.
Das passiert aber nicht, da wir den Text zurückgeben.
Du kannst das Ergebnis des Funktionsaufrufs in einer Variablen speichern und dann im nächsten Schritt ausgeben oder du
gibst den Rückgabewert der Funktion direkt aus:

```python
print(highscore_as_text(line[0], line[1], line[2]))
```

Führst du das Programm jetzt aus, dann solltest du als erste Zeile die Titelzeile unserer Datei sehen, die die Spalten
beschreibt:

```
name hat am datum punkte Punkte erreicht!
```

Das ist für das Beispiel jetzt nicht kritisch, aber wir wollen diese Zeile dennoch überspringen.
Wie das geht, ist an dieser Stelle dir überlassen.
Du kannst zum Beispiel überprüfen, ob der Name der Person nicht `name` lautet und nur dann die Funktion 
`highscore_to_text` aufrufen.
Bedenke, dass du an dieser Stelle den Code einrücken musst:
Immer, wenn du eine Schleife oder eine Bedingung schreibst, dann muss der nachfolgende Code eine "Stufe" weiter 
eingerückt werden!

Wenn du sicherstellen möchtest, dass eine Variable einen bestimmten Wert **nicht** hat, dann kannst du zum Beispiel 
folgendes schreiben:

```python
a = "Hallo"
b = "Welt"
if a != b:
    print("Die beiden Texte sind unterschiedlich!")
```

So wie du mit `==` überprüfen kannst, ob zwei Werte gleich sind, kannst du mit `!=` feststellen, ob zwei Werte 
unterschiedlich sind.
