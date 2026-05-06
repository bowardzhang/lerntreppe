EXERCISE = {
    "id": "0884",
    "subject": "Mathe",
    "grade": 4,
    "title": "Geometrie: Würfel und Körper",
    "topic": "Würfel-Eigenschaften, Körper benennen, Körperrätsel",
    "publisher": "CATLUX",
    "source_pdf": "0884.pdf",
    "answer_pdf": "0884 (1).pdf",
    "total_points": 16.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Lückentext zum Würfel",
        "text": (
            "Fuelle die Luecken im Text aus:\n"
            "Der Wuerfel hat ___ Ecken. Zwischen zwei benachbarten Ecken liegt "
            "eine ___. Der Wuerfel hat ___ davon. Der Wuerfel hat sechs ___. "
            "Sie haben die Form eines ___. Oben liegt die ___, unten liegt die ___, "
            "die restlichen vier heissen ___. Aus zwei aneinandergeklebten "
            "Wuerfeln entsteht ein ___. Ich brauche ___ kleine Wuerfel, um einen "
            "groesseren Wuerfel (Kantenlaenge 2) zu bauen."
        ),
        "answer": (
            "8 Ecken ; Kante ; 12 Kanten ; Flaechen ; Quadrats ; Deckflaeche ; "
            "Grundflaeche ; Seitenflaechen ; Quader ; 8 kleine Wuerfel"
        ),
        "steps": [
            "Wuerfel: 8 Ecken, 12 Kanten, 6 Flaechen (Quadrate).",
            "Oben = Deckflaeche, unten = Grundflaeche, Seiten = Seitenflaechen.",
            "2 Wuerfel zusammen = Quader.",
            "Wuerfel mit Kantenlaenge 2 = 2·2·2 = 8 kleine Wuerfel.",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
        ],
    },
    {
        "n": 2,
        "type": "Tabelle Zylinder und Kegel",
        "text": (
            "Vervollstaendige die Tabelle:\n"
            "Zylinder: ___ Flaechen, ___ Kanten, 0 Ecken\n"
            "Kegel:    ___ Flaechen, ___ Kanten, ___ Ecken (Spitzen)"
        ),
        "answer": (
            "Zylinder: 3 Flaechen (2 Kreise + 1 Mantel), 2 Kanten, 0 Ecken ; "
            "Kegel: 2 Flaechen (1 Kreis + 1 Mantel), 1 Kante, 1 Spitze"
        ),
        "steps": [
            "Zylinder: 2 Kreisflaechen + 1 Mantelflaeche = 3 Flaechen, 2 Kreis-Kanten.",
            "Kegel: 1 Kreisflaeche + 1 Mantelflaeche = 2 Flaechen, 1 Kreis-Kante, 1 Spitze.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
        ],
    },
    {
        "n": 3,
        "type": "Körperrätsel",
        "text": (
            "Welcher Koerper ist gemeint?\n"
            "a) Ich habe keine Ecken und keine Kanten und kann rollen.\n"
            "b) Ich habe 12 Kanten und 8 Ecken. Gegenueberliegende Flaechen "
            "sind gleich gross. Ich habe mindestens 4 rechteckige Flaechen.\n"
            "c) Ich habe genau eine Spitze.\n"
            "d) Ich habe zwei kreisfoermige Flaechen.\n"
            "e) Ich habe eine quadratische Grundflaeche und 4 gleich grosse "
            "dreieckige Seitenflaechen."
        ),
        "answer": (
            "a) Kugel ; b) Quader ; c) Kegel ; d) Zylinder ; e) (quadratische) Pyramide"
        ),
        "steps": [
            "a) Keine Ecken/Kanten + rollt = Kugel.",
            "b) 12 Kanten, 8 Ecken, Rechtecke = Quader.",
            "c) 1 Spitze + 1 Kreisflaeche = Kegel.",
            "d) 2 Kreisflaechen = Zylinder.",
            "e) Quadrat + 4 Dreiecke = Pyramide.",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
        ],
    },
    {
        "n": 4,
        "type": "Aussagen über den Würfel",
        "text": (
            "Welche Aussagen ueber den Wuerfel sind richtig? Kreuze an:\n"
            "(1) Der Wuerfel hat 8 Seiten.\n"
            "(2) Der Wuerfel hat 12 Kanten.\n"
            "(3) Der Wuerfel hat nur Rechtecke (keine Quadrate) als Flaechen.\n"
            "(4) Der Wuerfel hat 6 Seiten.\n"
            "(5) Der Wuerfel hat 8 Ecken.\n"
            "(6) Der Wuerfel hat 6 Ecken."
        ),
        "answer": "Richtig: (2), (4), (5).",
        "steps": [
            "(1) falsch: 6 Seiten, nicht 8.",
            "(2) richtig: 12 Kanten.",
            "(3) falsch: alle Flaechen sind Quadrate (Spezialfall des Rechtecks).",
            "(4) richtig: 6 Seiten/Flaechen.",
            "(5) richtig: 8 Ecken.",
            "(6) falsch: 8 Ecken, nicht 6.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.geometrie.koerper",
        ],
    },
]

NEW_KNOWLEDGE = []
