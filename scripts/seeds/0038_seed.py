EXERCISE = {
    "id": "0038",
    "subject": "Mathe",
    "grade": 4,
    "title": "2. Lernzielkontrolle",
    "topic": "Zahlenraum bis 10000",
    "publisher": "CATLUX",
    "source_pdf": "0038.pdf",
    "answer_pdf": "0038_Lösung.pdf",
    "total_points": 62.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Runden",
        "text": (
            "Runde auf Tausender!\n"
            "8501 ______________\n"
            "4120 ______________\n"
            "Runde auf Hunderter!\n"
            "3490 ______________\n"
            "7449 ______________\n"
            "Runde auf Zehner!\n"
            "4827 ______________\n"
            "8787 ______________"
        ),
        "answer": "8501→9000; 4120→4000 | 3490→3500; 7449→7400 | 4827→4830; 8787→8790",
        "steps": [
            "Auf Tausender runden: Hunderterstelle entscheidet (≥5 aufrunden, <5 abrunden)",
            "8501 → Hunderterstelle=5 → aufrunden → 9000",
            "4120 → Hunderterstelle=1 → abrunden → 4000",
            "Auf Hunderter runden: Zehnerstelle entscheidet",
            "3490 → Zehnerstelle=9 → aufrunden → 3500",
            "7449 → Zehnerstelle=4 → abrunden → 7400",
            "Auf Zehner runden: Einerstelle entscheidet",
            "4827 → Einerstelle=7 → aufrunden → 4830",
            "8787 → Einerstelle=7 → aufrunden → 8790",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.zahlen1000000.runden"],
    },
    {
        "n": 2,
        "type": "Stellenwerte",
        "text": (
            "Wie heißt die Zahl?\n"
            "3H 4T 9E = ___________\n"
            "3E 5T = ___________\n"
            "20H 2Z = ___________"
        ),
        "answer": "3H 4T 9E = 4309; 3E 5T = 5003; 20H 2Z = 2020",
        "steps": [
            "3H 4T 9E: T=Tausender, H=Hunderter, E=Einer → 4 × 1000 + 3 × 100 + 0 × 10 + 9 = 4309",
            "3E 5T: 5 × 1000 + 0 × 100 + 0 × 10 + 3 = 5003",
            "20H 2Z: 20 × 100 + 2 × 10 = 2000 + 20 = 2020",
        ],
        "points": 1.5,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.zahlen1000000.stellenwerte"],
    },
    {
        "n": 3,
        "type": "Schriftliche Addition und Subtraktion",
        "text": (
            "Rechne schriftlich bzw. ergänze!\n"
            "a) 3485 + 2674 + 305\n"
            "b) 406 + 5928 + 84 + 2949\n"
            "c) 9237 – 5694\n"
            "d) 7040 – 2798\n"
            "Ergänze die fehlenden Ziffern:\n"
            "  3□47\n"
            "+ 2 4□8\n"
            "-------\n"
            "□7 0 5\n"
            "\n"
            "  9 6 5□\n"
            "– 3□9 5\n"
            "-------\n"
            "□3□5"
        ),
        "answer": (
            "a) 6464; b) 9367; c) 3543; d) 4242; "
            "3247 + 2458 = 5705; 9650 – 3295 = 6355"
        ),
        "steps": [
            "a) 3485 + 2674 + 305 = 6464",
            "b) 406 + 5928 + 84 + 2949 = 9367",
            "c) 9237 – 5694 = 3543",
            "d) 7040 – 2798 = 4242",
            "Ergänzung: 3247 + 2458 = 5705 (fehlende Ziffern: 2, 4, 5)",
            "Ergänzung: 9650 – 3295 = 6355 (fehlende Ziffern: 0, 2, 6, 5)",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.schriftlich.addition", "mathe.klasse4.schriftlich.subtraktion"],
    },
    {
        "n": 4,
        "type": "Terme mit Rechenreihenfolge",
        "text": (
            "Hier musst du überlegen!\n"
            "a) 3 • 7 + 48 – 17 = _____\n"
            "b) 55 – 15 : 3 = _____\n"
            "c) 90 : 9 – 2 • 4 = _____"
        ),
        "answer": "a) 52; b) 50; c) 2",
        "steps": [
            "a) Punkt vor Strich: 3 × 7 = 21; dann 21 + 48 – 17 = 69 – 17 = 52",
            "b) Punkt vor Strich: 15 : 3 = 5; dann 55 – 5 = 50",
            "c) Punkt vor Strich: 90 : 9 = 10 und 2 × 4 = 8; dann 10 – 8 = 2",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.schriftlich.multiplikation", "mathe.klasse4.schriftlich.division"],
    },
    {
        "n": 5,
        "type": "Einmaleins und Kopfrechnen",
        "text": (
            "Kannst du das Einmaleins?\n"
            "6 • 30 = ____________\n"
            "900 • 6 = ____________\n"
            "4 • 400 = ____________\n"
            "40 • 80 = ____________\n"
            "8 • 320 = ____________\n"
            "870 • 3 = ____________"
        ),
        "answer": "180; 5400; 1600; 3200; 2560; 2610",
        "steps": [
            "6 × 30 = 6 × 3 × 10 = 180",
            "900 × 6 = 9 × 6 × 100 = 5400",
            "4 × 400 = 4 × 4 × 100 = 1600",
            "40 × 80 = 4 × 8 × 100 = 3200",
            "8 × 320 = 8 × 32 × 10 = 256 × 10 = 2560",
            "870 × 3 = 87 × 3 × 10 = 261 × 10 = 2610",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse2.einmaleins.reihen", "mathe.klasse4.schriftlich.multiplikation"],
    },
    {
        "n": 6,
        "type": "Faktorenpaare zu 10000",
        "text": (
            "10000 = ___________ • 500\n"
            "10000 = 5 • ___________\n"
            "10000 = ___________ • 2500\n"
            "10000 = 200 • ___________"
        ),
        "answer": "20 × 500; 5 × 2000; 4 × 2500; 200 × 50",
        "steps": [
            "10000 ÷ 500 = 20 → 10000 = 20 × 500",
            "10000 ÷ 5 = 2000 → 10000 = 5 × 2000",
            "10000 ÷ 2500 = 4 → 10000 = 4 × 2500",
            "10000 ÷ 200 = 50 → 10000 = 200 × 50",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.zahlen1000000.stellenwerte", "mathe.klasse4.schriftlich.division"],
    },
    {
        "n": 7,
        "type": "Zahlen dazwischen",
        "text": (
            "Welche Zahl liegt genau dazwischen?\n"
            "5000 ___________ 10000\n"
            "4560 ___________ 5000\n"
            "1000 ___________ 5000\n"
            "2000 ___________ 3000"
        ),
        "answer": "7500; 4780; 3000; 2500",
        "steps": [
            "(5000 + 10000) ÷ 2 = 15000 ÷ 2 = 7500",
            "(4560 + 5000) ÷ 2 = 9560 ÷ 2 = 4780",
            "(1000 + 5000) ÷ 2 = 6000 ÷ 2 = 3000",
            "(2000 + 3000) ÷ 2 = 5000 ÷ 2 = 2500",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.zahlen1000000.zahlenstrahl", "mathe.klasse4.zahlen1000000.vergleichen"],
    },
    {
        "n": 8,
        "type": "Division mit und ohne Rest",
        "text": (
            "Teile mit und ohne Rest!\n"
            "420 : 50 = ……………\n"
            "5600 : 70 = ……………\n"
            "2440 : 40 = ……………\n"
            "810 : 90 = ……………\n"
            "………. : 30 = 10 R 7\n"
            "…………: 70 = 30 R 40"
        ),
        "answer": "8 R 20; 80; 61; 9; 307; 2140",
        "steps": [
            "420 : 50 = 8 R 20 (8 × 50 = 400, Rest 20)",
            "5600 : 70 = 80 (80 × 70 = 5600)",
            "2440 : 40 = 61 (61 × 40 = 2440)",
            "810 : 90 = 9 (9 × 90 = 810)",
            "? : 30 = 10 R 7 → ? = 10 × 30 + 7 = 307",
            "? : 70 = 30 R 40 → ? = 30 × 70 + 40 = 2140",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.schriftlich.division", "mathe.klasse3.division.rest"],
    },
    {
        "n": 9,
        "type": "Magische Zeichen (Gleichungssystem)",
        "text": (
            "Magische Zeichen\n"
            "Achtung gleiche Zeichen = gleiche Zahl!\n"
            "[Tomate] + 5400 + [Paprika] = 10000\n"
            "[Tomate] – 2800 = 1000\n"
            "[Tomate] = _________  [Paprika] = _________"
        ),
        "answer": "Tomate = 3800; Paprika = 800",
        "steps": [
            "[Tomate] – 2800 = 1000 → [Tomate] = 1000 + 2800 = 3800",
            "[Tomate] + 5400 + [Paprika] = 10000 → 3800 + 5400 + [Paprika] = 10000",
            "9200 + [Paprika] = 10000 → [Paprika] = 10000 – 9200 = 800",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.sachaufgaben.zahlenraetsel", "mathe.klasse4.schriftlich.subtraktion"],
    },
    {
        "n": 10,
        "type": "Halbschriftliches Rechnen",
        "text": (
            "Rechne halbschriftlich!\n"
            "365 • 4 =\n"
            "7 • 418 =\n"
            "810 • 6 =\n"
            "1784 : 4 ="
        ),
        "answer": "1460; 2926; 4860; 446",
        "steps": [
            "365 × 4: 300×4=1200, 60×4=240, 5×4=20 → 1200+240+20=1460",
            "7 × 418: 7×400=2800, 7×10=70, 7×8=56 → 2800+70+56=2926",
            "810 × 6: 800×6=4800, 10×6=60 → 4800+60=4860",
            "1784 ÷ 4: 1600÷4=400, 160÷4=40, 24÷4=6 → 400+40+6=446",
        ],
        "points": 8.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.schriftlich.multiplikation", "mathe.klasse4.schriftlich.division_halbschriftlich"],
    },
    {
        "n": 11,
        "type": "Zahlenstrahl ablesen",
        "text": (
            "Wie heißen die Zahlen auf dem Zahlenstrahl?\n"
            "A: ____________ B: ____________ C: ____________ D: ____________\n"
            "E: ____________ F: ____________ G: ____________"
        ),
        "answer": "A: 5400, B: 6000, C: 6800, D: 7200, E: 5140, F: 5190, G: 5240",
        "steps": [
            "Erster Zahlenstrahl: Markierungen bei 5000, 5800, 6400 (Abstände je 200)",
            "A liegt 2 Schritte nach 5000: 5000 + 2×200 = 5400",
            "B liegt auf 5800 + 1 Großschritt: 6000",
            "C liegt auf 6400 + 2 Schritte: 6800",
            "D liegt auf 6400 + 4 Schritte: 7200",
            "Zweiter Zahlenstrahl: Markierungen bei 5200, 5250 (Abstände je 10)",
            "E: 5140, F: 5190, G: 5240",
        ],
        "points": 3.5,
        "has_image": True,
        "image": "0038_q11_zahlenstrahl_ad.png",
        "knowledge": ["mathe.klasse4.zahlen1000000.zahlenstrahl"],
    },
    {
        "n": 12,
        "type": "Streifenbild (Zerlegung)",
        "text": (
            "Setze in das Streifenbild die richtigen Zahlen ein!\n"
            "[Tabelle mit vorgegebenen Werten: 5000 oben, 2000 und 9000 eingetragen]"
        ),
        "answer": (
            "Zeile 1 (Gesamt oben): 4000 | 5000\n"
            "Zeile 2: 2000 | 1000 | 1000 | 2500 | 2500\n"
            "Zeile 3 (Mitte): 9000\n"
            "Zeile 4: 1000 | 4000 | 4000"
        ),
        "steps": [
            "Gesamtsumme = 9000, obere Hälfte = 4000 + 5000 = 9000",
            "2000 + 1000 + 1000 + 2500 + 2500 = 9000",
            "Untere Zeile: 1000 + 4000 + 4000 = 9000",
        ],
        "points": 4.0,
        "has_image": True,
        "image": "0038_q12_streifenbild.png",
        "knowledge": ["mathe.klasse4.zahlen1000000.stellenwerte", "mathe.klasse4.schriftlich.addition"],
    },
    {
        "n": 13,
        "type": "Sachaufgabe (Tabelle/Gewicht)",
        "text": (
            "Der Großbauer Huber aus Kleinostheim beliefert ein Unternehmen in München das "
            "Tomatenketchup herstellt. Er besitzt drei LKWs mit unterschiedlichem Leergewicht. "
            "Der erste LKW wiegt 7200 kg, der zweite LKW 3500 kg und der dritte LKW 6,5 t.\n"
            "Der erste LKW hat eine Ladung von 2,5 t. Der zweite und der dritte LKW teilen sich "
            "die Ladung von 7 t. Auf dem Weg nach München müssen die LKWs die nebenstehende "
            "Brücke überqueren. (Gewichtsbeschränkung: 8 t)\n"
            "Trage zuerst alle Informationen in die Tabelle ein und rechne dann mit Hilfe der Tabelle.\n"
            "Frage: Wer darf über die Brücke fahren?\n"
            "Antwort: _______________________________________________________"
        ),
        "answer": "Es darf der 2. LKW fahren (Gesamtgewicht 7000 kg = 7 t ≤ 8 t).",
        "steps": [
            "Einheiten umrechnen: 6,5 t = 6500 kg; 2,5 t = 2500 kg; 7 t = 7000 kg",
            "7 t Ladung wird geteilt: 7000 kg ÷ 2 = 3500 kg pro LKW (2. und 3.)",
            "1. LKW: Leergewicht 7200 kg + Ladung 2500 kg = 9700 kg → 9,7 t > 8 t → darf nicht",
            "2. LKW: Leergewicht 3500 kg + Ladung 3500 kg = 7000 kg → 7 t ≤ 8 t → darf",
            "3. LKW: Leergewicht 6500 kg + Ladung 3500 kg = 10000 kg → 10 t > 8 t → darf nicht",
            "A: Es darf der 2. LKW fahren.",
        ],
        "points": 10.0,
        "has_image": True,
        "image": "0038_q13_bruecke.png",
        "knowledge": ["mathe.klasse4.sachaufgaben.mehrstufig", "mathe.klasse4.sachaufgaben.tabellen"],
    },
    {
        "n": 14,
        "type": "Sachaufgabe (mehrstufig)",
        "text": (
            "Bei einem Schulfest werden insgesamt 968 Euro eingenommen. 308 Euro werden "
            "für Musikinstrumente ausgegeben. Für die Schulbücherei werden 8 Bücher "
            "gekauft. Ein Buch kostet 13 Euro. Wie viel Geld bleibt übrig?"
        ),
        "answer": "Es bleiben noch 556 Euro übrig.",
        "steps": [
            "Kosten für Bücher: 8 × 13 € = 104 €",
            "Einnahmen – Musikinstrumente – Bücher: 968 € – 308 € – 104 € = 556 €",
            "A: Es bleiben noch 556 Euro übrig.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.sachaufgaben.mehrstufig", "mathe.klasse4.schriftlich.subtraktion"],
    },
]

NEW_KNOWLEDGE = []
