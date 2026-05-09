EXERCISE = {
    "id": "0712",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Eulenspiegel will fliegen (Schwank)",
    "topic": "Leseverstehen, Schwank, Till Eulenspiegel, Magdeburg, Toren",
    "publisher": "CATLUX",
    "source_pdf": "0712.pdf",
    "answer_pdf": "0712 (1).pdf",
    "total_points": 33.0,
}

LESETEXT = (
    "Wie Eulenspiegel vorgab, dass er zu Magdeburg vom Balkon des Rathauses fliegen wollte\n\n"
    "An einem warmen Sommertag kam Eulenspiegel nach Magdeburg und kündigte an, "
    "dass er wie ein Vogel vom Balkon des Rathauses fliegen werde. Wie ein "
    "Lauffeuer verbreitete sich die Nachricht in der Stadt. Alt und Jung fand "
    "sich zur rechten Zeit auf dem Marktplatz ein, um dem Schauspiel "
    "beizuwohnen. Eulenspiegel traf dann auch seine Vorbereitungen, kletterte "
    "auf den Balkon und bewegte seine Arme, als ob er sogleich fliegen werde. "
    "Die Leute rissen Mund und Augen auf, guckten angespannt nach oben in der "
    "Annahme, dass er bald so weit wäre.\n\n"
    "Da lachte der Eulenspiegel und sprach: 'Ich glaubte, es gäbe in der Welt "
    "außer mir keine Toren und Narren. Jetzt sehe ich ein, dass hier die ganze "
    "Stadt voller Toren ist. Wenn ihr mir gesagt hättet, dass ihr fliegen "
    "wollt, ich hätte es nicht geglaubt. Ihr aber schenkt mir als einem Toren "
    "Glauben. Wie sollte ich denn fliegen können? Ich bin doch kein Vogel, "
    "habe keine Schwingen. Doch ohne sie und ohne Federn, das sollt ihr doch "
    "wissen, kann niemand fliegen. Nun könnt ihr ermessen, wie sehr ich euch "
    "zum Narren gehalten habe.\"\n\n"
    "Schnell stieg er hinunter auf die ebene Erde und lief von dannen. Das "
    "verblüffte Volk aber blieb – teils fluchend, teils lachend – zurück. "
    "'Das ist fürwahr ein Schalksnarr!', sagten sie, 'doch er hat die Wahrheit "
    "gesprochen!\" (Volksgut)"
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Textgattung und Merkmale",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Zu welcher Textgattung gehört die Geschichte?\n"
            "(a) Gedicht (b) Fabel (c) Schwank (d) Sachtext\n"
            "Nenne 4 verschiedene Merkmale dieser Textgattung."
        ),
        "answer": (
            "Richtig: (c) Schwank. ; "
            "Merkmale (4 davon): kurze Erzählung; komische Situation; ein Schelm "
            "überlistet andere; dumme Person wird betrogen; mehrere Lügen; "
            "witziger oder überraschender Schluss (Pointe); ungleiche Figuren."
        ),
        "steps": ["Schwank: kurze, witzige Geschichte mit Pointe."],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 2,
        "type": "Lückentext Aussehen",
        "text": (
            "Beschreibe das Aussehen von Till Eulenspiegel. Ergänze die Lücken!\n"
            "Eulenspiegel trägt eine Narrenkappe mit ___.\n"
            "___ mit Schellen und ein buntes ___."
        ),
        "answer": (
            "Eulenspiegel trägt eine Narrenkappe mit Schellen. "
            "Schuhe mit Schellen und ein buntes Hemd."
        ),
        "steps": ["Typische Narrenkleidung beschreiben."],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 3,
        "type": "Schauplatz",
        "text": "In welcher Stadt und an welchem Schauplatz spielt diese Geschichte?",
        "answer": "Auf dem Balkon des Rathauses von Magdeburg.",
        "steps": ["Aus dem ersten Satz."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 4,
        "type": "Jahreszeit ankreuzen",
        "text": (
            "In welcher Jahreszeit und bei welcher Witterung spielt diese Geschichte?\n"
            "(a) An einem windigen Sommertag\n"
            "(b) An einem warmen Herbsttag\n"
            "(c) An einem armen Sommertag\n"
            "(d) An einem warmen Sommertag"
        ),
        "answer": "Richtig: (d) An einem warmen Sommertag.",
        "steps": ["Erster Satz: 'An einem warmen Sommertag'."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 5,
        "type": "Wortbedeutung 'Toren'",
        "text": (
            "Till Eulenspiegel sprach: 'Ich glaubte, es gäbe in der Welt außer mir "
            "keine Toren und Narren.\" Was bedeutet 'Toren'?\n"
            "(a) Türen (b) Dummköpfe (c) Tore (d) Helden"
        ),
        "answer": "Richtig: (b) Dummköpfe.",
        "steps": ["Tor = Dummkopf, Narr."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 6,
        "type": "Textstellen finden",
        "text": (
            "Finde zu folgenden Aussagen die passende Stelle im Text und schreibe "
            "sie auf. Gib die Zeilen dazu an!\n"
            "(a) Till Eulenspiegel macht in Magdeburg eine besondere Ankündigung.\n"
            "(b) Eulenspiegel erklärt, warum er nicht fliegen kann.\n"
            "(c) Das Volk bleibt verblüfft zurück und zeigt verschiedene Reaktionen."
        ),
        "answer": (
            "(a) Z. 1–2: 'An einem warmen Sommertag kam Eulenspiegel nach Magdeburg "
            "und kündigte an, dass er wie ein Vogel vom Balkon des Rathauses "
            "fliegen werde.' ; "
            "(b) Z. 14–15: 'Ich bin doch kein Vogel, habe keine Schwingen. Doch "
            "ohne sie und ohne Federn, das sollt ihr doch wissen, kann niemand "
            "fliegen.' ; "
            "(c) Z. 18–19: 'Das verblüffte Volk aber blieb – teils fluchend, teils "
            "lachend – zurück. 'Das ist fürwahr ein Schalksnarr!', sagten sie, "
            "'doch er hat die Wahrheit gesprochen!''"
        ),
        "steps": ["Drei Textstellen mit Zeilenangaben."],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 7,
        "type": "Wendung 'von dannen'",
        "text": (
            "Nach seinem Streich lief Till Eulenspiegel 'von dannen'. Was bedeutet "
            "diese Formulierung?\n"
            "(a) Vom Donner gerührt sein\n"
            "(b) Von dort weglaufen\n"
            "(c) Dann weglaufen\n"
            "(d) Sich von Tannen entfernen"
        ),
        "answer": "Richtig: (b) Von dort weglaufen.",
        "steps": ["'von dannen' = von dort weg."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 8,
        "type": "Textstellen Schwächen",
        "text": (
            "Schreibe die Textstellen heraus, in denen Eulenspiegel die Schwächen "
            "der Menschen aufzeigt!\n"
            "Leichtgläubigkeit:\n"
            "Dummheit:\n"
            "Sensationsgier:"
        ),
        "answer": (
            "Leichtgläubigkeit (Z. 13): 'Ihr aber schenkt mir als einem Toren Glauben.' ; "
            "Dummheit (Z. 11–12): 'Jetzt sehe ich ein, dass hier die ganze Stadt voller Toren ist.' ; "
            "Sensationsgier (Z. 7–9): 'Die Leute rissen Mund und Augen auf, guckten "
            "angespannt nach oben in der Annahme, dass er bald soweit wäre.'"
        ),
        "steps": ["Drei verschiedene menschliche Schwächen finden."],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 9,
        "type": "Reaktionen ankreuzen",
        "text": (
            "Wie reagieren die Magdeburger auf Eulenspiegels Streich? Kreuze an!\n"
            "(a) weinen (b) fluchen (c) sind sprachlos (d) lachen "
            "(e) sind verblüfft (f) verfolgen ihn"
        ),
        "answer": "Richtig: (b) fluchen, (d) lachen, (e) sind verblüfft.",
        "steps": ["'teils fluchend, teils lachend' und 'verblüfftes Volk'."],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 10,
        "type": "Aussage bewerten",
        "text": (
            "'Die Bürger sehen alle nicht ein, dass Till Eulenspiegel mit seiner "
            "Rede recht hat.\" Die Aussage ist:\n"
            "(a) richtig (b) falsch\n"
            "Begründe!"
        ),
        "answer": (
            "Falsch. Sie erkennen, dass Till Eulenspiegel die Wahrheit gesprochen "
            "hat, auch wenn er ein Narr ist."
        ),
        "steps": ["'doch er hat die Wahrheit gesprochen!'"],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 11,
        "type": "Eigene Meinung heute",
        "text": (
            "Sind die Menschen heute (also über 650 Jahre später) noch leichtgläubig, "
            "dumm und sensationsgierig? Nenne 1 Beispiel und begründe deine Meinung "
            "ausführlich!"
        ),
        "answer": (
            "Individuelle Lösungen. Z. B.: leichtgläubig — Glauben an Werbung "
            "(Haarwuchsmittel) oder Wahlversprechen ; dumm — Kriege wegen Religion ; "
            "sensationsgierig — Schaulustige bei Unglücken oder Selbstmorden."
        ),
        "steps": ["Eigenes Beispiel mit Begründung."],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
]

NEW_KNOWLEDGE = []
