EXERCISE = {
    "id": "0010",
    "subject": "HSU",
    "grade": 4,
    "title": "Lernzielkontrolle: Wald und Pilze",
    "topic": "Wald, Laubbäume, Nadelbäume, Pilze, Ökosystem Wald",
    "publisher": "CATLUX",
    "source_pdf": "0010.pdf",
    "answer_pdf": "0010 (1).pdf",
    "total_points": 42.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Tabelle ergänzen",
        "text": (
            "Laubbäume kann man am Wuchs, an Form und Rand der Blätter, der Rinde, "
            "ihren Blüten und Früchten unterscheiden. Zeige was du kannst und "
            "vervollständige die Tabelle im Bild. Die ersten beiden Bäume sind nur "
            "durch je ein Bild (Frucht bzw. Blatt) angedeutet — du musst auch den "
            "Baumnamen selbst herausfinden."
        ),
        "answer": (
            "| Baum  | Blatt (Blattform, Blattrand)            | Frucht/Samen                              |\n"
            "|-------|-----------------------------------------|-------------------------------------------|\n"
            "| Buche | tropfenförmig, Rand leicht gewellt      | Buchecker                                 |\n"
            "| Linde | herzförmig, Rand fein gezackt           | Lindenfrüchte mit Flugblatt (Lindenblüte) |\n"
            "| Ahorn | handförmig (gelappt), Rand grob gezackt | Flugsamen (Doppelflügel/Propeller)        |"
        ),
        "steps": [
            "Buche: tropfenförmiges Blatt, leicht gewellter Rand, Bucheckern als Früchte.",
            "Linde: herzförmiges Blatt, Flugsamen mit Tragblatt.",
            "Ahorn: handförmiges Blatt, grob gezackter Rand, Flugsamen (Doppelflügel).",
        ],
        "points": 8.0,
        "has_image": True,
        "image": "0010_q1_laubbaeume.png",
        "knowledge": [
            "hsu.klasse4.umwelt.oekosysteme",
            "hsu.klasse2.tiere_pflanzen.pflanzen",
        ],
    },
    {
        "n": 2,
        "type": "Kurzantworten",
        "text": (
            "Du hast im Unterricht vier Nadelbäume kennen gelernt.\n"
            "a) Beschreibe die Nadeln der Kiefer!\n"
            "b) Was weißt du über die Nadeln der Lärche?\n"
            "c) Tanne und Fichte – Nenne je zwei Gemeinsamkeiten und zwei Unterschiede dieser "
            "Nadelbäume! Beschreibe genau!"
        ),
        "answer": (
            "a) Kiefernadeln: spitz, lang, wachsen paarweise aus dem Zweig.\n"
            "b) Lärchennadeln: wachsen in Büscheln aus dem Zweig, hellgrün, weich, fallen im Herbst ab.\n"
            "c) Gemeinsamkeiten von Tanne und Fichte: "
            "Nadeln wachsen einzeln aus dem Zweig; Zapfen als Früchte.\n"
            "Unterschiede – Tanne: Nadeln rund und eingekerbt, Früchte stehen aufrecht (himmelwärts).\n"
            "Unterschiede – Fichte: Nadeln vorne spitz, Früchte hängen herab."
        ),
        "steps": [
            "Kiefer: lange, spitze Nadeln, paarweise.",
            "Lärche: Büscheln, hellgrün, weich, laubabwerfend.",
            "Tanne und Fichte: beide Einzelnadeln und Zapfen.",
            "Tanne: runde, eingekerbte Nadeln, Zapfen aufrecht.",
            "Fichte: spitze Nadeln, Zapfen hängend.",
        ],
        "points": 6.0,
        "has_image": True,
        "image": "0010_q2_nadelbaeume.png",
        "knowledge": [
            "hsu.klasse4.umwelt.oekosysteme",
            "hsu.klasse2.tiere_pflanzen.pflanzen",
        ],
    },
    {
        "n": 3,
        "type": "Benennen",
        "text": (
            "Im Ökosystem Wald sind alle Bereiche wichtig, damit das notwendige Gleichgewicht "
            "erhalten bleibt. Benenne die Schichten des Waldes und schreibe zu jedem Stockwerk "
            "eine dort lebende Tierart!"
        ),
        "answer": (
            "Baumschicht: Eichhörnchen (oder Vogel).\n"
            "Strauchschicht: Reh.\n"
            "Krautschicht: Vogel (oder Igel).\n"
            "Moosschicht: Igel.\n"
            "Bodenschicht: Wurm."
        ),
        "steps": [
            "Waldschichten von oben nach unten: Baumschicht, Strauchschicht, Krautschicht, "
            "Moosschicht, Bodenschicht.",
            "Je eine Tierart pro Schicht, z. B.: Eichhörnchen, Reh, Vogel, Igel, Wurm.",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "hsu.klasse4.umwelt.oekosysteme",
            "hsu.klasse2.tiere_pflanzen.jahresverlauf",
        ],
    },
    {
        "n": 4,
        "type": "Benennen",
        "text": (
            "Tiere hinterlassen sichtbare „Spuren” (keine Fußabdrücke!) im Wald. "
            "Nenne die „Spuren” folgender Tiere!\n"
            "Eichhörnchen: ___________________\n"
            "Specht: ___________________\n"
            "Borkenkäfer: ___________________"
        ),
        "answer": (
            "Eichhörnchen: offene Nussschalen.\n"
            "Specht: Loch im Baum.\n"
            "Borkenkäfer: Gänge im Baum."
        ),
        "steps": [
            "Eichhörnchen knackt Nüsse und hinterlässt offene Schalen.",
            "Specht hackt Löcher in Baumstämme.",
            "Borkenkäfer frisst Gänge unter der Baumrinde.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "hsu.klasse4.umwelt.oekosysteme",
            "hsu.klasse2.tiere_pflanzen.jahresverlauf",
        ],
    },
    {
        "n": 5,
        "type": "Benennen",
        "text": "Benenne alle Teile des Knollenblätterpilzes! (Fachausdrücke!)",
        "answer": "Hut, Lamellen, Manschette, Stiel, Knolle, Wurzel.",
        "steps": [
            "Der Knollenblätterpilz (stark giftig) hat: Hut (oben), darunter Lamellen, "
            "am Stiel eine Manschette, am Stielende eine Knolle, darunter die Wurzel.",
        ],
        "points": 3.0,
        "has_image": True,
        "image": "0010_q5_knollenblaetterpilz.png",
        "knowledge": ["hsu.klasse4.umwelt.oekosysteme"],
    },
    {
        "n": 6,
        "type": "Kurzantwort",
        "text": "Warum wirft der Laubbaum im Herbst seine Blätter ab?",
        "answer": "Damit er nicht vertrocknet (Eigenschutz): Im Winter kann er nicht genug Wasser aus dem Boden aufnehmen.",
        "steps": [
            "Im Winter ist Wasser als Eis gebunden und nicht verfügbar.",
            "Über Blätter würde zu viel Wasser verdunsten.",
            "Der Baum wirft die Blätter ab, um sich vor Austrocknung zu schützen.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "hsu.klasse2.tiere_pflanzen.pflanzen",
            "hsu.klasse4.umwelt.oekosysteme",
        ],
    },
    {
        "n": 7,
        "type": "Aufzählen",
        "text": "Der Wald ist für den Menschen sehr wichtig. Nenne fünf Beispiele!",
        "answer": (
            "1. Liefert Sauerstoff.\n"
            "2. Dämmt Lärm.\n"
            "3. Liefert Holz zum Bauen.\n"
            "4. Liefert Brennholz.\n"
            "5. Erholungsgebiet für Menschen."
        ),
        "steps": [
            "Wald als Sauerstoffproduzent, Lärmschutz, Holzlieferant, Brennstoffquelle, Erholungsraum.",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "hsu.klasse4.umwelt.oekosysteme",
            "hsu.klasse4.umwelt.naturschutz",
        ],
    },
    {
        "n": 8,
        "type": "Kurzantwort",
        "text": (
            "Das Haus der Familie Müller liegt an einem Hang. Bei starkem Regen wird deshalb "
            "sehr viel Gartenerde weggespült. Gib der Familie einen Rat, was sie dagegen tun "
            "kann! Erkläre!"
        ),
        "answer": (
            "Sträucher anpflanzen, damit die Wurzeln die Erde festhalten und nicht weggespült wird."
        ),
        "steps": [
            "Pflanzen mit tiefen Wurzeln (z. B. Sträucher) binden die Erde.",
            "Wurzeln halten das Erdreich bei Regen fest.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "hsu.klasse4.umwelt.naturschutz",
            "hsu.klasse2.tiere_pflanzen.pflanzen",
        ],
    },
    {
        "n": 9,
        "type": "Zuordnen",
        "text": (
            "Schreibe zu jedem Pilz den passenden Sammelnamen, der uns hilft die Pilze zu unterscheiden!\n"
            "Champignon: ___________________\n"
            "Pfifferling: ___________________\n"
            "Satanspilz: ___________________\n"
            "Schwefelgelbe Koralle: ___________________\n"
            "Kartoffelbovist: ___________________"
        ),
        "answer": (
            "Champignon: Hutpilz.\n"
            "Pfifferling: Trichterpilz.\n"
            "Satanspilz: Hutpilz.\n"
            "Schwefelgelbe Koralle: Strauchpilz.\n"
            "Kartoffelbovist: Bauchpilz."
        ),
        "steps": [
            "Hutpilze: Champignon, Satanspilz (haben einen deutlichen Hut mit Stiel).",
            "Trichterpilze: Pfifferling (trichterförmig).",
            "Strauchpilze: Schwefelgelbe Koralle (verzweigt wie ein Strauch).",
            "Bauchpilze: Kartoffelbovist (kugelförmig, kein Stiel).",
        ],
        "points": 5.0,
        "has_image": True,
        "image": "0010_q9_pilze.png",
        "knowledge": ["hsu.klasse4.umwelt.oekosysteme"],
    },
    {
        "n": 10,
        "type": "Kurzantwort",
        "text": (
            "Peter findet im Wald einen Maronenröhrling. Er ist sich aber nicht ganz sicher, "
            "ob es sich um einen solchen handelt. Was kann er tun?"
        ),
        "answer": (
            "Den Pilz lieber stehen lassen, da er giftig sein könnte. "
            "Im Zweifelsfall einen Pilzsachverständigen befragen."
        ),
        "steps": [
            "Im Zweifel Pilz nicht mitnehmen oder essen.",
            "Einen Experten (Pilzsachverständigen) um Rat fragen.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse4.umwelt.oekosysteme"],
    },
    {
        "n": 11,
        "type": "Aufzählen",
        "text": "Nenne 4 Gefahren, die den Wald bedrohen können!",
        "answer": (
            "Vier der folgenden: Feuer, Wildverbiss, Abgase, saurer Regen, Industrie, Abholzung."
        ),
        "steps": [
            "Waldgefährdungen: Waldbrände, Wildverbiss, Luftverschmutzung/Abgase, "
            "saurer Regen, Industrieemissionen, Abholzung.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "hsu.klasse4.umwelt.naturschutz",
            "hsu.klasse4.umwelt.oekosysteme",
        ],
    },
    {
        "n": 12,
        "type": "Erklären",
        "text": (
            "Im Wald kann man kleine Eichen sehen, die an einer Stelle wachsen, "
            "wo es ansonsten nur große Nadelbäume gibt.\n"
            "a) Erkläre genau, warum die kleinen Eichen auch an Stellen wachsen, "
            "wo es keine großen Eichen gibt!\n"
            "b) Warum werden aus vielen kleinen Bäumchen nur wenige große Eichen? Erkläre!"
        ),
        "answer": (
            "a) Eichhörnchen sammeln Eicheln (Nüsse) als Wintervorrat und vergraben sie an "
            "verschiedenen Stellen im Wald. Vergessene Eicheln keimen aus und wachsen zu "
            "kleinen Eichen heran – auch dort, wo keine Eichen stehen.\n"
            "b) Viele kleine Bäumchen werden von Tieren gefressen oder zertreten, "
            "oder Menschen treten darauf. Nur wenige überleben und werden zu großen Eichen."
        ),
        "steps": [
            "a) Eichhörnchen vergraben Eicheln als Vorrat; vergessene Eicheln keimen.",
            "b) Fraß durch Tiere, Zertrampeln durch Tiere und Menschen → nur wenige überleben.",
        ],
        "points": 2.0,
        "has_image": True,
        "image": "0010_q12_eichen.png",
        "knowledge": [
            "hsu.klasse4.umwelt.oekosysteme",
            "hsu.klasse2.tiere_pflanzen.jahresverlauf",
        ],
    },
]

NEW_KNOWLEDGE = []
