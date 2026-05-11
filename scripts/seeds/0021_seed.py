EXERCISE = {
    "id": "0021",
    "subject": "Mathe",
    "grade": 4,
    "title": "Lernzielkontrolle: Zahlenraum bis 10 000",
    "topic": "schriftliche Addition, Subtraktion, Multiplikation, halbschriftl. Division, Sachaufgaben",
    "publisher": "CATLUX",
    "source_pdf": "0021.pdf",
    "answer_pdf": "0021 (1).pdf",
    "total_points": 41.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Vorgänger und Nachfolger",
        "text": (
            "Trage die Nachbarzahlen ein!\n"
            "Vorgänger | Zahl | Nachfolger\n"
            "_____ | 3100 | _____\n"
            "_____ | 7779 | _____\n"
            "_____ | 4000 | _____"
        ),
        "answer": "3099 | 3100 | 3101 ;  7778 | 7779 | 7780 ;  3999 | 4000 | 4001",
        "steps": [
            "Vorgänger = Zahl − 1, Nachfolger = Zahl + 1",
            "3100 → 3099 / 3101",
            "7779 → 7778 / 7780",
            "4000 → 3999 / 4001",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.zahlen1000000.vorgaenger_nachfolger"],
    },
    {
        "n": 2,
        "type": "Zahlen vergleichen",
        "text": (
            "Setze ein! >, < oder =\n"
            "1305 ___ 1350\n"
            "4149 ___ 4419\n"
            "9998 ___ 9989\n"
            "2438 ___ 2438"
        ),
        "answer": "1305 < 1350 ; 4149 < 4419 ; 9998 > 9989 ; 2438 = 2438",
        "steps": [
            "Stellenwerte vergleichen, beginnend bei der höchsten Stelle.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.zahlen1000000.vergleichen"],
    },
    {
        "n": 3,
        "type": "Zahlenfolgen fortsetzen",
        "text": (
            "Setze die Zahlenfolgen fort!\n"
            "3750  3810  3870  3930  ____  ____  ____\n"
            "8690  8660  8620  8570  ____  ____  ____"
        ),
        "answer": "3990, 4050, 4110 ;  8510, 8440, 8360",
        "steps": [
            "Erste Folge: +60 (3750→3810), aber Differenzen sind 60, 60, 60 — gleichbleibend +60. → 3990, 4050, 4110.",
            "Zweite Folge: Differenzen −30, −40, −50 — wachsen um 10. → 8570−60=8510, 8510−70=8440, 8440−80=8360.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.zahlen1000000.zahlenfolgen"],
    },
    {
        "n": 4,
        "type": "Schriftliches Rechnen",
        "text": (
            "Rechne schriftlich!\n"
            "  2498 + 3098 = ?\n"
            "  4065 + 5783 = ?\n"
            "  8764 − 5578 = ?\n"
            "  6908 − 5086 = ?"
        ),
        "answer": "5596 ; 9848 ; 3186 ; 1822",
        "steps": [
            "2498 + 3098 = 5596",
            "4065 + 5783 = 9848",
            "8764 − 5578 = 3186",
            "6908 − 5086 = 1822",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.schriftlich.addition",
            "mathe.klasse4.schriftlich.subtraktion",
        ],
    },
    {
        "n": 5,
        "type": "Sachaufgabe (Subtraktion)",
        "text": (
            "Familie Schmidt fährt mit ihrem neuen Auto in den Urlaub. "
            "Vor der Abfahrt zeigt der Tachometerstand 4769 km. Als sie wieder zu Hause sind, "
            "zeigt der Tachometerstand 6045 km.\n"
            "Wie viel Kilometer ist Familie Schmidt gefahren?"
        ),
        "answer": "Sie sind 1276 km gefahren.",
        "steps": [
            "F: Wie viele Kilometer wurden gefahren?",
            "R: 6045 km − 4769 km = 1276 km",
            "A: Sie sind 1276 km gefahren.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.schriftlich.subtraktion",
        ],
    },
    {
        "n": 6,
        "type": "Halbschriftliche Division",
        "text": (
            "Rechne halbschriftlich!\n"
            "  246 : 3 = ?\n"
            "  765 : 8 = ?"
        ),
        "answer": "246 : 3 = 82 ;  765 : 8 = 95 R 5",
        "steps": [
            "246 : 3 → 210:3=70, 30:3=10, 6:3=2 → 70+10+2 = 82",
            "765 : 8 → 720:8=90, 45:8=5 R 5 → 90+5 = 95, Rest 5",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.schriftlich.division_halbschriftlich"],
    },
    {
        "n": 7,
        "type": "Schriftliche Multiplikation",
        "text": (
            "Multipliziere schriftlich. Vergiss den Überschlag nicht!\n"
            "  467 · 5 = ?     Ü: ____\n"
            "  273 · 22 = ?    Ü: ____"
        ),
        "answer": "467 · 5 = 2335 (Ü: 500·5 = 2500) ;  273 · 22 = 6006 (Ü: 300·20 = 6000)",
        "steps": [
            "Überschlag 467·5 ≈ 500·5 = 2500; exakt 467·5 = 2335.",
            "Überschlag 273·22 ≈ 300·20 = 6000; exakt 273·22 = 273·20 + 273·2 = 5460 + 546 = 6006.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.schriftlich.multiplikation"],
    },
    {
        "n": 8,
        "type": "Umkehraufgabe / Zahlenrätsel",
        "text": (
            "Ich teile meine Zahl durch 12 und zähle dann 48 hinzu. Das Ergebnis lautet 670. "
            "Wie heißt meine Zahl?"
        ),
        "answer": "Die Zahl heißt 7464.",
        "steps": [
            "Rückwärts rechnen: 670 − 48 = 622",
            "622 · 12 = 7464",
            "Probe: 7464 : 12 = 622 ;  622 + 48 = 670 ✓",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.sachaufgaben.umkehraufgaben"],
    },
    {
        "n": 9,
        "type": "Umkehraufgabe / Zahlenrätsel",
        "text": (
            "Wenn ich von meiner Zahl 378 abziehe und das Ergebnis durch 9 teile, "
            "erhalte ich 8. Wie heißt die Zahl?"
        ),
        "answer": "Die Zahl heißt 450.",
        "steps": [
            "Rückwärts: 8 · 9 = 72",
            "72 + 378 = 450",
            "Probe: 450 − 378 = 72 ;  72 : 9 = 8 ✓",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.sachaufgaben.umkehraufgaben"],
    },
    {
        "n": 10,
        "type": "Sachaufgabe (Multiplikation)",
        "text": (
            "Eine Geschirrspülmaschine der Marke „Super X“ verbraucht bei einem Spülgang "
            "23 Liter Wasser.\n"
            "Wie viel Liter Wasser verbraucht ein Haushalt in einem Jahr, wenn die Maschine "
            "jeden Tag läuft?"
        ),
        "answer": "Ein Haushalt verbraucht im Jahr 8395 Liter.",
        "steps": [
            "Tage pro Jahr: 365",
            "365 · 23 = 365·20 + 365·3 = 7300 + 1095 = 8395",
            "A: Ein Haushalt verbraucht im Jahr 8395 Liter.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.schriftlich.multiplikation",
        ],
    },
    {
        "n": 11,
        "type": "Vielfache",
        "text": "Berechne das Siebenfache von 345!",
        "answer": "345 · 7 = 2415",
        "steps": [
            "345 · 7 = (300·7) + (40·7) + (5·7) = 2100 + 280 + 35 = 2415",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.schriftlich.multiplikation"],
    },
    {
        "n": 12,
        "type": "Zahlenstrahl",
        "text": (
            "Trage die fehlenden Zahlen ein und verbinde die Zahlen unten mit dem Zahlenstrahl! "
            ""
        ),
        "answer": "Die markierten Stellen auf dem Zahlenstrahl entsprechen den vorgegebenen Zahlen (siehe Bild).",
        "steps": [
            "Zahlen am Zahlenstrahl ablesen und zuordnen.",
        ],
        "points": 3.0,
        "has_image": True,
        "image": None,
        "knowledge": ["mathe.klasse4.zahlen1000000.zahlenstrahl"],
    },
    {
        "n": 13,
        "type": "Zahlenrätsel",
        "text": (
            "Addiere zur größtmöglichen vierstelligen Zahl aus den Ziffern 4, 6, 5 und 2 "
            "die kleinstmögliche vierstellige Zahl aus den Ziffern 9, 2, 7 und 3. "
            "Wie heißt die Summe?"
        ),
        "answer": "Die Summe ist 8921.",
        "steps": [
            "Größte Zahl aus 4, 6, 5, 2 → 6542 (Ziffern absteigend)",
            "Kleinste Zahl aus 9, 2, 7, 3 → 2379 (Ziffern aufsteigend)",
            "6542 + 2379 = 8921",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.zahlenraetsel",
            "mathe.klasse4.schriftlich.addition",
        ],
    },
    {
        "n": 14,
        "type": "Sachaufgabe (mehrstufig, Geld)",
        "text": (
            "Familie Meier kauft Weihnachtsgeschenke für die ganze Familie!\n"
            "Der 18-jährige Sohn bekommt einen Fernseher für 859 €, die 16-jährige Schwester "
            "wünscht sich eine neue Stereoanlage für 974 €. Außerdem kaufen sie 6 neue "
            "Videokassetten zu je 6 €. Mutter braucht dringend einen Wäschetrockner, der "
            "1720 € kostet. Sie können den Preis etwas herunterhandeln, weil ein kleiner "
            "Lackschaden daran ist und bezahlen deshalb 140 € weniger. Sie zahlen 1449 € an "
            "und möchten den Rest in 20 gleichen Raten abzahlen.\n"
            "Wie viel beträgt eine Rate?"
        ),
        "answer": "Eine Rate beträgt 100 €.",
        "steps": [
            "Wäschetrockner-Preis: 1720 € − 140 € = 1580 €",
            "6 Videokassetten: 6 · 6 € = 36 €",
            "Gesamtsumme: 859 + 974 + 1580 + 36 = 3449 €",
            "Restbetrag nach Anzahlung: 3449 − 1449 = 2000 €",
            "Eine Rate: 2000 € : 20 = 100 €",
            "A: Eine Rate beträgt 100 €.",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.groessen.geld",
            "mathe.klasse4.schriftlich.addition",
            "mathe.klasse4.schriftlich.subtraktion",
            "mathe.klasse4.schriftlich.division",
        ],
    },
]

NEW_KNOWLEDGE = []
