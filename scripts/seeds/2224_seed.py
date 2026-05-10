EXERCISE = {
    "id": "2224",
    "subject": "Mathe",
    "grade": 4,
    "title": "Kurzprobe: Hohlmaße und Gewichtsmaße",
    "topic": "Hohlmaße (l, ml, hl), Gewichtsmaße (g, kg, t), Dezimalzahlen, Brüche",
    "publisher": "CATLUX",
    "source_pdf": "2224.pdf",
    "answer_pdf": "2224 (1).pdf",
    "total_points": 41.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Größen ordnen",
        "text": (
            "Ordne nach der Größe.\n"
            "340 ml ; ¾ l ; 3,4 l ; 1 l ; 30 ml ; 43 ml ; 0,3 l\n"
            "______ < ______ < ______ < ______ < ______ < ______ < ______"
        ),
        "answer": "30 ml < 43 ml < 0,3 l (300 ml) < 340 ml < ¾ l (750 ml) < 1 l (1000 ml) < 3,4 l (3400 ml)",
        "steps": [
            "Alle Werte in ml umrechnen:",
            "  ¾ l = 750 ml ;  3,4 l = 3400 ml ;  1 l = 1000 ml ;  0,3 l = 300 ml",
            "Sortiert: 30 < 43 < 300 < 340 < 750 < 1000 < 3400 (in ml)",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.groessen.volumen",
            "mathe.klasse4.dezimalzahlen.grundlagen",
            "mathe.klasse4.brueche.vergleichen",
        ],
    },
    {
        "n": 2,
        "type": "Einheiten umwandeln (Liter → Milliliter)",
        "text": (
            "Wandle in Milliliter um!\n"
            "6 l = ____ ml\n"
            "1,3 l = ____ ml\n"
            "0,7 l = ____ ml\n"
            "0,02 l = ____ ml\n"
            "¼ l = ____ ml\n"
            "⅛ l = ____ ml\n"
            "¾ l = ____ ml\n"
            "½ l = ____ ml"
        ),
        "answer": "6000 ml ; 1300 ml ; 700 ml ; 20 ml ; 250 ml ; 125 ml ; 750 ml ; 500 ml",
        "steps": [
            "1 l = 1000 ml.",
            "6 l = 6000 ml ;  1,3 l = 1300 ml ;  0,7 l = 700 ml ;  0,02 l = 20 ml",
            "¼ l = 1000:4 = 250 ml ;  ⅛ l = 1000:8 = 125 ml ;  ¾ l = 750 ml ;  ½ l = 500 ml",
        ],
        "points": 8.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.groessen.volumen",
            "mathe.klasse4.brueche",
            "mathe.klasse4.dezimalzahlen.rechnen",
        ],
    },
    {
        "n": 3,
        "type": "Einheiten umwandeln (ml → l als Kommazahl)",
        "text": (
            "Wandle in Liter um und schreibe als Kommazahl!\n"
            "1400 ml = ____\n"
            "250 ml = ____\n"
            "2050 ml = ____\n"
            "125 ml = ____\n"
            "50 ml = ____\n"
            "25 ml = ____"
        ),
        "answer": "1,4 l ; 0,25 l ; 2,05 l ; 0,125 l ; 0,05 l ; 0,025 l",
        "steps": [
            "ml : 1000 = l (Komma um drei Stellen nach links).",
            "1400 → 1,4 ;  250 → 0,25 ;  2050 → 2,05 ;  125 → 0,125 ;  50 → 0,05 ;  25 → 0,025",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.groessen.volumen",
            "mathe.klasse4.dezimalzahlen.grundlagen",
        ],
    },
    {
        "n": 4,
        "type": "Ergänzen auf 1 Liter",
        "text": (
            "Wie viel fehlt zu einem Liter?\n"
            "0,6 l + ____\n"
            "¼ l + 60 ml + ____\n"
            "½ l + ____\n"
            "0,75 l + 125 ml + ____"
        ),
        "answer": "400 ml ; 690 ml ; 500 ml ; 125 ml",
        "steps": [
            "1 l = 1000 ml.",
            "1000 − 600 = 400 ml",
            "1000 − (250 + 60) = 1000 − 310 = 690 ml",
            "1000 − 500 = 500 ml",
            "1000 − (750 + 125) = 1000 − 875 = 125 ml",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.groessen.volumen",
            "mathe.klasse4.dezimalzahlen.rechnen",
        ],
    },
    {
        "n": 5,
        "type": "Sachaufgabe (Hohlmaße)",
        "text": (
            "Eine Regentonne fasst 5 hl Wasser. "
            "Wie oft muss man mit einem 10-l-Eimer schöpfen, bis die Tonne leer ist?"
        ),
        "answer": "Man muss 50-mal schöpfen.",
        "steps": [
            "5 hl = 500 l.",
            "500 l : 10 l = 50.",
            "A: Man muss 50-mal schöpfen.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.groessen.volumen",
            "mathe.klasse4.sachaufgaben.mehrstufig",
        ],
    },
    {
        "n": 6,
        "type": "Visuelle Zuordnung (Bildaufgabe)",
        "text": (
            "In eine Milchkanne passt immer genau ein Liter. Immer zwei Tropfen ergeben "
            "einen Liter. Male sie in der gleichen Farbe an!\n"
            "[Aufgabe mit Tropfen-Abbildungen — siehe Original-PDF]"
        ),
        "answer": "Visuelle Zuordnungsaufgabe — Tropfenpaare, deren Summe 1 Liter ergibt, gleich einfärben.",
        "steps": [
            "Werte addieren: jeweils zwei Tropfen, deren Summe genau 1 Liter (1000 ml) ergibt, bilden ein Paar.",
        ],
        "points": 2.0,
        "has_image": True,
        "image": None,
        "knowledge": [
            "mathe.klasse4.groessen.volumen",
            "mathe.klasse4.brueche.addieren",
        ],
    },
    {
        "n": 7,
        "type": "Ergänzen auf 8 Liter",
        "text": (
            "Ergänze auf 8 Liter:\n"
            "15 ml + ____ = 8 l\n"
            "5 371 ml + ____ = 8 l\n"
            "3 499 ml + ____ = 8 l\n"
            "7 101 ml + ____ = 8 l"
        ),
        "answer": "7 985 ml ; 2 629 ml ; 4 501 ml ; 899 ml",
        "steps": [
            "8 l = 8000 ml.",
            "8000 − 15 = 7985",
            "8000 − 5371 = 2629",
            "8000 − 3499 = 4501",
            "8000 − 7101 = 899",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.groessen.volumen",
            "mathe.klasse4.schriftlich.subtraktion",
        ],
    },
    {
        "n": 8,
        "type": "Vergleichen (Hohlmaße, mit Brüchen)",
        "text": (
            "Setze ein: <, > oder =\n"
            "3 400 ml ___ 7 · ½ l\n"
            "¼ l + 500 ml ___ 725 ml\n"
            "1 ¼ l ___ 1 125 ml\n"
            "3 l + 125 ml + ½ l ___ 3 000 ml + ¾ l"
        ),
        "answer": "3 400 ml < 3 500 ml ;  750 ml > 725 ml ;  1 250 ml > 1 125 ml ;  3 625 ml < 3 750 ml",
        "steps": [
            "7 · ½ l = 3,5 l = 3500 ml → 3400 < 3500.",
            "¼ l + 500 ml = 250 + 500 = 750 ml → 750 > 725.",
            "1 ¼ l = 1250 ml → 1250 > 1125.",
            "3 l + 125 ml + ½ l = 3000 + 125 + 500 = 3625 ml ;  3000 ml + ¾ l = 3000 + 750 = 3750 ml → 3625 < 3750.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.groessen.volumen",
            "mathe.klasse4.brueche.vergleichen",
            "mathe.klasse4.dezimalzahlen.rechnen",
        ],
    },
    {
        "n": 9,
        "type": "Aufteilen (Sachaufgabe)",
        "text": (
            "Wie viel Milch bekommt jeder? Schreibe in ml. Verteile 1 Liter Milch gerecht auf:\n"
            "8 Tassen: ____   2 Babyfläschchen: ____\n"
            "4 Katzennäpfe: ____   1 Kochtopf: ____"
        ),
        "answer": "8 Tassen → 125 ml ; 2 Babyfläschchen → 500 ml ; 4 Katzennäpfe → 250 ml ; 1 Kochtopf → 1000 ml",
        "steps": [
            "1 l = 1000 ml.",
            "1000 : 8 = 125 ;  1000 : 2 = 500 ;  1000 : 4 = 250 ;  1000 : 1 = 1000.",
        ],
        "points": 0.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.groessen.volumen",
            "mathe.klasse4.sachaufgaben.mehrstufig",
        ],
    },
    {
        "n": 10,
        "type": "Gewichtsangaben (Tabelle)",
        "text": (
            "Trage die fehlenden Gewichtsangaben ein. Die Tabelle hat drei Zeilen "
            "(in kg, in t und kg, in t als Kommazahl) und sechs Spalten:\n"
            "Spalte 1: 5040 kg | 5 t 40 kg | ____ t\n"
            "Spalte 2: ____ kg | 3 t 2 kg | ____ t\n"
            "Spalte 3: ____ kg | ____ | 0,750 t\n"
            "Spalte 4: 1010 kg | ____ | ____\n"
            "Spalte 5: ____ kg | 2 t | ____\n"
            "Spalte 6: ____ kg | ____ | 4,020 t"
        ),
        "answer": (
            "5040 kg = 5 t 40 kg = 5,04 t ; "
            "3002 kg = 3 t 2 kg = 3,002 t ; "
            "750 kg = 0 t 750 kg = 0,750 t ; "
            "1010 kg = 1 t 10 kg = 1,01 t ; "
            "2000 kg = 2 t = 2,000 t ; "
            "4020 kg = 4 t 20 kg = 4,020 t"
        ),
        "steps": [
            "1 t = 1000 kg.",
            "Umrechnung jeweils zwischen kg, t+kg-Schreibweise und t als Kommazahl.",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.groessen.gewicht",
            "mathe.klasse4.dezimalzahlen.grundlagen",
        ],
    },
    {
        "n": 11,
        "type": "Vergleichen (Gewichte)",
        "text": (
            "<, > oder =?\n"
            "30 g ___ 0,3 kg\n"
            "5,2 t ___ 5 t 2 kg\n"
            "8 700 g ___ 8,7 kg\n"
            "4 t 38 kg ___ 438 kg"
        ),
        "answer": "30 g < 0,3 kg ; 5,2 t > 5 t 2 kg ; 8 700 g = 8,7 kg ; 4 t 38 kg > 438 kg",
        "steps": [
            "0,3 kg = 300 g → 30 < 300.",
            "5,2 t = 5200 kg ;  5 t 2 kg = 5002 kg → 5200 > 5002.",
            "8700 g = 8,7 kg.",
            "4 t 38 kg = 4038 kg → 4038 > 438.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.groessen.gewicht",
            "mathe.klasse4.dezimalzahlen.grundlagen",
        ],
    },
    {
        "n": 12,
        "type": "Sachaufgabe (mehrstufig, Bowle)",
        "text": (
            "Familie Schmitz kauft für eine Party ein. Die Saftbowle besteht aus Ananassaft, "
            "Orangensaft, Apfelsaft und Mineralwasser. Es werden 3 Liter Orangensaft benötigt, "
            "halb so viel Ananassaft und 2 l Apfelsaft. Dazu kommen 2 Flaschen Mineralwasser "
            "mit je ¾ Liter.\n"
            "a) Wie viel Bowle wird zubereitet?\n"
            "b) In ein Glas passen ¼ Liter. Wie viele Gläser können befüllt werden?"
        ),
        "answer": "a) Es werden 8 Liter Bowle zubereitet. b) Es können 32 Gläser befüllt werden.",
        "steps": [
            "Orangensaft: 3,00 l ;  Ananassaft: 1,50 l (halb so viel wie Orange) ;  Apfelsaft: 2,00 l ;  Mineralwasser: 2 · 0,75 l = 1,50 l.",
            "Summe: 3,00 + 1,50 + 2,00 + 1,50 = 8,00 l.",
            "Glasgröße ¼ l = 250 ml = 0,25 l.",
            "8000 ml : 250 ml = 32 Gläser.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.groessen.volumen",
            "mathe.klasse4.brueche.addieren",
            "mathe.klasse4.dezimalzahlen.rechnen",
        ],
    },
]

NEW_KNOWLEDGE = []
