EXERCISE = {
    "id": "0904",
    "subject": "Mathe",
    "grade": 4,
    "title": "3. Probe: Zahlenraum bis 100 000",
    "topic": "Stellenwerte, Runden, Vergleichen, Kopfrechnen, Teilbarkeit, Sachaufgaben",
    "publisher": "CATLUX",
    "source_pdf": "0904.pdf",
    "answer_pdf": "0904 (1).pdf",
    "total_points": 51.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Runden und Säulendiagramm",
        "text": (
            "Runde die Besucherzahlen eines Tierparks auf 10 000 und stelle sie "
            "in einem Säulendiagramm dar! Denke an die richtige Beschriftung!\n"
            "März: 12 428    April: 18 369    Mai: 46 616    Juni: 65 379"
        ),
        "answer": "März: 10 000 ; April: 20 000 ; Mai: 50 000 ; Juni: 70 000",
        "steps": [
            "12 428 → auf 10 000 gerundet = 10 000 (12 < 15).",
            "18 369 → auf 10 000 gerundet = 20 000 (18 ≥ 15).",
            "46 616 → auf 10 000 gerundet = 50 000 (46 ≥ 45).",
            "65 379 → auf 10 000 gerundet = 70 000 (65 ≥ 65).",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.zahlen1000000.runden",
            "mathe.klasse4.sachaufgaben.tabellen",
        ],
    },
    {
        "n": 2,
        "type": "Stellenwertzerlegung",
        "text": (
            "Zerlege in Zehntausender (ZT), Tausender (T), Hunderter (H), "
            "Zehner (Z) und Einer (E).\n"
            "68 347 = ___\n"
            "63 402 = ___\n"
            " 6 401 = ___\n"
            "78 006 = ___"
        ),
        "answer": (
            "68 347 = 6 ZT 8 T 3 H 4 Z 7 E ; "
            "63 402 = 6 ZT 3 T 4 H 2 E ; "
            "6 401 = 6 T 4 H 1 E ; "
            "78 006 = 7 ZT 8 T 6 E"
        ),
        "steps": [
            "68 347: 6 ZT (60000) + 8 T (8000) + 3 H (300) + 4 Z (40) + 7 E.",
            "63 402: 6 ZT + 3 T + 4 H + 0 Z + 2 E.",
            "6 401: 0 ZT + 6 T + 4 H + 0 Z + 1 E.",
            "78 006: 7 ZT + 8 T + 0 H + 0 Z + 6 E.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.zahlen1000000.stellenwerte",
        ],
    },
    {
        "n": 3,
        "type": "Stellenwertdarstellung in Zahl",
        "text": (
            "Wie heißt die Zahl?\n"
            "7 ZT 4 T 8 H 5 Z 3 E = ___\n"
            "6 ZT 5 H 8 E = ___\n"
            "4 ZT 9 T 6 H 8 Z 7 E = ___\n"
            "9 ZT 3 T 5 Z = ___"
        ),
        "answer": "74 853 ; 60 508 ; 49 687 ; 93 050",
        "steps": [
            "7·10000 + 4·1000 + 8·100 + 5·10 + 3 = 74 853.",
            "6·10000 + 0·1000 + 5·100 + 0·10 + 8 = 60 508.",
            "4·10000 + 9·1000 + 6·100 + 8·10 + 7 = 49 687.",
            "9·10000 + 3·1000 + 0·100 + 5·10 + 0 = 93 050.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.zahlen1000000.stellenwerte",
        ],
    },
    {
        "n": 4,
        "type": "Zahlen vergleichen",
        "text": (
            "Kleiner oder größer? Trage ein: < >\n"
            "63 700 ___ 67 300    73 080 ___ 73 500    72 470 ___ 27 470\n"
            "50 620 ___ 50 260    84 540 ___ 85 440    31 860 ___ 38 610"
        ),
        "answer": "<, <, > ; >, <, <",
        "steps": [
            "63 700 < 67 300 (Tausender 3 < 7).",
            "73 080 < 73 500 (Hunderter 0 < 5).",
            "72 470 > 27 470 (Zehntausender 7 > 2).",
            "50 620 > 50 260 (Hunderter 6 > 2).",
            "84 540 < 85 440 (Tausender 4 < 5).",
            "31 860 < 38 610 (Tausender 1 < 8).",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.zahlen1000000.vergleichen",
        ],
    },
    {
        "n": 5,
        "type": "Kopfrechnen mit Tausendern",
        "text": (
            "Rechne im Kopf!\n"
            "+ 34 000:  54 000 → ___    38 000 → ___    58 000 → ___\n"
            "+ 26 000:  66 000 → ___    74 000 → ___    42 000 → ___\n"
            "− 35 000:  57 000 → ___    63 000 → ___    94 000 → ___"
        ),
        "answer": (
            "54 000+34 000 = 88 000 ; 38 000+34 000 = 72 000 ; 58 000+34 000 = 92 000 ; "
            "66 000+26 000 = 92 000 ; 74 000+26 000 = 100 000 ; 42 000+26 000 = 68 000 ; "
            "57 000−35 000 = 22 000 ; 63 000−35 000 = 28 000 ; 94 000−35 000 = 59 000"
        ),
        "steps": [
            "Summen +34 000: 88 000, 72 000, 92 000.",
            "Summen +26 000: 92 000, 100 000, 68 000.",
            "Differenzen −35 000: 22 000, 28 000, 59 000.",
        ],
        "points": 9.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.schriftlich.addition",
            "mathe.klasse4.schriftlich.subtraktion",
        ],
    },
    {
        "n": 6,
        "type": "Zahlenfolgen fortsetzen",
        "text": (
            "Setze die Zahlenfolgen fort!\n"
            "• 43 660, 53 760, 63 860, ___, ___, ___, ___, ___\n"
            "• 15 740, 15 630, 15 520, ___, ___, ___, ___, ___"
        ),
        "answer": (
            "Schritt +10 100: 73 960, 84 060, 94 160, 104 260, 114 360 ; "
            "Schritt −110: 15 410, 15 300, 15 190, 15 080, 14 970"
        ),
        "steps": [
            "1. Folge: jede Zahl + 10 100.",
            "2. Folge: jede Zahl − 110.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.zahlen1000000.zahlenfolgen",
        ],
    },
    {
        "n": 7,
        "type": "Größte und kleinste Zahl bilden",
        "text": (
            "Bilde aus den Ziffern 1, 3, 4, 5, 8 die größte und die kleinste "
            "5-stellige Zahl!\n"
            "kleinste Zahl: ___    größte Zahl: ___"
        ),
        "answer": "kleinste: 13 458 ; größte: 85 431",
        "steps": [
            "Kleinste: Ziffern aufsteigend → 1, 3, 4, 5, 8 → 13 458.",
            "Größte: Ziffern absteigend → 8, 5, 4, 3, 1 → 85 431.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.zahlen1000000.stellenwerte",
        ],
    },
    {
        "n": 8,
        "type": "Runden auf verschiedene Stellen",
        "text": (
            "Runde die Zahlen!\n"
            "Zahl   | ZT     | T      | H      | Z\n"
            "24 446 | ___    | ___    | ___    | ___\n"
            "86 521 | ___    | ___    | ___    | ___"
        ),
        "answer": (
            "24 446: ZT=20 000, T=24 000, H=24 400, Z=24 450 ; "
            "86 521: ZT=90 000, T=87 000, H=86 500, Z=86 520"
        ),
        "steps": [
            "24 446 → ZT (4<5)=20 000, T (4<5)=24 000, H (4<5)=24 400, Z (6≥5)=24 450.",
            "86 521 → ZT (6≥5)=90 000, T (5≥5)=87 000, H (2<5)=86 500, Z (1<5)=86 520.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.zahlen1000000.runden",
        ],
    },
    {
        "n": 9,
        "type": "Multiplikation und Division mit Vielfachen",
        "text": (
            "Berechne:\n"
            "60 · 30 = ___    60 · 400 = ___    7 · 6 000 = ___\n"
            "70 · 20 = ___    40 000 : 80 = ___    9 · 5 000 = ___\n"
            "80 · 40 = ___    63 000 : 7 000 = ___    4 · 7 000 = ___"
        ),
        "answer": (
            "1 800 ; 24 000 ; 42 000 ; "
            "1 400 ; 500 ; 45 000 ; "
            "3 200 ; 9 ; 28 000"
        ),
        "steps": [
            "60·30=1800 ; 60·400=24 000 ; 7·6000=42 000.",
            "70·20=1400 ; 40 000:80=500 ; 9·5000=45 000.",
            "80·40=3200 ; 63 000:7000=9 ; 4·7000=28 000.",
        ],
        "points": 4.5,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.schriftlich.multiplikation",
            "mathe.klasse4.schriftlich.division",
        ],
    },
    {
        "n": 10,
        "type": "Teilbarkeitsregeln",
        "text": (
            "Teilbarkeitsregeln: Durch welche Zahlen sind diese Zahlen teilbar? "
            "Kreuze an (2, 3, 4, 5, 9)!\n"
            "56 528 ; 34 952 ; 70 035"
        ),
        "answer": (
            "56 528: durch 2 und 4 ; "
            "34 952: durch 2 und 4 ; "
            "70 035: durch 3 und 5 (Quersumme 15, endet auf 5)"
        ),
        "steps": [
            "56 528: gerade ✓ (2), letzte 2 Ziffern '28' durch 4 ✓ (4); QS=26, nicht durch 3, 9; nicht durch 5.",
            "34 952: gerade ✓ (2), '52' durch 4 ✓ (4); QS=23, nicht durch 3, 9; nicht durch 5.",
            "70 035: nicht gerade; QS=15 → durch 3 ✓; endet auf 5 → durch 5 ✓; nicht durch 9 (15÷9).",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.zahlen1000000.teiler",
        ],
    },
    {
        "n": 11,
        "type": "Sachaufgabe (Dreisatz)",
        "text": (
            "Der Tierpark in Nürnberg braucht für seine 9 Elefanten jeden Tag "
            "27 Brote. Der Tierpark in München hat 3 Elefanten. "
            "Wie viele Brote braucht der Tierpark in München?"
        ),
        "answer": "Der Tierpark München braucht 9 Brote pro Tag.",
        "steps": [
            "1 Elefant: 27 : 9 = 3 Brote.",
            "3 Elefanten: 3 · 3 = 9 Brote.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
        ],
    },
    {
        "n": 12,
        "type": "Knobelaufgabe (Beine zählen)",
        "text": (
            "Im Tierpark laufen Flamingos und Elche in einem gemeinsamen Gehege. "
            "Ein Besucher namens Florian zählt 64 Beine. Florian sagt, er sieht "
            "7 Elche mehr als Flamingos. Wie viele Flamingos und Elche sind "
            "im Gehege?"
        ),
        "answer": "6 Flamingos und 13 Elche.",
        "steps": [
            "Elch hat 4 Beine, Flamingo hat 2 Beine; insgesamt 64 Beine.",
            "7 Elche mehr als Flamingos → diese 7 Elche bringen 7·4 = 28 Beine.",
            "Übrig: 64 − 28 = 36 Beine, verteilt auf gleich viele Elch-Flamingo-Paare (1 Paar = 6 Beine).",
            "Anzahl Paare: 36 : 6 = 6 → 6 Flamingos, 6 Elche-Paar + 7 Extra-Elche = 13 Elche.",
        ],
        "points": 3.5,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.zahlenraetsel",
        ],
    },
    {
        "n": 13,
        "type": "Sachaufgabe (Verhältnis)",
        "text": (
            "Im Tierpark schert Schäfer Heinrich 72 Schafe in 28 Stunden. "
            "Bei Bauer Sippel schert er nur 36 Schafe, weil die Schere stumpf "
            "ist. Wie lange braucht er bei Bauer Sippel?"
        ),
        "answer": "Er braucht 14 Stunden.",
        "steps": [
            "36 Schafe sind die Hälfte von 72 Schafen.",
            "→ Halbe Zeit: 28 : 2 = 14 Stunden.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
        ],
    },
    {
        "n": 14,
        "type": "Sachaufgabe (Bewegung aufeinander zu)",
        "text": (
            "Schildkröten Luis und Emma sind 3,6 Meter voneinander entfernt und "
            "bewegen sich aufeinander zu. Luis legt in 4 Minuten 16 cm zurück, "
            "Emma in 8 Minuten 4 cm. Wie lange brauchen sie, bis sie sich "
            "treffen?"
        ),
        "answer": "Sie brauchen 80 Minuten.",
        "steps": [
            "Strecke: 3,6 m = 360 cm.",
            "Luis: 16 cm in 4 min → 4 cm pro Minute.",
            "Emma: 4 cm in 8 min → 0,5 cm pro Minute.",
            "Gemeinsam pro Minute: 4 + 0,5 = 4,5 cm.",
            "Zeit: 360 : 4,5 = 80 Minuten.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.groessen.laenge",
            "mathe.klasse4.groessen.zeit",
        ],
    },
]

NEW_KNOWLEDGE = []
