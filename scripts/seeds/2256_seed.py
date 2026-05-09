EXERCISE = {
    "id": "2256",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Kleine Ursache, große Wirkung (Waldbrände)",
    "topic": "Leseverstehen, Sachtext, Waldbrände, Brandstiftung, Klimawandel, Umwelt",
    "publisher": "CATLUX",
    "source_pdf": "2256.pdf",
    "answer_pdf": "2256 (1).pdf",
    "total_points": 23.0,
}

LESETEXT = (
    "Kleine Ursache, große Wirkung\n\n"
    "Ein Lagerfeuer, eine achtlos weggeworfene Zigarette oder bewusste "
    "Brandstiftung: Für Waldbrände gibt es viele Ursachen. Nur in wenigen "
    "Fällen werden sie allein durch Naturgewalt ausgelöst, etwa durch einen "
    "Blitzeinschlag. So gestand etwa nach einem Großfeuer im Wald des "
    "US-Bundesstaates Colorado eine Mitarbeiterin der Forstbehörde 2002, auf "
    "einem abgelegenen Campingplatz einen Brief ihres Ehemanns aus Wut "
    "verbrannt zu haben. Dafür wurde sie zu zwölf Jahren Haft verurteilt.\n\n"
    "Auch für einen Waldbrand im US-Staat Arizona war ein Brandstifter "
    "verantwortlich: Ein arbeitslos gewordener Feuerwehrmann hatte gezündelt, "
    "um seinen Job wiederzubekommen.\n\n"
    "Egal warum – wenn der Wald erst brennt, kann sich das Feuer bei extremer "
    "Trockenheit durch Wärmeübertragung rasant schnell auf Gras, Gebüsch, "
    "Unterholz und Bäume ausbreiten. Wasser allein reicht zur Bekämpfung eines "
    "größeren Waldbrandes nicht aus, selbst wenn Löschflugzeuge eingesetzt "
    "werden. Löschtrupps schlagen breite Schneisen in den Wald oder legen "
    "kontrollierte Gegenfeuer, um ein Überspringen und Ausweiten des Feuers "
    "zu verhindern – oder das Feuer zumindest umzulenken, damit Menschen und "
    "Gebäude geschützt werden. Auch flammenhemmende Chemikalien werden "
    "eingesetzt.\n\n"
    "Dass heute häufig mehr Brände entstehen, die größere Schäden anrichten, "
    "ist zu einem großen Teil Schuld der Menschen. Großstädte in Kalifornien "
    "oder Australien, aber auch Ferienwohnungen im Mittelmeerraum, weiten "
    "sich zunehmend in akut brandgefährdete Wälder und Buschländer aus. Das "
    "idyllische Wohnen mitten in der einsamen Natur bringt Stromleitungen, "
    "Elektrogeräte und möglicherweise auch unachtsame Menschen als denkbare "
    "Brandverursacher in die Wildnis. Vor allem in Kalifornien siedeln viele "
    "Menschen in waldbrandgefährdeten Gebieten und bringen sich dadurch "
    "selbst in Gefahr. Nicht zuletzt heizt der Mensch durch Brandrodungen in "
    "Regenwaldgebieten den Klimawandel an. Höhere Temperaturen rund um den "
    "Globus lassen Landstriche schneller und umfangreicher verdorren und "
    "erhöhen dadurch auch die Brandgefahr."
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Zusammenfassung",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Fasse in einem Satz zusammen, worum es in dem Text 'Kleine Ursache, "
            "große Wirkung\" geht."
        ),
        "answer": (
            "In dem Text geht es um Waldbrände, ihre Ursachen und die Möglichkeiten "
            "der Bekämpfung."
        ),
        "steps": ["Hauptthema identifizieren."],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 2,
        "type": "Wärmeübertragung",
        "text": "Auf was kann sich ein Waldbrand durch Wärmeübertragung rasant schnell ausbreiten?",
        "answer": "Auf Gras, Gebüsch, Unterholz und Bäume.",
        "steps": ["Aus dem 3. Absatz."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 3,
        "type": "Wörter erklären",
        "text": (
            "Erkläre die Bedeutung folgender Wörter:\n"
            "(a) Brandstiftung (Z. 2)\n"
            "(b) rasant (Z. 12)\n"
            "(c) hemmend (Z. 18)\n"
            "(d) idyllische (Z. 23)"
        ),
        "answer": (
            "(a) Brandstiftung: wenn absichtlich ein Feuer gelegt wird. ; "
            "(b) rasant: sehr schnell. ; "
            "(c) hemmend: bremsend. ; "
            "(d) idyllisch: schönes, friedliches Wohnen."
        ),
        "steps": ["Wortbedeutungen erklären."],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 4,
        "type": "Sinnabschnitte gliedern",
        "text": (
            "Gliedere den Text in 3 Sinnabschnitte und finde Zwischenüberschriften!"
        ),
        "answer": (
            "Abschnitt 1 (Z. 1-10): Wie entstehen Waldbrände? ; "
            "Abschnitt 2 (Z. 11-18): Wie können Waldbrände gelöscht werden? ; "
            "Abschnitt 3 (Z. 19-30): Der Mensch ist schuld, dass mehr Waldbrände entstehen."
        ),
        "steps": ["Inhaltliche Gliederung in 3 Abschnitte."],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 5,
        "type": "Schaubilder R/F/Nicht enthalten",
        "text": (
            "Multiple-Choice zu Schaubildern (richtig/falsch/nicht enthalten):\n"
            "(a) Im Jahr 2016 gab es in Deutschland 423 Waldbrände.\n"
            "(b) In Sachsen und Hessen brannte es 2018 seltener als in Brandenburg.\n"
            "(c) Im Saarland gab es 1991-2017 im Durchschnitt 9 Waldbrände.\n"
            "(d) Es entstanden mehr Waldbrände durch natürliche Ursachen als durch Brandstiftung."
        ),
        "answer": "(a) falsch ; (b) richtig ; (c) nicht enthalten ; (d) falsch.",
        "steps": ["Schaubilder auswerten."],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 6,
        "type": "Schaubilder Informationen",
        "text": "Entnimm den Schaubildern noch 2 treffende Informationen und schreibe sie in ganzen Sätzen!",
        "answer": (
            "Z. B.: Im Jahr 2016 entstanden die meisten Waldbrände durch unbekannte "
            "Ursachen. ; Im Jahr 2018 brannte es in Brandenburg am häufigsten. ; "
            "Im Jahr 2016 gab es am wenigsten Waldbrände durch natürliche Ursachen."
        ),
        "steps": ["Eigene Sätze formulieren."],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
]

NEW_KNOWLEDGE = []
