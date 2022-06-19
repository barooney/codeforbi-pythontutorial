# Eine Bibliothek einbinden

Wenn wir nun auf eine Bibliothek oder auf eine Funktion daraus zugreifen wollen, dann müssen wir in unserem Programm
darauf verweisen.
Nur so kann Python die Bibliothek laden.

Es könnte eine Bibliothek geben, die eine Funktion `berechne_summe(liste_von_zahlen)` anbietet, gleichzeitig kann es 
aber auch eine andere Bibliothek geben, die dieselbe Funktion anbietet.
Hier wüsste Python nicht, welche Funktion gemeint ist, weswegen wir diese explizit angeben müssen.

Funktionalitäten können auf verschiedene Arten eingebunden werden, die gängigsten werden wir uns ansehen.
Hier kommt es immer auch auf die Bibliothek an, in den meisten Fällen wird dies in der Installationsanleitung oder
anhand eines Beispiels erklärt.

Im nebenstehenden Beispiel wird ein sogenannter `Counter` importiert.
Dieser befindet sich in der Bibliothek `collections`, die Python selbst bereits mitbringt.
Dafür verwenden wir die Schlüsselwörter `from` und `import`:

```python
from collections import Counter
```

`from` gibt an, aus welcher Bibliothek die nachfolgende Funktion importiert werden soll.
`import` gibt dann an, welche Funktionalität in diesem Fall importiert werden soll.

Diese Schreibweise hilft uns dabei, unseren Code kürzer zu fassen.
Eine andere Möglichkeit wäre zum Beispiel, folgende Zeile zu schreiben:

```python
import collections
```

Dann müssten wir aber immer, wenn wir einen Counter verwenden wollen, z.B. `counter = collections.Counter()` schreiben.
Um uns die Schreibarbeit zu sparen, schreiben wir daher explizit auf, welche Funktionalität wir aus dieser Bibliothek
verwenden wollen und können unseren Code dann kürzer fassen.

**Wichtig:** Auf den ersten Blick im Code kann man nicht erkennen, ob eine Bibliothek zu Python selbst gehört oder ob 
diese manuell installiert werden muss.
