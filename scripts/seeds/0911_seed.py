EXERCISE = {
    "id": "0911",
    "subject": "Mathe",
    "grade": 4,
    "title": "Geometrie: Arbeit mit Zirkel und Geodreieck",
    "topic": "Geometrie, Zirkel, Geodreieck, Parallelen, Kreise, Sechseck, Patchwork, Streichholz-Vierlinge",
    "publisher": "CATLUX",
    "source_pdf": "0911.pdf",
    "answer_pdf": "0911 (1).pdf",
    "total_points": 40.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Lückentext Geometrie",
        "text": (
            "Ergaenze folgenden Lueckentext:\n"
            "Ein ___ hat drei Ecken. Ein Quadrat hat 4 Seiten, die alle ___ sind. "
            "Bei einem ___ liegen die gegenueberliegenden Seiten parallel zueinander. "
            "Ein 90 Grad Winkel heisst ___ Winkel. Das Zeichen || bedeutet ___. "
            "Parallelen haben ___ Schnittpunkt."
        ),
        "answer": (
            "Dreieck ; gleich lang ; Rechteck ; rechter ; parallel ; keinen."
        ),
        "steps": [
            "Dreieck = 3 Ecken.",
            "Quadrat: alle 4 Seiten gleich lang.",
            "Rechteck: gegenueberliegende Seiten parallel.",
            "90 Grad = rechter Winkel.",
            "|| bedeutet 'parallel'.",
            "Parallelen schneiden sich nie.",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.geometrie.vierecke",
            "mathe.klasse4.geometrie.dreiecke",
        ],
    },
    {
        "n": 2,
        "type": "Rechte Winkel markieren",
        "text": "Markiere alle rechten Winkel in der gegebenen Figur (Geodreieck-Bild).",
        "answer": "Alle 90 Grad Winkel werden mit dem Geodreieck geprueft und mit einem kleinen Quadrat markiert.",
        "steps": ["Geodreieck anlegen, 90 Grad pruefen, dann markieren."],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse3.geometrie.winkel"],
    },
    {
        "n": 3,
        "type": "Parallele zeichnen",
        "text": "Zeichne eine Parallele, die durch den Punkt C verlaeuft.",
        "answer": "Geodreieck an die gegebene Gerade anlegen, parallel verschieben bis zur Hoehe von C, neue Linie ziehen.",
        "steps": ["Geodreieck-Kante an Gerade legen.", "Parallel verschieben bis Punkt C.", "Linie zeichnen."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.geometrie.vierecke"],
    },
    {
        "n": 4,
        "type": "Strecke mit zwei Kreisen",
        "text": (
            "Zeichne die Strecke EF = 6 cm. Zeichne um E einen Kreis mit dem "
            "Durchmesser d = 7 cm. Zeichne um F einen Kreis mit dem Radius r = 2,5 cm."
        ),
        "answer": (
            "Strecke EF = 6 cm zeichnen. Kreis um E mit Radius 3,5 cm (d=7 cm). "
            "Kreis um F mit Radius 2,5 cm."
        ),
        "steps": [
            "Durchmesser 7 cm bedeutet Radius 3,5 cm.",
            "Zirkel auf 3,5 cm einstellen, in E einstechen.",
            "Zirkel auf 2,5 cm einstellen, in F einstechen.",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse1.geometrie.formen"],
    },
    {
        "n": 5,
        "type": "Kreisteile benennen",
        "text": "Zeichne alle Teile des Kreises ein und benenne sie!",
        "answer": "d = Durchmesser ; r = Radius (Halbmesser) ; M = Mittelpunkt ; Kreislinie und Kreisflaeche.",
        "steps": ["Mittelpunkt M einzeichnen.", "Radius r vom M zur Kreislinie.", "Durchmesser d quer durch M (= 2r)."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse1.geometrie.formen"],
    },
    {
        "n": 6,
        "type": "Geraden-Konstruktionen",
        "text": (
            "a) Zeichne drei Geraden, die sich in einem Punkt schneiden.\n"
            "b) Zeichne eine Strecke, die eine Laenge von 5 cm hat.\n"
            "c) Zeichne zwei Halbgeraden, die senkrecht aufeinander stehen.\n"
            "d) Zeichne drei Geraden, die sich in drei Punkten schneiden.\n"
            "e) Zeichne drei Geraden, die zueinander parallel liegen."
        ),
        "answer": (
            "a) Drei Linien durch einen gemeinsamen Schnittpunkt. ; "
            "b) Strecke A--B mit Laenge 5 cm. ; "
            "c) Zwei Halbgeraden im 90 Grad Winkel zueinander. ; "
            "d) Drei Geraden in Dreiecksform (jede schneidet die anderen). ; "
            "e) Drei Geraden ohne Schnittpunkte, alle parallel zueinander."
        ),
        "steps": [
            "Halbgerade hat Anfangspunkt + unendliches Ende.",
            "Senkrecht = rechter Winkel = 90 Grad.",
            "Drei Schnittpunkte: jede Gerade schneidet die anderen einmal.",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.geometrie.vierecke"],
    },
    {
        "n": 7,
        "type": "Sechseck und Stern",
        "text": "Zeichne in den ersten Kreis ein regelmaessiges Sechseck. Zeichne in den zweiten Kreis einen sechseckigen Stern.",
        "answer": (
            "Sechseck: Zirkel auf Radius des Kreises lassen, vom Kreisrand "
            "ausgehend sechsmal abtragen, Punkte verbinden. ; "
            "Stern: dieselben sechs Punkte verwenden, aber jeweils ueberspringen "
            "(Punkt 1->3->5->1, Punkt 2->4->6->2)."
        ),
        "steps": [
            "Bei Sechseck-Konstruktion: Radius = Seitenlaenge.",
            "6 gleiche Punkte auf der Kreislinie abtragen.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse1.geometrie.formen"],
    },
    {
        "n": 8,
        "type": "Patchwork-Decke",
        "text": (
            "Lisa moechte fuer ihren Puppenwagen eine Patchwork-Decke in Form "
            "eines Quadrates naehen. Sie braucht gleichgrosse Stoffquadrate "
            "(Seitenlaenge 8 cm). Sie hat 48 Quadrate fuer den aeusseren Rand "
            "der Decke zugeschnitten.\n"
            "a) Aus wievielen Stoffquadraten besteht jede Seite der Decke?\n"
            "b) Wieviele Stoffquadrate muss Lisa noch zuschneiden, um die "
            "fertige Decke zu erhalten?\n"
            "c) Wie breit ist die fertige Decke?"
        ),
        "answer": (
            "a) 48 - 4 (Eckquadrate doppelt) = 44 ; 44 / 4 = 11 ; "
            "11 + 2 Ecken = 13 Quadrate je Seite. ; "
            "b) 11 x 11 = 121 weitere Quadrate fuer das Innere. ; "
            "c) 13 x 8 cm = 104 cm breit."
        ),
        "steps": [
            "Rand-Quadrate: 4 Ecken werden doppelt gezaehlt -> 48 - 4 = 44.",
            "44 / 4 Seiten = 11 Mittelquadrate je Seite.",
            "Mit den 2 Ecken pro Seite: 11 + 2 = 13 Quadrate Seitenlaenge.",
            "Innenflaeche ist (13 - 2) x (13 - 2) = 11 x 11 = 121.",
            "Breite = 13 x 8 cm = 104 cm.",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse4.geometrie.flaeche"],
    },
    {
        "n": 9,
        "type": "Streichholz-Vierlinge",
        "text": (
            "a) Vergleiche die Streichholz-Vierlinge. Welche gehoeren zusammen?\n"
            "b) Wenn du am 'Start-Vierling' ein Streichholz umlegst, welche "
            "Streichholz-Vierlinge kannst du erzeugen? Kreuze an.\n"
            "c) Bei jedem Vierling laesst sich durch Umlegen eines Streichholzes "
            "ein anderer Vierling erzeugen. Drehen erlaubt, spiegeln nicht. "
            "Nummeriere die Karten in der richtigen Reihenfolge."
        ),
        "answer": (
            "a) 4 Karten gehoeren zusammen (durch Drehen identisch). ; "
            "b) 3 erreichbare Folge-Vierlinge angekreuzt. ; "
            "c) Reihenfolge: 5 - 2 - 4 - 3."
        ),
        "steps": [
            "Drehen: gleiche Form, andere Lage = gehoeren zusammen.",
            "Spiegeln zaehlt nicht als gleich.",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": ["mathe.klasse1.geometrie.muster"],
    },
]

NEW_KNOWLEDGE = []
