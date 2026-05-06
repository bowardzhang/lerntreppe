EXERCISE = {
    "id": "0023",
    "subject": "Mathe",
    "grade": 4,
    "title": "3. Lernzielkontrolle: Zahlenraum 100 000",
    "topic": "Zahlen bis 100 000: Ziffern, Runden, Vergleichen, Stellenwerte, Nachbarzahlen, Sachaufgaben",
    "publisher": "CATLUX",
    "source_pdf": "0023.pdf",
    "answer_pdf": "0023 (1).pdf",
    "total_points": 53.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Zahlen in Ziffern schreiben",
        "text": (
            "Schreibe folgende Zahlen in Ziffern!\n"
            "dreiundsechzigtausendzweiundfünfzig: ______________________\n"
            "siebzigtausendfünfhundert: ______________________"
        ),
        "answer": "63 052 ; 70 500",
        "steps": [
            "dreiundsechzigtausendzweiundfünfzig = 63 052",
            "siebzigtausendfünfhundert = 70 500",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.zahlen1000000.stellenwerte",
        ],
    },
    {
        "n": 2,
        "type": "Runden",
        "text": (
            "Runde auf volle Zehner, Hunderter, Tausender und Zehntausender!\n"
            "        | Zehner | Hunderter | Tausender | Zehntausender\n"
            "51 462  |        |           |           |\n"
            "72 356  |        |           |           |\n"
            "27 346  |        |           |           |\n"
            "36 487  |        |           |           |\n"
            "24 916  |        |           |           |\n"
            "43 548  |        |           |           |\n"
            "64 426  |        |           |           |\n"
            "79 573  |        |           |           |"
        ),
        "answer": (
            "51 462 → 51 460 / 51 500 / 51 000 / 50 000 ; "
            "72 356 → 72 360 / 72 400 / 72 000 / 70 000 ; "
            "27 346 → 27 350 / 27 300 / 27 000 / 30 000 ; "
            "36 487 → 36 490 / 36 500 / 36 000 / 40 000 ; "
            "24 916 → 24 920 / 24 900 / 25 000 / 20 000 ; "
            "43 548 → 43 550 / 43 500 / 44 000 / 40 000 ; "
            "64 426 → 64 430 / 64 400 / 64 000 / 60 000 ; "
            "79 573 → 79 570 / 79 600 / 80 000 / 80 000"
        ),
        "steps": [
            "Auf Zehner runden: letzte Stelle → 0, ≥5 aufrunden.",
            "Auf Hunderter runden: letzte zwei Stellen → 00, ≥50 aufrunden.",
            "Auf Tausender runden: letzte drei Stellen → 000, ≥500 aufrunden.",
            "Auf Zehntausender runden: letzte vier Stellen → 0000, ≥5000 aufrunden.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.zahlen1000000.runden",
        ],
    },
    {
        "n": 3,
        "type": "Sachaufgabe (Runden)",
        "text": (
            "Herr Sparsam kauft sich ein gebrauchtes Auto. Seine Frau fragt: "
            "„Wie viel hat es denn gekostet?“ Weil er es nicht genau sagen möchte, "
            "rundet er auf Tausender und antwortet: „Ich habe rund 16 000 Euro bezahlt.“\n"
            "Wie viel hat Herr Sparsam mindestens und höchstens bezahlt?\n"
            "mindestens: ______________ Euro   höchstens: ______________ Euro"
        ),
        "answer": "mindestens: 15 500 Euro ; höchstens: 16 499 Euro",
        "steps": [
            "Gerundet auf Tausender ergibt 16 000 → Originalwert liegt im Bereich [15 500, 16 499].",
            "15 500 rundet auf 16 000 ✓ ; 16 499 rundet auf 16 000 ✓.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.zahlen1000000.runden",
            "mathe.klasse4.sachaufgaben.mehrstufig",
        ],
    },
    {
        "n": 4,
        "type": "Zahlen der Größe nach ordnen",
        "text": (
            "Ordne die Zahlen der Größe nach!\n"
            "a) 70 000  69 900  9 999  10 002  66 980\n"
            "   _____ > _____ > _____ > _____ > _____\n"
            "b) 81 000  81 801  8 420  88 880\n"
            "   _____ < _____ < _____ < _____"
        ),
        "answer": (
            "a) 70 000 > 69 900 > 66 980 > 10 002 > 9 999 ; "
            "b) 8 420 < 81 000 < 81 801 < 88 880"
        ),
        "steps": [
            "a) Ziffernweise von links vergleichen: 70 000 > 69 900 > 66 980 > 10 002 > 9 999.",
            "b) 8 420 < 81 000 < 81 801 < 88 880.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.zahlen1000000.vergleichen",
        ],
    },
    {
        "n": 5,
        "type": "Richtige Aussagen ankreuzen",
        "text": (
            "Kreuze die richtigen Aussagen an!\n"
            "○ Die Zahl 22 000 ist um 2 000 größer als 20 000.\n"
            "○ Die Zahl 10 420 hat doppelt so viele Hunderter wie Zehner.\n"
            "○ Die Zahl 93 400 hat zweimal so viele ZT wie T.\n"
            "○ Die Zahl 7 500 ist halb so groß wie die Zahl 15 000."
        ),
        "answer": "Richtig: Aussage 1 (22 000 = 20 000 + 2 000), Aussage 2 (4 H, 2 Z → 4 = 2·2), Aussage 4 (7 500 = 15 000 : 2). Falsch: Aussage 3 (93 400: 9 ZT, 3 T → 9 ≠ 2·3).",
        "steps": [
            "Aussage 1: 22 000 − 20 000 = 2 000 ✓",
            "Aussage 2: 10 420 → H=4, Z=2 → 4 = 2·2 ✓",
            "Aussage 3: 93 400 → ZT=9, T=3 → 9 ≠ 2·3 ✗",
            "Aussage 4: 7 500 · 2 = 15 000 ✓",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.zahlen1000000.stellenwerte",
            "mathe.klasse4.zahlen1000000.vergleichen",
        ],
    },
    {
        "n": 6,
        "type": "Zahlenrätsel (mehrteilig)",
        "text": (
            "Zahlenrätsel\n"
            "a) Füge ich zum Doppelten meiner Zahl die Zahl 15 000 hinzu, "
            "erhalte ich die Hälfte von 70 000. Wie heißt meine Zahl?\n"
            "b) Drei Zahlen ergeben zusammen 100 000. Die erste Zahl ist 34 855, "
            "die zweite ist um 7 699 kleiner als die erste. Wie heißt die dritte Zahl?\n"
            "c) Berechne den Unterschied der größten und der kleinsten 5-stelligen Zahl "
            "aus den Ziffern 3, 5, 7 und 9 (jede Ziffer mindestens einmal).\n"
            "d) Wenn ich von 16 000 den 40. Teil dazu zähle, erhalte ich um 6 000 mehr "
            "als mein Freund. Wie viel hat mein Freund?\n"
            "e) Wie heißen die kleinste und die größte sechsstellige Zahl, bei denen "
            "keine 9 und keine 0 vorkommen?"
        ),
        "answer": (
            "a) Die Zahl heißt 10 000. ; "
            "b) Die dritte Zahl heißt 37 989. ; "
            "c) Der Unterschied ist 66 174. ; "
            "d) Mein Freund hat 10 400. ; "
            "e) kleinste: 111 111 ; größte: 888 888."
        ),
        "steps": [
            "a) 70 000 : 2 = 35 000 ; 35 000 − 15 000 = 20 000 ; 20 000 : 2 = 10 000.",
            "b) 2. Zahl: 34 855 − 7 699 = 27 156 ; 1.+2. = 62 011 ; 100 000 − 62 011 = 37 989.",
            "c) Größte: 99 753 ; Kleinste: 33 579 ; 99 753 − 33 579 = 66 174.",
            "d) 16 000 : 40 = 400 ; 16 000 + 400 = 16 400 ; 16 400 − 6 000 = 10 400.",
            "e) Ohne 0 und 9: kleinste = 111 111, größte = 888 888.",
        ],
        "points": 14.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.zahlenraetsel",
            "mathe.klasse4.schriftlich.addition",
            "mathe.klasse4.schriftlich.subtraktion",
            "mathe.klasse4.zahlen1000000.stellenwerte",
        ],
    },
    {
        "n": 7,
        "type": "Stellenwertdarstellung → Zahl",
        "text": (
            "Schreibe als Zahlen!\n"
            "4H 9ZT 4E 8T = ____________________\n"
            "4E 8H 4Z 9ZT = ____________________\n"
            "3E 9H 4ZT = ____________________"
        ),
        "answer": "98 404 ; 90 844 ; 40 903",
        "steps": [
            "4H 9ZT 4E 8T = 90 000 + 8 000 + 400 + 4 = 98 404.",
            "4E 8H 4Z 9ZT = 90 000 + 800 + 40 + 4 = 90 844.",
            "3E 9H 4ZT = 40 000 + 900 + 3 = 40 903.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.zahlen1000000.stellenwerte",
        ],
    },
    {
        "n": 8,
        "type": "Nachbarzahlen ergänzen",
        "text": (
            "Ergänze die Nachbarzahlen (Einer-, Zehner-, Hunderter-, Tausender-Nachbar)!\n"
            "... | ... | ... | ... | 14 306 | ... | ... | ... | ...\n"
            "... | ... | ... | ... | 79 619 | ... | ... | ... | ..."
        ),
        "answer": (
            "14 306: Tausend-Vorg=13 306, Hundert-Vorg=14 206, Zehn-Vorg=14 296, Einer-Vorg=14 305 | "
            "14 307 | Zehn-Nachf=14 316, Hundert-Nachf=14 406, Tausend-Nachf=15 306 ; "
            "79 619: 78 619 | 79 519 | 79 609 | 79 618 | 79 620 | 79 629 | 79 719 | 80 619"
        ),
        "steps": [
            "Jede Nachbarzahl entsteht durch ±1, ±10, ±100, ±1 000 von der Ausgangszahl.",
            "14 306: ±1→14305/14307, ±10→14296/14316, ±100→14206/14406, ±1000→13306/15306.",
            "79 619: ±1→79618/79620, ±10→79609/79629, ±100→79519/79719, ±1000→78619/80619.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.zahlen1000000.vorgaenger_nachfolger",
        ],
    },
    {
        "n": 9,
        "type": "Sachaufgabe (Aliens auf dem Mars)",
        "text": (
            "Auf dem Mars landen 3 Raumschiffe. Aus einem steigen 28 763 Aliens aus, "
            "aus einem anderen 35 633 und aus einem dritten 32 998. "
            "11 799 Aliens steigen gleich in ein anderes Raumschiff um, "
            "da sie weiter zum Planeten Xgenius fliegen.\n"
            "Wie viele Aliens bleiben auf dem Mars?"
        ),
        "answer": "Es bleiben 85 595 Aliens auf dem Mars.",
        "steps": [
            "28 763 + 35 633 + 32 998 = 97 394 (alle Aliens gesamt).",
            "97 394 − 11 799 = 85 595.",
            "A: Es bleiben 85 595 Aliens auf dem Mars.",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.schriftlich.addition",
            "mathe.klasse4.schriftlich.subtraktion",
        ],
    },
    {
        "n": 10,
        "type": "Sachaufgabe (Kilometerzähler)",
        "text": (
            "Herr Meier musste geschäftlich nach Hamburg fahren. "
            "Die Fahrstrecke dorthin betrug 463 km. Die Rückfahrt war um 47 km länger. "
            "Als er wieder zu Hause war, zeigte der Kilometerzähler genau 52 015 km an.\n"
            "Bei welchem Kilometerstand war Herr Meier abgefahren?"
        ),
        "answer": "Herr Meier ist bei einem Kilometerstand von 51 042 km abgefahren.",
        "steps": [
            "Rückfahrt: 463 + 47 = 510 km.",
            "Gesamtstrecke: 463 + 510 = 973 km.",
            "51 042 + 973 = 52 015 ✓ → Abfahrt bei 52 015 − 973 = 51 042 km.",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.schriftlich.addition",
            "mathe.klasse4.schriftlich.subtraktion",
        ],
    },
    {
        "n": 11,
        "type": "Sachaufgabe (Lastwagen, Gewicht)",
        "text": (
            "Ein Lastwagen wird beladen: 7 Kisten à 40 kg, 10 Kisten ohne Gewichtsangabe, "
            "eine Kiste Sand mit 0,620 t und 4 Paletten Holz à ½ Tonne.\n"
            "Wie viele kg wiegt jede Kiste ohne Gewichtsangabe, wenn der Lastwagen vorher "
            "3 t 900 kg wog und nach der Beladung 7 t wiegt?"
        ),
        "answer": "Jede Kiste ohne Gewichtsangabe wiegt 20 kg.",
        "steps": [
            "7 t = 7 000 kg ; Leergewicht = 3 900 kg.",
            "Zuladung gesamt: 7 000 − 3 900 = 3 100 kg.",
            "7 × 40 kg = 280 kg ; 0,620 t = 620 kg ; 4 × 500 kg = 2 000 kg → bekannte Ladung = 2 900 kg.",
            "Gewicht der 10 unbekannten Kisten: 3 100 − 2 900 = 200 kg.",
            "Pro Kiste: 200 : 10 = 20 kg.",
        ],
        "points": 7.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.groessen.gewicht",
            "mathe.klasse4.schriftlich.addition",
            "mathe.klasse4.schriftlich.subtraktion",
            "mathe.klasse4.schriftlich.multiplikation",
            "mathe.klasse4.schriftlich.division",
        ],
    },
]

NEW_KNOWLEDGE = []
