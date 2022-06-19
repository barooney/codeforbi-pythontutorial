# Neue Bibliotheken installieren

Neue Bibliotheken können über die Kommandozeile installiert werden.
Das ist in vielen Fällen sinnvoll, zum Beispiel wenn man ein Projekt nur verwenden will, das jemand anderes bereits
programmiert hat.

Die meisten Projekte liefern eine Datei mit, die `requirements.txt` heißt.
Ist eine solche Datei vorhanden, dann lassen sich die notwendigen Bibliotheken mittels des Programms `pip`
(**P**ip **I**nstalls **P**ackages) herunterladen und installieren.
Dazu navigiert man zu dem Ordner, in dem die Datei liegt und ruft dann folgenden Befehl auf:

```bash
pip install -r requirements.txt 
```

Da wir in PyCharm arbeiten und diese Datei (noch) nicht besitzen, werden wir vorerst auf die Funktionalität unserer IDE
zurückgreifen:

Im nebenstehenden Beispiel wird ein sogenannter `DataFrame` erzeugt.
Dieser stammt aus der Bibliothek `pandas`.
`pandas` ist eine Bibliothek, die nicht zur Grundausstattung von Python gehört – sie muss nachträglich installiert 
werden.
Dies wollen wir nun tun, indem wir sie importieren:

Schreibe dazu die Zeile

```python
import pandas
```

in die erste Zeile der Datei.
PyCharm wird dir nun `pandas` rot unterschlängeln und dich somit darauf hinweisen, dass hier etwas nicht stimmt.
Du kannst mittels Klick auf die rote Glühbirne und dann im sich öffnenden Kontextmenü "Install pandas" auswählen.
Oder du öffnest das Menü mittels Tastendruck auf Strg-Enter bzw. Alt-Enter und wählst dann dieselbe Option aus.

Nun siehst du am unteren Rand von PyCharm eine Fortschrittsanzeige, die dich darüber informiert, was gerade getan wird.
PyCharm installiert jetzt mehrere Dinge:
Zum einen die Bibliothek `pandas` und zum anderen auch `numpy` (eine weitere Bibliothek zur Berechnung von 
verschiedenen Dingen) sowie weitere Abhängigkeiten.
Du merkst schon:
Eine Bibliothek kommt selten allein!

Wenn du dir den Code nun noch einmal anschaust, dann dürfte dir auffallen, dass wir statt `pandas` `pd` schreiben.
Das ist gängige Praxis, denn Programmierer sind faul und kürzen Dinge ab, wo es irgend möglich ist.
Deswegen können wir die Zeile `import pandas` oben um den Zusatz `as pd` ergänzen:

```python
import pandas as pd
```

Damit definieren wir, dass wir die Bibliothek `pandas` verwenden wollen, aber statt `pandas` zu schreiben, wollen wir 
sie mit `pd` abkürzen.

Hast du die Bibliothek `pandas` erfolgreich importiert und den Alias `pd` verwendet, dann kannst du nun auf "Check"
klicken und deine Eingabe überprüfen lassen.
