EXERCISE = {
    "id": "0044",
    "subject": "Mathe",
    "grade": 4,
    "title": "Vorbereitung Probeunterricht – Geometrie",
    "topic": "Geometrie",
    "publisher": "CATLUX",
    "source_pdf": "0044.pdf",
    "answer_pdf": "0044 (1).pdf",
    "total_points": 36.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Körper analysieren",
        "text": (
            "Betrachte die Körper A und B.\n"
            "Beantworte für jeden Körper:\n"
            "– Aus wie vielen Würfeln bestehen die Körper?\n"
            "– Wie viele Würfel fehlen zum Würfel?\n"
            "– Wie viele Würfel musst du mindestens hinzufügen, damit ein Quader entsteht?\n"
            "Zeichne außerdem die Baupläne zu den Körpern A und B!"
        ),
        "answer": (
            "A: 10 Würfel, 17 fehlen zum Würfel, 8 hinzufügen für Quader.\n"
            "B: 10 Würfel, 17 fehlen zum Würfel, 8 hinzufügen für Quader.\n"
            "Bauplan A: 3 Ebenen (oben: 1-1-1, mitte: 2-1-1, unten: 3-2-1).\n"
            "Bauplan B: 3 Ebenen (oben: 1-1-1-1, mitte: 1-2-1, unten: 1-1-1-1)."
        ),
        "steps": [
            "Würfel abzählen: A = 10, B = 10",
            "Zum Würfel fehlen: A = 3×3×3 – 10 = 27 – 10 = 17, B = 17",
            "Für Quader mindestens hinzufügen: kleinste Quaderform bestimmen; A und B je 8",
            "Bauplan: Draufsicht mit Zahl der gestapelten Würfel pro Position eintragen",
        ],
        "points": 1.0,
        "has_image": True,
        "image": "0044_q1_koerper_AB.png",
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
        ],
    },
    {
        "n": 2,
        "type": "Quader ergänzen",
        "text": (
            "Wie viele Würfel musst du hinzufügen, bis ein Quader entsteht?\n"
            "Aus wie vielen Würfeln besteht dann der Quader?\n"
            "Beantworte für alle drei abgebildeten Körper (je a und b)."
        ),
        "answer": (
            "Körper 1: a) 80 hinzufügen, b) 100 Würfel gesamt.\n"
            "Körper 2: a) 35 hinzufügen, b) 45 Würfel gesamt.\n"
            "Körper 3: a) 52 hinzufügen, b) 80 Würfel gesamt."
        ),
        "steps": [
            "Vorhandene Würfel zählen",
            "Kleinste Quaderform bestimmen, die den Körper umschließt",
            "Fehlende Würfel = Quadervolumen – vorhandene Würfel",
        ],
        "points": 1.0,
        "has_image": True,
        "image": "0044_q2_quader_ergaenzen.png",
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
        ],
    },
    {
        "n": 3,
        "type": "Würfel mit Farbe bemalt",
        "text": (
            "Der nebenstehende Körper besteht aus lauter kleinen Würfeln und ist außen\n"
            "komplett mit Farbe bemalt worden.\n"
            "Aus wie vielen Würfeln besteht der Körper?\n"
            "Wie viele Würfel sind auf nur einer Seite bemalt?\n"
            "Wie viele Würfel sind auf 3 Seiten bemalt?\n"
            "Wie viele Würfel sind gar nicht bemalt?"
        ),
        "answer": (
            "Aus wie vielen Würfeln: 9 + 12 + 3 = 24\n"
            "Auf nur einer Seite bemalt: 4\n"
            "Auf 3 Seiten bemalt: 8\n"
            "Gar nicht bemalt: 1"
        ),
        "steps": [
            "Annahme: unten 3 Würfel verbaut (sichtbare Schichten auszählen)",
            "Gesamtzahl: 9 + 12 + 3 = 24",
            "1 Seite bemalt: oben 1, Vorderseite 1, Rückseite 1, mittlere Ebene 3. Reihe mittlerer Stein = 4",
            "3 Seiten bemalt: alle Eckwürfel = 8",
            "Gar nicht bemalt: innenliegender Würfel = 1",
        ],
        "points": 3.0,
        "has_image": True,
        "image": "0044_q3_wuerfel_bemalt.png",
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
        ],
    },
    {
        "n": 4,
        "type": "Ansichten zuordnen",
        "text": (
            "Wer sieht welche Ansicht? Trage den richtigen Buchstaben ein!\n"
            "Ein Quader wird von den Seiten A (links), B (oben), C (rechts), D (unten) betrachtet.\n"
            "Sechs Ansichten (1–6) sind abgebildet. Ordne jeder Ansicht den richtigen\n"
            "Buchstaben zu!"
        ),
        "answer": (
            "Ansicht 1 → A\n"
            "Ansicht 2 → B\n"
            "Ansicht 3 → A\n"
            "Ansicht 4 → (Lösung siehe Ansichtsbild)\n"
            "Ansicht 5 → D\n"
            "Ansicht 6 → C"
        ),
        "steps": [
            "Betrachte die Anordnung der Figuren (Rechteck, Dreieck, Kreis) in der Ansicht",
            "Vergleiche mit der Perspektive je nach Blickrichtung A, B, C, D",
            "Trage den passenden Buchstaben ein",
        ],
        "points": 1.0,
        "has_image": True,
        "image": "0044_q4_ansichten.png",
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
        ],
    },
    {
        "n": 5,
        "type": "Quader-Flächen benennen",
        "text": (
            "Trage in die Flächen des Quaders ein, welche oben (o), unten (u), vorne (v),\n"
            "hinten (h), rechts (r) oder links (l) liegen!\n"
            "Drei verschiedene Quadernetz-Entfaltungen sind abgebildet."
        ),
        "answer": (
            "Netz 1: h oben, r rechts, o Mitte, v unten, l links, u ganz unten\n"
            "Netz 2: u oben, h rechts, v links, o Mitte, r rechts unten\n"
            "Netz 3: l oben, v links, o Mitte, h rechts, u rechts, r außen"
        ),
        "steps": [
            "Quadernetz im Geiste zusammenfalten",
            "Lage jeder Fläche relativ zur Standardposition bestimmen",
            "Buchstaben eintragen: o/u/v/h/r/l",
        ],
        "points": 2.0,
        "has_image": True,
        "image": "0044_q5_quader_flaechen.png",
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
        ],
    },
    {
        "n": 6,
        "type": "Symmetrieachsen finden",
        "text": (
            "Finde die möglichen Symmetrieachsen, zeichne sie ein und schreibe die Anzahl auf!\n"
            "Drei Figuren sind abgebildet (Pfeilform, Kreuzform, Zackenform)."
        ),
        "answer": (
            "Pfeilform: Anzahl = 1\n"
            "Kreuzform: Anzahl = 0\n"
            "Zackenform: Anzahl = 0"
        ),
        "steps": [
            "Jede Figur auf mögliche Spiegelachsen prüfen (vertikal, horizontal, diagonal)",
            "Symmetrieachse einzeichnen, wenn Figur auf beiden Seiten identisch",
            "Anzahl notieren",
        ],
        "points": 2.0,
        "has_image": True,
        "image": "0044_q6_symmetrie.png",
        "knowledge": [
            "mathe.klasse4.geometrie.vierecke",
        ],
    },
    {
        "n": 7,
        "type": "Parallele zeichnen",
        "text": (
            "Zeichne eine Parallele zur Geraden g, die durch den Punkt C verläuft!"
        ),
        "answer": "Eine Gerade parallel zu g durch Punkt C gezeichnet.",
        "steps": [
            "Geodreieck anlegen: eine Kante an g ausrichten",
            "Geodreieck verschieben bis es durch C verläuft",
            "Parallele einzeichnen",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.geometrie.dreiecke",
        ],
    },
    {
        "n": 8,
        "type": "Senkrechte zeichnen",
        "text": (
            "Zeichne eine Senkrechte zu Gerade a, die durch Punkt B verläuft!"
        ),
        "answer": "Eine Gerade senkrecht zu a durch Punkt B gezeichnet.",
        "steps": [
            "Geodreieck anlegen: rechten Winkel an Gerade a ausrichten",
            "Senkrechte durch B einzeichnen",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.geometrie.dreiecke",
        ],
    },
    {
        "n": 9,
        "type": "Quadrat konstruieren",
        "text": (
            "a) Zeichne auf der Geraden g die Strecke AB = 3 cm ein.\n"
            "b) Zeichne vom Punkt A aus eine senkrechte Strecke mit der Länge 3 cm. "
            "Der zweite Endpunkt erhält die Bezeichnung C.\n"
            "c) Zeichne durch den Punkt C eine parallele Gerade zur Geraden g.\n"
            "d) Zeichne durch den Punkt B eine parallele Gerade zu AC. Der Schnittpunkt "
            "mit der Geraden, auf welcher der Punkt C liegt, heißt D.\n"
            "Die Strecke BD hat die Länge ________ cm.\n"
            "e) Die Figur, die du gezeichnet hast, ist _______________________________."
        ),
        "answer": (
            "Die Strecke BD hat die Länge 3 cm.\n"
            "Die Figur, die du gezeichnet hast, ist ein Quadrat (Viereck)."
        ),
        "steps": [
            "AB = 3 cm auf g einzeichnen",
            "Senkrechte AC = 3 cm in A errichten",
            "Parallele zu g durch C ziehen",
            "Parallele zu AC durch B ziehen → Schnittpunkt D",
            "BD messen: 3 cm (da Quadrat mit Seitenlänge 3 cm entsteht)",
            "Figur benennen: Quadrat",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.geometrie.vierecke",
            "mathe.klasse4.geometrie.dreiecke",
        ],
    },
    {
        "n": 10,
        "type": "Würfelnetz falten",
        "text": (
            "Falte im Gedanken das Würfelnetz zu einem Würfel.\n"
            "Welche der abgebildeten Würfel entstehen? Kreuze an!"
        ),
        "answer": "Die Würfel 2 und 4 (mit X markiert) entstehen aus dem Netz.",
        "steps": [
            "Würfelnetz im Geiste zusammenfalten",
            "Position der Symbole (★, ○, □) auf den Seitenflächen bestimmen",
            "Mit den abgebildeten Würfeln vergleichen",
        ],
        "points": 1.0,
        "has_image": True,
        "image": "0044_q10_wuerfelnetz.png",
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
        ],
    },
    {
        "n": 11,
        "type": "Spielwürfel-Netz ergänzen",
        "text": (
            "Beim Spielwürfel haben die gegenüberliegenden Flächen zusammen sieben Punkte.\n"
            "Trage die fehlenden Punkte richtig ins Würfelnetz ein!"
        ),
        "answer": "Die fehlenden Flächen erhalten: 6 gegenüber 1, 5 gegenüber 2, 4 gegenüber 3 – entsprechend eingetragen.",
        "steps": [
            "Regel: Gegenüberliegende Flächen ergeben zusammen 7",
            "1 ↔ 6, 2 ↔ 5, 3 ↔ 4",
            "Im Netz die Lage der gegebenen Zahlen bestimmen",
            "Fehlende Augenzahlen auf den gegenüberliegenden Flächen eintragen",
        ],
        "points": 1.0,
        "has_image": True,
        "image": "0044_q11_spielwuerfel.png",
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
        ],
    },
    {
        "n": 12,
        "type": "Quadernetze prüfen",
        "text": (
            "Trage unten ein!\n"
            "Folgende Netze ergeben einen Quader: ______________________\n"
            "Keinen Quader gibt es bei _____ und _____, weil\n"
            "______________ / ______________\n"
            "Vier Netze (a, b, c, d) sind abgebildet."
        ),
        "answer": (
            "Folgende Netze ergeben einen Quader: a, c\n"
            "Keinen Quader gibt es bei b und d, weil b) Fläche zu klein; d) Fläche zu viel."
        ),
        "steps": [
            "Netz a: im Geiste falten → ergibt Quader ✓",
            "Netz b: eine Fläche hat die falsche Größe → kein Quader ✗",
            "Netz c: im Geiste falten → ergibt Quader ✓",
            "Netz d: eine Fläche zu viel / falsch positioniert → kein Quader ✗",
        ],
        "points": 1.0,
        "has_image": True,
        "image": "0044_q12_quadernetze.png",
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
        ],
    },
    {
        "n": 13,
        "type": "Würfelnetz einfärben",
        "text": (
            "Der abgebildete Würfel wurde bis zur Hälfte seiner Höhe in einen Farbeimer getaucht.\n"
            "Male entsprechende Flächen des unten gezeichneten Würfelnetzes so an, dass beim\n"
            "Zusammenfalten der abgebildete Würfel entsteht. Eine Seitenfläche ist bereits\n"
            "richtig eingefärbt."
        ),
        "answer": "Die untere Hälfte aller vier Seitenflächen sowie die Bodenfläche werden eingefärbt. Die obere Hälfte und die Deckfläche bleiben weiß.",
        "steps": [
            "Würfelnetz im Geiste zusammenfalten",
            "Boden → komplett eingefärbt",
            "Vier Seitenflächen → untere Hälfte eingefärbt",
            "Decke → weiß",
        ],
        "points": 2.0,
        "has_image": True,
        "image": "0044_q13_wuerfel_farbe.png",
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
        ],
    },
    {
        "n": 14,
        "type": "Quader-Netze einfärben",
        "text": (
            "3 Quader wurden zur Hälfte in Farbe getaucht. Färbe die Netze ein!"
        ),
        "answer": "Für jeden Quader: die Bodenfläche und die unteren Hälften der Seitenflächen werden eingefärbt.",
        "steps": [
            "Für jeden der 3 Quader das Netz zusammenfalten (gedanklich)",
            "Untere Hälfte des Körpers bestimmen",
            "Entsprechende Netz-Flächen einfärben (Boden + untere Seitenhälften)",
        ],
        "points": 2.0,
        "has_image": True,
        "image": "0044_q14_quader_farbe.png",
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
        ],
    },
    {
        "n": 15,
        "type": "Parallele und Senkrechte zeichnen",
        "text": (
            "a) Zeichne durch die Kreuze Linien, die parallel zu der Linie sind!\n"
            "b) Zeichne durch die Kreuze Linien, die senkrecht durch die Linie gehen!"
        ),
        "answer": "a) Durch jedes Kreuz eine zur gegebenen Linie parallele Gerade einzeichnen.\nb) Durch jedes Kreuz eine zur gegebenen Linie senkrechte Gerade einzeichnen.",
        "steps": [
            "a) Geodreieck an gegebene Linie anlegen, dann parallel verschieben und durch Kreuz ziehen",
            "b) Geodreieck so anlegen, dass der 90°-Winkel zur Linie steht; Senkrechte durch Kreuz ziehen",
        ],
        "points": 1.0,
        "has_image": True,
        "image": "0044_q15_parallelen.png",
        "knowledge": [
            "mathe.klasse4.geometrie.dreiecke",
        ],
    },
    {
        "n": 16,
        "type": "Quadernetz korrigieren",
        "text": (
            "Die Zeichnung soll ein Quadernetz darstellen. Verbessere den Fehler und ergänze\n"
            "die fehlende Fläche. Zeichne mit dem Geodreieck ganz genau!"
        ),
        "answer": "Die fehlerhafte Fläche wird korrigiert (auf richtige Größe gebracht) und die fehlende sechste Fläche ergänzt.",
        "steps": [
            "Vorhandene Flächen analysieren und Fehler identifizieren",
            "Falsche Fläche korrigieren (Größe/Lage)",
            "Fehlende Fläche mit Geodreieck ergänzen",
        ],
        "points": 1.0,
        "has_image": True,
        "image": "0044_q16_quadernetz_fehler.png",
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
        ],
    },
    {
        "n": 17,
        "type": "Figur verschieben",
        "text": (
            "Verschiebe nach der angegebenen Vorschrift!\n"
            "Figur 1: 9 nach rechts, 3 nach oben\n"
            "Figur 2: 6 nach links, 3 nach unten"
        ),
        "answer": "Figur 1 um 9 Kästchen nach rechts und 3 nach oben verschoben eingezeichnet.\nFigur 2 um 6 Kästchen nach links und 3 nach unten verschoben eingezeichnet.",
        "steps": [
            "Jeden Punkt der Figur um die angegebene Anzahl Kästchen verschieben",
            "Figur 1: alle Punkte +9 in x-Richtung, +3 in y-Richtung",
            "Figur 2: alle Punkte –6 in x-Richtung, –3 in y-Richtung",
            "Verschobene Figur einzeichnen",
        ],
        "points": 1.0,
        "has_image": True,
        "image": "0044_q17_verschieben.png",
        "knowledge": [
            "mathe.klasse4.geometrie.vierecke",
        ],
    },
    {
        "n": 18,
        "type": "Spiegelbild zeichnen",
        "text": (
            "Ergänze die folgende Figur zu einer spiegelbildlichen Figur! Benutze das Geodreieck!"
        ),
        "answer": "Die Figur wird an der eingezeichneten Achse gespiegelt und die fehlende Hälfte ergänzt.",
        "steps": [
            "Achse identifizieren (diagonal)",
            "Für jeden Punkt der Figur den Spiegelpunkt auf der anderen Seite der Achse bestimmen",
            "Gespiegelte Figur einzeichnen",
        ],
        "points": 2.0,
        "has_image": True,
        "image": "0044_q18_spiegel.png",
        "knowledge": [
            "mathe.klasse4.geometrie.vierecke",
        ],
    },
    {
        "n": 19,
        "type": "Ameise auf Würfel",
        "text": (
            "Eine Ameise sitzt auf einem Würfel und krabbelt darauf rum. Sie bewegt sich\n"
            "von A über Punkte B, C, D und E auf den Punkt F.\n"
            "a) Zeichne ein Netz des Würfels, wenn die Seitenlänge 3 cm beträgt!\n"
            "b) Zeichne den Weg der Ameise im Netz ein!\n"
            "c) Wie weit ist die Ameise gekrabbelt?\n"
            "d) Auf welchem Weg wäre die Ameise am schnellsten gewesen? "
            "(Zeichne diesen Weg in den Würfel mit grün ein!)"
        ),
        "answer": (
            "a) Würfelnetz mit Seitenlänge 3 cm gezeichnet.\n"
            "b) Weg A→B→C→D→E→F im Netz eingezeichnet.\n"
            "c) 2,8 cm + 2,2 cm + 2 cm + 2 cm + 2 cm = 11 cm\n"
            "d) Der kürzeste Weg ist die gerade Linie von A nach F auf dem abgerollten Netz."
        ),
        "steps": [
            "Würfelnetz zeichnen: 6 Quadrate à 3 cm",
            "Weg der Ameise über die Flächen im Netz einzeichnen",
            "Einzelne Teilstrecken messen: 2,8 + 2,2 + 2 + 2 + 2 = 11 cm",
            "Kürzester Weg: direkte Gerade von A nach F auf dem aufgeklappten Netz",
        ],
        "points": 3.0,
        "has_image": True,
        "image": "0044_q19_ameise.png",
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
            "mathe.klasse4.geometrie.flaeche",
        ],
    },
    {
        "n": 20,
        "type": "Sachaufgabe Patchwork-Decke",
        "text": (
            "Lisa möchte für ihren Puppenwagen eine sogenannte Patchwork-Decke in Form eines\n"
            "Quadrates nähen. Dafür benötigt sie verschieden farbige gleichgroße Stoffquadrate\n"
            "mit einer Seitenlänge von 8 cm.\n"
            "Jetzt hat Lisa genau 48 Quadrate zugeschnitten. Dies soll der äußere Rand der Decke sein.\n"
            "a) Aus wie viel Stoffquadraten besteht jede Seite der Decke?\n"
            "b) Wie viel Stoffquadrate muss Lisa noch zuschneiden, um eine fertige Decke zu erhalten?\n"
            "c) Wie breit ist die fertige Decke?"
        ),
        "answer": (
            "a) Jede Seite besteht aus 13 Quadraten.\n"
            "b) Lisa muss noch 121 Quadrate zuschneiden.\n"
            "c) Die fertige Decke ist 104 cm breit."
        ),
        "steps": [
            "Randquadrate: 48 Stück = 4 Seiten × (n–2) Ecken zählen nur einmal",
            "48 – 4 = 44 (ohne Eckquadrate), 44 ÷ 4 = 11 pro Seite (ohne Ecken), +2 Ecken = 13",
            "Innenfläche: 11 × 11 = 121 Quadrate",
            "Breite: 13 × 8 cm = 104 cm",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.geometrie.flaeche",
        ],
    },
    {
        "n": 21,
        "type": "Rechtecke zeichnen",
        "text": (
            "Zeichne zwei Rechtecke, die genau einen gemeinsamen Punkt haben. Verwende ein Lineal!"
        ),
        "answer": "Zwei Rechtecke gezeichnet, die sich nur in einem Eckpunkt berühren.",
        "steps": [
            "Erstes Rechteck zeichnen",
            "Zweites Rechteck so zeichnen, dass eine Ecke des zweiten mit einer Ecke des ersten übereinstimmt",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.geometrie.vierecke",
        ],
    },
    {
        "n": 22,
        "type": "Spiegelbilder erstellen",
        "text": (
            "Erstelle 3 Spiegelbilder zur Figur!"
        ),
        "answer": "Die Figur wird an der vertikalen und horizontalen Achse gespiegelt (insgesamt 4 Quadranten ausgefüllt).",
        "steps": [
            "Figur an vertikaler Achse spiegeln",
            "Figur an horizontaler Achse spiegeln",
            "Figur an beiden Achsen spiegeln (Quadrant 3)",
        ],
        "points": 2.0,
        "has_image": True,
        "image": "0044_q22_spiegelbilder.png",
        "knowledge": [
            "mathe.klasse4.geometrie.vierecke",
        ],
    },
    {
        "n": 23,
        "type": "Verschiebevorschrift bestimmen",
        "text": (
            "Wie heißt die Verschiebevorschrift?\n"
            "(Eine Figur und ihre verschobene Version sind im Gitter abgebildet.)"
        ),
        "answer": "7 nach rechts, 2 nach oben (7r 2o)",
        "steps": [
            "Einen markanten Punkt der Ausgangsfigur wählen",
            "Denselben Punkt in der verschobenen Figur finden",
            "Differenz in x-Richtung (rechts) und y-Richtung (oben) ablesen",
        ],
        "points": 1.0,
        "has_image": True,
        "image": "0044_q23_verschiebevorschrift.png",
        "knowledge": [
            "mathe.klasse4.geometrie.vierecke",
        ],
    },
]

NEW_KNOWLEDGE = []
