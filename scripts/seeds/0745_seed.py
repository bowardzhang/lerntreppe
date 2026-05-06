EXERCISE = {
    "id": "0745",
    "subject": "Mathe",
    "grade": 4,
    "title": "Vorbereitung Probeunterricht: Maßeinheiten und Sachaufgaben",
    "topic": "Längenmaße, Gewichte, Volumen, Zeit, Einheitenumrechnung, Sachaufgaben",
    "publisher": "CATLUX",
    "source_pdf": "0745.pdf",
    "answer_pdf": "0745 (1).pdf",
    "total_points": 19.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Längen berechnen",
        "text": (
            "Berechne: 60 m 9 dm + 6 dm 9 cm – 906 cm = ___ m ___ dm ___ cm"
        ),
        "answer": "52 m 5 dm 3 cm",
        "steps": [
            "Alles in cm: 60 m 9 dm = 6090 cm.",
            "6 dm 9 cm = 69 cm.",
            "6090 + 69 – 906 = 5253 cm.",
            "5253 cm = 52 m 5 dm 3 cm.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.groessen.laenge",
        ],
    },
    {
        "n": 2,
        "type": "Gewicht dividieren",
        "text": "Berechne: 475 t 11 kg : 73 = ___",
        "answer": "6507 kg",
        "steps": [
            "475 t 11 kg = 475011 kg.",
            "475011 : 73 = 6507 kg.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.groessen.gewicht",
            "mathe.klasse4.schriftlich.division",
        ],
    },
    {
        "n": 3,
        "type": "Sachaufgabe: LKW-Beladung",
        "text": (
            "Ein LKW wird beladen: 7 Kisten à 40 kg, 10 Kisten unbekannten Gewichts, "
            "1 Kiste Sand (0,620 t) und 4 Paletten Holz (je ½ Tonne). "
            "Der leere LKW wog 3 t 900 kg, voll wiegt er 7 t. "
            "Wie viele kg wiegt jede der 10 unbekannten Kisten?"
        ),
        "answer": "20 kg pro Kiste.",
        "steps": [
            "7 × 40 = 280 kg + 620 kg + 4 × 500 = 2000 kg → Gesamtbeladung (ohne die 10 Kisten): 2900 kg.",
            "Gesamtzuladung: 7000 – 3900 = 3100 kg.",
            "Gewicht der 10 Kisten: 3100 – 2900 = 200 kg.",
            "200 : 10 = 20 kg pro Kiste.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.groessen.gewicht",
        ],
    },
    {
        "n": 4,
        "type": "Sachaufgabe: Regentonne",
        "text": (
            "Ein Regenfass fasst 5 hl. Wie oft muss man mit einem 10-Liter-Eimer "
            "schoepfen, um es vollstaendig zu leeren?"
        ),
        "answer": "50 Mal.",
        "steps": [
            "5 hl = 500 l.",
            "500 : 10 = 50 Mal.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.groessen.volumen",
        ],
    },
    {
        "n": 5,
        "type": "Kilometer rechnen",
        "text": (
            "Berechne:\n"
            "a) 5 km 600 m + 4,6 km = ___\n"
            "b) 5,009 km – 1809 m = ___"
        ),
        "answer": "a) 10,2 km ; b) 3,2 km",
        "steps": [
            "a) 5,6 km + 4,6 km = 10,2 km.",
            "b) 5,009 km – 1,809 km = 3,2 km.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.groessen.laenge",
        ],
    },
    {
        "n": 6,
        "type": "Einheiten umrechnen (leicht)",
        "text": (
            "Rechne um:\n"
            "8 m 99 cm 98 mm = ___ mm\n"
            "3 kg 64 g = ___ g\n"
            "18 000 Sekunden = ___ Stunden"
        ),
        "answer": "9088 mm ; 3064 g ; 5 Stunden",
        "steps": [
            "8 m 99 cm 98 mm: 8 m = 8000 mm, 99 cm = 990 mm; 8000 + 990 – 898 + 98 = 9088 mm. (Direkt: 8×1000 + 99×10 + 98 = 9088 mm.)",
            "3 kg 64 g = 3000 + 64 = 3064 g.",
            "18000 s : 60 = 300 min : 60 = 5 Stunden.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.groessen.laenge",
            "mathe.klasse4.groessen.gewicht",
            "mathe.klasse4.groessen.zeit",
        ],
    },
    {
        "n": 7,
        "type": "Einheiten umrechnen (schwer)",
        "text": (
            "Rechne um:\n"
            "32 kg 8 g = ___ g\n"
            "85 m 4 cm = ___ cm\n"
            "1 d 6 h 15 min = ___ min"
        ),
        "answer": "32008 g ; 8504 cm ; 1815 min",
        "steps": [
            "32 kg 8 g = 32000 + 8 = 32008 g.",
            "85 m 4 cm = 8500 + 4 = 8504 cm.",
            "1 d 6 h 15 min = 24×60 + 6×60 + 15 = 1440 + 360 + 15 = 1815 min.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.groessen.gewicht",
            "mathe.klasse4.groessen.laenge",
            "mathe.klasse4.groessen.zeit",
        ],
    },
    {
        "n": 8,
        "type": "Größen der Größe nach ordnen",
        "text": (
            "Ordne mit < (kleinste zuerst):\n"
            "800 mm / 80,1 cm / 82 dm\n"
            "402 kg / 420 000 g / 0,4 t"
        ),
        "answer": "800 mm < 80,1 cm < 82 dm ; 0,4 t < 402 kg < 420000 g",
        "steps": [
            "Längen in mm: 800 mm / 801 mm / 8200 mm → 800 < 801 < 8200.",
            "Gewichte in g: 402000 g / 420000 g / 400000 g → 400000 < 402000 < 420000.",
            "→ 0,4 t < 402 kg < 420000 g.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.groessen.laenge",
            "mathe.klasse4.groessen.gewicht",
        ],
    },
    {
        "n": 9,
        "type": "Sachaufgabe: Apfelsaft-Flaschen",
        "text": (
            "Ein Haendler befuellt 790 l Apfelsaft. Zuerst fuellt er 33 Kisten mit "
            "je 20 Flaschen à 1 l. Wie viele volle Kisten kann er dann noch mit "
            "½-Liter-Flaschen (je 26 Flaschen pro Kiste) befuellen?"
        ),
        "answer": "10 volle Kisten.",
        "steps": [
            "Verbrauch fuer 1-Liter-Flaschen: 33 × 20 = 660 l.",
            "Rest: 790 – 660 = 130 l.",
            "Pro ½-l-Kiste: 26 × 0,5 = 13 l.",
            "130 : 13 = 10 volle Kisten.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.groessen.volumen",
        ],
    },
    {
        "n": 10,
        "type": "Sachaufgabe: Aepfel wiegen",
        "text": (
            "Julia wiegt Aepfel auf einer Balkenwaage. Auf der linken Seite liegt "
            "ein 500-g-Gewicht. Auf der rechten Seite liegen Aepfel, 2 Gewichte "
            "à 50 g und 1 Gewicht à 10 g – die Waage ist nicht im Gleichgewicht. "
            "Julia tauscht ein 50-g-Gewicht gegen ein 20-g-Gewicht aus, jetzt ist "
            "die Waage im Gleichgewicht. Wie viel wiegen die Aepfel?"
        ),
        "answer": "420 g",
        "steps": [
            "Nach dem Tausch: 500 g = Aepfel + 50 g + 10 g + 20 g.",
            "Aepfel = 500 – 80 = 420 g.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.groessen.gewicht",
        ],
    },
]

NEW_KNOWLEDGE = []
