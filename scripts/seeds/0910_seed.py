EXERCISE = {
    "id": "0910",
    "subject": "Mathe",
    "grade": 4,
    "title": "Geometrie: Arbeit mit Zirkel und Geodreieck",
    "topic": "Geometrie, Zirkel, Geodreieck, Parallelen, Senkrechte, Kreis, Rechteck",
    "publisher": "CATLUX",
    "source_pdf": "0910.pdf",
    "answer_pdf": "0910 (1).pdf",
    "total_points": 35.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Lückentext Kreis",
        "text": (
            "Fuelle die Luecken mit den richtigen Begriffen:\n"
            "Um einen Kreis zu zeichnen, brauchst du einen ___. Die Spitze "
            "stichst du in den ___, dann kannst du den Kreis zeichnen. Die "
            "Entfernung von der Kreislinie zur Mitte ist ueberall gleich groß. "
            "Sie wird ___ genannt. Wenn du durch die Mitte des Kreises eine "
            "gerade Linie zeichnest, bekommst du den ___ des Kreises. Er ist "
            "doppelt so lang wie der ___."
        ),
        "answer": "Zirkel ; Mittelpunkt ; Radius ; Durchmesser ; Radius.",
        "steps": [
            "Werkzeug zum Kreiszeichnen: Zirkel.",
            "Stechpunkt = Mittelpunkt M.",
            "r = Radius (vom Rand bis Mitte).",
            "d = Durchmesser = 2 x Radius.",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse1.geometrie.formen"],
    },
    {
        "n": 2,
        "type": "Parallelen pruefen",
        "text": "Ueberpruefe mit deinem Geodreieck, ob die drei waagerechten Geraden parallel sind. (3 Geraden zu pruefen)",
        "answer": "Alle drei Antworten: ja - die Geraden sind parallel.",
        "steps": [
            "Geodreieck-Kante an die erste Gerade anlegen.",
            "Senkrechten Abstand zur naechsten Gerade messen.",
            "Wenn der Abstand gleich bleibt -> parallel.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.geometrie.vierecke"],
    },
    {
        "n": 3,
        "type": "Senkrechte und Parallele konstruieren",
        "text": (
            "Fuehre nach Vorschrift aus:\n"
            "a) Zeichne durch die Punkte A und B Geraden, die senkrecht auf der "
            "Geraden g stehen.\n"
            "b) Zeichne durch die Punkte A und B eine Gerade. Nenne sie h.\n"
            "c) Zeichne eine weitere Gerade, die im Abstand von 2 cm parallel "
            "zur Geraden h verlaeuft."
        ),
        "answer": (
            "a) Geodreieck mit 90-Grad-Marke an g anlegen, durch A bzw. B Senkrechte zeichnen. ; "
            "b) Lineal an A und B legen, Gerade h zeichnen. ; "
            "c) Geodreieck an h anlegen, 2 cm parallel verschieben, neue Gerade ziehen."
        ),
        "steps": [
            "Senkrechte = 90 Grad.",
            "Parallel verschieben mit dem Geodreieck.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.geometrie.vierecke"],
    },
    {
        "n": 4,
        "type": "Muster nachzeichnen",
        "text": "Zeichne das vorgegebene Muster genau nach.",
        "answer": "Sauber mit Geodreieck und Zirkel uebertragen, alle Linien und Kreise massgenau.",
        "steps": [
            "Hilfslinien benutzen.",
            "Zirkelweite einstellen, Mittelpunkt setzen.",
            "Linien mit Lineal/Geodreieck nachziehen.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse1.geometrie.muster"],
    },
    {
        "n": 5,
        "type": "Rechteck mit Diagonalen und Kreis",
        "text": (
            "Zeichne ein Rechteck mit der Länge 7 cm und der Breite 4 cm. "
            "Verbinde die gegenueberliegenden Eckpunkte (Diagonalen). Du "
            "erhaelst den Schnittpunkt S. Zeichne um S einen Kreis mit dem "
            "Radius r = 2 cm."
        ),
        "answer": (
            "Rechteck 7 cm x 4 cm zeichnen ; beide Diagonalen ziehen ; "
            "Schnittpunkt S ist die Mitte des Rechtecks ; Zirkel auf 2 cm "
            "einstellen, in S einstechen, Kreis ziehen."
        ),
        "steps": [
            "Rechteck mit Geodreieck zeichnen, rechte Winkel pruefen.",
            "Diagonalen schneiden sich genau in der Mitte.",
            "Kreis r = 2 cm um S.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.geometrie.vierecke"],
    },
    {
        "n": 6,
        "type": "Mittelpunkte erkennen",
        "text": "Welche Punkte sind Mittelpunkte? Schreibe die Buchstaben auf.",
        "answer": "B, F, G.",
        "steps": [
            "Mittelpunkt liegt genau in der Mitte einer Figur.",
            "Bei einem Kreis ist es der Stechpunkt des Zirkels.",
            "Abstand zu allen Randpunkten muss gleich sein.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse1.geometrie.formen"],
    },
    {
        "n": 7,
        "type": "Figuren uebertragen",
        "text": "Uebertrage die gegebenen Figuren ganz genau.",
        "answer": "Massgenaue Uebertragung mit Geodreieck und Zirkel ausfuehren.",
        "steps": [
            "Strecken mit Geodreieck ausmessen.",
            "Winkel ablesen und nachzeichnen.",
            "Kreise mit gleichem Radius zeichnen.",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse1.geometrie.formen"],
    },
    {
        "n": 8,
        "type": "Kombi-Konstruktion",
        "text": (
            "Zeichne mit Geodreieck und Zirkel:\n"
            "a) Einen Kreis mit 3 cm Radius. Wie groß ist der Durchmesser?\n"
            "b) Zeichne durch den Mittelpunkt des Kreises eine Gerade.\n"
            "c) Zeichne zu deiner Geraden eine parallele Gerade im Abstand 2 cm.\n"
            "d) Zeichne zu der Geraden von b) zwei senkrechte Geraden."
        ),
        "answer": (
            "a) Durchmesser = 2 x 3 cm = 6 cm. ; "
            "b) Linie durch M ziehen. ; "
            "c) Geodreieck an die Gerade legen, 2 cm parallel verschieben. ; "
            "d) Geodreieck mit 90-Grad-Marke an die Gerade aus b) legen, zwei "
            "Senkrechte zeichnen."
        ),
        "steps": [
            "d = 2 x r.",
            "Parallel: Abstand bleibt gleich.",
            "Senkrecht: 90 Grad.",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse1.geometrie.formen",
            "mathe.klasse4.geometrie.vierecke",
        ],
    },
]

NEW_KNOWLEDGE = []
