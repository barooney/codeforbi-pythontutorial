# Daten filtern

Abschließend wollen wir uns noch damit beschäftigen, wie wir Daten filtern können.

Bevor die Platzkarten gedruckt werden können, wollen wir noch einmal manuell über die Liste schauen und die zu langen
Namen gegebenenfalls selbst kürzen.

Doch wie finden wir jetzt heraus, welche Namen zu lang sind?
Also klar, wir wissen ja, wie lang die einzelnen Namen sind.
Doch wie sortieren wir nun die aus, die kürzer sind?

Wir können Filter auf einen `DataFrame` anwenden.
Dies wollen wir in der Funktion `filter_long_names` tun.

Um einen Filter auf einen `DataFrame` anzuwenden, müssen wir zuerst eine Bedingung definieren, die wir kontrollieren
wollen.
In unserem Fall ist das folgende:

```python
names["length"] >= 14
```

Ist die Länge des Namens größer oder gleich 14.

Nur, wenn das der Fall ist, soll die Zeile ausgewählt werden, andere Zeilen werden dann verworfen.
Die Bedingung an sich hilft uns aber noch nicht so recht, da wir nicht definieren, dass wir diese auch anwenden wollen.
Daher verwenden wir den Parameter `names`, den wir erhalten und notieren dann in eckigen Klammern und zusätzlich dazu 
dann auch nochmal in runden Klammern unsere Bedingungen an die Daten:

```python
return names[(names["length"] >= 14)]
```

In den eckigen Klammern beschreiben wir in diesem Fall nicht, welche Spalten wir verwenden wollen, sondern welche
Bedingungen erfüllt sein müssen, um Zeilen auszuwählen.
Anschließend wird die Liste von Namen, die zu lang sind, ausgegeben, sodass wir diese manuell kontrollieren können.
