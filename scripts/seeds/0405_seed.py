EXERCISE = {
    "id": "0405",
    "subject": "Deutsch",
    "grade": 4,
    "title": "2. Lernzielkontrolle: 4 Fälle, Satzglieder",
    "topic": "Kasus (Nominativ, Genitiv, Dativ, Akkusativ), Satzgegenstand und Satzaussage",
    "publisher": "CATLUX",
    "source_pdf": "0405.pdf",
    "answer_pdf": "0405 (1).pdf",
    "total_points": 47.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Lateinische Begriffe der Fälle",
        "text": (
            "Schreibe den lateinischen Begriff für die Fälle auf. Notiere "
            "dahinter, wie du genau nach dem Fall fragst!\n"
            "1. Fall = ___    Frage: ___\n"
            "2. Fall = ___    Frage: ___\n"
            "3. Fall = ___    Frage: ___\n"
            "4. Fall = ___    Frage: ___"
        ),
        "answer": (
            "1. Nominativ (Wer oder was?) ; "
            "2. Genitiv (Wessen?) ; "
            "3. Dativ (Wem?) ; "
            "4. Akkusativ (Wen oder was?)"
        ),
        "steps": [
            "1. Fall = Nominativ — Frage 'Wer oder was?'",
            "2. Fall = Genitiv — Frage 'Wessen?'",
            "3. Fall = Dativ — Frage 'Wem?'",
            "4. Fall = Akkusativ — Frage 'Wen oder was?'",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.kasus",
        ],
    },
    {
        "n": 2,
        "type": "Nomen 'der Junge' im richtigen Fall",
        "text": (
            "Setze 'der Junge' in der richtigen Form ein und notiere den Fall.\n"
            "___ kommt zu Sandras Geburtstag. (___)\n"
            "Sandra begrüßt ___ herzlich. (___)\n"
            "Sie bringt ___ ein Glas Saft. (___)\n"
            "Das Geschenk ___ gefällt Sandra gut. (___)"
        ),
        "answer": (
            "Der Junge kommt … (1. Fall) ; "
            "Sandra begrüßt den Jungen … (4. Fall) ; "
            "Sie bringt dem Jungen … (3. Fall) ; "
            "Das Geschenk des Jungen gefällt … (2. Fall)"
        ),
        "steps": [
            "Subjekt → Nominativ (1. Fall): Der Junge.",
            "Akkusativobjekt nach 'begrüßen' (Wen?) → 4. Fall: den Jungen.",
            "Dativobjekt nach 'bringen' (Wem?) → 3. Fall: dem Jungen.",
            "Genitivattribut zu 'Geschenk' (Wessen?) → 2. Fall: des Jungen.",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.kasus",
        ],
    },
    {
        "n": 3,
        "type": "Fall der unterstrichenen Wörter bestimmen",
        "text": (
            "Schreibe den richtigen Fall hinter das Wort.\n"
            "Die Schwester (___) meines Klassenkameraden (___) lieh ihrer "
            "Freundin (___) das Fahrrad (___) zum Heimfahren.\n"
            "Den Eltern (___) des Mädchens (___) gefiel das Mountainbike (___). "
            "So riefen sie gleich den Fahrradhändler (___) an."
        ),
        "answer": (
            "Schwester = 1. Fall ; Klassenkameraden = 2. Fall ; "
            "Freundin = 3. Fall ; Fahrrad = 4. Fall ; "
            "Eltern = 3. Fall ; Mädchens = 2. Fall ; "
            "Mountainbike = 1. Fall ; Fahrradhändler = 4. Fall"
        ),
        "steps": [
            "Schwester = Subjekt → 1. Fall.",
            "meines Klassenkameraden = Genitivattribut → 2. Fall.",
            "ihrer Freundin = Dativobjekt von 'leihen' → 3. Fall.",
            "das Fahrrad = Akkusativobjekt → 4. Fall.",
            "Den Eltern = Dativobjekt von 'gefallen' → 3. Fall.",
            "des Mädchens = Genitivattribut → 2. Fall.",
            "das Mountainbike = Subjekt → 1. Fall.",
            "den Fahrradhändler = Akkusativobjekt → 4. Fall.",
        ],
        "points": 8.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.kasus",
        ],
    },
    {
        "n": 4,
        "type": "Satzglieder farbig unterstreichen",
        "text": (
            "Unterstreiche im Text richtig (Satzaussage rot, 1. Fall blau, "
            "2. Fall orange, 3. Fall gelb, 4. Fall grün):\n\n"
            "Die Klassenfahrt war super. Marias Streiche waren sehr lustig "
            "und Karims Grimassen waren einfach herrlich. Aber auch die "
            "Ideen der Lehrer waren toll. Die Stimmung der Kinder war prima. "
            "Martin hatte einen Fotoapparat dabei. Damit schoss er viele "
            "Schnappschüsse von seinen Freunden. Die Kinder versteckten "
            "auch einmal die Schuhe der Lehrerin."
        ),
        "answer": (
            "1. Fall (Subjekte): Die Klassenfahrt; Marias Streiche; "
            "Karims Grimassen; die Ideen; Die Stimmung; Martin; er; Die Kinder. "
            "2. Fall (Genitiv): der Lehrer; der Kinder; der Lehrerin. "
            "3. Fall (Dativ): von seinen Freunden. "
            "4. Fall (Akkusativ): einen Fotoapparat; viele Schnappschüsse; "
            "die Schuhe. "
            "Satzaussage: war (super); waren (lustig); waren (herrlich); waren (toll); "
            "war (prima); hatte (dabei); schoss; versteckten."
        ),
        "steps": [
            "Subjekte (1. Fall) im Nominativ erkennen.",
            "Genitivattribute (2. Fall) erkennt man durch 'Wessen?'.",
            "Dativ (3. Fall) durch 'Wem?', Akkusativ (4. Fall) durch 'Wen/was?'.",
            "Satzaussagen sind die finiten Verben der Sätze.",
        ],
        "points": 12.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.kasus",
            "deutsch.klasse4.grammatik.satzglieder",
        ],
    },
    {
        "n": 5,
        "type": "Frage stellen und Fall bestimmen",
        "text": (
            "Stelle die passende Frage zum unterstrichenen Satzglied und "
            "bestimme den Fall.\n"
            "1. Martina hat viele Kinder zu ihrer Geburtstagsfeier eingeladen. "
            "(viele Kinder)\n"
            "2. Mutter serviert den Gästen einen leckeren Kuchen. (den Gästen)\n"
            "3. Martins Jacke liegt auf dem Boden. (Martins)\n"
            "4. Allen Jungen und Mädchen gefällt die Geburtstagsfeier sehr. "
            "(die Geburtstagsfeier)"
        ),
        "answer": (
            "1. 'Wen oder was hat Martina eingeladen?' → 4. Fall (Akkusativ). "
            "2. 'Wem serviert Mutter einen Kuchen?' → 3. Fall (Dativ). "
            "3. 'Wessen Jacke liegt auf dem Boden?' → 2. Fall (Genitiv). "
            "4. 'Wer oder was gefällt allen Jungen und Mädchen?' → 1. Fall (Nominativ)."
        ),
        "steps": [
            "1. Wen/was? → Akkusativ (4. Fall).",
            "2. Wem? → Dativ (3. Fall).",
            "3. Wessen? → Genitiv (2. Fall).",
            "4. Wer/was? → Nominativ (1. Fall).",
        ],
        "points": 8.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.kasus",
            "deutsch.klasse4.grammatik.satzglieder",
        ],
    },
    {
        "n": 6,
        "type": "Wörter im richtigen Fall einsetzen",
        "text": (
            "Setze die Wörter in Klammern im richtigen Fall ein.\n"
            "Carolin gibt ___ die Jacke. (Freundin)\n"
            "Schnell holt Vater ___. (Staubsauger)\n"
            "___ hat sich zum Glück nicht beschwert. (Nachbar)\n"
            "Für Carina war das der schönste Tag ___. (Jahr)\n"
            "Bald ist ___ wieder aufgeräumt. (Kinderzimmer)"
        ),
        "answer": (
            "Carolin gibt ihrer Freundin die Jacke. (3. Fall) ; "
            "Schnell holt Vater den Staubsauger. (4. Fall) ; "
            "Der Nachbar hat sich … nicht beschwert. (1. Fall) ; "
            "… der schönste Tag des Jahres. (2. Fall) ; "
            "Bald ist das Kinderzimmer wieder aufgeräumt. (1. Fall)"
        ),
        "steps": [
            "geben + Wem? → Dativ: ihrer Freundin (3. Fall).",
            "holen + Wen/was? → Akkusativ: den Staubsauger (4. Fall).",
            "Subjekt → Nominativ: Der Nachbar (1. Fall).",
            "Wessen? → Genitiv: des Jahres (2. Fall).",
            "Subjekt → Nominativ: das Kinderzimmer (1. Fall).",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.kasus",
        ],
    },
    {
        "n": 7,
        "type": "Sätze mit Wort im richtigen Fall bilden",
        "text": (
            "Bilde mit dem Wort im richtigen Fall einen Satz.\n"
            "Schullandheim (4. Fall): ___\n"
            "Schildkröte (2. Fall): ___\n"
            "Sternwarte (1. Fall): ___\n"
            "Opa (3. Fall): ___"
        ),
        "answer": (
            "Beispiele: Die Klasse besucht das Schullandheim. ; "
            "Der Panzer der Schildkröte ist hart. ; "
            "Die Sternwarte hat heute geöffnet. ; "
            "Ich schenke Opa ein Buch."
        ),
        "steps": [
            "4. Fall: 'Wen/was besucht die Klasse?' → das Schullandheim.",
            "2. Fall: 'Wessen Panzer ist hart?' → der Schildkröte.",
            "1. Fall: Subjekt = Die Sternwarte.",
            "3. Fall: 'Wem schenke ich ein Buch?' → Opa.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.kasus",
        ],
    },
]

NEW_KNOWLEDGE = []
