EXERCISE = {
    "id": "0045",
    "subject": "Mathe",
    "grade": 4,
    "title": "Vorbereitung Probeunterricht: Grundrechenarten",
    "topic": "Grundrechenarten, Zahlenraum, Runden, Zahlenfolgen, Sachaufgaben, Probeunterricht",
    "publisher": "CATLUX",
    "source_pdf": "0045.pdf",
    "answer_pdf": "0045 (1).pdf",
    "total_points": 30.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Dreieck-Aufgabe Division",
        "text": (
            "Welche Zahl kannst du fuer das Dreieck einsetzen?\n"
            "[Dreieck] : 9 = 417 Rest 7"
        ),
        "answer": "[Dreieck] = 417 x 9 + 7 = 3753 + 7 = 3760.",
        "steps": [
            "Bei Division mit Rest: Dividend = Quotient x Divisor + Rest.",
            "417 x 9 = 3753.",
            "3753 + 7 = 3760.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.schriftlich.division"],
    },
    {
        "n": 2,
        "type": "Drei-Zahlen-Summe",
        "text": (
            "Drei Zahlen ergeben zusammen 100 000. Die erste Zahl ist 34 855. "
            "Die zweite Zahl ist um 7 699 kleiner als die erste. Wie heisst "
            "die dritte Zahl?"
        ),
        "answer": (
            "1. Zahl: 34 855 ; "
            "2. Zahl: 34 855 - 7 699 = 27 156 ; "
            "Summe der ersten zwei: 34 855 + 27 156 = 62 011 ; "
            "3. Zahl: 100 000 - 62 011 = 37 989."
        ),
        "steps": [
            "Zweite Zahl berechnen.",
            "Beide aufaddieren.",
            "Von 100 000 abziehen.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.schriftlich.subtraktion"],
    },
    {
        "n": 3,
        "type": "Zeichen ersetzen Gleichungen",
        "text": (
            "Setze fuer die Zeichen Zahlen ein. Dieselben Zeichen bedeuten "
            "dieselbe Zahl:\n"
            "[Stern] : 9 = [Kreis] ; [Stern] x 36 = 11 052 ; [Kreis] - [Quadrat] = 3552 : 12"
        ),
        "answer": (
            "[Stern] = 11 052 : 36 = 307 ; "
            "[Kreis] = 307 : 9 ... Probe: 3552 : 12 = 296 ; "
            "[Kreis] - [Quadrat] = 296, also [Quadrat] = 307 - 296 = 11. "
            "Test: 11 x 9 = 99 = [Kreis]. "
            "Endergebnis: [Stern] = 307 ; [Kreis] = 99 ; [Quadrat] = 11."
        ),
        "steps": [
            "Erst 11052 : 36 berechnen -> Stern.",
            "Dann 3552 : 12 berechnen -> Differenz.",
            "Wert vom Quadrat aus den Bedingungen ableiten.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.sachaufgaben.zahlenraetsel"],
    },
    {
        "n": 4,
        "type": "Ungleichungen mit Ziffern",
        "text": (
            "Gleiche Zeichen = gleiche Zahlen. Gib alle Zahlen an, die du einsetzen darfst:\n"
            "a) 95 365 - [Kasten] > 95 356\n"
            "b) 400 x [Kasten] < 600"
        ),
        "answer": (
            "a) 0, 1, 2, 3, 4, 5, 6, 7, 8 ; "
            "b) 0, 1 (denn 400 x 1 = 400 < 600 ; 400 x 2 = 800 > 600). "
            "Hinweis: Wenn Zahlenraum erweitert: 0 und 1."
        ),
        "steps": [
            "a) 95365 - x > 95356 -> x < 9.",
            "b) 400 * x < 600 -> x < 1,5 -> 0 oder 1.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.schriftlich.subtraktion"],
    },
    {
        "n": 5,
        "type": "Groesste/kleinste Zahl + 100000",
        "text": (
            "Bilde aus den Ziffern 6, 0, 8, 7, 1 die groesste und die kleinste "
            "Zahl. Verwende jede Ziffer nur einmal. Ergaenze jede der Zahlen zu 100 000."
        ),
        "answer": (
            "Kleinste Zahl: 10 678 (fuehrende 0 nicht erlaubt). "
            "Ergaenzung: 100 000 - 10 678 = 89 322. "
            "Groesste Zahl: 87 610. "
            "Ergaenzung: 100 000 - 87 610 = 12 390."
        ),
        "steps": [
            "Fuer kleinste Zahl: aufsteigend, ohne fuehrende 0.",
            "Fuer groesste Zahl: absteigend.",
            "Beides zu 100 000 ergaenzen.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.zahlen1000000.stellenwerte"],
    },
    {
        "n": 6,
        "type": "Zahl in der Mitte",
        "text": "Welche Zahl liegt genau in der Mitte von 97 und 117?",
        "answer": "(97 + 117) : 2 = 214 : 2 = 107.",
        "steps": ["Mittelwert = (a+b) : 2."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.zahlen1000000.stellenwerte"],
    },
    {
        "n": 7,
        "type": "Zahlen in Ziffern",
        "text": (
            "Schreibe in Ziffern:\n"
            "a) dreiundsechzigtausendzweiundfuenfzig\n"
            "b) siebzigtausendfuenfhundert"
        ),
        "answer": "a) 63 052 ; b) 70 500.",
        "steps": ["Tausender und Einer korrekt einsetzen."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.zahlen1000000.stellenwerte"],
    },
    {
        "n": 8,
        "type": "Zahlenraetsel Verdoppeln",
        "text": (
            "Fuege ich zum Doppelten meiner Zahl die Zahl 15 000 hinzu, so "
            "erhalte ich die Haelfte von 70 000. Wie heisst die Zahl?"
        ),
        "answer": (
            "Haelfte von 70 000 = 35 000. "
            "35 000 - 15 000 = 20 000 (= 2 x Zahl). "
            "20 000 : 2 = 10 000. "
            "Die Zahl heisst 10 000."
        ),
        "steps": [
            "Haelfte von 70 000 berechnen.",
            "15 000 abziehen.",
            "Durch 2 teilen.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.sachaufgaben.zahlenraetsel"],
    },
    {
        "n": 9,
        "type": "Runden Hunderter",
        "text": (
            "Eine Zahl wurde auf Hunderter gerundet zu 1 900.\n"
            "a) Welche kleinstmoegliche Zahl ergibt gerundet 1 900?\n"
            "b) Welche groesstmoegliche?"
        ),
        "answer": "a) 1 850 ; b) 1 949.",
        "steps": [
            "Rundungsspanne fuer 1 900: 1 850 bis 1 949.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.zahlen1000000.runden"],
    },
    {
        "n": 10,
        "type": "Runden auf Hunderter und Tausender",
        "text": (
            "a) Runde auf volle Hunderter: 6 353 ; 8 970.\n"
            "b) 83 000 ist auf Tausender gerundet. Gib die kleinste Zahl an, "
            "die so gerundet 83 000 ergibt.\n"
            "c) 47 000 ist auf Tausender gerundet. Gib die groesste Zahl an, "
            "die so gerundet 47 000 ergibt."
        ),
        "answer": "a) 6 400 ; 9 000. ; b) 82 500. ; c) 47 499.",
        "steps": [
            "Hunderter-Stelle pruefen.",
            "Bei 5 oder mehr aufrunden.",
            "Bei Tausender: Spanne 500 unter bis 499 ueber.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.zahlen1000000.runden"],
    },
    {
        "n": 11,
        "type": "Zahlenfolgen fortsetzen",
        "text": (
            "Setze die Zahlenfolge nach links und nach rechts um zwei Glieder fort:\n"
            "a) ___, ___, 17, 34, 37, 74, 77, ___, ___\n"
            "b) ___, ___, 178, 176, 181, 179, 184, ___, ___"
        ),
        "answer": (
            "a) 7 ; 14 ; 17 ; 34 ; 37 ; 74 ; 77 ; 154 ; 157. "
            "(Regel abwechselnd: x 2 ; + 3) ; "
            "b) 175 ; 173 ; 178 ; 176 ; 181 ; 179 ; 184 ; 182 ; 187. "
            "(Regel abwechselnd: -2 ; +5)."
        ),
        "steps": [
            "Regel der Folge erkennen (oft zwei wechselnde Operationen).",
            "Rueckwaerts und vorwaerts anwenden.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.zahlen1000000.stellenwerte"],
    },
    {
        "n": 12,
        "type": "Verdreifachen Drei-Zahlen-Summe",
        "text": (
            "Drei Zahlen ergeben zusammen 90 000. Wenn du die kleinste Zahl "
            "verdreifachst, erhaelst du die groesste, naemlich 43 653. Wie "
            "heissen die drei Zahlen?"
        ),
        "answer": (
            "Kleinste: 43 653 : 3 = 14 551 ; "
            "Groesste: 43 653 ; "
            "Mittlere: 90 000 - 43 653 - 14 551 = 31 796."
        ),
        "steps": [
            "Kleinste = Groesste / 3.",
            "Summe der drei = 90 000.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.schriftlich.multiplikation"],
    },
    {
        "n": 13,
        "type": "Vierstellige Zahlen zaehlen",
        "text": "Wie viele vierstellige Zahlen gibt es insgesamt?",
        "answer": "9 000 (von 1 000 bis 9 999).",
        "steps": ["9 999 - 1 000 + 1 = 9 000."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.zahlen1000000.stellenwerte"],
    },
    {
        "n": 14,
        "type": "Geburtsdatum-Raetsel",
        "text": (
            "Mein Freund verraet sein Geburtsdatum nicht direkt: 'Das Doppelte "
            "von 285 vermindere ich um 239 und multipliziere das Ergebnis mit "
            "64. Die erste Ziffer ergibt den Tag, die naechsten zwei den Monat, "
            "die letzten zwei das Geburtsjahr.' Wann wurde er geboren?"
        ),
        "answer": (
            "285 x 2 = 570 ; 570 - 239 = 331 ; 331 x 64 = 21 184. "
            "Antwort: 2.11.84 - geboren am 2. November 1984."
        ),
        "steps": [
            "Reihenfolge der Operationen einhalten.",
            "Ergebnis auseinander schneiden: 2 / 11 / 84.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.schriftlich.multiplikation"],
    },
    {
        "n": 15,
        "type": "Sechsstellig ohne 9 und 0",
        "text": (
            "Wie heissen die kleinste und die groesste sechsstellige Zahl, bei "
            "denen weder 9 noch 0 vorkommen?"
        ),
        "answer": "Kleinste: 111 111 ; groesste: 888 888.",
        "steps": [
            "Erlaubte Ziffern: 1, 2, 3, 4, 5, 6, 7, 8.",
            "Kleinste: alle 1 ; groesste: alle 8.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.zahlen1000000.stellenwerte"],
    },
    {
        "n": 16,
        "type": "Drei-Zahlen mit 27396",
        "text": (
            "Drei Zahlen ergeben zusammen 100 000. Eine Zahl heisst 27 396. Sie "
            "ist genau dreimal so gross wie die kleinste Zahl. Wie heissen die "
            "drei Zahlen?"
        ),
        "answer": (
            "Kleinste: 27 396 : 3 = 9 132 ; "
            "Mittlere: 27 396 ; "
            "Groesste: 100 000 - 9 132 - 27 396 = 63 472."
        ),
        "steps": [
            "Kleinste aus Verhaeltnis berechnen.",
            "Drittzahl = Summe minus die anderen beiden.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.schriftlich.multiplikation"],
    },
    {
        "n": 17,
        "type": "Begruenden Division",
        "text": "Begruende ohne zu rechnen: 544 666 : 4 > 544 666 : 5.",
        "answer": (
            "Wenn man eine Zahl in weniger Teile aufteilt (durch 4), ist jeder "
            "Teil groesser. Teilt man durch 5, bekommt jeder weniger ab. "
            "Daher ist 544 666 : 4 groesser als 544 666 : 5."
        ),
        "steps": [
            "Verstaendnis: Division = aufteilen.",
            "Weniger Teile -> jeder Teil ist groesser.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.schriftlich.division"],
    },
    {
        "n": 18,
        "type": "Zwei Zahlen Differenz",
        "text": (
            "Zwei Zahlen ergeben zusammen 20 991. Eine ist um 999 groesser als "
            "die andere. Wie heissen die beiden Zahlen?"
        ),
        "answer": (
            "20 991 - 999 = 19 992 ; 19 992 : 2 = 9 996 (kleinere Zahl) ; "
            "9 996 + 999 = 10 995 (groessere Zahl). "
            "Die Zahlen sind 9 996 und 10 995."
        ),
        "steps": [
            "Differenz von der Summe abziehen.",
            "Durch 2 teilen -> kleinere Zahl.",
            "Differenz wieder addieren -> groessere Zahl.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.schriftlich.subtraktion"],
    },
    {
        "n": 19,
        "type": "40. Teil dazuzaehlen",
        "text": (
            "Wenn ich von 16 000 den 40. Teil dazuzaehle, erhalte ich um 6 000 "
            "mehr als mein Freund. Wie viel hat mein Freund?"
        ),
        "answer": (
            "40. Teil von 16 000 = 16 000 : 40 = 400 ; "
            "16 000 + 400 = 16 400 ; "
            "Freund hat: 16 400 - 6 000 = 10 400."
        ),
        "steps": [
            "40. Teil = durch 40 teilen.",
            "Dazuzaehlen.",
            "6 000 abziehen.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.schriftlich.division"],
    },
    {
        "n": 20,
        "type": "Herr Sparsam Auto",
        "text": (
            "Herr Sparsam hat ein Auto auf Tausender gerundet fuer rund 16 000 "
            "Euro gekauft. Wie viel hat er mindestens und hoechstens bezahlt?"
        ),
        "answer": "Mindestens: 15 500 Euro ; hoechstens: 16 499 Euro.",
        "steps": [
            "Tausender-Spanne fuer 16 000: von 15 500 bis 16 499.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.zahlen1000000.runden"],
    },
]

NEW_KNOWLEDGE = []
