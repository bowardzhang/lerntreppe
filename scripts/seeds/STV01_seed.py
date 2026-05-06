EXERCISE = {
    "id": "STV01",
    "subject": "Mathe",
    "grade": 4,
    "title": "Sachaufgaben: Textverständnis trainieren",
    "topic": "Passende Frage finden, passende Rechnung erkennen",
    "publisher": "Online-Übungen",
    "source_pdf": "Sachaufgaben_Textverständnis trainieren.pdf",
    "answer_pdf": "Sachaufgaben_Textverständnis trainieren_Lösung.pdf",
    "total_points": 6.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Passende Frage finden (Fußballturnier)",
        "text": (
            "Welche Frage passt zum Text? Streiche falsche Fragen durch und "
            "rechne die richtige Frage aus.\n"
            "'Beim Fussballturnier der Schule spielen 8 Mannschaften gegeneinander. "
            "Das Fussballfeld ist 60 Meter lang und 40 Meter breit. Es ist also "
            "kleiner als ein normales Fussballfeld. Deshalb spielen in jeder "
            "Mannschaft nur 8 Spieler.'\n"
            "(a) Wie viele Tore wurden geschossen?\n"
            "(b) Welche Mannschaft hat gewonnen?\n"
            "(c) Wie viele Spieler nehmen am Fussballturnier teil?"
        ),
        "answer": (
            "Richtige Frage: (c). 8 Mannschaften · 8 Spieler = 64 Spieler. "
            "Antwort: Es nehmen 64 Spieler am Fussballturnier teil."
        ),
        "steps": [
            "Frage (a) und (b) lassen sich aus dem Text nicht ausrechnen.",
            "Frage (c): 8 · 8 = 64 Spieler.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
        ],
    },
    {
        "n": 2,
        "type": "Passende Frage finden (Linda und Oma)",
        "text": (
            "Welche Frage passt zum Text? Streiche falsche Fragen durch und "
            "rechne die richtige Frage aus.\n"
            "'Linda wuerde gern mit ihrem Pferd zu ihrer Oma reiten. Oma wohnt "
            "allerdings 214 km vom Pferdestall entfernt. Lindas Oma ist 82 Jahre "
            "alt. Sie liebt Pferde und ist frueher mindestens 3 Stunden pro Woche "
            "geritten. Linda ist 67 Jahre juenger als Oma.'\n"
            "(a) Wie lang braucht Linda mit dem Pferd, bis sie bei Oma ist?\n"
            "(b) Wann kommt Linda bei Oma an?\n"
            "(c) Wie alt ist Linda?"
        ),
        "answer": (
            "Richtige Frage: (c). 82 - 67 = 15. Antwort: Linda ist 15 Jahre alt."
        ),
        "steps": [
            "Fragen (a) und (b) sind ohne Reitgeschwindigkeit / Startzeit nicht zu beantworten.",
            "Frage (c): 82 - 67 = 15 Jahre.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
        ],
    },
    {
        "n": 3,
        "type": "Profi-Zusatz: weitere Frage",
        "text": (
            "Finde zur zweiten Sachaufgabe (Linda/Oma) eine weitere Frage, "
            "die man mit einer Rechnung beantworten kann."
        ),
        "answer": (
            "Beispiel: 'Wie viele Stunden ist Oma frueher mindestens in einem "
            "Jahr geritten?' 3 h · 52 Wochen = 156 h pro Jahr."
        ),
        "steps": [
            "Frage formulieren, die Daten aus dem Text nutzt.",
            "Beispiel: 3 h pro Woche · 52 Wochen = 156 h pro Jahr.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
        ],
    },
    {
        "n": 4,
        "type": "Passende Geschichte zur Rechnung 63 : 7",
        "text": (
            "Welche Rechengeschichte passt zur Aufgabe 63 : 7? Kreise ein und "
            "schreibe einen Antwortsatz.\n"
            "(a) Am T-Ball-Turnier nehmen 63 Kinder teil. In einer Mannschaft "
            "spielen immer 7 Kinder.\n"
            "(b) Am T-Ball-Turnier nehmen 63 Kinder teil. 7 Kinder werden krank.\n"
            "(c) Beim T-Ball-Turnier der Stadt gibt es 63 Mannschaften. In jeder "
            "Mannschaft spielen 7 Kinder."
        ),
        "answer": (
            "Richtige Geschichte: (a). 63 : 7 = 9. "
            "Antwort: Es nehmen 9 Mannschaften am Turnier teil."
        ),
        "steps": [
            "(b) waere 63 - 7 = 56.",
            "(c) waere 63 · 7 = 441.",
            "(a) passt zu 63 : 7 = 9 Mannschaften.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
        ],
    },
    {
        "n": 5,
        "type": "Passende Geschichte zur Rechnung 4 · 20",
        "text": (
            "Welche Rechengeschichte passt zur Aufgabe 4 · 20? Kreise ein und "
            "schreibe einen Antwortsatz.\n"
            "(a) Max wiegt viermal so viel wie sein kleiner Bruder. Max wiegt 20 kg.\n"
            "(b) Lisa wiegt 20 kg. Ihre grosse Schwester Ina wiegt doppelt so viel. "
            "Ihr Vater wiegt nochmal doppelt so viel wie Ina.\n"
            "(c) Paul, Paula, Max und Maxi wiegen zusammen 20 kg."
        ),
        "answer": (
            "Richtige Geschichte: (b). 4 · 20 = 80. "
            "Antwort: Lisas Vater wiegt 80 kg."
        ),
        "steps": [
            "(a) waere 20 : 4 = 5 (kleiner Bruder).",
            "(c) Keine Rechnung moeglich, ausser alle wiegen gleich viel.",
            "(b) Vater = 4 · Lisa = 4 · 20 = 80 kg.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
        ],
    },
    {
        "n": 6,
        "type": "Passende Geschichte zur Rechnung 18 : 2 - 1",
        "text": (
            "Welche Rechengeschichte passt zur Aufgabe 18 : 2 - 1? Kreise ein und "
            "schreibe einen Antwortsatz.\n"
            "(a) Hans braucht 18 min bis zur Schule. Alle 2 Tage braucht er 1 min "
            "weniger, weil er mit Franz um die Wette rennt.\n"
            "(b) Hans braucht 18 min bis zur Schule. Franz braucht halb so lang. "
            "Mit dem Fahrrad waere Hans 1 min schneller als Franz.\n"
            "(c) Hans braucht 18 min bis zur Schule. Franz braucht doppelt so "
            "lang, waere mit dem Fahrrad aber 1 min schneller."
        ),
        "answer": (
            "Richtige Geschichte: (b). 18 : 2 - 1 = 8. "
            "Antwort: Mit dem Fahrrad braucht Hans 8 Minuten bis zur Schule."
        ),
        "steps": [
            "(a) Keine eindeutige Rechnung moeglich.",
            "(c) waere 18 · 2 - 1 = 35.",
            "(b) Franz: 18 : 2 = 9; Hans (Fahrrad): 9 - 1 = 8.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
        ],
    },
]

NEW_KNOWLEDGE = []
