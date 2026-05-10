EXERCISE = {
    "id": "0360",
    "subject": "Mathe",
    "grade": 4,
    "title": "Lernzielkontrolle: Geometrie — Körper",
    "topic": "3D-Körper: Eigenschaften, Benennen, Kanten, Ecken, Flächen",
    "publisher": "CATLUX",
    "source_pdf": "0360.pdf",
    "answer_pdf": "0360 (1).pdf",
    "total_points": 10.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "2D-Formen benennen",
        "text": "Nenne 6 verschiedene ebene Figuren, die ihr gelernt habt.",
        "answer": "Rechteck, Kreis, Dreieck, Raute, Drache, Viereck (andere richtige Formen werden ebenfalls akzeptiert)",
        "steps": [
            "Ebene Figuren: Rechteck, Quadrat, Dreieck, Kreis, Raute, Drache, Sechseck, Acht­eck, Parallelogramm usw.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
        ],
    },
    {
        "n": 2,
        "type": "Körper an Beschreibungen erkennen",
        "text": (
            "Benenne den Körper, der zur Beschreibung passt:\n"
            "a) Er hat genau 2 gleiche runde Flächen.\n"
            "b) Er hat 8 Kanten, 5 Ecken und 5 Flächen.\n"
            "c) Er hat 6 gleiche quadratische Flächen, 12 Kanten und 8 Ecken.\n"
            "d) Er hat 2 dreieckige und 3 rechteckige Flächen, 6 Ecken und 9 Kanten."
        ),
        "answer": "a) Zylinder ; b) (viereckige) Pyramide ; c) Würfel ; d) Dreiecksprisma",
        "steps": [
            "a) 2 runde Flächen + Mantel = Zylinder.",
            "b) 5 Flächen (1 Quadrat + 4 Dreiecke), 8 Kanten, 5 Ecken = quadratische Pyramide.",
            "c) 6 Quadrate, 12 Kanten, 8 Ecken = Würfel.",
            "d) 2 Dreiecke + 3 Rechtecke, 9 Kanten, 6 Ecken = Dreiecksprisma.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
        ],
    },
    {
        "n": 3,
        "type": "Würfelrollaufgabe",
        "text": (
            "Ein Würfel liegt auf dem Feld A. Die gegenüberliegenden Seiten "
            "ergeben zusammen immer 7. Der Würfel zeigt auf Feld A oben die 2. "
            "Er wird nach rechts auf Feld B gekippt, dann erneut nach rechts auf "
            "Feld C. Welche Zahl zeigt der Würfel jeweils oben?\n"
            "Feld A (Start, oben = 2): ___\n"
            "Feld B (nach 1. Kippen): ___\n"
            "Feld C (nach 2. Kippen): ___"
        ),
        "answer": "Feld A: 2 ; Feld B: 5 ; Feld C: 6",
        "steps": [
            "Gegenüberliegende Flächen: 1-6, 2-5, 3-4.",
            "Start: oben = 2, unten = 5.",
            "Kippen nach rechts: die rechte Seite wird zur neuen Unterseite; oben wird die vorherige Vorderseite.",
            "Nach 1. Kippen (Feld B): oben = 5.",
            "Nach 2. Kippen (Feld C): oben = 6.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
        ],
    },
]

NEW_KNOWLEDGE = []
