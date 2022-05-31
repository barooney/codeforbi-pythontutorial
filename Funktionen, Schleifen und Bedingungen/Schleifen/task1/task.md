# Was ist eine Schleife?

Schleifen kennen wir meistens von Geschenken.
Die Schleifen, von denen wir in Python sprechen, sind ähnlich dazu – meistens nicht rund, aber wenn man will, dann kann
man immer wieder von vorne anfangen, wenn man das Geschenkband mit dem Finger entlangfährt.

Im Agenturalltag kennt man den Begriff Korrekturschleifen, in denen ein Kunde Änderungen an den Produkten, 
beispielsweise einer Webseite, äußert.
Anschließend nehmen die Entwickler die Änderungen vor und präsentieren dem Kunden das Ergebnis erneut.
Ist der Kunde noch immer nicht zufrieden, so wird erneut eine Korrekturschleife angehängt.

Wir können eine solche Schleife formal beschreiben.
Dabei gibt es Unterschiede, wie lange solche Schleifen ausgeführt werden.
Bei den Korrekturschleifen ist das (potenziell) eine unendlich lange Schleife, wenn der Kunde nie zufrieden ist.
Wenn du im Fitnessstudio bist und dir vornimmst, eine Übung zehnmal zu wiederholen, dann ist das sehr überschaubar.

Für die Korrekturschleife ließe sich das also wie folgt formulieren:

```
Solange der Kunde Änderungswünsche hat ist folgendes zu tun:
  - nimm die Änderungen vor
  - zeige sie dem Kunden
  - Warte auf die Änderungswünsche
```

Im Fitnessstudio würde die Formulierung etwas anders lauten:

```
Wiederhole zehnmal folgende Übung:
  - Bankdrücken 50kg
```

Letzten Endes werden beide Schleifen für den Computer in dieselbe Form gebracht, jedoch lassen sie sich verschieden
ausdrücken, um dem natürlichen Sprachgebrauch etwas näher zu sein.
Wir wollen uns für diese Übung mit `for`-Schleifen beschäftigten.
Diese entsprechen dem Fitnessstudio-Beispiel.
Dazu brauchen wir noch etwas Hintergrundwissen zu Variablen in Python, genauer gesagt benötigen wir noch etwas Wissen 
über sogenannte Listen.

Eine Liste in Python ist nichts anderes als die Verkettung von verschiedenen Variablen und/oder Werten.
Diese Listen können dann wiederum in Variablen gespeichert werden.
Eine Liste kann beliebig viele Elemente haben, Elemente können hinzugefügt oder entfernt werden.
Theoretisch funktioniert eine Liste in Python wie eine Einkaufsliste, auf die man schreibt, was man einkaufen will und 
durchstreicht, was man bekommen hat.

Beginnen wir mit einem Einkauf, dann können wir anhand der Liste von oben nach unten zu jedem Artikel im Laden gehen und
diesen in den Einkaufswagen legen.
Wir gehen dabei _iterativ_ vor und nehmen immer einen Artikel, haken ihn ab und gehen dann zum nächsten.
Haben wir die Liste abgearbeitet, dann verlassen wir die Schleife und setzen das Programm an der Stelle nach der 
Schleife fort.

Im Code-Editor siehst du schon eine beispielhafte Schleife.
Sie wird mit dem Schlüsselwort `for` eingeleitet.
Dann folgt ein Variablenbezeichner und dann das Schlüsselwort `in`.
Nun folgt eine Liste – in diesem Fall verwenden wir die Funktion `range`, die uns eine Liste von Zahlen von einem 
Startwert – hier die 1 – bis zu einem Endwert – hier die 10 – liefert.

Warum 10, wenn im Code 11 steht?
Python (und Computer allgemein) beginnen bei der 0 zu zählen.
Wenn ich die Funktion `range` nur mit dem Argument 10 aufrufe, dann erhalte ich eine Liste mit zehn Elementen.
Dabei ist das erste Element die 0 und das letzte Element die 9.
Gebe ich zwei Argumente an – also Start- und Endwert, dann verschiebt sich alles, weswegen diese Korrektur notwendig 
ist.

Um eine Liste auszugeben, können wir wieder die Funktion `print` verwenden.
Führst du das Programm aus, so siehst du zehnmal "Hallo" und dann die Zeile `range(1,11)`.
Diese Repräsentation ist an der Stelle nicht wirklich hilfreich, wenn du wissen willst, welche Zahlen nun wirklich in 
der Liste vorhanden sind.
Deswegen gibt es die Funktion `list`.
Übergibst du dieser Funktion eine Liste, so werden die einzelnen Elemente aufgelöst und die Liste mit ihren Elementen
dargestellt:
`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`

Um dein Wissen zu Schleifen und Listen zu vertiefen kannst du jetzt die richtigen Aussagen unterhalb dieser Übung
ankreuzen und dann mit der nächsten Aufgabe weitermachen.
