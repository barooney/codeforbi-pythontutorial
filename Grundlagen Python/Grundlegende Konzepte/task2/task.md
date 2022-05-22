# Eingaben und Ausgaben

Algorithmen nutzen Daten.
Diese Daten kann man entweder manuell erfassen oder aus Dateien laden – oder direkt von einem Server in das eigene
Programm einfließen lassen.

Wir wollen nun ein kleines Programm schreiben, das nach dem Namen der nutzenden Person fragt.
Anschließend wollen wir eine personalisierte Begrüßung ausgeben.

Python bietet die beiden Methoden `input` und `print` an, mit denen wir über unser Programm kommunizieren können.

## Eingabe

`input` ist eine Funktion, mit der wir eine Eingabe anfordern können:

```python
eingabe = input()
```

Wenn wir diese Zeile in unseren Code schreiben und das Programm ausführen, dann taucht unten das "Run"-Fenster auf, es
passiert aber nichts weiter.
Das ist richtig, weil das Programm darauf wartet, dass du Text eingibst.
Erst, wenn du auf Enter drückst, wird deine Eingabe verarbeitet und wird dann beispielsweise in `eingabe` gespeichert.

`eingabe` ist dabei eine Variable.
Du kannst dir eine Variable wie eine große Box vorstellen, in der du alles verstauen kannst.
Auf die Box klebst du dann die Beschriftung `eingabe` und immer, wenn du wissen willst, was die Eingabe war, dann kannst
du die Box hervorholen und hineinschauen.

Du kannst allerdings auch wieder etwas anderes in die Box legen:

```python
eingabe = input()
eingabe = "Mir gehts gut und selbst?"
```

Der alte Wert – zum Beispiel der Name, nach dem wir gefragt haben, ist dann aber weg.

Die Funktion `input` erlaubt uns aber auch, noch einen Text mitzugeben, der angezeigt werden soll, wenn die nutzende
Person etwas eingeben soll:

```python
name = input("Wie heißt du? ")
```

## Ausgabe

Nachdem wir einen Namen erhalten haben wollen wir die nutzende Person nun auch mit ihrem Namen begrüßen.

Dafür nutzen wir den Befehl `print`, der historisch gesehen früher wirklich etwas ausgedruckt hat, heute aber Text auf
dem Bildschirm ausgibt:

```python
print("Hallo Bielefeld!")
```

In den Klammern geben wir den sogenannten Parameter an, der ausgegeben werden soll.
Wir können zum Beispiel auch den Namen ausgeben.
Dazu können wir folgenden Code schreiben:

```python
print(name)
```

Um verschiedene Texte zusammen auszugeben, können wir diese mit einem Plus verbinden:

```python
name = input("Wie heißt du?")
print("Hallo " + name)
```

**Kannst du auch nach einem Nachnamen fragen und in der Form "Vorname Nachname" und "Nachname, Vorname" ausgeben 
lassen?**
