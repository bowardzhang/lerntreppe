EXERCISE = {
    "id": "1005",
    "subject": "Mathe",
    "grade": 4,
    "title": "2. Lernzielkontrolle: Division, Multiplikation, Teiler, Vielfache, Teilbarkeitsregeln",
    "topic": "Division/Multiplikation halbschriftlich, Teiler, Vielfache, Teilbarkeitsregeln",
    "publisher": "CATLUX",
    "source_pdf": "1005.pdf",
    "answer_pdf": "1005 (1).pdf",
    "total_points": 45.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Grundaufgaben Division und Multiplikation",
        "text": (
            "Löse die Aufgaben.\n"
            "650 : 10 = ___    50 · 30 = ___\n"
            "700 : 70 = ___     7 · 90 = ___\n"
            "420 :  6 = ___    60 ·  8 = ___"
        ),
        "answer": "65 ; 1 500 ; 10 ; 630 ; 70 ; 480",
        "steps": [
            "650 : 10 = 65 ;  50 · 30 = 1 500",
            "700 : 70 = 10 ;   7 · 90 = 630",
            "420 :  6 = 70 ;  60 ·  8 = 480",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.schriftlich.multiplikation",
            "mathe.klasse4.schriftlich.division_halbschriftlich",
        ],
    },
    {
        "n": 2,
        "type": "Halbschriftliche Multiplikation",
        "text": (
            "Multipliziere halbschriftlich!\n"
            "32 · 5 = ___    4 · 98 = ___    78 · 7 = ___    175 · 6 = ___"
        ),
        "answer": "160 ; 392 ; 546 ; 1 050",
        "steps": [
            "32 · 5 = 30·5 + 2·5 = 150 + 10 = 160.",
            "4 · 98 = 4·90 + 4·8 = 360 + 32 = 392.",
            "78 · 7 = 70·7 + 8·7 = 490 + 56 = 546.",
            "175 · 6 = 100·6 + 70·6 + 5·6 = 600 + 420 + 30 = 1 050.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.schriftlich.multiplikation",
        ],
    },
    {
        "n": 3,
        "type": "Halbschriftliche Multiplikation und Division",
        "text": (
            "Berechne halbschriftlich.\n"
            "8 · 63 = ___    747 : 9 = ___"
        ),
        "answer": "504 ; 83",
        "steps": [
            "8 · 63 = 8·60 + 8·3 = 480 + 24 = 504.",
            "747 : 9 = 720:9 + 27:9 = 80 + 3 = 83.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.schriftlich.multiplikation",
            "mathe.klasse4.schriftlich.division_halbschriftlich",
        ],
    },
    {
        "n": 4,
        "type": "Klecksaufgaben (Umkehraufgaben)",
        "text": (
            "Klecksaufgaben. Schreibe die richtigen Zahlen in die Felder.\n"
            "  ___ · 9 = ___   (294 : ___ = ___)\n"
            "  ___ · 2 = ___   (280 : ___ = 40)\n"
            "  ___ · ___       (360 : 60 = ___)\n"
            "(Hinweis: Fehlende Faktoren/Divisoren so bestimmen, dass die Gleichungen aufgehen.)"
        ),
        "answer": "294 : 7 = 42 ; 280 : 7 = 40 ; 360 : 60 = 6",
        "steps": [
            "Zeile 1: 294 : 7 = 42 (da 42 · 7 = 294).",
            "Zeile 2: 280 : 7 = 40 (da 40 · 7 = 280).",
            "Zeile 3: 360 : 60 = 6 (da 6 · 60 = 360).",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.umkehraufgaben",
            "mathe.klasse4.schriftlich.division_halbschriftlich",
        ],
    },
    {
        "n": 5,
        "type": "Teiler einer Zahl",
        "text": (
            "Schreibe alle Teiler der Zahl auf.\n"
            "Teiler von 20: _________________________________________________\n"
            "Teiler von 64: _________________________________________________"
        ),
        "answer": "Teiler von 20: 1, 2, 4, 5, 10, 20 ; Teiler von 64: 1, 2, 4, 8, 16, 32, 64",
        "steps": [
            "20 = 1·20 = 2·10 = 4·5 → Teiler: 1, 2, 4, 5, 10, 20.",
            "64 = 1·64 = 2·32 = 4·16 = 8·8 → Teiler: 1, 2, 4, 8, 16, 32, 64.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.zahlen1000000.teiler",
        ],
    },
    {
        "n": 6,
        "type": "Knobelaufgabe (Zahlenrätsel)",
        "text": (
            "Florians Onkel hat einen Sohn, der 20 Jahre jünger ist als er selbst. "
            "Zusammen sind die beiden 48 Jahre alt.\n"
            "Wie alt ist Florians Onkel? Wie alt ist sein Sohn?"
        ),
        "answer": "Florians Onkel ist 34 Jahre alt, sein Sohn ist 14 Jahre alt.",
        "steps": [
            "Sei Sohn = x, dann Onkel = x + 20.",
            "x + (x + 20) = 48 → 2x = 28 → x = 14.",
            "Sohn: 14 Jahre ; Onkel: 34 Jahre.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.zahlenraetsel",
        ],
    },
    {
        "n": 7,
        "type": "Sachaufgabe (Schulfest, Geld)",
        "text": (
            "Bei einem Schulfest werden insgesamt 968 Euro eingenommen. "
            "Dann werden davon 308 Euro für Musikinstrumente ausgegeben. "
            "Für die Schulbücherei werden 8 Bücher gekauft. Jedes Buch kostet 8 Euro.\n"
            "Wie viel Geld bleibt übrig?"
        ),
        "answer": "Es bleiben 596 Euro übrig.",
        "steps": [
            "8 Bücher: 8 · 8 € = 64 €.",
            "Ausgaben gesamt: 308 € + 64 € = 372 €.",
            "Rest: 968 € − 372 € = 596 €.",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.groessen.geld",
            "mathe.klasse4.schriftlich.multiplikation",
            "mathe.klasse4.schriftlich.subtraktion",
        ],
    },
    {
        "n": 8,
        "type": "Sachaufgabe (Division mit Rest)",
        "text": (
            "Herr Meier möchte 439 Murmeln an seine 6 Kinder verteilen.\n"
            "Wie viele Murmeln bekommt jedes Kind?"
        ),
        "answer": "Jedes Kind bekommt 73 Murmeln und 1 Murmel bleibt übrig.",
        "steps": [
            "439 : 6 = 420:6 + 19:6 = 70 + 3 R 1 = 73 R 1.",
            "Jedes Kind: 73 Murmeln, Rest: 1 Murmel.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.schriftlich.division_halbschriftlich",
        ],
    },
    {
        "n": 9,
        "type": "Vielfache",
        "text": (
            "Schreibe vier Vielfache der Zahl 8 auf:\n"
            "_________________________________________________________________\n"
            "Schreibe aus den Zahlen 320 bis 570 alle Vielfachen von 70 auf:\n"
            "_________________________________________________________________"
        ),
        "answer": "Vielfache von 8 (Beispiele): 8, 16, 24, 32 (… bis 80 usw.) ; Vielfache von 70 zwischen 320 und 570: 350, 420, 490, 560",
        "steps": [
            "Vielfache von 8: 8, 16, 24, 32, 40, …",
            "Vielfache von 70 im Bereich [320, 570]: 70·5=350, 70·6=420, 70·7=490, 70·8=560.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.zahlen1000000.teiler",
        ],
    },
    {
        "n": 10,
        "type": "Teilbarkeitsregeln",
        "text": (
            "Kreise Zahlen, die durch 5 teilbar sind, ein und unterstreiche die, "
            "die durch 6 teilbar sind:\n"
            "72   16   335   822   5 220   69   7   4 155\n\n"
            "Vervollständige: Eine Zahl ist durch 2 teilbar, wenn …"
        ),
        "answer": (
            "Durch 5 teilbar (enden auf 0 oder 5): 335, 5 220, 4 155. "
            "Durch 6 teilbar (gerade UND durch 3): 72, 822, 5 220. "
            "Durch 2 teilbar: … sie eine gerade Zahl ist (letzte Ziffer 0, 2, 4, 6 oder 8)."
        ),
        "steps": [
            "Teilbar durch 5: letzte Ziffer 0 oder 5 → 335, 5 220, 4 155.",
            "Teilbar durch 6: gerade UND Quersumme durch 3 → 72 (Q=9✓,gerade✓), 822 (Q=12✓,gerade✓), 5 220 (Q=9✓,gerade✓).",
            "Teilbar durch 2: Zahl ist gerade (endet auf 0, 2, 4, 6, 8).",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.zahlen1000000.teiler",
        ],
    },
    {
        "n": 11,
        "type": "Halbschriftlich rechnen (schriftlich aufgestellt)",
        "text": (
            "Schreibe stellengerecht untereinander und rechne halbschriftlich aus.\n"
            "a) 39 · 6 = ___\n"
            "b) 235 · 4 = ___\n"
            "c) 647 : 7 = ___\n"
            "d) 294 : 6 = ___\n"
            "e) 447 : 5 = ___"
        ),
        "answer": "a) 234 ; b) 940 ; c) 92 R 3 ; d) 49 ; e) 89 R 2",
        "steps": [
            "a) 39·6 = 30·6 + 9·6 = 180 + 54 = 234.",
            "b) 235·4 = 200·4 + 35·4 = 800 + 140 = 940.",
            "c) 647:7 = 630:7 + 17:7 = 90 + 2 R 3 = 92 R 3.",
            "d) 294:6 = 240:6 + 54:6 = 40 + 9 = 49.",
            "e) 447:5 = 440:5 + 7:5 = 88 + 1 R 2 = 89 R 2.",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.schriftlich.multiplikation",
            "mathe.klasse4.schriftlich.division_halbschriftlich",
        ],
    },
]

NEW_KNOWLEDGE = []
