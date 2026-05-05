EXERCISE = {
    "id": "0431",
    "subject": "Mathe",
    "grade": 4,
    "title": "2. Lernzielkontrolle",
    "topic": "Zahlenraum bis 10000",
    "publisher": "CATLUX",
    "source_pdf": "0431.pdf",
    "answer_pdf": "0431 (1).pdf",
    "total_points": 63.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Zahlenstrahl",
        "text": (
            "Lies die Zahlen vom Zahlenstrahl ab! Trage ein!\n\n"
            "Zahlenstrahl 1 (7600–8300):\n"
            "A: ___ B: ___ C: ___ D: ___\n\n"
            "Zahlenstrahl 2 (5700–6000):\n"
            "E: ___ F: ___ G: ___ H: ___\n\n"
            "Zahlenstrahl 3 (9680–9710):\n"
            "J: ___ K: ___ L: ___ M: ___"
        ),
        "answer": (
            "A: 7650   B: 7860   C: 8080   D: 8240\n"
            "E: 5760   F: 5800   G: 5880   H: 5950\n"
            "J: 9681   K: 9690   L: 9695   M: 9708"
        ),
        "steps": [
            "Zahlenstrahl 1: Abschnitt 7600–8300 (700 Einheiten), Pfeile ablesen",
            "Zahlenstrahl 2: Abschnitt 5700–6000 (300 Einheiten), Pfeile ablesen",
            "Zahlenstrahl 3: Abschnitt 9680–9710 (30 Einheiten), Pfeile ablesen",
        ],
        "points": 6.0,
        "has_image": True,
        "image": "0431_q1_xref24_596x73.png",
        "knowledge": [
            "mathe.klasse4.zahlen1000000.zahlenstrahl",
        ],
    },
    {
        "n": 2,
        "type": "Tabelle",
        "text": (
            "Schreibe die Nachbarzahlen auf!\n\n"
            "Fülle die Tabelle aus (Nachbar-Tausender, Nachbar-Hunderter, Nachbar-Zehner, "
            "Vorgänger, Zahl, Nachfolger, Nachbar-Zehner, Nachbar-Hunderter, Nachbar-Tausender):\n"
            "Zeile 1: Zahl = 7898\n"
            "Zeile 2: Nachbar-Zehner links = 3580"
        ),
        "answer": (
            "7898: Nachbar-Tausender: 7000 | 8000, Nachbar-Hunderter: 7800 | 7900, "
            "Nachbar-Zehner: 7890 | 7900, Vorgänger: 7897, Nachfolger: 7899\n"
            "3580: Nachbar-Tausender: 3000 | 4000, Nachbar-Hunderter: 3500 | 3600, "
            "Nachbar-Zehner: 3580 | 3590, Vorgänger: 3581, Nachfolger: 3583\n\n"
            "Vollständige Tabellenzeilen:\n"
            "7000 | 7800 | 7890 | 7897 | 7898 | 7899 | 7900 | 7900 | 8000\n"
            "3000 | 3500 | 3580 | 3581 | 3582 | 3583 | 3590 | 3600 | 4000"
        ),
        "steps": [
            "Nachbar-Tausender: nächste kleinere und größere durch 1000 teilbare Zahl",
            "Nachbar-Hunderter: nächste kleinere und größere durch 100 teilbare Zahl",
            "Nachbar-Zehner: nächste kleinere und größere durch 10 teilbare Zahl",
            "Vorgänger = Zahl – 1, Nachfolger = Zahl + 1",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.zahlen1000000.vorgaenger_nachfolger",
            "mathe.klasse4.zahlen1000000.stellenwerte",
        ],
    },
    {
        "n": 3,
        "type": "Lückentext",
        "text": (
            "Finde die Nachbarzahlen!\n\n"
            "Zehnernachbarn:    ___ < 4123 < ___\n"
            "Hunderternachbarn: ___ < 3567 < ___\n"
            "Tausendernachbarn: ___ < 9435 < ___"
        ),
        "answer": (
            "Zehnernachbarn:    4120 < 4123 < 4130\n"
            "Hunderternachbarn: 3500 < 3567 < 3600\n"
            "Tausendernachbarn: 9000 < 9435 < 10000"
        ),
        "steps": [
            "Zehnernachbarn von 4123: abrunden auf 4120, aufrunden auf 4130",
            "Hunderternachbarn von 3567: abrunden auf 3500, aufrunden auf 3600",
            "Tausendernachbarn von 9435: abrunden auf 9000, aufrunden auf 10000",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.zahlen1000000.runden",
            "mathe.klasse4.zahlen1000000.vorgaenger_nachfolger",
        ],
    },
    {
        "n": 4,
        "type": "Vergleichen",
        "text": (
            "Setze ein: <, >, =\n\n"
            "5960 ○ 5T 9H 6Z\n"
            "3085 ○ 3055 + 300\n"
            "7527 – 300 ○ 7527 – 50\n"
            "8T 7H 8E ○ 8T 8Z 7E"
        ),
        "answer": (
            "5960 = 5T 9H 6Z\n"
            "3085 < 3055 + 300\n"
            "7527 – 300 < 7527 – 50\n"
            "8T 7H 8E > 8T 8Z 7E"
        ),
        "steps": [
            "5T 9H 6Z = 5000 + 900 + 60 = 5960 → =",
            "3055 + 300 = 3355 > 3085 → <",
            "7527 – 300 = 7227; 7527 – 50 = 7477 → 7227 < 7477",
            "8T 7H 8E = 8708; 8T 8Z 7E = 8087 → 8708 > 8087",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.zahlen1000000.vergleichen",
            "mathe.klasse4.zahlen1000000.stellenwerte",
        ],
    },
    {
        "n": 5,
        "type": "Zahlenfolgen",
        "text": (
            "Schreibe die fehlenden Zahlen in die Reihen!\n\n"
            "8840, 8480, 8120, ___\n"
            "___, 3734, 3781, ___\n"
            "3717, 3711, 3705, ___, ___, 3687"
        ),
        "answer": (
            "8840, 8480, 8120, 7760  (–360)\n"
            "3687, 3734, 3781, 3828  (+47)\n"
            "3717, 3711, 3705, 3699, 3693, 3687  (–6)"
        ),
        "steps": [
            "Reihe 1: Differenz 8840 – 8480 = 360; nächste Zahl: 8120 – 360 = 7760",
            "Reihe 2: Differenz 3781 – 3734 = 47; fehlende Zahl vorne: 3734 – 47 = 3687; hinten: 3781 + 47 = 3828",
            "Reihe 3: Differenz 3717 – 3711 = 6; fehlende Zahlen: 3705 – 6 = 3699, 3699 – 6 = 3693",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.zahlen1000000.zahlenfolgen",
        ],
    },
    {
        "n": 6,
        "type": "Tabelle",
        "text": (
            "Zehntausendertafel. Schreibe die Zahlen der Sterne auf!\n\n"
            "Die Tafel hat die Achsen 100–1000 (waagerecht) und Tausenderwerte (senkrecht).\n"
            "*A befindet sich in Zeile 2, Spalte 3\n"
            "*B befindet sich in Zeile 5100, Spalte Mitte (zwischen 5100 und 6000)\n"
            "*C befindet sich in Zeile 7900, Spalte 9 (nahe 1000)\n"
            "*D befindet sich in Zeile 8200, Spalte 2\n\n"
            "*A = ___   *B = ___   *C = ___   *D = ___"
        ),
        "answer": "*A = 1300   *B = 5600   *C = 7900   *D = 8200",
        "steps": [
            "Zehntausendertafel: waagerechte Achse = Hunderterwerte (100–1000), senkrechte Achse = Tausenderwerte",
            "Position ablesen: Zeilenwert (Tausender) + Spaltenwert (Hunderter)",
            "*A: Zeile 1000, Spalte 300 → 1300",
            "*B: Zeile 5000, Spalte 600 → 5600",
            "*C: Zeile 7000, Spalte 900 → 7900",
            "*D: Zeile 8000, Spalte 200 → 8200",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.zahlen1000000.stellenwerte",
        ],
    },
    {
        "n": 7,
        "type": "Rechnen",
        "text": (
            "Rechne aus!\n"
            "60 • 9 = ___\n"
            "4 • 210 = ___\n"
            "80 • 20 = ___\n"
            "80 • ___ = 7200\n"
            "___ • 80 = 7200\n"
            "3600 : 6 = ___\n"
            "1800 : 90 = ___\n"
            "4500 : 500 = ___"
        ),
        "answer": (
            "60 • 9 = 540\n"
            "4 • 210 = 840\n"
            "80 • 20 = 1600\n"
            "80 • 90 = 7200\n"
            "90 • 80 = 7200\n"
            "3600 : 6 = 600\n"
            "1800 : 90 = 20\n"
            "4500 : 500 = 9"
        ),
        "steps": [
            "Multiplikation mit Zehnern: Kernergebnis • Zehner-Nullen anhängen",
            "Lücken füllen: 7200 : 80 = 90",
            "Division mit Zehnern: Nullen kürzen",
        ],
        "points": 8.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.schriftlich.multiplikation",
            "mathe.klasse4.schriftlich.division",
        ],
    },
    {
        "n": 8,
        "type": "Zahlenrätsel",
        "text": (
            "Zahlenrätsel\n\n"
            "Rätsel 1: Meine Zahl liegt zwischen 3200 und 4200. "
            "Sie hat doppelt so viele Hunderter wie Tausender. Wie heißt die Zahl?\n\n"
            "Rätsel 2: Ich denke mir eine Zahl. Sie ist größer als 8000 und sie hat einen "
            "Hunderter weniger als Tausender und einen Zehner weniger als Hunderter. "
            "Welche Zahl denke ich mir? Schreibe drei mögliche Zahlen!"
        ),
        "answer": (
            "Rätsel 1: 3600\n"
            "Rätsel 2: z. B. 9870, 8760, 9876"
        ),
        "steps": [
            "Rätsel 1: Tausender = 3, doppelt so viele Hunderter = 6 → 3600 (liegt zwischen 3200 und 4200)",
            "Rätsel 2: Tausender = T, Hunderter = T–1, Zehner = T–2; z. B. T=9: 9870; T=8: 8760; gemischt: 9876",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.zahlenraetsel",
            "mathe.klasse4.zahlen1000000.stellenwerte",
        ],
    },
    {
        "n": 9,
        "type": "Rechnen",
        "text": (
            "a) Berechne die Quersumme der Zahlen!\n"
            "194 > ___   830 > ___   357 > ___\n\n"
            "b) Schreibe drei Zahlen auf mit der Quersumme:\n"
            "8 < ___________________________"
        ),
        "answer": (
            "a) 194 > 14   830 > 11   357 > 15\n"
            "b) z. B. 53; 152; 31121"
        ),
        "steps": [
            "Quersumme: alle Ziffern einer Zahl addieren",
            "194: 1 + 9 + 4 = 14",
            "830: 8 + 3 + 0 = 11",
            "357: 3 + 5 + 7 = 15",
            "Zahlen mit Quersumme 8: z. B. 53 (5+3=8), 152 (1+5+2=8), 31121 (3+1+1+2+1=8)",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.zahlen1000000.stellenwerte",
        ],
    },
    {
        "n": 10,
        "type": "Sachaufgabe",
        "text": (
            "Florian ist ein fleißiger Zeichner. Ein Stapel mit 600 Blatt Zeichenpapier ist 6 cm hoch. "
            "Wie hoch ist ein Stapel von 10 000 Blatt?"
        ),
        "answer": "100 cm = 1 m",
        "steps": [
            "600 Blatt = 6 cm → 1 Blatt = 6 cm : 600 = 0,01 cm",
            "10 000 Blatt = 10 000 • 0,01 cm = 100 cm = 1 m",
            "Alternativ: 10 000 : 600 • 6 cm = 100 cm",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.schriftlich.division",
        ],
    },
    {
        "n": 11,
        "type": "Sachaufgabe",
        "text": (
            "In der Glasfabrik werden pro Stunde 10 000 Gläser hergestellt. "
            "Der fünfte Teil davon sind Sektgläser. Der Rest besteht zur Hälfte aus Biergläsern und Weingläsern. "
            "Zeichne ein passendes Streifenbild. Frage, rechne und antworte!"
        ),
        "answer": (
            "F: Wie viel Sekt-, Wein- und Biergläser sind es jeweils?\n"
            "Sektgläser: 10 000 : 5 = 2000\n"
            "Rest: 10 000 – 2000 = 8000\n"
            "Biergläser = Weingläser: 8000 : 2 = 4000\n"
            "A: Es sind 2000 Sektgläser und je 4000 Bier- und Weingläser."
        ),
        "steps": [
            "Sektgläser: 1/5 von 10 000 = 2000",
            "Restliche Gläser: 10 000 – 2000 = 8000",
            "Biergläser und Weingläser je zur Hälfte: 8000 : 2 = 4000",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.brueche.gemischt",
        ],
    },
    {
        "n": 12,
        "type": "Sachaufgabe",
        "text": (
            "Um wie viel ist der Unterschied zwischen 5378 und 8413 größer als die "
            "kleinstmögliche vierstellige Zahl, in der die Ziffer 9 zweimal vorkommt?\n"
            "A: ___"
        ),
        "answer": "A: Der Unterschied ist um 1936 größer.",
        "steps": [
            "Unterschied: 8413 – 5378 = 3035",
            "Kleinstmögliche vierstellige Zahl mit 9 zweimal: 1099",
            "3035 – 1099 = 1936",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.zahlenraetsel",
            "mathe.klasse4.schriftlich.subtraktion",
        ],
    },
    {
        "n": 13,
        "type": "Rechnen",
        "text": (
            "Rechne schriftlich! Wandle zuerst um!\n"
            "2,08 t + 4965 kg + 0,009 t + 70 kg ="
        ),
        "answer": "7124 kg",
        "steps": [
            "2,08 t = 2080 kg",
            "0,009 t = 9 kg",
            "2080 kg + 4965 kg + 9 kg + 70 kg = 7124 kg",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.schriftlich.addition",
            "mathe.klasse4.dezimalzahlen.rechnen",
        ],
    },
    {
        "n": 14,
        "type": "Sachaufgabe",
        "text": (
            'Der Gebrauchtwagenhändler "Schrotti" verkauft in seiner Aktionswoche "Ungerade Preise". '
            "Einen Ford für 6432 €, einen alten Golf für 2471 € und 8 Winterreifen zu je 90 €. "
            "Am selben Tag kauft er für sein Büro neue Computer für 4780 € und neue Möbel für 3478 €. "
            "Muss der Händler noch zusätzlich Geld von seinem Konto abheben?"
        ),
        "answer": (
            "Nein, er muss kein Geld abheben, da er mehr einnimmt als ausgibt.\n"
            "Einnahmen: 6432 € + 2471 € + 720 € = 9623 €\n"
            "Ausgaben: 4780 € + 3478 € = 8258 €"
        ),
        "steps": [
            "Einnahmen: 8 • 90 € = 720 €; 6432 € + 2471 € + 720 € = 9623 €",
            "Ausgaben: 4780 € + 3478 € = 8258 €",
            "Vergleich: 9623 € > 8258 € → kein Geld abheben nötig",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.schriftlich.addition",
            "mathe.klasse4.schriftlich.multiplikation",
        ],
    },
]

NEW_KNOWLEDGE = []
