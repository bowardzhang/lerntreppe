EXERCISE = {
    "id": "2162",
    "subject": "Mathe",
    "grade": 4,
    "title": "Lernzielkontrolle: Arbeit mit Zirkel und Geodreieck",
    "topic": "Geometrie, Zirkel, Geodreieck, Parallelen, Senkrechte, Kreise, Parkettieren",
    "publisher": "CATLUX",
    "source_pdf": "2162.pdf",
    "answer_pdf": "2162 (1).pdf",
    "total_points": 34.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Wahre Aussagen ankreuzen",
        "text": (
            "Stimmen diese Aussagen? Kreuze die richtigen Aussagen an!\n"
            "(a) Parallelen müssen mindestens 5 mm Abstand haben.\n"
            "(b) Eine Gerade hat einen Anfangspunkt A.\n"
            "(c) Ein Rechteck hat vier gleich lange Seiten.\n"
            "(d) Gerade Linien, die senkrecht zueinander verlaufen, bilden einen rechten Winkel.\n"
            "(e) Eine Senkrechte zwischen 2 Parallelen ist die kuerzeste Verbindung "
            "zwischen diesen Geraden.\n"
            "(f) Parallele Geraden haben irgendwann einen Schnittpunkt.\n"
            "(g) Der Durchmesser eines Kreises ist dreimal so groß wie der Radius."
        ),
        "answer": "Richtig: (d) und (e).",
        "steps": [
            "(a) falsch: Parallelen können jeden Abstand haben.",
            "(b) falsch: Gerade ist endlos, Strahl/Halbgerade hat Anfangspunkt.",
            "(c) falsch: Quadrat hat 4 gleiche Seiten, Rechteck nur Paare.",
            "(d) richtig.",
            "(e) richtig: senkrecht = kuerzeste Verbindung.",
            "(f) falsch: Parallelen schneiden sich nie.",
            "(g) falsch: Durchmesser = 2 x Radius.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.geometrie.vierecke"],
    },
    {
        "n": 2,
        "type": "Fachbegriffe Zirkel und Geodreieck",
        "text": (
            "Beschrifte die Teile des Zirkels und des Geodreiecks! Nenne die "
            "Fachbegriffe (Felder 1 bis 8)."
        ),
        "answer": (
            "1) Mittelpunkt ; 2) Durchmesser ; 3) Radius ; 4) Kreisflaeche ; "
            "5) Kreislinie ; 6) Strecke ; 7) Strahl ; 8) Schnittpunkt."
        ),
        "steps": ["Fachbegriffe der Geometrie auswendig wissen."],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse1.geometrie.formen"],
    },
    {
        "n": 3,
        "type": "Rechteck messen und zeichnen",
        "text": (
            "Rechteck-Aufgabe:\n"
            "a) Miss die Seitenlaengen und trage deine Masse ein.\n"
            "b) Kennzeichne alle rechten Winkel.\n"
            "c) Zeichne dieses Rechteck noch einmal in doppelter Groesse und "
            "ziehe 2 Diagonalen."
        ),
        "answer": (
            "a) 2 cm und 3,5 cm. ; "
            "b) Alle 4 Ecken sind rechte Winkel (mit Quadrat-Symbol markieren). ; "
            "c) Doppelte Groesse: 4 cm und 7 cm Seiten, dazu 2 Diagonalen "
            "von Ecke zu Ecke."
        ),
        "steps": [
            "Mit Geodreieck die Seitenlaengen messen.",
            "Doppelte Groesse: jede Seite x 2.",
            "Diagonalen verbinden gegenueberliegende Ecken.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.geometrie.vierecke"],
    },
    {
        "n": 4,
        "type": "Stadtplan-Konstruktion",
        "text": (
            "Stadtplan-Aufgabe: Zeichne zur Hauptstrasse eine parallele Straße, "
            "die durch den Parkplatz (P) geht. Mache dann von der Schule (S) aus "
            "einen geraden Weg, der im rechten Winkel zur Hauptstrasse führt."
        ),
        "answer": (
            "1. Geodreieck an Hauptstrasse anlegen, parallel verschieben bis P, Linie ziehen. ; "
            "2. Geodreieck so anlegen, dass eine Achse auf der Hauptstrasse liegt; "
            "von S aus senkrecht (90 Grad) zur Hauptstrasse zeichnen."
        ),
        "steps": [
            "Parallel zeichnen: Geodreieck verschieben.",
            "Senkrecht = 90 Grad, mit der Mittelmarke des Geodreiecks ausrichten.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.geometrie.vierecke"],
    },
    {
        "n": 5,
        "type": "Konstruktion Quadrat",
        "text": (
            "a) Zeichne auf der Geraden g die Strecke AB = 3 cm.\n"
            "b) Zeichne vom Punkt A aus eine senkrechte Strecke mit Länge 3 cm. "
            "Der zweite Endpunkt heißt C.\n"
            "c) Zeichne durch C eine parallele Gerade zu g.\n"
            "d) Zeichne durch B eine parallele Gerade zu AC. Der Schnittpunkt "
            "mit der Geraden durch C heißt D. Wie lang ist BD?\n"
            "e) Welche Figur hast du gezeichnet?"
        ),
        "answer": (
            "a) AB = 3 cm auf g. ; "
            "b) AC senkrecht zu g, Länge 3 cm. ; "
            "c) Parallele zu g durch C. ; "
            "d) BD = 3 cm. ; "
            "e) Ein Quadrat (Viereck mit 4 gleichen Seiten und 4 rechten Winkeln)."
        ),
        "steps": [
            "Schritt für Schritt mit Geodreieck konstruieren.",
            "AC und BD beide senkrecht und beide 3 cm -> alle Seiten gleich.",
            "Vier rechte Winkel + 4 gleiche Seiten = Quadrat.",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.geometrie.vierecke"],
    },
    {
        "n": 6,
        "type": "Kreis-Beschriftung",
        "text": (
            "Schreibe die Abkuerzungen der Fachbegriffe in die Klammer und "
            "kennzeichne mit der vorgegebenen Farbe:\n"
            "gruen: Mittelpunkt ( ___ )\n"
            "blau: Durchmesser ( ___ )\n"
            "orange: Radius ( ___ )\n"
            "Der ___ ist immer doppelt so lang wie der ___."
        ),
        "answer": (
            "gruen: Mittelpunkt (M) ; blau: Durchmesser (d) ; orange: Radius (r). ; "
            "Der Durchmesser ist immer doppelt so lang wie der Radius (d = 2r)."
        ),
        "steps": ["Standard-Abkuerzungen: M, d, r."],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse1.geometrie.formen"],
    },
    {
        "n": 7,
        "type": "Zwei Kreise und Dreieck",
        "text": (
            "Zeichne 2 ineinander liegende Kreise. Der Radius ist bei einem 1,5 cm, "
            "beim anderen das Doppelte. Der Abstand soll gleich sein. Konstruiere "
            "ein Dreieck, das den aeusseren Kreis dreimal beruehrt!"
        ),
        "answer": (
            "Innerer Kreis: r = 1,5 cm; aeusserer Kreis: r = 3 cm; "
            "gleicher Mittelpunkt M (konzentrische Kreise). "
            "Dreieck: drei Tangenten an den aeusseren Kreis - regelmaessiges "
            "(gleichseitiges) Dreieck, dessen Seiten den Kreis je einmal beruehren."
        ),
        "steps": [
            "Beide Kreise haben denselben Mittelpunkt M.",
            "Drei Beruehrpunkte gleichmaessig auf der Kreislinie verteilen (120 Grad).",
            "Tangenten zeichnen, sie schneiden sich zu einem gleichseitigen Dreieck.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.geometrie.dreiecke"],
    },
    {
        "n": 8,
        "type": "Konstruktion beschreiben",
        "text": (
            "Uebertrage die gegebene Figur und beschreibe anschliessend, wie du "
            "der Reihe nach vorgegangen bist!"
        ),
        "answer": (
            "1. Zirkel auf Radius 2 cm einstellen und einen Kreis ziehen. ; "
            "2. Mit gleichem Radius vom Mittelpunkt zwei Halbkreise ziehen. ; "
            "3. Zirkel auf halben Radius (1 cm) einstellen. ; "
            "4. Gerade durch den Mittelpunkt ziehen. ; "
            "5. Am Kreisrand einstechen und wieder zwei Halbkreise ziehen."
        ),
        "steps": ["Reihenfolge in vollstaendigen Sätzen aufschreiben."],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse1.geometrie.formen"],
    },
    {
        "n": 9,
        "type": "Parkettieren erklären",
        "text": "Parkettieren. Erklaere diesen Begriff!",
        "answer": "Parkettieren bedeutet, eine Flaeche luckenlos mit einem Muster zu befuellen.",
        "steps": ["Lueckenlos = ohne Zwischenraeume.", "Sich wiederholendes Muster."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse1.geometrie.muster"],
    },
    {
        "n": 10,
        "type": "Parkett fortsetzen / erfinden",
        "text": (
            "a) Setze die gegebene Parkettierung in alle möglichen Richtungen einmal fort.\n"
            "b) Parkettmuster können auch aus zwei verschiedenen Formen bestehen. "
            "Erfinde ein Parkett mit Sechsecken und entweder Dreiecken oder Vierecken. "
            "Zeichne es mindestens viermal."
        ),
        "answer": "Individuelle Loesungen. Wichtig: lueckenlos und ohne Ueberlappung.",
        "steps": ["Mustermass beibehalten.", "Formen sauber zeichnen."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse1.geometrie.muster"],
    },
]

NEW_KNOWLEDGE = []
