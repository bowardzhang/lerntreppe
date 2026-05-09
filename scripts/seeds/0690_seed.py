EXERCISE = {
    "id": "0690",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Der Affe als Schiedsrichter",
    "topic": "Leseverstehen, Fabel, Affe, Hund, Fuchs, Wurst, Streit",
    "publisher": "CATLUX",
    "source_pdf": "0690.pdf",
    "answer_pdf": "0690 (1).pdf",
    "total_points": 31.0,
}

LESETEXT = (
    "Der Affe als Schiedsrichter\n\n"
    "Ein Hund und ein Fuchs erblickten gleichzeitig eine schöne große Wurst, die "
    "jemand auf dem Weg verloren hatte.\n\n"
    "'Sie gehört mir!', rief der Fuchs. 'Nein, sie gehört mir!', schrie der Hund. "
    "Jeder bekam ein Ende zu fassen. Böse sahen sie sich an, wollte doch jeder das "
    "größere Stück fassen. Nachdem sie eine Weile unentschieden darum gekämpft "
    "hatten, beschlossen sie, mit der Beute zum klugen Affen zu gehen. Sein "
    "Schiedsspruch sollte gültig sein.\n\n"
    "'Warum streitet ihr?', fragte der Affe sie. 'Wir haben eine Wurst und wissen "
    "nicht, wie wir sie teilen sollen\", erklärten der Hund und der Fuchs. 'Das ist "
    "ganz einfach, ich werde sie teilen, rief der Affe.\" 'Kommt mit mir nach Hause. "
    "Ich habe eine Waage. Wir wollen jedem ehrlich seine Hälfte abwiegen.\" Dann "
    "zerbrach der Affe die Wurst und legte die beiden Teile auf die Waage. 'Oh "
    "weh\", rief er dann, 'das eine Stück ist schwerer!'. Er packte das Stück und "
    "biss kräftig hinein. Dann legte er es wieder auf die Waage und er wog die "
    "Stücke von neuem. Da senkte sich die andere Waagschale. Nun war das andere "
    "Stück zu schwer. Happ-schnapp, kürzte er auch diesen Teil. Nun war das andere "
    "Stück zu schwer. Da musste der Affe auch hier wieder ein Stück abbeißen. Das "
    "ging so lange hin und her, denn der Affe versuchte weiterhin jedem zu seinem "
    "rechtmäßigen Teil zu verhelfen. Die Enden wurden dabei immer kleiner und die "
    "Augen von Hund und Fuchs immer größer. Schließlich, rutsch-futsch, war auch "
    "der Rest hier und dort verschlungen. Die ganze Wurst war vom Affen "
    "aufgefressen worden. Mit eingezogenen Ruten schlichen Hund und Fuchs in "
    "verbissener Wut davon. In gehöriger Entfernung fielen sie beide übereinander "
    "her und zerzausten sich das Fell."
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Streitende Tiere benennen",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Wer stritt um die verlorene Wurst? Schreibe auf!"
        ),
        "answer": "Ein Hund und ein Fuchs stritten sich um die verlorene Wurst.",
        "steps": ["Aus dem ersten Absatz."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 2,
        "type": "Frage des Affen",
        "text": "Was fragte der Affe die beiden Tiere, als er ihnen begegnete?",
        "answer": "Der Affe fragte die Tiere, warum sie streiten.",
        "steps": ["'Warum streitet ihr?', fragte der Affe sie."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 3,
        "type": "Vorschlag des Affen",
        "text": "Welchen Vorschlag machte der Affe, um den Streitfall zu lösen? Schreibe auf.",
        "answer": (
            "Der Affe schlug vor, nach Hause zu gehen und die Wurst zu teilen "
            "und mit der Waage abzuwiegen."
        ),
        "steps": ["'Kommt mit mir nach Hause. Ich habe eine Waage.'"],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 4,
        "type": "Erste Wägung",
        "text": "Was stellte der Affe fest, als er die beiden Wursthälften zum ersten Mal wog?",
        "answer": "Der Affe stellte fest, dass das eine Stück schwerer war als das andere Stück.",
        "steps": ["'das eine Stück ist schwerer!'"],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 5,
        "type": "Trick beschreiben",
        "text": "Mit welchem Trick überlistete der Affe die beiden Streithähne. Beschreibe genau!",
        "answer": (
            "Er überlistete sie, indem er erst von der einen Wurst abgebissen hat "
            "und dann wieder von der anderen. Dies ging so lange, bis die ganze "
            "Wurst aufgegessen war."
        ),
        "steps": ["Wechselseitiges Abbeißen, bis nichts mehr übrig war."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 6,
        "type": "Sätze im Text erkennen",
        "text": (
            "Welche Sätze stehen genauso im Text? Kreuze an!\n"
            "(1) Sein Urteil sollte gültig sein.\n"
            "(2) Kommt mit mir nach Hause.\n"
            "(3) Nun war das andere Stück zu schwer.\n"
            "(4) Er packte das Stück und biss hinein."
        ),
        "answer": (
            "Richtig: (2) und (3). ; "
            "(1) falsch: im Text 'Sein Schiedsspruch sollte gültig sein.' ; "
            "(4) falsch: im Text 'Er packte das Stück und biss kräftig hinein.'"
        ),
        "steps": ["Genauen Wortlaut prüfen."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 7,
        "type": "Adjektiv zum Verhalten",
        "text": (
            "Nenne je ein passendes Adjektiv für das Verhalten der Tiere und begründe!\n"
            "Hund und Fuchs:\n"
            "Affe:"
        ),
        "answer": (
            "Hund und Fuchs: Sie sind dumm, denn sie lassen sich vom Affen "
            "überlisten (austricksen). ; "
            "Affe: Der Affe ist schlau (klug), denn er überlistet beide und hat "
            "am Ende die ganze Wurst gegessen."
        ),
        "steps": ["Charakter der Tiere aus dem Verhalten ableiten."],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 8,
        "type": "Synonyme suchen",
        "text": (
            "Suche die Wörter im Text, die du durch folgende Wörter ersetzen "
            "könntest und schreibe sie auf!\n"
            "herzhaft: ___\n"
            "weiter: ___"
        ),
        "answer": (
            "herzhaft → kräftig ; "
            "weiter → weiterhin (im Text Z. 18: 'der Affe versuchte weiterhin')."
        ),
        "steps": ["Synonyme im Text finden."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 9,
        "type": "Wort ersetzen",
        "text": (
            "'In gehöriger Entfernung fielen sie beide übereinander her und "
            "zerzausten sich das Fell.\"\n"
            "Ersetze 'gehöriger' durch ein anderes passendes Wort!"
        ),
        "answer": "Z. B.: sicherer, ausreichender, ordentlicher.",
        "steps": ["Bedeutung 'ausreichend, angemessen'."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 10,
        "type": "Gegenteile finden",
        "text": (
            "Finde immer das Wort, das das Gegenteil bedeutet im Text. "
            "Gib die Zeile an!\n"
            "dumm → ___\n"
            "leicht → ___\n"
            "ungültig → ___"
        ),
        "answer": (
            "dumm → klugen (Z. 6) ; "
            "leicht → schwerer (Z. 13) ; "
            "ungültig → gültig (Z. 7)."
        ),
        "steps": ["Antonyme im Text suchen."],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 11,
        "type": "Wortarten unterstreichen",
        "text": (
            "Unterstreiche in der Geschichte 2 Nomen (grün), 2 Verben (blau) "
            "und 2 Adjektive (gelb)."
        ),
        "answer": (
            "Z. B.: Nomen: Wurst, Fell, Augen. ; "
            "Verben: verhelfen, fassen, abwiegen. ; "
            "Adjektive: schöne, große, klugen."
        ),
        "steps": ["Verschiedene Wortarten im Text identifizieren."],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 12,
        "type": "Textsorte und Moral",
        "text": (
            "(a) Du weißt sicher, wie man diese Art der Geschichten nennt. Schreibe auf!\n"
            "(b) Warum handelt es sich um diese bestimmte Textsorte? Schreibe zwei "
            "Merkmale auf und je ein Beispiel aus der Geschichte dazu!\n"
            "(c) Du kennst sicher noch mindestens zwei weitere Geschichten, die man "
            "dieser Textform zuordnen kann. Schreibe sie auf!\n"
            "(d) Meistens kann man aus dieser Art von Geschichten etwas lernen. "
            "Was meinst du, ist es in dieser Geschichte? "
            "Begründe deine Meinung mit eigenen Worten (Satz)!"
        ),
        "answer": (
            "(a) Fabel. ; "
            "(b) Die Tiere können sprechen und denken: 'Sie gehört mir!', rief der Fuchs. ; "
            "Die handelnden Personen sind Tiere: der Affe, der Hund und der Fuchs. ; "
            "Die Tiere haben menschliche Eigenschaften: schlichen in verbissener Wut davon. ; "
            "(c) Z. B.: Zwei Frösche in der Milch, Der Panther in der Grube, Der Fuchs "
            "und die Gänse. ; "
            "(d) Wenn zwei sich streiten, freut sich der Dritte."
        ),
        "steps": [
            "(a) Fabel.",
            "(b) Merkmale: Tiere, Sprechen, Moral.",
            "(c) Bekannte Fabeln nennen.",
            "(d) Sprichwort als Moral.",
        ],
        "points": 8.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
]

NEW_KNOWLEDGE = []
