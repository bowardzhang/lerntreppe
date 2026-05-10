EXERCISE = {
    "id": "0894",
    "subject": "Mathe",
    "grade": 4,
    "title": "Übungsaufgaben: Wahrscheinlichkeit und Häufigkeit",
    "topic": "Faires/unfaires Spiel, Glücksräder, Wahrscheinlichkeitsstreifen, Kombinatorik",
    "publisher": "CATLUX",
    "source_pdf": "0894.pdf",
    "answer_pdf": "0894 (1).pdf",
    "total_points": 17.5,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Begriffe erklären",
        "text": (
            "Versuche, folgende Wörter zu erklären:\n"
            "Ein Spiel ist fair, wenn …\n"
            "Ein Spiel ist unfair, wenn …"
        ),
        "answer": (
            "Fair: Jeder Spieler hat die gleiche Gewinnchance. "
            "Unfair: Ein Spieler hat mehr Gewinnchancen als der andere."
        ),
        "steps": [
            "Fair = gleiche Gewinnchancen für alle Beteiligten.",
            "Unfair = ein Spieler/eine Seite ist im Vorteil.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.wahrscheinlichkeit.chancen",
        ],
    },
    {
        "n": 2,
        "type": "Glücksräder färben",
        "text": (
            "Ein Glücksrad hat 10 gleich große Felder. Färbe so, dass …\n"
            "a) Mit den Farben Rot, Grün, Gelb: Rot soll wahrscheinlicher gewinnen.\n"
            "b) Mit den Farben Rot, Grün, Gelb, Blau: Blau soll die gleiche Gewinnchance haben wie die anderen Farben.\n"
            "c) Mit den Farben Rot, Grün, Blau: alle Farben sollen die gleiche Gewinnchance haben."
        ),
        "answer": (
            "a) Rot bekommt mehr Felder als die anderen Farben (z. B. 6 Rot, 2 Grün, 2 Gelb). "
            "b) Geht nicht: 10 Felder lassen sich nicht durch 4 gleichmäßig teilen (10 : 4 ist kein ganzzahliges Ergebnis). "
            "c) Geht nicht: 10 Felder lassen sich nicht durch 3 gleichmäßig teilen (10 : 3 ist kein ganzzahliges Ergebnis)."
        ),
        "steps": [
            "a) Ungleiche Verteilung mit Mehrheit für Rot.",
            "b) 10 : 4 = 2,5 → keine ganzzahlige gleiche Aufteilung möglich.",
            "c) 10 : 3 ≈ 3,33 → keine ganzzahlige gleiche Aufteilung möglich.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.wahrscheinlichkeit.chancen",
        ],
    },
    {
        "n": 3,
        "type": "Sicher/wahrscheinlich/unmöglich",
        "text": (
            "Ordne den Aussagen 'sicher', 'wahrscheinlich' oder 'unmöglich' zu.\n"
            "a) Wenn ich mich nicht eincreme, bekomme ich einen Sonnenbrand.\n"
            "b) Ein Pferd fliegt über die Schule.\n"
            "c) Morgen wird es regnen.\n"
            "d) Mein Vater ist jünger als ich.\n"
            "e) Ich brauche täglich etwas zum Trinken."
        ),
        "answer": (
            "a) wahrscheinlich ; b) unmöglich ; c) wahrscheinlich ; "
            "d) unmöglich ; e) sicher"
        ),
        "steps": [
            "a) je nach Sonne/Hauttyp meist wahrscheinlich.",
            "b) Pferde können nicht fliegen → unmöglich.",
            "c) hängt vom Wetter ab → wahrscheinlich (nicht sicher).",
            "d) ein Vater ist immer älter als sein Kind → unmöglich.",
            "e) Wasser braucht der Mensch täglich → sicher.",
        ],
        "points": 2.5,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.wahrscheinlichkeit.chancen",
        ],
    },
    {
        "n": 4,
        "type": "Bonbons im Beutel — beste Mischung",
        "text": (
            "Du füllst 10 Bonbons in einen Beutel (rot oder gelb). Tim zieht "
            "mit verbundenen Augen zwei Bonbons. Wie musst du den Beutel "
            "füllen, damit er möglichst sicher einen roten UND einen gelben "
            "Bonbon zieht?"
        ),
        "answer": "5 rote und 5 gelbe Bonbons.",
        "steps": [
            "Bei 5 Rot und 5 Gelb sind die Chancen für jede Farbe gleich groß.",
            "Eine ausgewogene Mischung maximiert die Wahrscheinlichkeit, beide Farben zu ziehen.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.wahrscheinlichkeit.chancen",
        ],
    },
    {
        "n": 5,
        "type": "Bonbons ohne Zurücklegen",
        "text": (
            "Im Beutel sind 5 Bonbons: 4 rote und 1 gelber. Du ziehst zweimal "
            "ohne Zurücklegen.\n"
            "a) Wie wahrscheinlich ist es, dass du den gelben Bonbon ziehst?\n"
            "b) Wie kann man die Wahrscheinlichkeit für Gelb erhöhen?\n"
            "c) Wie kann man die Wahrscheinlichkeit für Rot senken?"
        ),
        "answer": (
            "a) Es gibt 2 Möglichkeiten, den gelben zu ziehen: 1. Zug Gelb, 2. Zug Rot ; oder 1. Zug Rot, 2. Zug Gelb. "
            "Bei 2 Zügen ohne Zurücklegen ist die Chance, den gelben zu erwischen, recht hoch (2 von 5 Zügen). "
            "b) Mehr gelbe Bonbons in den Beutel füllen. "
            "c) Gezogene rote Bonbons nicht zurücklegen ODER mehr gelbe Bonbons hinzufügen."
        ),
        "steps": [
            "a) Pfade mit Gelb: GR und RG (2 günstige Folgen).",
            "b) Anteil Gelb erhöhen → mehr Gelb hinzufügen.",
            "c) Anteil Rot senken → Rot entfernen oder Gelb hinzufügen.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.wahrscheinlichkeit.chancen",
        ],
    },
    {
        "n": 6,
        "type": "Häufigkeitsdiagramm interpretieren",
        "text": (
            "Tim und Tom haben über 200-mal je einen Bonbon aus ihrem Beutel "
            "gezogen und wieder zurückgelegt. Im Balkendiagramm war Weiß am "
            "höchsten, gefolgt von Blau, Rot und Grün. Welche Bonbons-Mischung "
            "war wahrscheinlich im Beutel?\n"
            "a) 3 grüne; 2 blaue; 1 weiße; 2 rote\n"
            "b) 2 blaue; 5 weiße; 2 gelbe; 3 rote\n"
            "c) 2 grüne; 2 blaue; 2 weiße; 2 rote\n"
            "d) 1 grüne; 2 blaue; 4 weiße; 1 rote"
        ),
        "answer": "d) 1 grüne; 2 blaue; 4 weiße; 1 rote — weil Weiß am häufigsten gezogen wurde.",
        "steps": [
            "Weiß ist im Diagramm am höchsten → muss am meisten im Beutel sein.",
            "Option d) hat 4 weiße (mehr als alle anderen) → passt zur Beobachtung.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.wahrscheinlichkeit.haeufigkeit",
        ],
    },
    {
        "n": 7,
        "type": "Kombinatorik (Eis zusammenstellen)",
        "text": (
            "An einem Eisstand gibt es Schokoladen- und Vanilleeis. Dazu kann "
            "man rote oder gelbe Zuckerstreusel wählen und das Eis mit "
            "Zuckerherzen oder Zuckerperlen garnieren. Wie viele "
            "Möglichkeiten hat Tim, sich ein Eis zusammenzustellen?"
        ),
        "answer": "8 Möglichkeiten.",
        "steps": [
            "2 Sorten · 2 Streusel · 2 Garnierungen = 2 · 2 · 2 = 8.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.wahrscheinlichkeit.kombinatorik",
            "mathe.klasse4.sachaufgaben.zahlenraetsel",
        ],
    },
    {
        "n": 8,
        "type": "Kombinatorik (Reihenfolgen)",
        "text": (
            "Tim, Florian und Julia wollen sich nebeneinander aufstellen. "
            "Wie viele Möglichkeiten gibt es? Schreibe alle auf "
            "(Anfangsbuchstaben T, F, J)."
        ),
        "answer": "6 Möglichkeiten: TFJ, TJF, FTJ, FJT, JFT, JTF.",
        "steps": [
            "An Position 1: 3 Möglichkeiten; Position 2: 2 Möglichkeiten; Position 3: 1 Möglichkeit.",
            "Insgesamt 3 · 2 · 1 = 6.",
            "Liste: TFJ, TJF, FTJ, FJT, JFT, JTF.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.wahrscheinlichkeit.kombinatorik",
            "mathe.klasse4.sachaufgaben.zahlenraetsel",
        ],
    },
]

NEW_KNOWLEDGE = []
