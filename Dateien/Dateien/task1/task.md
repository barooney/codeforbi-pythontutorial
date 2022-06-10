# Was sind Dateien?

Für die meisten sind Dateien etwas Alltägliches bei der Arbeit mit dem Computer.
Doch aus was bestehen Dateien eigentlich genau?
Und wo ist der Unterschied zu Daten?

Du hast sicher schon mal mit Word und Excel gearbeitet und kennst entsprechend auch Word-Dokumente und Excel-Tabellen.
Diese Dateien haben in den meisten Fällen die Endungen `.docx` oder `.xlsx`.
Daran erkennt Windows, welches Programm es verwenden soll, um die Datei zu öffnen.
Linux und macOS nehmen die Dateiendung zwar zur Kenntnis, diese Systeme verlassen sich aber nicht darauf, dass die
Dateiendung auch wirklich zu dem Inhalt passt, der in der Datei gespeichert ist.
Die Systeme schauen in die Datei und versuchen anhand der ersten paar Zeichen zu ermitteln, um welchen Dateityp es sich
handelt.

In unserem Fall und mit unseren Dateien soll uns das nicht weiter stören, wir werden mit reinen Text-Dateien arbeiten.
Damit können wir unsere Text-Dateien auch dann bearbeiten, wenn wir kein Word zur Hand haben.
Doch was ist eine reine Text-Datei?
Im Falle von Word gibt es Formatierungen - Dinge wie fett gedruckten Text, unter- oder durchgestrichenen Text und
Hervorhebungen wie beispielsweise Überschriften.

In reinem Text verzichten wir nicht auf Auszeichnungen, wir sind jedoch etwas limitiert, was die Auszeichnungen angeht.
Wir sind nicht völlig aufgeschmissen, da es beispielsweise Formate wie
[Markdown](https://daringfireball.net/projects/markdown/) gibt, die es erlauben, auch in einfachen Textdateien 
entsprechende Auszeichnungen vorzunehmen.
Wir wollen uns damit aktuell nicht weiter beschäftigen, aber ein Blick über den Tellerrand schadet nie!

In unseren Dateien steht also reiner Text, den man als Mensch lesen und verstehen kann und keinen Computer benötigt, um
den Inhalt zu verstehen.
Ein Word-Dokument ist in den meisten Fällen ein ZIP-Archiv, das man entpacken kann und dann viele weitere Dateien und 
Ordner dabei zum Vorschein kommen.
Als Mensch ein ZIP-Archiv auf dem Papier zu entpacken ist möglich, aber offensichtlich nicht komfortabel.

Unser reiner Text sind also unsere Daten – und werden in Dateien gespeichert.
Wie das im Detail funktioniert ist auch ein spannendes Thema, damit werden wir uns an dieser Stelle aber nicht 
detaillierter beschäftigen, da es für die Programmierung nicht notwendig ist.
Wir akzeptieren, dass unser Betriebssystem (Windows, Linux oder macOS) die Dateien für uns organisiert und wir sie über
einen Dateinamen in einem Ordner identifizieren können.

Wenn wir eine Datei in Python öffnen, dann sprechen wir nicht mehr von Dateien, sondern von Ressourcen, auf die wir 
zugreifen können.
Jede Datei ist eine Abfolge von Zeichen und wir können von einer Ressource eine bestimmte Menge an Zeichen (oder 
Informationen) anfordern.
Am Ende der Ressource (wenn wir alle Zeichen aus der Datei eingelesen haben) müssen wir diese wieder freigeben, da sonst
unter Umständen das Betriebssystem die Datei nicht mehr löschen kann, falls du das tun willst.
Das Betriebssystem merkt sich, dass ein Programm auf eine Datei zugreift.
Das Programm ist dann aber dafür zuständig, dem Betriebssystem Bescheid zu sagen, dass die Datei nicht mehr verwendet
wird.
Tut das Programm das nicht, dann hat das besagte Nebeneffekte, dass man Dateien beispielsweise nicht mehr löschen kann,
bis man den Computer neu startet (und die Liste von Programmen, die auf die Datei zugreifen wollen, gelöscht wird).

Wenn du das nebenstehende Programm ausführst, dann wirst du sehen, dass der Text "Hallo Welt!" aus der Date `file.txt`
ausgelesen wird.
Änderst du den Text in der Datei und speicherst sie, dann gibt auch das Programm anderen Text aus.
Damit wird dein Code zu einem großen Teil unabhängig von deinen Daten, die du einlesen oder analysieren möchtest.
Hier spielen auch wieder Funktionen eine Rolle:
Solange deine Daten ein bestimmtes Format haben, kannst du sie mit deinem Programm auswerten.
Dieses Format schreibt der Code vor, den du entwickelst.
Oftmals gibt es bereits Daten, die du auswerten möchtest.
Dann wirst du dich eher nach dem Format richten, das du erhältst.
Das ist aber immer abhängig vom Anwendungsfall:

Gibt es bereits viele Daten in einem Format und du beginnst damit, eine Analyse dieser Daten vorzunehmen, dann kann es
sinnvoll sein, dein Programm so zu entwickeln, dass es mit den Daten zurechtkommt.
Hast du bereits eine Software entwickelt und möchtest Daten einlesen, die nicht zu deinem Code passen, dann wirst du
eher die Daten in ein Format umwandeln, das dein Code einlesen und verarbeiten kann.

Um das Gelernte zu vertiefen, gibt es nun wieder einige Aussagen.
Kreuze die richtigen an:
