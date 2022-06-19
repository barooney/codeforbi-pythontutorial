# Daten verändern und hinzufügen

Nachdem wir unsere Namen erfolgreich eingelesen haben, wollen wir nun einige Veränderungen daran vornehmen.

Wir wollen Platzkarten für ein Abendessen drucken.
Zum einen haben wir einen Namen falsch geschrieben, den müssen wir zuerst korrigieren.
Dann haben wir außerdem eine Absage erhalten, die wollen wir aus unserer Gästeliste auch entfernen.

Falls der Name einer Person zu lang ist, dann müssen wir ihn abkürzen, damit er auf die Platzkarte passt.
Dazu müssen wir auch wissen, wie lang die Namen sind.

## Eine Zelle bearbeiten

Um einen einzelnen Wert zu verändern, können wir die Eigenschaft `at` des `DataFrames` verwenden:

```python
df.at[0, "firstname"]  = "Neuer Name"
```

Dabei geben wir innerhalb der eckigen Klammern erst die Zeile und dann mit einem Komma getrennt die Spalte an, auf die
wir zugreifen wollen.
Genauso können wir auch darauf zugreifen und den Text, der darin steht, ausgeben:

```python
print(df.at[0, "firstname"])
```

Die Eigenschaft `at` gibt uns Zugriff auf alle "Felder" in unserer "Tabelle" und wir können darüber Daten auslesen oder
auch verändern.

## Eine Zeile löschen

Wenn du das Programm ausführst, dann stellst du fest, dass Asif Ramos den Index 17 erhalten hat.
Diese Zeile wollen wir entfernen.

Dazu gibt es die Funktion `drop`, die wir auf dem `DataFrame` ausführen können.
Dabei wird die Zeile gelöscht, die Funktion gibt uns dann einen neuen `DataFrame` zurück, den wir uns an Stelle des 
alten merken wollen:

```python
df = df.drop(92) # Löscht die Zeile mit dem Index 92
```

## Weitere Informationen zur Tabelle hinzufügen

Wir wollen nun eine weitere Spalte hinzufügen, in der wir Vor- und Nachname zusammen stehen haben.
Dafür können wir etwas Magie verwenden, die Pandas uns mit den `DataFrames` liefert:
Wir definieren beispielsweise eine neue Spalte `"company_name"` innerhalb unseres `DataFrames` und greifen dabei auf
die Spalten zu, die wir mit weiterem Text zusammenfügen wollen:

```python
df["company_name"] = df["lastname"] + " GmbH"
```

Genauso können wir weitere Spalten hinzufügen.
Deine Aufgabe ist es, eine Spalte `fullname` zu dem `DataFrame` hinzuzufügen, der aus dem Vornamen `Riley` und dem 
Nachnamen `Ryan` den vollen Namen `Riley Ryan` macht.
Achte hierbei auf das Leerzeichen!

## Länge von Zeichenketten in DataFrames ermitteln

Nun wollen wir noch eine Spalte `"length"` zu unserem `DataFrame` hinzufügen, die die Länge der Namen in Zeichen
beinhalten soll.
Der Name "Riley Ryan" hat damit beispielsweise zehn Zeichen – fünf für "Riley", vier für "Ryan" und ein Leerzeichen.

Um eine Spalte zum `DataFrame` hinzuzufügen, so haben wir jetzt gelernt, können wir eine neue Spalte definieren und ihr
einen Wert zuordnen:

```python
df["length"] = 0
```

Damit hätte jeder Name standardmäßig die Länge null, was ja falsch ist.

Doch wie erhalten wir nun die Länge des Namens?
Offensichtlich wollen wir auf die Spalte `"fullname"` zugreifen.
Python bietet die Funktion `len` an, die die Länge einer Zeichenkette zurückgibt, doch wenn wir `len(df["fullname"])` 
angeben, dann erhalten wir immer den Wert 19, weil in der Spalte 19 Elemente vorhanden sind.
Pandas bietet jedoch die Eigenschaft `str` an, die man auf einer Spalte anwenden kann.
Und auf dieser Eigenschaft lässt sich die Funktion `len` aufrufen.

Damit können wir die Länge jedes Namens also wie folgt in der Tabelle festhalten:

```python
df["length"] = df["fullname"].str.len()
```

Damit können wir nun sehen, dass die Namen zwischen 10 und 14 Zeichen lang sind.
In der folgenden Aufgabe wollen wir uns um die Personen kümmern, deren Name zu lang ist.
