# Dateien einlesen

Du hast im Beispiel eben schon gesehen, dass Dateien einlesen in Python in wenigen Zeilen geht.
Doch so unkommentiert soll das nicht stehen bleiben.

In der Datei `chat.txt` gibt es einige fiktive Chat-Nachrichten, die beispielsweise in einem 
[Twitch](https://www.twitch.tv/)-Stream geschrieben werden könnten.
Eine Zeile entspricht dabei einer Nachricht:

```
<Benutzername>: <Nachricht>
```

In einem anderen Fall kann die Nachricht aber auch bedeuten, dass ein Zuschauer der streamenden Person nun folgt:

```
<Benutzername> folgt dir jetzt!
```

Wir wollen die Datei nun einlesen und herausfinden, ob ein Nutzer eine Nachricht geschrieben hat oder ob er folgt.
Dafür müssen wir die Datei in der Funktion `load_chat` zuerst öffnen, diese referenzieren wir über den Dateinamen, also
den Parameter `filename`.

## Datei öffnen

Im folgenden Abschnitt lernen wir einige neue Schlüsselwörter von Python kennen, die uns die Arbeit an vielen Stellen
vereinfachen wird.
Mit dem Sprachkonstrukt `with <Ressource> as <Variablenname>` sorgen wir dafür, dass wir eine Ressource verwenden können
und Python sich darum kümmert, wenn wir sie nicht mehr benötigen.
Dabei beschreibt der Teil zwischen `with` und `as` die Ressource (in unserem Fall also die geöffnete Datei) und der Teil
nach `as` die Variable, über die wir mit der Datei interagieren können.

Die verwendete Variable kann dann im folgenden Block verwendet werden, um auf die Ressource zuzugreifen und Daten daraus
auszulesen oder auch zu schreiben.
Zum Schreiben in Dateien kommen wir später nochmal genauer, das Auslesen der Dateien wollen wir uns im Moment genauer 
anschauen.

Das nächste Schlüsselwort bzw. die in Python integrierte Funktion ist `open`.
Diese Funktion akzeptiert mindestens ein Argument und kann mit weiteren Argumenten zum Beispiel verschiedene sogenannte
Encodings einlesen.
In unserem Beispiel benötigen wir das jedoch nicht, für andere Fälle lohnt sich ein Blick in die 
[Dokumentation](https://docs.python.org/3.9/library/functions.html#open) der Funktion.

Wollen wir beispielsweise die Datei `chat.txt` öffnen, dann benötigen wir den Aufruf `open("chat.txt")`.
Ein weiterer, sinnvoller Parameter ist der _Modus_, in der die Datei geöffnet wird.
Standardmäßig wird eine Datei im "Nur-Lesen"-Modus geöffnet – wollen wir dies explizit angeben, dann schreiben wir
`open("chat.txt", "r")`.
Das `"r"` im zweiten Parameter steht dabei für das Englische _read_.
Genauso kann eine Datei mit dem Modus `"w"` geöffnet werden, um in die Datei zu Schreiben (Englisch _write_).
Alternativ kann die Datei auch im _read write_-Modus `"rw"` geöffnet werden.
Damit kann man Daten aus der Datei auslesen und beispielsweise neue Daten zurückschreiben.

Versuche nun, die Zeile zu vervollständigen, indem du die Datei, deren Dateinamen du in dem Parameter `filename` 
erhältst, im Lese-Modus öffnest und in einer Variablen, beispielsweise `chat` speicherst.

## Daten auslesen

Nachdem die Datei geöffnet ist, wollen wir nun Informationen aus der Datei auslesen.
Dafür werden wir eine Schleife verwenden, die du bereits in der vorigen Übung kennengelernt hast.
Wenn du dich an die Korrekturschleifen in einer Agentur erinnerst, dann ist es nicht ganz klar, wie viele es davon geben
wird.
Genauso ist es auch mit den Zeilen in einer Datei – du kannst nicht genau vorhersagen, ob eine Datei eine oder eine 
Million Zeilen hat.
Deswegen können wir hier nicht mit einer fixen Zahl arbeiten, da wir gegebenenfalls versuchen, mehr Zeilen zu lesen, als
in der Datei vorhanden sind (das führt zu einem Fehler) oder wir lesen nicht alle Zeilen aus, was dazu führt, dass unser
Programm nicht auf alle Daten zugreifen kann oder unsere Auswertungen gegebenenfalls falsch sind.

Wir arbeiten nun mit einer `for`-Schleife.
Eine kurze Erinnerung, wie diese Schleifen aussehen können:

```python
for i in range(1, 11):
    print(i)
```

Dabei werden für `i` die Werte 1 bis 10 eingesetzt und dann alles ausgeführt, was eingerückt im sogenannten Block 
darunter steht, also in diesem Fall die Zahl selbst ausgegeben.

Bei den Dateien ist das nicht anders, bloß werden wir für das `i` und `range(1, 11)` andere Begriffe und Funktionen
einsetzen.
Zum einen wollen wir Zeilen aus der Datei lesen, also sollten wir `i` zum Beispiel zu `line` (Englisch für Zeile)
umbenennen.
Und für `range(1, 11)` wollen wir jetzt auf die Zeilen der Datei zugreifen.
Dafür können wir auf eine sogenannte _Methode_ unserer Ressource zugreifen: `readlines()`

Methoden sind Funktionen, die nicht alleinstehend aufgerufen werden können, sondern zum Beispiel nur für Dateien zur
Verfügung stehen.
Statt `range(1, 11)` könnten wir daher zum Beispiel `chat.readlines()` notieren.
`chat` ist dabei unsere Ressource, dann folgt ein Punkt und dann die Methode, die wir auf dieser Ressource aufrufen
wollen – in diesem Fall `readlines()`.
Wir sehen später noch mehr Beispiele für Methoden zum Beispiel für Zeichenketten.

Versuche nun, die Schleife zu vervollständigen.

## Daten ausgeben

Zu guter letzt wollen wir die Daten jetzt wieder ausgeben, um zu kontrollieren, ob unser Programm funktioniert.
Um das zu kontrollieren, kannst du mittels der Funktion `print` jede einzelne Zeile ausgeben, die in der Schleife
eingelesen wird.
Wie das geht, weißt du bereits.

Was dir auffallen dürfte, ist die Tatsache, dass zwischen jeder Zeile in der Ausgabe deines Programms eine Leerzeile 
auftaucht.
Warum ist das so?
Immer, wenn du `print` aufrufst, wird am Ende deines Textes eine neue Zeile begonnen.
Jede Zeile des Textes, den du einliest, hat allerdings auch noch einen Zeilenumbruch am Ende.
Dieser Zeilenumbruch wird ebenfalls mit ausgegeben.
In den meisten Fällen benötigt man diesen jedoch nicht, sodass man ihn entfernen kann.

Dafür können wir die Methode `strip` von Zeichenketten verwenden.
Sie entfernt Leerzeichen, Tabs, Zeilenumbrüche und viele andere Zeichen, die keine Buchstaben oder Zahlen sind, vom 
Anfang und Ende einer Zeichenkette.
Damit wird eine Zeichenkette wie 

```
    Hier steht Text!
    
```

zu

```
Hier steht Text!
```

Du hast mehrere Möglichkeiten, die Zeilenumbrüche zu entfernen:
Entweder du rufst die Methode auf und speicherst ihr Ergebnis in derselben Variable, zum Beispiel wie folgt:

```python
line = line.strip()
```

Oder du entscheidest dich dazu, deinen Code kürzer zu schreiben und rufst `strip` direkt auf dem Argument der 
`print`-Funktion auf:

```python
print(line.strip())
```

Beides ist möglich, beides hat seine Vor- und Nachteile:

Im ersten Beispiel ist dein Code wesentlich besser lesbar und es ist klar nachvollziehbar, was in dieser einen Zeile 
passiert.
Im zweiten Beispiel passieren gleich mehrere Dinge:
Zum einen wird die Zeichenkette gekürzt, zum anderen wird sie dann auch gleich ausgegeben.

Im ersten Beispiel veränderst du die Zeichenkette – möchtest du später damit weiterarbeiten hast du dazu keine
Möglichkeit mehr.
Im zweiten Beispiel entfernst du die Zeichen ausschließlich für die Ausgabe.

Beide Vorgehen haben ihre Daseinsberechtigung, es kommt auf den Verwendungszweck an, den du umsetzen willst.
