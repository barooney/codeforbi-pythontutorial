# Was ist PyCharm?

PyCharm ist eine sogenannte *integrierte Entwicklungsumgebung*, kurz **IDE** (Integrated Development Environment) für 
Python.

Während man Python-Skripte auch in einem herkömmlichen Editor schreiben kann, so bietet der Einsatz einer IDE den
Vorteil, dass man viele Werkzeuge an einem Ort vereint, die sonst an verschiedenen Stellen zu finden und kompliziert zu
bedienen sind.

Gängige Editoren sind beispielsweise:

* Notepad (Windows)
* TextEdit (macOS)
* GEdit (Linux)

Während sie in der Erfassung von Text unschlagbar sind, so sind sie für das Schreiben von Code denkbar ungeeignet, da
sie keinerlei Unterstützung bei der Entwicklung von Software bieten.
Eine IDE hingegen analysiert deinen Code und erkennt, wenn du etwas vergessen hast oder macht dir Vorschläge, wie man
etwas besser programmieren kann.

## Syntax und Semantik - die Rechtschreibung von Programmen

Schaust du in den Code zu dieser Aufgabe, dann siehst du, dass eine IDE ähnlich wie ein Textverarbeitungsprogramm
funktioniert.
Die unterschlängelten Begriffe zeigen dir an, dass etwas entweder falsch oder unvollständig ist (wie im ersten
Beispiel).
So wollen wir den Wert einer Addition berechnen – allerdings haben wir nur einen Wert angegeben.
Hier fehlt also offensichtlich noch etwas, damit der Computer weiß, was er an dieser Stelle zu tun hat, wenn wir unser
Programm ausführen wollen.
PyCharm liefert also so etwas wie eine Rechtschreibkorrektur mit.

Du kannst an der Stelle, wo `#füge hier eine Zahl deiner Wahl ein.` steht, eine beliebige Zahl eintippen, um den roten
Schlängel in der Zeile zu entfernen.

Das zweite Beispiel ist nicht falsch, wird aber dennoch gelb unterschlängelt.
Hier haben wir ein Beispiel, das die IDE gerne "umformulieren" möchte.
Der Code, der dort steht, funktioniert, entspricht aber nicht dem vorgeschlagenen "Stil".

Während PyCharm uns bei dem ersten Beispiel nicht so recht weiterhelfen kann, weil es nicht weiß, was wir addieren 
wollen, kann uns PyCharm im zweiten Beispiel helfen, unseren Code lesbarer zu machen.
Dafür gibt es die Kurzbefehle, die an entsprechenden Stellen verwendet werden können.
Klickst du auf die gelb unterschlängelte Zeile und drückst dann Strg-Enter (unter macOS Alt-Enter), dann erscheint ein
kleines Hilfsfenster.
Die Glühbirne signalisiert eine "Idee" von PyCharm und schlägt dir vor, diesen Ausdruck zu vereinfachen.
Wenn du in dem Kontextmenü nun auf "Simplify chained comparison" klickst, wird der Ausdruck lesbarer:

```
if 0 < gepflanzte_baueme < 4:
```

Wir können PyCharm also nutzen, um unseren Code lesbarer zu machen.
Auf den ersten Blick erkenne ich nun, dass der Wert `gepflanzte_baeume` zwischen 0 und 4 liegen muss, damit etwas
bestimmtes passiert.

Im dritten und letzten Beispiel ist eigentlich alles richtig, bloß haben wir einen kleinen Fehler gemacht, als wir eine
Berechnung durchführen wollten.
Statt `a - b` zu rechnen, ziehen wir von dem Wert `a` jetzt einfach immer 5 ab.
An der Stelle werden wir von PyCharm darauf aufmerksam gemacht, dass wir uns mehr Arbeit gemacht haben als notwendig.
In den Klammern haben wir die beiden sogenannten Parameter `a` und `b` angegeben, verwendet wird aber nur `a`.
Das `b` ist gräulich dargestellt.
Drückst du jetzt wieder Strg-Enter (unter macOS Alt-Enter), dann kannst du den Vorschlag "Remove Parameter" auswählen.
Damit verschwindet das `b` aus den Klammern.

Was genau all diese Dinge bedeuten, die da stehen, ist noch nicht so wichtig.
Du hast jetzt die wichtigste Komponente in Bezug zum Code-Editor in PyCharm gelernt: die "Rechtschreibkorrektur".

## Ausführen von Code

Du willst dein Programm ausführen?
Es wäre ja sehr umständlich, wenn das nicht aus PyCharm heraus ginge.
Deswegen zeigt PyCharm dir in einigen Dateien einen grünen "Play"-Pfeil in der ersten Zeile an, den du anklicken kannst.
Hast du den Fehler im ersten Beispiel behoben und eine Zahl eingefügt, dann kannst du das Programm ausführen.

Am unteren Fensterrand von PyCharm erscheint das "Run"-Fenster, das dir anzeigt, was dein Programm getan hat - 
beispielsweise, welchen Text es ausgegeben hat - in unserem Fall nur "Hallo Bielefeld!"

Nun wieder eine kleine Fragerunde zur Selbstkontrolle:

**Was grenzt PyCharm als IDE von Texteditoren ab?**

