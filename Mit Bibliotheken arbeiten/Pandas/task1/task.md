# Daten mit Pandas einlesen

"Pandas" steht für "Python Data Analysis Library" – nicht so offensichtlich, aber umso treffender, wenn man den 
Funktionsumfang betrachtet, den die Bibliothek bietet.

Wie du in der letzten Aufgabe aus dem vorigen Abschnitt schon gesehen hast, geht es bei Pandas ganz oft um sogenannte
`DataFrames`.
`DataFrames` kannst du verstehen wie Tabellen, in denen Daten zeilen- und spaltenweise angezeigt, ausgewertet und
manipuliert werden können.

Wir wollen mit Pandas einige kleine Übungen machen, um ein Gefühl dafür zu bekommen, wie man damit umgeht und welche
Möglichkeiten es gibt, um mit Daten umzugehen.

In diesem Beispiel soll es darum gehen, die Datei `names.csv` einzulesen.
Hierbei handelt es sich wieder um eine CSV-Datei – den Umgang damit hast du in der letzten Übung kennengelernt.
Dieses Mal verwenden wir allerdings Pandas und nicht den CSV-Reader, den Python standardmäßig mitliefert.

Um eine CSV-Datei zu laden, können wir die Funktion `read_csv` verwenden, die `pandas` oder `pd` anbietet:

```python
dataframe = pd.read_csv(filename)
```

Damit erledigen wir innerhalb von einer Zeile das, was mit dem CSV-Reader viele Zeilen benötigt hat – vom Öffnen der 
Datei, das Erzeugen des Readers, das zeilenweise Einlesen der Datei...

Die Funktion `load_names` soll diesen `DataFrame` nun zurückgeben, damit wir damit weiterarbeiten können.
Beispielsweise gibt uns die Methode `head` des `DataFrame` den "Kopf" der Tabelle aus, die er repräsentiert.
Im Normalfall sind das die Titel der Spalten und die ersten fünf Zeilen, jedoch kann man als Parameter angeben, wie 
viele Zeilen man anzeigen lassen möchte.
Da die Datei 20 Zeilen hat, lassen wir uns alle 20 anzeigen.

Versuche nun eigenständig, die Platzhalter im Code zu füllen:

- importiere die Bibliothek Pandas und benenne sie zu `pd`
- lade in der Funktion `load_names` die CSV-Datei, deren Dateiname als Parameter übergeben wird
- speichere den `DataFrame` in einer Variablen
- gib diesen mittels `return` zurück

Wenn du alles richtig gemacht hast, solltest du in der Konsole, wenn du das Programm über den grünen Pfeil neben Zeile
1 ausführst, eine Liste von Namen sehen.
