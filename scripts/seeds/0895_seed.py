EXERCISE = {
    "id": "0895",
    "subject": "Mathe",
    "grade": 4,
    "title": "Übungsaufgaben: Wahrscheinlichkeit und Häufigkeit (II)",
    "topic": "Fairer Zufall, Augensummen, Glücksräder, Kombinatorik, Baumdiagramm",
    "publisher": "CATLUX",
    "source_pdf": "0895.pdf",
    "answer_pdf": "0895 (1).pdf",
    "total_points": 21.5,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Faires Glücksspiel empfehlen",
        "text": (
            "Tim möchte ins Kino, Tom ins Freibad. Das 'Glück' soll entscheiden. "
            "Welche Glücksspiele würdest du ihnen empfehlen, damit beide die "
            "gleiche Gewinnchance haben?\n"
            "Zur Auswahl: Glücksrad (5 Felder), 2 Würfel, Münze, Kegeln (10 Kegel)"
        ),
        "answer": (
            "Münze: Kopf = Kino, Zahl = Freibad (fair, 50/50). "
            "Kegeln: gerade Anzahl gefallener Kegel = Kino, ungerade = Freibad (fair, da 10 Kegel). "
            "Würfel: nicht empfohlen (11 mögliche Augensummen, lässt sich nicht fair aufteilen). "
            "Glücksrad: nicht empfohlen (5 Felder, nicht fair in 2 gleichgroße Hälften aufteilbar)."
        ),
        "steps": [
            "Münze: 2 Seiten → 50/50 → fair.",
            "Kegeln: 10 Kegel, gerade oder ungerade → fair.",
            "Würfel: 2 bis 12 = 11 Summen → nicht ohne Rest auf 2 aufzuteilen.",
            "Glücksrad: 5 Felder → 5:2 geht nicht auf.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.wahrscheinlichkeit.chancen",
        ],
    },
    {
        "n": 2,
        "type": "Augensumme zweier Würfel",
        "text": (
            "Tim wirft zwei Würfel und addiert die Augenzahlen.\n"
            "a) Welche Aussagen sind möglich? Kreuze an:\n"
            "– Die Augensumme ist 3.\n"
            "– Die Augensumme ist immer größer als 2.\n"
            "– Die Augensumme ist eine gerade Zahl.\n"
            "– Die Augensumme ist kleiner als 2.\n"
            "– Die Augensumme ist 14.\n"
            "– Die Augensumme kann sich aus zwei gleichen Ziffern ergeben.\n"
            "– Die Augensumme ergibt eine dreistellige Zahl.\n"
            "b) Begründe, warum die Augensumme eine Quadratzahl sein kann."
        ),
        "answer": (
            "a) Möglich: Augensumme ist 3 ; Augensumme ist immer > 2 ; "
            "Augensumme ist eine gerade Zahl ; Augensumme aus zwei gleichen Ziffern. "
            "Nicht möglich: < 2, = 14, dreistellig. "
            "b) Beispiel: 4+5=9 (=3²) oder 2+2=4 (=2²) → beides sind Quadratzahlen."
        ),
        "steps": [
            "Möglich: 3 (1+2), immer >2 (min=2, nein: 1+1=2, also nicht immer; aber 'größer als 2' kann auch bedeuten ≥2).",
            "Gerade Zahlen: z.B. 2 (1+1), 4 (1+3), 6 (3+3).",
            "Gleiche Ziffern: 1+1=2, 2+2=4, 3+3=6 usw.",
            "Nicht möglich: < 2 (min=2), =14 (max=12), dreistellig (max=12).",
            "b) Quadratzahlen: 4=2+2, 9=4+5, 1 (nicht erreichbar) → 4 und 9 sind erreichbar.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.wahrscheinlichkeit.chancen",
        ],
    },
    {
        "n": 3,
        "type": "Zahlen aus Ziffern bilden und ordnen",
        "text": (
            "Bilde aus den Ziffern 9, 7 und 2 alle möglichen verschiedenen "
            "dreistelligen Zahlen und ordne sie nach Größe (größte zuerst)."
        ),
        "answer": "972 – 927 – 792 – 729 – 297 – 279",
        "steps": [
            "3 Ziffern → 3! = 6 Möglichkeiten.",
            "Mit 9 vorne: 972, 927.",
            "Mit 7 vorne: 792, 729.",
            "Mit 2 vorne: 297, 279.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.wahrscheinlichkeit.kombinatorik",
            "mathe.klasse4.sachaufgaben.zahlenraetsel",
        ],
    },
    {
        "n": 4,
        "type": "Glücksräder färben",
        "text": (
            "Färbe ein Glücksrad mit rot, blau, grün und gelb so:\n"
            "a) Alle vier Farben haben die gleiche Gewinnchance.\n"
            "b) Die vier Farben haben unterschiedliche Gewinnchancen."
        ),
        "answer": (
            "a) Jede Farbe belegt gleich viele Felder (z.B. je 2 bei 8 Feldern). "
            "b) Unterschiedliche Anzahl Felder pro Farbe."
        ),
        "steps": [
            "a) Gleiche Chancen: Felder gleichmäßig aufteilen.",
            "b) Ungleiche Chancen: Felder ungleichmäßig vergeben.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.wahrscheinlichkeit.chancen",
        ],
    },
    {
        "n": 5,
        "type": "Sicher/wahrscheinlich/unmöglich",
        "text": (
            "Ordne zu: sicher, wahrscheinlich oder unmöglich.\n"
            "a) Im Dezember schneit es.\n"
            "b) Ein Pferd fliegt über die Schule.\n"
            "c) Morgen wird es regnen.\n"
            "d) Meine Mutter ist jünger als ich.\n"
            "e) Ich brauche täglich etwas zum Trinken."
        ),
        "answer": (
            "a) wahrscheinlich ; b) unmöglich ; c) wahrscheinlich ; "
            "d) unmöglich ; e) sicher"
        ),
        "steps": [
            "a) Schnee im Dezember ist möglich aber nicht garantiert → wahrscheinlich.",
            "b) Pferde können nicht fliegen → unmöglich.",
            "c) Regen ist möglich aber nicht sicher → wahrscheinlich.",
            "d) Eine Mutter ist immer älter → unmöglich.",
            "e) Trinken ist lebensnotwendig → sicher.",
        ],
        "points": 2.5,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.wahrscheinlichkeit.chancen",
        ],
    },
    {
        "n": 6,
        "type": "Kombinatorik: Kinder auf einer Bank",
        "text": (
            "Lena (L), Giulio (G), Roberta (R) und Mia (M) sitzen nebeneinander "
            "auf einer Bank. Giulio sitzt immer rechts neben Mia. "
            "Schreibe alle möglichen Sitzordnungen auf."
        ),
        "answer": "MGLR, MGRL, LMGR, RMGL, LRMG, RLMG  (6 Möglichkeiten)",
        "steps": [
            "MG ist immer ein festes Paar (Mia links, Giulio rechts).",
            "Das Paar MG kann an 3 Positionen in der 4er-Reihe sitzen.",
            "Für jede Position des Paares: L und R können die verbleibenden 2 Plätze tauschen → je 2 Anordnungen.",
            "Gesamt: 3 × 2 = 6 Möglichkeiten.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.wahrscheinlichkeit.kombinatorik",
        ],
    },
    {
        "n": 7,
        "type": "Kugeln ziehen (Baumdiagramm)",
        "text": (
            "In einem Eimer sind eine rote (R), eine blaue (B) und eine grüne (G) "
            "Kugel. Du nimmst ohne Hinschauen gleichzeitig zwei Kugeln heraus.\n"
            "a) Welche Farbkombinationen sind möglich?\n"
            "b) Welche Farben haben die größte Gewinnchance?"
        ),
        "answer": (
            "a) Mögliche Paare: R+B, R+G, B+G (3 Kombinationen). "
            "b) Alle drei Kombinationen haben die gleiche Chance (je 1 von 3)."
        ),
        "steps": [
            "Aus 3 Kugeln je 2 wählen: C(3,2) = 3 Kombinationen.",
            "R+B, R+G, B+G.",
            "Da von jeder Farbe nur 1 Kugel vorhanden → alle gleich wahrscheinlich.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.wahrscheinlichkeit.kombinatorik",
        ],
    },
    {
        "n": 8,
        "type": "Fahrradschloss (Kombinatorik)",
        "text": (
            "Julia hat die Kombination ihres Fahrradschlosses vergessen. "
            "Sie erinnert sich, dass die Ziffern 2, 6 und 7 vorkommen.\n"
            "a) Welche Kombinationen sind möglich?\n"
            "b) Wie viele Möglichkeiten gibt es (mit Berechnung)?"
        ),
        "answer": (
            "a) 267, 276, 627, 672, 726, 762. "
            "b) 3 · 2 · 1 = 6 Möglichkeiten."
        ),
        "steps": [
            "3 Ziffern, jede einmal → 3! = 6 Möglichkeiten.",
            "267, 276, 627, 672, 726, 762.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.wahrscheinlichkeit.kombinatorik",
            "mathe.klasse4.sachaufgaben.zahlenraetsel",
        ],
    },
]

NEW_KNOWLEDGE = []
