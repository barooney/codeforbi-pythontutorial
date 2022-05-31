# Eine eigene Funktion definieren

In der letzten Aufgabe haben wir schon ein paar Funktionen gesehen, die einen Taschenrechner anbieten sollte.
Da diese bereits in Python implementiert sind, werden wir uns auf andere Funktionen konzentrieren.
Dazu greifen wir das Beispiel aus der letzten Übung auf, in der es um die Begrüßung einer nutzenden Person ging.

Nehmen wir an, wir erhalten den Namen der nutzenden Person als Parameter, dann wollen wir eine personalisierte Begrüßung
ausgeben.
Ein Beispiel könnte wie folgt aussehen:

```
Hallo! Wie heißt du? Daniel
Hallo Daniel! Schön dich kennenzulernen!
```

Mit den beiden Funktionen `input` und `print` bist du seit der letzten Übung vertraut.
Nun wollen wir die Funktion `greeting` implementieren, die als Parameter `name` den Namen annimmt.

Funktionen müssen definiert werden – wenn sie nicht definiert ist, dann kann sie auch nicht verwendet werden.
Dazu kennt Python das sogenannte **Schlüsselwort** `def` – eine Abkürzung für `definition`.
Falls dir das Stereotyp noch nicht begegnet ist, dass Informatiker faul sind:
Hier ist der Beweis.
Aber mal ehrlich, Funktionen helfen uns dabei, uns seltener zu wiederholen.
Dabei machen wir uns das Prinzip der Lokalität zunutze:
Wir sorgen dafür, dass etwas an genau einer einzigen Stelle getan wird.
Sollten wir also irgendwann etwas an einer Berechnung verändern, dann müssen wir das genau an einer einzigen Stelle tun.

Um eine Funktion zu definieren, schreiben wir also 

```python
def funktionsname():
```

Damit hat unsere Funktion schon einen eigenen Namen (`funktionsname`), aber einen Parameter benötigt sie ja auch noch.
Deswegen ergänzen wir die Funktionsdefinition in den Klammern um den Parameter `x`:

```python
def funktionsname(x):
```

Hiermit geben wir dem Computer zu verstehen:
Ab jetzt kommt eine Funktion.
Immer, wenn ich die Funktion `funktionsname` aufrufe, dann mache das Folgende.
Dabei müssen wir ein paar Sachen berücksichtigen:
Alles, was zu der Funktion gehört, also immer dann ausgeführt werden soll, wenn die Funktion aufgerufen wird, muss
eingerückt werden.
Das kann beispielsweise mit einem Tab oder Leerzeichen geschehen.
Wichtig ist, dass alle Zeilen, die zu der Funktion gehören, untereinander stehen.
Wir werden gleich noch Ausnahmen kennenlernen, aber für den Moment soll uns diese Definition genügen.

Wenn unsere Funktion nun den mathematischen Ausdruck `3x - 7` auswerten soll, dann können wir das natürlich so 
aufschreiben.
Um aber deutlich zu machen, dass eine Funktion mehrere Schritte haben kann, werden wir diesen Ausdruck in unserer
Funktion in mehrere Schritte zerlegen:

```python
def funktionsname(x):
    zwischenergebnis = 3 * x
    zwischenergebnis = zwischenergebnis -7
    return zwischenergebnis 
```

Wir nutzen eine Variable `zwischenergebnis`, um zuerst `3 * x` zu berechnen.
In einem weiteren Schritt ziehen wir dann 7 von `zwischenergebnis` ab und weisen im selben Schritt diesen neuen Wert
auch wieder der Variable `zwischenergebnis` zu.
Das mag unintuitiv klingen, ist aber nicht schwer zu verstehen:
Du weißt, wie alt du bist (du bist beispielsweise 24 Jahre alt: `alter = 24`).
Wenn du nun Geburtstag hast, dann wirst du ein Jahr älter.
Dafür musst du in der Theorie nicht einmal wissen, **wie** alt du bist – solange du weißt, **dass** du ein Alter hast:

```
alter = alter + 1
```

Diese Zuweisung wäre immer dann gültig, wenn in der Variablen `alter` eine Zahl gespeichert ist.

Ein weiteres Schlüsselwort, das du noch nicht kennst, ist `return`.
`return` erlaubt es dir, die Funktion zu beenden und dorthin zurückzukehren, wo du die Funktion in deinem Programm
aufgerufen hast.
Dabei werden weitere Anweisungen unterhalb von `return` nicht mehr ausgeführt.

Im doppelten Sinne kannst du auch einen Wert zurückgeben – so wie wir oben unser berechnetes Zwischenergebnis
zurückgeben.
So wie wir eine mathematische Funktion ausrechnen, so können wir das Ergebnis auch außerhalb der Funktion
weiterverwenden.
Im Code-Editor siehst du einigen Code, in dem beispielsweise der sogenannte Rückgabewert (Englisch: "return value") in
der Variablen `gruss` gespeichert und anschließend ausgegeben wird.

## Aufgabe

Versuche nun, die Funktion `greeting` zu implementieren.
Sie soll den Parameter `name` annehmen und basierend auf dem Namen eine personalisierte Begrüßung ausgeben.
Hier kannst du eine Form wie `Hallo <Name>! Schön dich zu sehen!` wählen.
Bist du fertig, dann klicke auf "Check" und lasse deinen Code direkt überprüfen.

<div class="hint">
  Du kannst Zeichenketten wie Zahlen miteinander addieren, indem du sie mit einem Plus verbindest.
</div>

<div class="hint">
  Denke daran, die resultierende Zeichenkette mittels <code>return</code> zurückzugeben.
</div>
