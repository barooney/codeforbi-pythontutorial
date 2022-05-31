# Was sind Bedingungen?

"Wenn du deine Hausaufgaben nicht machst, dann gibt es heute kein Abendessen!"
So oder so ähnlich hat jeder diesen Satz wahrscheinlich schon einmal gehört.

Solche Kausalitätszusammenhänge lassen sich (vereinfacht) auch im Computer abbilden.
Der Computer ist eine streng logisch denkende Maschine.
Ihm fallen logische Ausdrücke und Aussagen sehr leicht und wahrscheinlich löst er Aufgaben dieses Typs schneller als du 
selbst – solange man sie ihm begreiflich machen kann.

Um einem Computer Logik nahezubringen, muss man die Aussagen, die man überprüfen möchte, in die sogenannte Boolesche
Algebra überführen.
In dieser haben Ausdrücke nur die Werte "wahr", `True` und `1` oder "falsch", `False` und `0`.

Ein Satz wie "Ich gieße meine Blumen jeden Tag, an dem es nicht regnet oder schneit und mittwochs" ist für uns erstmal
leicht zu erfassen und wahrscheinlich auch manuell schnell auszuwerten.
Sätze wie "Ich mag Bücher, in denen eine Protagonistin mitspielt, die rote Haare hat, und dessen Genre Horror ist oder 
dessen Cover blau-grün ist, aber nur wenn das Genre dann nicht Fantasy lautet, genauso gefallen mir Abenteuerberichte, 
die eine Motorrad-Reise entlang der Ostküste Australiens beschreiben" sind auf den ersten Blick eher schwer zu 
verstehen und nicht so leicht zu prüfen.

Hier haben wir eine Vielzahl an Merkmalen, die wir für ein Buch überprüfen müssen – und bestenfalls widerspricht sich 
keines davon.

Das "Mögen" eines Buches lässt sich also in mehrere unabhängige Bedingungen zerlegen:

Für den ersten Teil des Satzes erkennen wir die folgenden Merkmale:

* Es muss eine Protagonistin geben (A)
* diese muss rote Haare haben (B)
* Das Genre des Buches muss "Horror" lauten (C)

Für den zweiten Teil des Satzes finden wir die folgenden Merkmale:

* Das Cover muss blau-grün sein (D)
* Das Genre darf nicht "Fantasy" lauten (E)

Der letzte Teil beschreibt die Bücher mit diesen Merkmalen:

* Das Genre muss "Abenteuerbericht" sein (F)
* Es muss um eine Motorrad-Reise gehen (G)
* Diese Reise muss an der Ostküste Australiens stattgefunden haben (H)

So weit, so gut.
Wir möchten dieser Person nun ein Buch schenken.
Dank der detaillierten Beschreibung der Wunschlektüre stehen wir nun im Laden und haben eigentlich das perfekte Buch
gefunden:

Wir haben eine Protagonistin mit roten Haaren, das Cover ist blau-grün und es handelt sich um einen Abenteuerbericht.

Wollen wir nun prüfen, ob das Buch infrage kommt, dann müssen wir Schritt für Schritt jedes Merkmal in jeder der drei 
Listen kontrollieren.
Sobald wir für eine der drei Listen alle Merkmale bestätigen können, können wir dieses Buch kaufen.

Fangen wir an:

Wir haben eine Protagonistin, diese hat rote Haare, das Genre ist aber nicht Horror.
Auf die erste Kategorie von Büchern trifft das Buch nicht zu.

Für die zweite Kategorie sieht es besser aus:
Das Cover ist blau-grün und das Genre ist nicht Fantasy – es ist ein Abenteuerbericht.
Top!
Die dritte Kategorie brauchen wir nicht mehr überprüfen, denn wir haben ja eine der drei Schubladen getroffen.

Obwohl wir viele Beschränkungen haben, wie das Buch sein darf und wie nicht, so ist unsere Entscheidung letzten Endes
ein "Ja" oder ein "Nein".
Hier kommen wir wieder zurück zu den Boolschen Ausdrücken.

<div class="hint">
    Für die, die es interessiert:
    Ein Boolscher Ausdruck zu dem Satz oben könnte etwa <code>(A^B^C)v(D^E)v(F^G^H)</code> lauten.
    Die <code>v</code>s stehen dabei für "Oder" und die <code>^</code>s für "Und".
    Es müssen also A, B <strong>UND</strong> C zutreffen <strong>ODER</strong> D <strong>UND</strong> E <strong>ODER
    </strong> F, G <strong>UND</strong> H.
</div>


Wir wollen nicht damit anfangen und diesen Buchauswahl-Algorithmus in Code zwängen.
Es soll nur ein (hoffentlich) anschauliches Beispiel sein, wie solche Bedingungen gestaltet sein können.

Im folgenden Abschnitt schauen wir uns an, wie wir Bedingungen in Python implementieren können.
