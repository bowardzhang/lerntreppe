EXERCISE = {
    "id": "2257",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Kleine Ursache, große Wirkung (Waldbrände)",
    "topic": "Leseverstehen, Sachtext, Waldbrände, Aboriginals, Brandbekämpfung",
    "publisher": "CATLUX",
    "source_pdf": "2257.pdf",
    "answer_pdf": "2257 (1).pdf",
    "total_points": 23.0,
}

LESETEXT = (
    "Kleine Ursache, große Wirkung\n\n"
    "Ein Lagerfeuer, eine achtlos weggeworfene Zigarette oder bewusste "
    "Brandstiftung: Fuer Waldbraende gibt es viele Ursachen. Nur in wenigen "
    "Faellen werden sie allein durch Naturgewalt ausgeloest, etwa durch einen "
    "Blitzeinschlag.\n\n"
    "Wenn der Wald erst brennt, kann sich das Feuer bei extremer Trockenheit "
    "durch Waermeuebertragung rasant schnell auf Gras, Gebuesch, Unterholz und "
    "Baeume ausbreiten. Wasser allein reicht zur Bekaempfung eines groesseren "
    "Waldbrandes nicht aus, selbst wenn Loeschflugzeuge eingesetzt werden.\n\n"
    "Loeschtrupps schlagen breite Schneisen in den Wald oder legen "
    "kontrollierte Gegenfeuer, um ein Ueberspringen und Ausweiten des Feuers zu "
    "verhindern - oder das Feuer zumindest umzulenken, damit Menschen und "
    "Gebaeude geschuetzt werden. Auch flammenhemmende Chemikalien werden "
    "eingesetzt.\n\n"
    "Die Ureinwohner Australiens, die Aboriginals, pflegten jahrtausendelang "
    "Feuer im Wald zu legen - im Fruehjahr, wenn der Boden vom Winter noch "
    "feucht war. Diese 'reinigenden' Feuer verbrannten das hohe Gras des "
    "vergangenen Sommers und die Schichten abgeworfener Baumrinden, nicht aber "
    "die noch feuchten Baeume. So gewannen die Aboriginals einerseits "
    "wertvollen Duenger und beugten gleichzeitig katastrophalen Waldbraenden "
    "vor, weil sie das brennbare Material am Boden schon vorher beseitigt "
    "hatten.\n\n"
    "Dass heute tendenziell mehr Braende entstehen, die groessere Schaeden "
    "anrichten, ist zu einem grossen Teil Schuld der Menschen. Grossstaedte in "
    "Kalifornien oder Australien, aber auch Ferienwohnungen im Mittelmeerraum "
    "weiten sich zunehmend in akut brandgefaehrdete Waelder und Buschlaender "
    "aus. Nicht zuletzt heizt der Mensch durch Brandrodungen in "
    "Regenwaldgebieten den Klimawandel an. Hoehere Temperaturen rund um den "
    "Globus lassen Landstriche schneller und umfangreicher verdorren und "
    "erhoehen dadurch auch die Brandgefahr."
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Textinhalt zusammenfassen",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Fasse in einem Satz zusammen, worum es im Text 'Kleine Ursache, "
            "grosse Wirkung' geht."
        ),
        "answer": (
            "Im Text geht es um Waldbraende, ihre Ursachen und um die "
            "Moeglichkeiten der Bekaempfung."
        ),
        "steps": [
            "Hauptthema identifizieren: Waldbraende.",
            "Kernaspekte: Ursachen + Bekaempfung + Folgen.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 2,
        "type": "Information aus dem Text",
        "text": (
            "Auf was kann sich ein Waldbrand durch Waermeuebertragung rasant "
            "schnell ausbreiten?"
        ),
        "answer": "Auf Gras, Gebuesch, Unterholz und Baeume.",
        "steps": [
            "Direkt aus dem Text entnehmen.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 3,
        "type": "Wortbedeutungen erklären",
        "text": (
            "Erklaere die Bedeutung folgender Woerter:\n"
            "(a) Brandstiftung\n"
            "(b) rasant\n"
            "(c) breite Schneise\n"
            "(d) hemmend\n"
            "(e) idyllisch"
        ),
        "answer": (
            "(a) Brandstiftung: wenn absichtlich ein Feuer gelegt wird. ; "
            "(b) rasant: sehr schnell. ; "
            "(c) breite Schneise: ein freier (gerodeter) Weg im Wald. ; "
            "(d) hemmend: bremsend, abhaltend. ; "
            "(e) idyllisch: friedlich, schoen, ruhig (z. B. schoenes Wohnen)."
        ),
        "steps": [
            "Kontext im Text beachten.",
            "Mit eigenen Worten erklaeren.",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 4,
        "type": "Text in Sinnabschnitte gliedern",
        "text": (
            "Gliedere den Text in 4 Sinnabschnitte und finde Zwischenueberschriften."
        ),
        "answer": (
            "Abschnitt 1: 'Wie entstehen Waldbraende?' ; "
            "Abschnitt 2: 'Wie koennen Waldbraende geloescht werden?' ; "
            "Abschnitt 3: 'Wie schuetzen sich die Aboriginals vor Waldbraenden?' ; "
            "Abschnitt 4: 'Der Mensch ist schuld, dass mehr Waldbraende entstehen.'"
        ),
        "steps": [
            "Themenwechsel im Text erkennen.",
            "Pro Abschnitt eine kurze Frage oder Aussage formulieren.",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 5,
        "type": "Aussagen zu Waldbrand-Schaubildern",
        "text": (
            "Sind diese Aussagen richtig (R), falsch (F) oder nicht im Schaubild "
            "enthalten (N)?\n"
            "(1) Im Jahr 2016 gab es in Deutschland 423 Waldbraende.\n"
            "(2) In Sachsen und Hessen brannte es 2018 seltener als in "
            "Brandenburg.\n"
            "(3) Im Saarland gab es in den Jahren 1991-2017 im Durchschnitt 9 "
            "Waldbraende.\n"
            "(4) Es entstanden mehr Waldbraende durch natuerliche Ursachen als "
            "durch Brandstiftung."
        ),
        "answer": "(1) F ; (2) R ; (3) N ; (4) F",
        "steps": [
            "Aus den Schaubildern (im PDF) ablesen.",
        ],
        "points": 4.0,
        "has_image": True,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
            "mathe.klasse4.sachaufgaben.tabellen",
        ],
    },
    {
        "n": 6,
        "type": "Eigene Aussagen aus Schaubildern",
        "text": (
            "Entnimm den Schaubildern noch 2 treffende Informationen und "
            "schreibe sie jeweils in einem ganzen Satz."
        ),
        "answer": (
            "Beispiele: (1) Im Jahr 2016 entstanden die meisten Waldbraende "
            "durch unbekannte Ursachen. (2) Im Jahr 2018 brannte es in "
            "Brandenburg am haeufigsten."
        ),
        "steps": [
            "Auffaelligkeiten im Schaubild auswaehlen.",
            "Ganze Saetze formulieren.",
        ],
        "points": 4.0,
        "has_image": True,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
]

NEW_KNOWLEDGE = []
