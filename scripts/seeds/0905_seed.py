EXERCISE = {
    "id": "0905",
    "subject": "Mathe",
    "grade": 4,
    "title": "Übungsaufgaben – Geometrie: Quader",
    "topic": "Geometrie: Quader",
    "publisher": "CATLUX",
    "source_pdf": "0905.pdf",
    "answer_pdf": "0905 (1).pdf",
    "total_points": 12.0,  # only Q4 (4pts) and Q11 (8pts) carry explicit marks
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Kreuze an",
        "text": (
            "Kreuze an! (ja / nein)\n"
            "1. An jeder Quaderkante stoßen drei Flächen zusammen.\n"
            "2. Ein Quader hat sechs gleich lange Kanten.\n"
            "3. Beim Quader sind gegenüberliegende Flächen gleich.\n"
            "4. Jeder Quader ist zugleich ein Würfel.\n"
            "5. Ein Quader hat 8 Flächen.\n"
            "6. Der Würfel hat zwölf Kanten und acht Ecken.\n"
            "7. Ein Prisma hat manchmal zehn Kanten."
        ),
        "answer": (
            "1. nein  2. nein  3. ja  4. nein  5. nein  6. ja  7. nein"
        ),
        "steps": [
            "1. nein – An jeder Quaderkante stoßen zwei (nicht drei) Flächen zusammen.",
            "2. nein – Ein Quader hat drei Gruppen je vier gleich langer Kanten, aber nicht alle 12 gleich lang.",
            "3. ja – Gegenüberliegende Flächen sind kongruent.",
            "4. nein – Nur ein Würfel (Sonderfall Quader) hat alle gleich langen Kanten.",
            "5. nein – Ein Quader hat 6 Flächen, nicht 8.",
            "6. ja – Ein Würfel hat 12 Kanten und 8 Ecken.",
            "7. nein – Ein Prisma hat je nach Grundfläche eine feste Kantenzahl; ein Dreiecksprisma hat 9 Kanten.",
        ],
        "points": 0.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
        ],
    },
    {
        "n": 2,
        "type": "Würfelbauwerk analysieren",
        "text": (
            "Betrachte die Körper A und B (aus Würfeln aufgebaut).\n\n"
            "Fülle die Tabelle aus:\n"
            "- Aus wie vielen Würfeln bestehen die Körper?\n"
            "- Wie viele Würfel fehlen zum Würfel?\n"
            "- Wie viele Würfel musst du mindestens hinzufügen, damit ein Quader entsteht?\n\n"
            "Zeichne die Baupläne zu den Körpern A und B!"
        ),
        "answer": (
            "A: 10 Würfel, fehlen zum Würfel: 17, mindestens hinzufügen für Quader: 8\n"
            "B: 10 Würfel, fehlen zum Würfel: 17, mindestens hinzufügen für Quader: 8"
        ),
        "steps": [
            "Körper A: besteht aus 10 Würfeln",
            "Körper B: besteht aus 10 Würfeln",
            "Für einen Würfel (3×3×3 = 27) fehlen jeweils 17 Würfel",
            "Für einen Quader genügen mindestens 8 zusätzliche Würfel (ergibt 2×3×3 = 18)",
            "Bauplan A: 3. Reihe: 3-2-1; 2. Reihe: 2-1-1 (von vorn gesehen)",
            "Bauplan B: 3×3-Raster mit Höhen 1-1-1 / 1-2-1 / 1-1-1",
        ],
        "points": 0.0,
        "has_image": True,
        "image": "0905_q2_koerper_AB.png",
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
        ],
    },
    {
        "n": 3,
        "type": "Würfelergänzung",
        "text": (
            "Wie viele Würfel musst du hinzufügen, bis ein Quader entsteht? "
            "Aus wie vielen Würfel besteht dann der Quader?\n\n"
            "Bestimme dies für drei abgebildete Körper (je a und b angeben)."
        ),
        "answer": (
            "Körper 1: a) 80 hinzufügen, b) Quader hat 100 Würfel\n"
            "Körper 2: a) 35 hinzufügen, b) Quader hat 45 Würfel\n"
            "Körper 3: a) 52 hinzufügen, b) Quader hat 80 Würfel"
        ),
        "steps": [
            "Körper 1: a) 80 Würfel hinzufügen, b) Quader: 100 Würfel",
            "Körper 2: a) 35 Würfel hinzufügen, b) Quader: 45 Würfel",
            "Körper 3: a) 52 Würfel hinzufügen, b) Quader: 80 Würfel",
        ],
        "points": 0.0,
        "has_image": True,
        "image": "0905_q3_koerper_ergaenzung.png",
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
        ],
    },
    {
        "n": 4,
        "type": "Bauplan ergänzen / Sachaufgabe",
        "text": (
            "Florian hat den nebenstehenden Körper aus Holzwürfeln aufgestellt.\n\n"
            "a) Ergänze den Bauplan so, dass er zum Würfelbauwerk passt! "
            "Gegeben ist ein teilweise ausgefüllter Bauplan mit den Werten: 4 (oben Mitte), "
            "1 (links Mitte), 1 (Mitte), 2 (rechts Mitte), 1 (rechts unten).\n"
            "Wie viele Würfel hat das Bauwerk insgesamt?\n\n"
            "b) Florians Würfelbauwerk soll zu einer Treppe ergänzt werden (siehe Skizze). "
            "Wie viele Holzwürfel braucht er noch? Füge eine Rechnung hinzu!"
        ),
        "answer": (
            "a) Bauplan: Zeile 1: _, 3, 4, 4; Zeile 2: 1, 2, 1, 3; Zeile 3: _, 1, _, 2; Zeile 4: _, _, _, 1. "
            "Anzahl der Würfel: 22\n"
            "b) Florian braucht noch 18 Würfel."
        ),
        "steps": [
            "Bauplan vollständig: Zeile 1 (oben): [_, 3, 4, 4]; Zeile 2: [1, 2, 1, 3]; Zeile 3: [_, 1, _, 2]; Zeile 4: [_, _, _, 1]",
            "Anzahl der Würfel: 22",
            "Treppe: 16 + 12 + 8 + 4 = 40 Würfel gesamt",
            "40 – 22 = 18 Würfel fehlen noch",
            "A: Florian braucht noch 18 Würfel.",
        ],
        "points": 4.0,
        "has_image": True,
        "image": "0905_q4_florian_bauwerk.png",
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
            "mathe.klasse4.sachaufgaben.mehrstufig",
        ],
    },
    {
        "n": 5,
        "type": "Würfelkörper analysieren",
        "text": (
            "Der nebenstehende Körper besteht aus lauter kleinen Würfeln und ist außen komplett mit Farbe "
            "bemalt worden.\n\n"
            "- Aus wie vielen Würfeln besteht der Körper?\n"
            "- Wie viele Würfel sind auf nur einer Seite bemalt?\n"
            "- Wie viele Würfel sind auf 3 Seiten bemalt?\n"
            "- Wie viele Würfel sind gar nicht bemalt?"
        ),
        "answer": (
            "Körper: 9 + 12 + 3 = 24 Würfel. "
            "Nur eine Seite bemalt: 4. "
            "3 Seiten bemalt: 8. "
            "Gar nicht bemalt: 1."
        ),
        "steps": [
            "Annahme: unten sind 3 Würfel verbaut",
            "Anzahl Würfel: 9 + 12 + 3 = 24",
            "Nur eine Seite bemalt: 4 (oben 1, Vorderseite 1, Rückseite 1, mittlere Ebene 3. Reihe von links mittlerer Stein)",
            "3 Seiten bemalt: 8 (Ecken)",
            "Gar nicht bemalt: 1",
        ],
        "points": 0.0,
        "has_image": True,
        "image": "0905_q5_farbwuerfel.png",
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
        ],
    },
    {
        "n": 6,
        "type": "Quader beschriften",
        "text": (
            "Trage in die Flächen des Quaders ein, welche oben (o), unten (u), vorne (v), "
            "hinten (h), rechts (r) oder links (l) liegen!"
        ),
        "answer": (
            "Quader 1 (Schrägbild links): h oben, r rechts, o/l links, v unten, u ganz unten\n"
            "Quader 2 (Draufsicht): u oben, l/h rechts, v/o mitte\n"
            "Quader 3 (Frontalansicht): l links, v/o/h/u von links nach rechts"
        ),
        "steps": [
            "Quader 1: h (hinten oben), r (rechts), o (oben links), l (links), v (vorne), u (unten)",
            "Quader 2: u (unten), l (links), h (hinten), v (vorne), o (oben)",
            "Quader 3: l (links), v (vorne), o (oben), h (hinten), u (unten)",
        ],
        "points": 0.0,
        "has_image": True,
        "image": "0905_q6_quader_beschriften.png",
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
        ],
    },
    {
        "n": 7,
        "type": "Zeichenaufgabe",
        "text": (
            "Zeichne zwei Rechtecke, die genau einen gemeinsamen Punkt haben. Verwende ein Lineal!"
        ),
        "answer": (
            "Verschiedene Möglichkeiten: zwei Rechtecke, die sich an genau einer Ecke berühren "
            "(z. B. eine Ecke des einen liegt auf einer Ecke des anderen)."
        ),
        "steps": [
            "Zeichne ein erstes Rechteck mit dem Lineal.",
            "Zeichne ein zweites Rechteck so, dass eine Ecke des zweiten genau auf einer Ecke des ersten liegt.",
            "Die Rechtecke dürfen sich nur in diesem einen Punkt berühren, nicht überlappen.",
        ],
        "points": 0.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.geometrie.vierecke",
        ],
    },
    {
        "n": 8,
        "type": "Quadernetz bestimmen",
        "text": (
            "Trage unten ein!\n"
            "Vier Netze (a, b, c, d) sind abgebildet. "
            "Folgende Netze ergeben einen Quader: ______. "
            "Keinen Quader gibt es bei ___ und ___, weil ________________________."
        ),
        "answer": (
            "Folgende Netze ergeben einen Quader: a, c. "
            "Keinen Quader gibt es bei b und d, weil b) Fläche zu klein; d) Fläche zu viel."
        ),
        "steps": [
            "Netz a: ergibt einen Quader (korrekte Anordnung der 6 Flächen)",
            "Netz b: ergibt keinen Quader – eine Fläche ist zu klein",
            "Netz c: ergibt einen Quader",
            "Netz d: ergibt keinen Quader – eine Fläche zu viel (7 Flächen statt 6)",
        ],
        "points": 0.0,
        "has_image": True,
        "image": "0905_q8_quadernetz.png",
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
        ],
    },
    {
        "n": 9,
        "type": "Quadernetz einfärben",
        "text": (
            "3 Quader wurden zur Hälfte in Farbe getaucht. Färbe die Netze ein!"
        ),
        "answer": (
            "Jeweils die unteren drei Flächen des Netzes werden eingefärbt "
            "(die Flächen, die beim Eintauchen zur Hälfte in Farbe lagen)."
        ),
        "steps": [
            "Bestimme, welche Hälfte des Quaders eingetaucht wurde.",
            "Übertrage die entsprechenden Flächen auf das Netz und färbe sie ein.",
        ],
        "points": 0.0,
        "has_image": True,
        "image": "0905_q9_quader_faerben.png",
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
        ],
    },
    {
        "n": 10,
        "type": "Quadernetz korrigieren",
        "text": (
            "Die Zeichnung soll ein Quadernetz darstellen. Verbessere den Fehler und ergänze "
            "die fehlende Fläche. Zeichne mit dem Geodreieck ganz genau!"
        ),
        "answer": (
            "Eine falsch platzierte Fläche (im Netz mit X markiert) wird entfernt/korrigiert "
            "und die fehlende sechste Fläche an der richtigen Stelle ergänzt."
        ),
        "steps": [
            "Identifiziere die falsche Fläche im abgebildeten Netz.",
            "Zeichne die fehlende sechste Fläche an der korrekten Position.",
            "Überprüfe: Das korrigierte Netz muss beim Falten einen Quader ergeben.",
        ],
        "points": 0.0,
        "has_image": True,
        "image": "0905_q10_quadernetz_korrektur.png",
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
        ],
    },
    {
        "n": 11,
        "type": "Sachaufgabe",
        "text": (
            "Florian baut aus Draht einen Würfel und einen Quader. Beide haben dieselbe Länge von 10cm. "
            "Der Quader ist 4cm breit. Insgesamt braucht Florian für beide Körper 200cm Draht. "
            "Wie hoch ist der Quader? (Schreibe alle Rechnungen auf!)"
        ),
        "answer": "Der Quader ist 6cm hoch.",
        "steps": [
            "Würfel: 12 Kanten × 10cm = 120cm Draht",
            "Draht für Quader: 200cm – 120cm = 80cm",
            "Quader hat 4 Längen + 4 Breiten + 4 Höhen",
            "4 × 10cm = 40cm (Längen), 4 × 4cm = 16cm (Breiten) → 40cm + 16cm = 56cm",
            "Draht für Höhen: 80cm – 56cm = 24cm",
            "Höhe: 24cm : 4 = 6cm",
            "A: Der Quader ist 6cm hoch.",
        ],
        "points": 8.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
            "mathe.klasse4.sachaufgaben.mehrstufig",
        ],
    },
]

NEW_KNOWLEDGE = []
