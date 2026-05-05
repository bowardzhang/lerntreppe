EXERCISE = {
    "id": "0025",
    "subject": "Mathe",
    "grade": 4,
    "title": "1/2. Übungslernzielkontrolle",
    "topic": "Zahlenraum bis 1000; Sachaufgaben",
    "publisher": "CATLUX",
    "source_pdf": "0025.pdf",
    "answer_pdf": "0025 (1).pdf",
    "total_points": 59.0,  # sum of all …/N: 3+3+5+3+2+5+4+4+2+9+4+3+4+4+4=59; no Notentabelle in PDF
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Sachaufgabe (F-R-A)",
        "text": (
            "Löse die Aufgabe in der Form (F – R – A)!\n"
            "Peter bekommt vom Nikolaus einen 2 kg schweren Sack. Er enthält 225 g Nüsse, "
            "620 g Äpfel, 329 g Mandarinen und ein Buch."
        ),
        "answer": "Das Buch wiegt 826 g.",
        "steps": [
            "F: Wie schwer ist das Buch?",
            "225 g + 620 g + 329 g = 1174 g",
            "2 kg = 2000 g",
            "2000 g – 1174 g = 826 g",
            "A: Das Buch wiegt 826 g.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.sachaufgaben.mehrstufig", "mathe.klasse4.schriftlich.addition", "mathe.klasse4.schriftlich.subtraktion"],
    },
    {
        "n": 2,
        "type": "Sachaufgabe",
        "text": (
            "Drei Äpfel wiegen zusammen 620 g. Der erste Apfel wiegt 260 g, der zweite doppelt "
            "soviel wie der dritte. Wie viel wiegt jeder der beiden Äpfel?"
        ),
        "answer": "Ein Apfel wiegt 120 g, der andere 240 g.",
        "steps": [
            "Apfel 1 + Apfel 2 + Apfel 3 = 620 g",
            "260 g + Apfel 2 + Apfel 3 = 620 g",
            "620 g – 260 g = 360 g (Summe von Apfel 2 und Apfel 3)",
            "Apfel 2 = 2 × Apfel 3  →  Apfel 3 + 2 × Apfel 3 = 3 × Apfel 3 = 360 g",
            "360 g : 3 = 120 g (Apfel 3)",
            "120 g × 2 = 240 g (Apfel 2)",
            "Probe: 120 + 240 + 260 = 620 ✓",
            "A: Ein Apfel wiegt 120 g, der andere 240 g.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.sachaufgaben.mehrstufig", "mathe.klasse4.schriftlich.division"],
    },
    {
        "n": 3,
        "type": "Sachaufgabe",
        "text": (
            "Der Nikolaus füllt auf seinen Schlitten 4 Säcke Nüsse zu 50 kg, 5 Säcke "
            "Mandarinen zu 25 kg und 198 kg Äpfel. Wie viele Rentiere braucht er für seinen "
            "Schlitten, wenn ein Rentier 100 kg ziehen kann?"
        ),
        "answer": "Er braucht 6 Rentiere.",
        "steps": [
            "4 × 50 kg = 200 kg (Nüsse)",
            "5 × 25 kg = 125 kg (Mandarinen)",
            "200 + 125 + 198 = 523 kg (Gesamtlast)",
            "523 kg ÷ 100 kg = 5 Rentiere tragen 500 kg, aber es bleiben 23 kg übrig",
            "Also werden 6 Rentiere benötigt.",
            "A: Er braucht 6 Rentiere.",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.sachaufgaben.mehrstufig", "mathe.klasse4.schriftlich.multiplikation"],
    },
    {
        "n": 4,
        "type": "Teiler bestimmen",
        "text": (
            "Suche die Teiler!\n"
            "18 hat Teiler: ___________________\n"
            "23 hat Teiler: ___________________\n"
            "42 hat Teiler: ___________________"
        ),
        "answer": "18: 2, 3, 6, 9 | 23: Primzahl | 42: 2, 3, 6, 7, 14, 21",
        "steps": [
            "18: 18 ÷ 2 = 9, 18 ÷ 3 = 6, 18 ÷ 6 = 3, 18 ÷ 9 = 2 → Teiler: 1, 2, 3, 6, 9, 18 (außer 1 und 18 gesucht: 2, 3, 6, 9)",
            "23: 23 ist durch keine Zahl außer 1 und 23 teilbar → Primzahl",
            "42: 42 ÷ 2 = 21, 42 ÷ 3 = 14, 42 ÷ 6 = 7, 42 ÷ 7 = 6, 42 ÷ 14 = 3, 42 ÷ 21 = 2 → Teiler: 2, 3, 6, 7, 14, 21",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.sachaufgaben.zahlenraetsel"],
    },
    {
        "n": 5,
        "type": "Sachaufgabe",
        "text": (
            "Der Erfinder der Glühbirne, Thomas Edison hat in 25 Jahren etwa "
            "1000 wichtige Erfindungen gemacht.\n"
            "Wie viel Erfindungen machte er dann in zwei Jahren?"
        ),
        "answer": "In zwei Jahren hat Edison 80 Erfindungen gemacht.",
        "steps": [
            "25 Jahre → 1000 Erfindungen",
            "1 Jahr → 1000 ÷ 25 = 40 Erfindungen",
            "2 Jahre → 2 × 40 = 80 Erfindungen",
            "A: In zwei Jahren hat Edison 80 Erfindungen gemacht.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.sachaufgaben.mehrstufig", "mathe.klasse4.schriftlich.multiplikation"],
    },
    {
        "n": 6,
        "type": "Sachaufgabe",
        "text": (
            "Alle 5 Minuten fährt das Karussell mit 7 Kindern los. Wie viele Kinder sind\n"
            "a) in 20 Minuten\n"
            "b) in einer Stunde mit dem Karussell gefahren?"
        ),
        "answer": "a) 28 Kinder in 20 Minuten; b) 84 Kinder in einer Stunde.",
        "steps": [
            "5 min → 7 Kinder",
            "10 min → 14 Kinder",
            "20 min → 28 Kinder (4 Fahrten × 7 Kinder)",
            "60 Minuten = 3 × 20 Minuten",
            "3 × 28 = 84 Kinder in einer Stunde",
            "A: In 20 Minuten sind es 28 Kinder, in einer Stunde 84 Kinder.",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.sachaufgaben.mehrstufig", "mathe.klasse4.schriftlich.multiplikation"],
    },
    {
        "n": 7,
        "type": "Sachaufgabe",
        "text": (
            "Ein Schifahrer braucht für eine 720 Meter lange Abfahrt 1 Minute "
            "und 30 Sekunden. Wie viele Meter legt er in einer Sekunde zurück?"
        ),
        "answer": "Der Schifahrer legt in der Sekunde 8 m zurück.",
        "steps": [
            "1 Minute 30 Sekunden = 60 s + 30 s = 90 s",
            "720 m ÷ 90 s = 8 m/s",
            "A: Der Schifahrer legt in der Sekunde 8 m zurück.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.sachaufgaben.mehrstufig", "mathe.klasse4.schriftlich.division"],
    },
    {
        "n": 8,
        "type": "Stellenwerte",
        "text": (
            "Wie heißt die Zahl?\n"
            "1 T + 5 H + 4 Z + 2 E = _________\n"
            "3 T + 8 Z = _________\n"
            "4 H + 7 Z + 1 E = _________\n"
            "2 T + 9 H + 4 E = _________"
        ),
        "answer": "1542; 3080; 471; 2904",
        "steps": [
            "1 T + 5 H + 4 Z + 2 E = 1000 + 500 + 40 + 2 = 1542",
            "3 T + 8 Z = 3000 + 80 = 3080",
            "4 H + 7 Z + 1 E = 400 + 70 + 1 = 471",
            "2 T + 9 H + 4 E = 2000 + 900 + 4 = 2904",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.zahlen1000000.stellenwerte"],
    },
    {
        "n": 9,
        "type": "Zahlenstrahl",
        "text": (
            "Wie heißen die Zahlen?\n"
            "600\n"
            "_______|__________________|_________|_______________|_______|__1000\n"
            "_I_._._._._i_._._._._I_._._._._i_._._._._I_._._._._i_._._._._I_._._._._i_._._._._I"
        ),
        "answer": "640, 760, 820, 920, 970",
        "steps": [
            "Der Zahlenstrahl geht von 600 bis 1000 (Abstand 400).",
            "Die Markierungen teilen den Strahl in Abschnitte zu je 40.",
            "Abgelesene Zahlen: 640, 760, 820, 920, 970",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.zahlen1000000.zahlenstrahl"],
    },
    {
        "n": 10,
        "type": "Kopfrechnen Multiplikation",
        "text": (
            "Rechne aus!\n"
            "400 • 6 = _____\n"
            "402 • 6 = _____\n"
            "405 • 6 = _____\n"
            "_____ • 5 = 3000\n"
            "_____ • 5 = 3015\n"
            "_____ • 5 = 3030\n"
            "200 • 9 = _____\n"
            "_____ • 9 = 1854\n"
            "204 • 9 = _____"
        ),
        "answer": "2400; 2412; 2430 | 600; 603; 606 | 1800; 206; 1836",
        "steps": [
            "400 × 6 = 2400",
            "402 × 6 = 2412",
            "405 × 6 = 2430",
            "600 × 5 = 3000",
            "603 × 5 = 3015",
            "606 × 5 = 3030",
            "200 × 9 = 1800",
            "206 × 9 = 1854",
            "204 × 9 = 1836",
        ],
        "points": 9.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.schriftlich.multiplikation", "mathe.klasse4.zahlen1000000.stellenwerte"],
    },
    {
        "n": 11,
        "type": "Kopfrechnen Addition/Subtraktion",
        "text": (
            "Rechne aus!\n"
            "2 371 + 50 = _______\n"
            "3 000 – 480 = _______\n"
            "1 649 + 80 = _______\n"
            "1 707 – 190 = _______"
        ),
        "answer": "2421; 2520; 1729; 1517",
        "steps": [
            "2371 + 50 = 2421",
            "3000 – 480 = 2520",
            "1649 + 80 = 1729",
            "1707 – 190 = 1517",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.schriftlich.addition", "mathe.klasse4.schriftlich.subtraktion"],
    },
    {
        "n": 12,
        "type": "Größen: Volumen/Liter",
        "text": (
            "Wie viel Liter sind es?\n"
            "1/2 l: 5 Flaschen Milch = ____ l\n"
            "1/4 l: 6 Dosen Cola = _____ l\n"
            "0,2 l: 7 Tassen Kaffee = ____ l"
        ),
        "answer": "5 Flaschen Milch = 2 1/2 l; 6 Dosen Cola = 1 1/2 l; 7 Tassen Kaffee = 1,4 l",
        "steps": [
            "5 × 1/2 l = 2,5 l = 2 1/2 l",
            "6 × 1/4 l = 1,5 l = 1 1/2 l",
            "7 × 0,2 l = 1,4 l",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.dezimalzahlen.grundlagen", "mathe.klasse4.sachaufgaben.mehrstufig"],
    },
    {
        "n": 13,
        "type": "Sachaufgabe",
        "text": (
            "Rechne aus!\n"
            "Tatjana holt auf ihrem Schulweg immer ihre Freundin Ilona ab. Bis zu Ilona sind es "
            "300 Meter und von Ilonas Haus bis zur Schule noch einmal 200 Meter.\n"
            "Wie viel Meter legt Tatjana jeden Tag auf ihrem Schulweg zurück? "
            "(Bitte Hin- und Rückweg berücksichtigen!)"
        ),
        "answer": "Tatjana legt jeden Tag 1000 m zurück.",
        "steps": [
            "Hinweg: 300 m (zu Ilona) + 200 m (zur Schule) = 500 m",
            "Rückweg: ebenfalls 500 m",
            "500 × 2 = 1000 m pro Tag",
            "A: Tatjana legt jeden Tag 1000 m zurück.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.sachaufgaben.mehrstufig", "mathe.klasse4.schriftlich.multiplikation"],
    },
    {
        "n": 14,
        "type": "Zeitrechnung",
        "text": (
            "Bestimme die fehlenden Zeitangaben!\n"
            "Beginn:  8.35  |  11.45  |  ___   |  20.03  |  ___\n"
            "Ende:    ___   |  13.05  |  12.50 |  ___    |  15.15\n"
            "Dauer:   2h 20 min | ___ | 1h 30 min | 2h 14 min | 50 min"
        ),
        "answer": (
            "Beginn 8.35 → Ende 10.55 (Dauer 2h 20min); "
            "Beginn 11.45 → Ende 13.05 (Dauer 1h 20min); "
            "Beginn 11.20 → Ende 12.50 (Dauer 1h 30min); "
            "Beginn 20.03 → Ende 22.17 (Dauer 2h 14min); "
            "Beginn 14.25 → Ende 15.15 (Dauer 50min)"
        ),
        "steps": [
            "8.35 + 2h 20min = 10.55 → Ende: 10.55",
            "13.05 – 11.45 = 1h 20min → Dauer: 1h 20min",
            "12.50 – 1h 30min = 11.20 → Beginn: 11.20",
            "20.03 + 2h 14min = 22.17 → Ende: 22.17",
            "15.15 – 50min = 14.25 → Beginn: 14.25",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse3.groessen.zeit"],
    },
    {
        "n": 15,
        "type": "Größen ergänzen (Zeit)",
        "text": (
            "Ergänze!\n"
            "4 h = ____ min\n"
            "7 h = ____ min\n"
            "3 Tage = ____ h\n"
            "8 Tage = ____ h\n"
            "4 Wochen = ____ Tage\n"
            "11 Wochen = ____ Tage\n"
            "5 min = ____ s\n"
            "9 min = ____ s"
        ),
        "answer": "240 min; 420 min; 72 h; 192 h; 28 Tage; 77 Tage; 300 s; 540 s",
        "steps": [
            "4 h = 4 × 60 = 240 min",
            "7 h = 7 × 60 = 420 min",
            "3 Tage = 3 × 24 = 72 h",
            "8 Tage = 8 × 24 = 192 h",
            "4 Wochen = 4 × 7 = 28 Tage",
            "11 Wochen = 11 × 7 = 77 Tage",
            "5 min = 5 × 60 = 300 s",
            "9 min = 9 × 60 = 540 s",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse3.groessen.zeit"],
    },
]

NEW_KNOWLEDGE = [
    {
        "id": "mathe.klasse4.zahlen1000.teiler",
        "name": "Teiler und Primzahlen",
        "parent": "mathe.klasse4.zahlen1000000",
    },
]
