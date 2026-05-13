EXERCISE = {
    "id": "0014",
    "subject": "HSU",
    "grade": 4,
    "title": "Lernzielkontrolle: Wasser, Wetter",
    "topic": "Wasser – Kreislauf, Niederschläge, Aggregatzustände, Grundwasser, Wasserschutz",
    "publisher": "CATLUX",
    "source_pdf": "0014.pdf",
    "answer_pdf": "0014_Lösung.pdf",
    "total_points": 35.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Lückentext (Wasserkreislauf)",
        "text": (
            "Fülle die Lücken!\n"
            "Die ___ erhitzt das Wasser aus Seen, Flüssen und dem ___. "
            "Das Wasser ___ und wird hoch oben wieder zu ___, weil es oben ___ ist. "
            "So entstehen allmählich ___."
        ),
        "answer": (
            "Die (Sonne) erhitzt das Wasser aus Seen, Flüssen und dem (Meer). "
            "Das Wasser (verdunstet) und wird hoch oben wieder zu (kleinen Tropfen), "
            "weil es oben (kälter) ist. So entstehen allmählich (Wolken)."
        ),
        "steps": [
            "Sonne erhitzt Wasser → Verdunstung.",
            "Wasserdampf steigt auf → kühlt ab → kondensiert zu kleinen Tropfen.",
            "Tropfen bilden Wolken.",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 2,
        "type": "Erklärungsaufgabe (Wolken und Niederschlag)",
        "text": "Was meint man wenn man sagt: „Die Wolke ist zu schwer!” Erkläre!",
        "answer": (
            "Durch die kalte Luft verdichten sich die Wassertröpfchen in der Wolke zu größeren Tropfen. "
            "Die Wolke wird dadurch immer schwerer und die Tropfen fallen schließlich als Niederschlag zur Erde."
        ),
        "steps": [
            "Wassertröpfchen in der Wolke nehmen noch mehr Wasser auf und werden größer.",
            "Die Wolke kann das Gewicht nicht mehr halten → Niederschlag fällt.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf", "hsu.klasse3.luft_wetter.phaenomene"],
    },
    {
        "n": 3,
        "type": "Erklärungsaufgabe (Hagelbildung)",
        "text": "Erkläre wie Hagel entsteht!",
        "answer": (
            "Wind wirbelt Regen nach oben in eine kalte Luftschicht. Dort gefrieren die Regentropfen. "
            "Dieser Vorgang kann sich mehrfach wiederholen. Schließlich fällt der Hagel zur Erde."
        ),
        "steps": [
            "Regen wird von starkem Wind nach oben gewirbelt.",
            "In der kalten Luftschicht gefrieren die Wassertropfen.",
            "Hagel fällt zur Erde (kann mehrere Eisschichten haben).",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.luft_wetter.phaenomene"],
    },
    {
        "n": 4,
        "type": "Freie Antwort (Schnee vs. Graupel)",
        "text": "Was ist der Unterschied zwischen Schnee und Graupel?",
        "answer": (
            "Beim Schnee verdichtet sich der Wasserdampf bzw. gefriert und fällt als Eiskristalle zur Erde. "
            "Beim Graupel taut der verdichtete Wasserdampf während des Falls erneut auf, gefriert aber wieder "
            "und fällt als Graupel zur Erde. Beim Graupel gibt es während des Falls zwei Temperaturunterschiede."
        ),
        "steps": [
            "Schnee: Wasserdampf gefriert direkt zu Eiskristallen.",
            "Graupel: Eiskristalle tauen teilweise auf und gefrieren erneut – dadurch rundliche Form.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.luft_wetter.phaenomene"],
    },
    {
        "n": 5,
        "type": "Tabelle (Aggregatzustände des Wassers)",
        "text": (
            "Wasser hat 3 Zustandsformen. Nenne die fehlenden zwei und "
            "schreibe ihre Eigenschaft (=Wiewort) dazu (wie im Beispiel)!\n\n"
            "___       → ___       → Dampf\n"
            " ↓           ↓           ↓\n"
            "___       → ___       → gasförmig"
        ),
        "answer": (
            "(Eis)     → (Wasser)  → Dampf\n"
            " ↓           ↓           ↓\n"
            "(fest)    → (flüssig) → gasförmig"
        ),
        "steps": [
            "Drei Aggregatzustände: fest (Eis), flüssig (Wasser), gasförmig (Wasserdampf).",
            "Stoffname über der Linie, Eigenschaft (Wiewort) darunter.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 6,
        "type": "Richtig/Falsch (Der blaue Planet)",
        "text": (
            "Der „blaue” Planet! richtig (r) oder falsch (f)\n"
            "1. Die Erdoberfläche ist zum größten Teil mit Wasser bedeckt.\n"
            "2. Auf der Erde gibt es für alle Menschen genügend Trinkwasser.\n"
            "3. Der Mensch kommt mehrere Wochen ohne Nahrung und ohne Wasser aus.\n"
            "4. Ein Liter Öl verschmutzt 1 000 000 Liter Trinkwasser.\n"
            "5. Das Wasser der Meere ist salzig."
        ),
        "answer": (
            "1. r (richtig)\n"
            "2. f (falsch)\n"
            "3. f (falsch – ohne Wasser überlebt der Mensch nur wenige Tage)\n"
            "4. r (richtig)\n"
            "5. r (richtig)"
        ),
        "steps": [
            "Ca. 71 % der Erdoberfläche sind mit Wasser bedeckt.",
            "Trinkwasser ist knapp – viele Menschen haben keinen Zugang zu sauberem Wasser.",
            "Der Mensch überlebt ohne Wasser nur wenige Tage (nicht Wochen).",
            "Öl breitet sich auf Wasser aus und verschmutzt enorme Mengen.",
            "Meerwasser ist salzig und nicht direkt trinkbar.",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf", "hsu.klasse3.wasser.gewaesser"],
    },
    {
        "n": 7,
        "type": "Zuordnung (Niederschlagsarten)",
        "text": (
            "Welcher Niederschlag ist gemeint?\n"
            "Das sind gefrorene Wassertropfen. → ___________\n"
            "Eine Wolke in Bodennähe. → ___________\n"
            "Kleine Eiskristalle an Gräsern und Blättern. → ___________\n"
            "Kondensierte Wasserteilchen an Blättern und Gräsern. → ___________\n"
            "Wasserteilchen gefrieren und fallen als Eiskristalle herab. → ___________\n"
            "Welcher Niederschlag fehlt? ___________"
        ),
        "answer": (
            "Gefrorene Wassertropfen → Hagel\n"
            "Wolke in Bodennähe → Nebel\n"
            "Kleine Eiskristalle an Gräsern → Reif\n"
            "Kondensierte Wasserteilchen an Pflanzen → Tau\n"
            "Wasserteilchen gefrieren und fallen als Eiskristalle → Schnee\n"
            "Fehlender Niederschlag: Regen"
        ),
        "steps": [
            "Hagel = gefrorene Regentropfen.",
            "Nebel = Wolke in Bodennähe (Wassertröpfchen).",
            "Reif = gefrorener Tau (Eiskristalle an Pflanzen).",
            "Tau = kondensiertes Wasser an Pflanzen (flüssig).",
            "Schnee = gefrorene Wasserteilchen in der Wolke fallen als Eiskristalle.",
            "Regen fehlt in der Liste.",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.luft_wetter.phaenomene"],
    },
    {
        "n": 8,
        "type": "Beschriften (Erdschichten)",
        "text": (
            "Benenne die Erdschichten (1–4)! "
            "Ordne diesen zu: wasserdurchlässig / wasserundurchlässig! "
            "[Zeichnung mit 4 Erdschichten]"
        ),
        "answer": (
            "(1) Humus – wasserdurchlässig\n"
            "(2) Sand – wasserdurchlässig\n"
            "(3) Kies – wasserdurchlässig\n"
            "(4) Ton – wasserundurchlässig\n"
            "(Alternativ: Sand / Kies / Ton / Gestein – je nach Schulbuch)"
        ),
        "steps": [
            "Wasserdurchlässige Schichten: Humus, Sand, Kies – Wasser kann durchsickern.",
            "Wasserundurchlässige Schicht: Ton (oder Lehm/Gestein) – Wasser staut sich darüber.",
        ],
        "points": 4.0,
        "has_image": True,
        "image": "0014_q8_erdschichten.png",
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 9,
        "type": "Freie Antwort (Grundwasserreinigung)",
        "text": (
            "Was geschieht mit dem Wasser, während es durch die Erdschichten sickert automatisch?"
        ),
        "answer": "Es wird gereinigt (gefiltert).",
        "steps": [
            "Die Erdschichten (Humus, Sand, Kies) filtern das Wasser beim Durchsickern und reinigen es.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 10,
        "type": "Begründungsaufgabe (Wasserschutzgebiet)",
        "text": (
            "Bauer Meier düngt seinen Acker. Direkt vor seinem Acker steht dieses Zeichen [Wasserschutzgebiet-Schild]. "
            "Eine Woche später bekommt er eine Strafe von der Polizei. "
            "Kannst du dir vorstellen, warum? Begründe kurz!"
        ),
        "answer": (
            "In einem Wasserschutzgebiet darf Bauer Meier sein Feld nicht düngen, denn durch den Dünger "
            "wird das Grundwasser verschmutzt, aus dem z. B. wieder Trinkwasser gewonnen wird."
        ),
        "steps": [
            "Dünger enthält Nitrate und Schadstoffe, die ins Grundwasser gelangen.",
            "Wasserschutzgebiete schützen das Trinkwasser vor Verunreinigung.",
            "Düngen in Wasserschutzgebieten ist verboten und wird bestraft.",
        ],
        "points": 2.0,
        "has_image": True,
        "image": "0014_q10_schutzgebiet.png",
        "knowledge": ["hsu.klasse3.wasser.kreislauf", "hsu.klasse3.wasser.gewaesser"],
    },
]

NEW_KNOWLEDGE = []
