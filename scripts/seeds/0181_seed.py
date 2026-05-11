EXERCISE = {
    "id": "0181",
    "subject": "HSU",
    "grade": 4,
    "title": "Lernzielkontrolle: Abwasser, Kläranlage",
    "topic": "Abwasser, Kläranlage, Wasserreinigung, Trinkwasser",
    "publisher": "CATLUX",
    "source_pdf": "0181.pdf",
    "answer_pdf": "0181 (1).pdf",
    "total_points": 44.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Beschriften Kläranlage",
        "text": (
            "Abwasser fliesst durch die Kanalisation in die Kläranlage. "
            "Beschrifte die Zeichnung mit den richtigen Fachbegriffen "
            "(8 Stationen)."
        ),
        "answer": (
            "1. Kanaleinlauf mit Hebewerk\n"
            "2. Grobrechen\n"
            "3. Sandfang\n"
            "4. Vorklärbecken\n"
            "5. Belebungsbecken\n"
            "6. Nachklärbecken\n"
            "7. Faulbehaelter\n"
            "8. Schlammtrockenbeet"
        ),
        "steps": ["Reihenfolge der Kläranlage durchgehen."],
        "points": 8.0,
        "has_image": True,
        "image": "0181_q1_beschriften_klranlage.png",
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 2,
        "type": "Belebungsbecken",
        "text": (
            "Ein wichtiges Reinigungsbecken ist das Belebungsbecken. "
            "Welchen Namen für dieses Becken kennst du noch? "
            "Was geschieht in diesem Becken? Erklaere genau!"
        ),
        "answer": (
            "Anderer Name: Belüftungsbecken.\n"
            "Im Belebungsbecken fressen winzige Bakterien Schmutzteilchen "
            "und wandeln so den Schmutz in Klärschlamm um. Die Bakterien "
            "benoetigen Sauerstoff zum Leben. Dieser wird in das Becken "
            "geblasen. Deshalb auch Belüftungsbecken genannt."
        ),
        "steps": ["Funktion der Bakterien erklaeren.", "Sauerstoffzufuhr erwaehnen."],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 3,
        "type": "Zusatzbecken moderne Kläranlage",
        "text": (
            "Moderne Kläranlagen benoetigen oft noch ein zusaetzliches "
            "Becken. Wie heißt dieses Becken und was geschieht in diesem Becken?"
        ),
        "answer": (
            "Chemische Reinigungsstufe. In diesem Becken werden Chemikalien, "
            "Gifte und Salze entfernt."
        ),
        "steps": ["Dritte Reinigungsstufe nennen."],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 4,
        "type": "Wasserverschmutzung",
        "text": "Wodurch wird das Wasser verschmutzt und was kann man dagegen tun?",
        "answer": (
            "- beim Waeschewaschen: mit dem Waschpulver sparen, keinen "
            "Weichspueler verwenden\n"
            "- beim Autowaschen: nur auf ausgewiesenen Plaetzen\n"
            "- durch Medikamente im Abfluss: Gifte treten aus, alte "
            "Medikamente im Hausmuell entsorgen"
        ),
        "steps": ["Mindestens drei Beispiele mit Loesung nennen."],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 5,
        "type": "Gefahren für Grundwasser",
        "text": (
            "Betrachte die Bilder! Beschreibe, warum hier Gefahren für das "
            "Grundwasser entstehen und nenne Folgen, die bald danach "
            "eintreten können (in Sätzen)."
        ),
        "answer": (
            "Wenn Oel in Gewässer laeuft, kann das ökologische "
            "Gleichgewicht gestoert werden. Das Wasser kann umkippen. Wenn "
            "das Oel in das Grundwasser eindringt und wir es trinken, "
            "können wir uns selbst vergiften.\n"
            "Wenn Pflanzenschutzmittel in das Grundwasser eindringt und wir "
            "oder Lebewesen davon trinken oder darin schwimmen, können wir "
            "krank werden. Das Wasser in den Blättern der Pflanzen "
            "verdunstet und steigt auf. Das Gift kommt mit dem Regen wieder "
            "herunter und gelangt ins Grundwasser."
        ),
        "steps": ["Oel und Pflanzenschutzmittel als Beispiele nennen.", "Folgen für Mensch und Natur erklaeren."],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 6,
        "type": "Gründe Gefahr Wasserverschmutzung",
        "text": "Nenne 3 Gründe, warum Wasserverschmutzung so gefaehrlich ist!",
        "answer": (
            "1. Trinkwasser (Grundwasser) wird auch verschmutzt.\n"
            "2. Baden in Fluessen und Seen ist gesundheitsschaedlich.\n"
            "3. Fische können in verschmutzten Gewässern sterben."
        ),
        "steps": ["Drei verschiedene Gründe nennen."],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 7,
        "type": "Abwasser vs. Regenwasser",
        "text": (
            "a) Warum muss Abwasser erst in der Kläranlage gereinigt "
            "werden, bevor es in Gewässer zurückgeleitet wird?\n"
            "b) Erklaere, warum Regenwasser ohne Klaerung weitergeleitet "
            "werden darf."
        ),
        "answer": (
            "a) Abwasser ist durch viele Dinge (Abfall, Chemikalien, "
            "Schmutzstoffe etc.) stark verunreinigt. Wuerde man dieses "
            "Abwasser ungereinigt in die Gewässer leiten, haette dies "
            "schaedliche Folgen für die Natur, Tiere und schließlich für "
            "den Menschen selbst (Grundwasser!).\n"
            "b) Das Regenwasser wird von uns Menschen nicht verschmutzt und "
            "enthaelt somit keine Schadstoffe wie das Abwasser. Deshalb "
            "kann es ohne Reinigung in die Natur geleitet werden."
        ),
        "steps": ["Verunreinigung Abwasser erklaeren.", "Sauberkeit Regenwasser begruenden."],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 8,
        "type": "Lueckentext Kläranlage",
        "text": "Ergaenze die Luecken in den folgenden Sätzen sinnvoll.",
        "answer": (
            "Im Sandfang wird Sand und Oel mit einem Räumer entfernt. Im "
            "Vorklärbecken werden feine Teilchen entfernt. Im Grobrechen "
            "sammeln sich alle Abwaesser. Mit dem Grobrechen entfernt man "
            "grobe Schmutzteile. Im Nachklärbecken setzt sich der "
            "restliche Schlamm am Boden ab und wird mit dem Schieber "
            "entfernt. Im Belüftungsbecken werden Bakterien und "
            "Sauerstoff zugefuegt."
        ),
        "steps": ["Funktionen der einzelnen Becken kennen."],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 9,
        "type": "Wasserentsorgungsverfahren",
        "text": (
            "a) Wie heißen die beiden Verfahren zur Wasserentsorgung aus "
            "den Wohnhaeusern?\n"
            "b) Erklaere die beiden Verfahren."
        ),
        "answer": (
            "a) Mischverfahren und Trennverfahren.\n"
            "b) Mischverfahren: Beim Mischverfahren fliessen Abwasser und "
            "Regenwasser zusammen in einer Leitung zur Kläranlage. "
            "Trennverfahren: Beim Trennverfahren fliessen Abwasser und "
            "Regenwasser jeweils in einer eigenen Leitung. Das Regenwasser "
            "wird in nahegelegene Gewässer geleitet. Das Abwasser wird in "
            "die Kläranlage geleitet."
        ),
        "steps": ["Beide Verfahrennamen nennen.", "Unterschied erklaeren."],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 10,
        "type": "Trinkwasserquellen",
        "text": "Woher bekommen wir unser Trinkwasser? Nenne 4 Möglichkeiten!",
        "answer": (
            "Aus Seen, Fluessen, Baechen, vom Grundwasser, Regenwasser, "
            "vom entsalzten Meer."
        ),
        "steps": ["Vier Wasserquellen aufzaehlen."],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.gewaesser"],
    },
]

NEW_KNOWLEDGE = []
