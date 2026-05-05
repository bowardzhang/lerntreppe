EXERCISE = {
    "id": "0401",
    "subject": "Mathe",
    "grade": 4,
    "title": "3. Lernzielkontrolle",
    "topic": "Zahlenraum bis 100000, Multiplizieren und Dividieren, halbschriftlich dividieren, Maßeinheiten, Liter",
    "publisher": "CATLUX",
    "source_pdf": "0401.pdf",
    "answer_pdf": "0401 (1).pdf",
    "total_points": 56.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Rechnen",
        "text": (
            "Berechne:\n"
            "72391 • 6 = ___\n"
            "4706 • 9 = ___\n"
            "258 • 70 = ___\n"
            "6,99 € • 3 = ___\n"
            "13,85 € • 5 = ___\n"
            "89,42 € • 2 = ___"
        ),
        "answer": (
            "72391 • 6 = 434346\n"
            "4706 • 9 = 42354\n"
            "258 • 70 = 18060\n"
            "6,99 € • 3 = 20,97 €\n"
            "13,85 € • 5 = 69,25 €\n"
            "89,42 € • 2 = 178,84 €"
        ),
        "steps": [
            "Schriftliche Multiplikation: einstellige Zahl oder Zehner mit mehrstelliger Zahl multiplizieren",
            "Bei Geldbeträgen: Ergebnis auf zwei Dezimalstellen runden",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.schriftlich.multiplikation",
        ],
    },
    {
        "n": 2,
        "type": "Rechnen",
        "text": (
            "a) 82 899 + 9 300 = ___\n"
            "   36 607 + 450 = ___\n"
            "   43 296 + 7 400 = ___\n"
            "b) 24 132 – 5 200 = ___\n"
            "   67 514 – 860 = ___\n"
            "   50 669 – 6 800 = ___"
        ),
        "answer": (
            "a) 82 899 + 9 300 = 92199\n"
            "   36 607 + 450 = 37057\n"
            "   43 296 + 7 400 = 50696\n"
            "b) 24 132 – 5 200 = 18932\n"
            "   67 514 – 860 = 66654\n"
            "   50 669 – 6 800 = 43869"
        ),
        "steps": [
            "Halbschriftliche Addition und Subtraktion im Zahlenraum bis 100000",
            "Ziffern stellenweise addieren bzw. subtrahieren",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.schriftlich.addition",
            "mathe.klasse4.schriftlich.subtraktion",
        ],
    },
    {
        "n": 3,
        "type": "Rechnen",
        "text": (
            "125 : 25 = ___\n"
            "275 : 25 = ___\n"
            "72 : 12 = ___\n"
            "84 : 12 = ___"
        ),
        "answer": (
            "125 : 25 = 5\n"
            "275 : 25 = 11\n"
            "72 : 12 = 6\n"
            "84 : 12 = 7"
        ),
        "steps": [
            "Division durch zweistellige Divisoren (25 und 12) auswendig oder durch Umkehren der Multiplikation",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.schriftlich.division",
        ],
    },
    {
        "n": 4,
        "type": "Umrechnen",
        "text": (
            "Wandle um in Milliliter (ml)!\n"
            "6 l = ___ ml\n"
            "1,3 l = ___ ml\n"
            "0,7 l = ___ ml\n"
            "0,02 l = ___ ml\n"
            "¼ l = ___ ml\n"
            "1/8 l = ___ ml\n"
            "¾ l = ___ ml\n"
            "½ l = ___ ml"
        ),
        "answer": (
            "6 l = 6000 ml\n"
            "1,3 l = 1300 ml\n"
            "0,7 l = 700 ml\n"
            "0,02 l = 20 ml\n"
            "¼ l = 250 ml\n"
            "1/8 l = 125 ml\n"
            "¾ l = 750 ml\n"
            "½ l = 500 ml"
        ),
        "steps": [
            "1 l = 1000 ml",
            "Dezimalzahlen und Brüche in ml umrechnen: Zahl mit 1000 multiplizieren",
            "¼ l = 250 ml, ½ l = 500 ml, ¾ l = 750 ml, 1/8 l = 125 ml",
        ],
        "points": 8.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.dezimalzahlen.grundlagen",
            "mathe.klasse4.groessen.volumen",
        ],
    },
    {
        "n": 5,
        "type": "Umrechnen",
        "text": (
            "Wandle um in Liter (l)! Benutze die Kommaschreibweise!\n"
            "250 ml = ___ l\n"
            "1400 ml = ___ l\n"
            "125 ml = ___ l\n"
            "2050 ml = ___ l\n"
            "50 ml = ___ l\n"
            "25 ml = ___ l"
        ),
        "answer": (
            "250 ml = 0,25 l\n"
            "1400 ml = 1,4 l\n"
            "125 ml = 0,125 l\n"
            "2050 ml = 2,05 l\n"
            "50 ml = 0,05 l\n"
            "25 ml = 0,025 l"
        ),
        "steps": [
            "ml in l umrechnen: durch 1000 dividieren",
            "Ergebnis als Dezimalzahl (Kommaschreibweise) angeben",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.dezimalzahlen.grundlagen",
            "mathe.klasse4.groessen.volumen",
        ],
    },
    {
        "n": 6,
        "type": "Ordnen",
        "text": (
            "Ordne nach der Größe! Beginne mit der kleinsten Menge!\n"
            "200 ml   0,3 l   ¾ l   0,125 l   ½ l   800 ml   1 l"
        ),
        "answer": "0,125 l < 200 ml < 0,3 l < ½ l < ¾ l < 800 ml < 1 l",
        "steps": [
            "Alle Mengen in dieselbe Einheit umrechnen (z. B. ml): 0,125 l = 125 ml, 0,3 l = 300 ml, ½ l = 500 ml, ¾ l = 750 ml, 1 l = 1000 ml",
            "Aufsteigend sortieren: 125 < 200 < 300 < 500 < 750 < 800 < 1000",
        ],
        "points": 7.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.dezimalzahlen.grundlagen",
            "mathe.klasse4.zahlen1000000.vergleichen",
            "mathe.klasse4.groessen.volumen",
        ],
    },
    {
        "n": 7,
        "type": "Rechnen",
        "text": (
            "Rechne aus!\n"
            "a) 3 600 : 6 = ___\n"
            "   45 000 : 9 = ___\n"
            "   6 400 : 8 = ___\n"
            "   56 000 : 7 = ___\n"
            "b) 180 000 : 30 = ___\n"
            "   300 000 : 600 = ___\n"
            "   320 000 : 40 = ___\n"
            "   540 000 : 900 = ___"
        ),
        "answer": (
            "a) 3 600 : 6 = 600\n"
            "   45 000 : 9 = 5000\n"
            "   6 400 : 8 = 800\n"
            "   56 000 : 7 = 8000\n"
            "b) 180 000 : 30 = 6000\n"
            "   300 000 : 600 = 500\n"
            "   320 000 : 40 = 8000\n"
            "   540 000 : 900 = 600"
        ),
        "steps": [
            "Nullen kürzen: z. B. 3600 : 6 = 36 Hunderter : 6 = 6 Hunderter = 600",
            "Bei mehrstufigen Divisoren: z. B. 300 000 : 600 = 3000 : 6 = 500",
        ],
        "points": 8.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.schriftlich.division",
            "mathe.klasse4.schriftlich.division_halbschriftlich",
        ],
    },
    {
        "n": 8,
        "type": "Rechnen",
        "text": (
            "Rechne halbschriftlich!\n"
            "a) 28 200 : 2\n"
            "b) 1592 : 8\n"
            "c) 39 824 : 4\n"
            "d) 3061 : 3"
        ),
        "answer": (
            "a) 28200 : 2 = 14100\n"
            "b) 1592 : 8 = 199\n"
            "c) 39824 : 4 = 9956\n"
            "d) 3061 : 3 = 1020 R1"
        ),
        "steps": [
            "a) 20000 : 2 = 10000; 8000 : 2 = 4000; 200 : 2 = 100 → 14100",
            "b) 800 : 8 = 100; 720 : 8 = 90; 72 : 8 = 9 → 199",
            "c) 36000 : 4 = 9000; 3600 : 4 = 900; 200 : 4 = 50; 24 : 4 = 6 → 9956",
            "d) 3000 : 3 = 1000; 30 : 3 = 10; 30 : 3 = 10; 1 : 3 = Rest 1 → 1020 R1",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.schriftlich.division_halbschriftlich",
        ],
    },
    {
        "n": 9,
        "type": "Sachaufgabe",
        "text": (
            "Löse die Sachaufgaben! Schreibe Rechnung (R:) und Antwort (A:) auf!\n\n"
            "a) Das Ehepaar Schulz hat drei Kinder. Bei jedem Duschen werden 60 l Wasser "
            "verbraucht. Jeder duscht einmal am Tag. "
            "Wie viel Liter Wasser verbraucht die Familie am Tag beim Duschen?\n\n"
            "b) Frau Meiers Klasse will Cornflakes zum Frühstück machen. Dafür benötigen sie "
            "1875 g Flakes und 7,5 l Milch. "
            "Wie viel Euro müssen sie bezahlen? "
            "(Preise laut Abbildung: Milch 1 l = 0,69 €, 0,5 l = 0,45 €; "
            "Cornflakes 750 g = 2,75 €, 375 g = 1,45 €)"
        ),
        "answer": (
            "a) R: 5 • 60 l = 300 l\n"
            "   A: Die Familie verbraucht am Tag beim Duschen 300 l.\n\n"
            "b) Milch: 0,69 € • 7 = 4,83 €; 4,83 € + 0,45 € = 5,28 €\n"
            "   Flakes: 2,75 € • 2 = 5,50 €; 5,50 € + 1,45 € = 6,95 €\n"
            "   Gesamt: 5,28 € + 6,95 € = 12,23 €\n"
            "   A: Sie müssen 12,23 € bezahlen."
        ),
        "steps": [
            "a) Familie = 2 Erwachsene + 3 Kinder = 5 Personen; 5 • 60 l = 300 l",
            "b) Milch: 7,5 l = 7 × 1 l + 1 × 0,5 l → 7 • 0,69 € + 0,45 € = 4,83 € + 0,45 € = 5,28 €",
            "b) Flakes: 1875 g = 2 × 750 g + 1 × 375 g → 2 • 2,75 € + 1,45 € = 5,50 € + 1,45 € = 6,95 €",
            "b) Gesamt: 5,28 € + 6,95 € = 12,23 €",
        ],
        "points": 7.0,
        "has_image": True,
        "image": "0401_q9b_xref30_273x400.png",
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.groessen.volumen",
            "mathe.klasse4.schriftlich.multiplikation",
        ],
    },
]

NEW_KNOWLEDGE = [
    {
        "id": "mathe.klasse4.groessen.volumen",
        "name": "Volumen und Hohlmaße (Liter, Milliliter)",
        "parent": "mathe.klasse4.groessen",
    }
]
