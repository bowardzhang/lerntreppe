EXERCISE = {
    "id": "0411",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Berühmte Piraten",
    "topic": "Leseverstehen, Sachtext, Piraten Schwarzbart und Störtebeker",
    "publisher": "CATLUX",
    "source_pdf": "0411.pdf",
    "answer_pdf": "0411 (1).pdf",
    "total_points": 21.0,
}

LESETEXT = (
    "Berühmte Piraten\n\n"
    "Seit dreitausend Jahren machten Piraten die Meere unsicher. Viele von ihnen "
    "waren so gefuerchtet, dass wir ihre Geschichten auch heute noch kennen. "
    "Meist waren Piraten Maenner, doch es gab auch weibliche Piraten.\n\n"
    "Einer der beruechtigtsten Piraten war der Englaender 'Blackbeard', zu Deutsch "
    "'Schwarzbart'. Sein richtiger Name war eigentlich Edward Teach und geboren "
    "wurde er 1680 in Bristol. Als junger Mann hat er als einfacher Matrose auf "
    "englischen Militaerschiffen gearbeitet. Mit diesen Schiffen war er dann in "
    "der Karibik unterwegs, wo er mit seiner Mannschaft waehrend eines Krieges "
    "fuer England feindliche Schiffe pluenderte. Dabei hat Schwarzbart gelernt, "
    "wie man andere Schiffe ausraubt.\n\n"
    "Eines Tages hatte Schwarzbart dann keine Lust mehr fuer das englische "
    "Militaer zu arbeiten und heuerte auf einem richtigen Piratenschiff an. "
    "Kurze Zeit spaeter gelang es diesen Piraten, ein beruehmtes franzoesisches "
    "Handelsschiff, die 'Concorde', zu ueberfallen. Zur Belohnung wurde "
    "Schwarzbart zum Kapitaen des erbeuteten Schiffes ernannt.\n\n"
    "Das Besondere an Blackbeard war, dass er bei seinen Beutezuegen immer "
    "besonders grausam aussah. Er hatte naemlich immer mehrere Messer und "
    "Pistolen an seinem Koerper haengen, und band sich an die Enden seines "
    "langen, schwarzen Bartes brennende Lunten, die gluehten und rauchten. "
    "Blackbeard muss dabei wirklich ausgesehen haben wie der Teufel persoenlich, "
    "so dass sich die Leute auf den ueberfallenen Schiffen oft von selbst "
    "ergaben.\n\n"
    "Ein anderer sehr gefuerchteter Pirat war Klaus Stoertebeker. Er segelte "
    "in der Nord- und Ostsee. Wann immer ihm danach war, hat er die Schiffe "
    "der Kaufleute oder andere prall mit Waren gefuellte Schiffe ueberfallen.\n\n"
    "Als Stoertebeker gefasst wurde, wurde sein Kopf auf einen Pfahl genagelt "
    "und am Ufer der Hamburger Elbe zur Schau gestellt - zusammen mit den "
    "70 Koepfen seiner Mannschaft.\n\n"
    "Stoertebekers letzter Wunsch ist ganz beruehmt: Er wollte, dass jeder "
    "seiner Maenner, an dem er ohne Kopf noch vorbeilaufen konnte, verschont "
    "werden sollte. Angeblich lief er kopflos noch an elf Maennern vorbei. "
    "Da wurde es dem Henker zu bunt und er stellte ihm ein Bein."
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Textstellen unterstreichen",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Finde die Stellen im Text! Markiere:\n"
            "(a) rot: Was machte Kapitaen Schwarzbart, bevor er Pirat wurde?\n"
            "(b) gruen: Was war Klaus Stoertebekers letzter Wunsch?\n"
            "(c) blau: Wo wurde Kapitaen Schwarzbart geboren?"
        ),
        "answer": (
            "(a) Er hat als einfacher Matrose auf englischen Militaerschiffen gearbeitet. ; "
            "(b) Er wollte, dass jeder seiner Maenner, an dem er ohne Kopf noch "
            "vorbeilaufen konnte, verschont wird. ; "
            "(c) Er wurde 1680 in Bristol geboren."
        ),
        "steps": [
            "(a) Hinweis: 'Als junger Mann ... auf englischen Militaerschiffen gearbeitet'.",
            "(b) Hinweis: 'Stoertebekers letzter Wunsch ist ganz beruehmt'.",
            "(c) Hinweis: 'geboren wurde er 1680 in Bristol'.",
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
        "type": "Fragen mit ganzen Sätzen beantworten",
        "text": (
            "Beantworte folgende Fragen mit vollstaendigen Saetzen:\n"
            "(a) Warum sah Kapitaen Schwarzbart bei seinen Beutezuegen immer "
            "besonders grausam aus?\n"
            "(b) In welchen Meeren segelte Klaus Stoertebeker?\n"
            "(c) Was tat der Henker, als Stoertebeker an elf seiner Maenner "
            "vorbeigelaufen war?"
        ),
        "answer": (
            "(a) Er sah so grausam aus, weil er mehrere Messer und Pistolen an "
            "seinem Koerper haengen hatte und weil er sich brennende Lunten an "
            "seinem langen Bart band. ; "
            "(b) Er segelte in der Nordsee und in der Ostsee. ; "
            "(c) Der Henker stellte Stoertebeker ein Bein."
        ),
        "steps": [
            "Antworten in vollstaendigen Saetzen formulieren.",
            "Auf Textstellen Bezug nehmen.",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 3,
        "type": "Richtig oder Falsch ankreuzen",
        "text": (
            "Welche Aussagen sind richtig? Kreuze nur die richtigen an:\n"
            "(1) Blackbeard heisst zu Deutsch Schwarzbrot.\n"
            "(2) In Wirklichkeit heisst Kapitaen Schwarzbart Edward Teach.\n"
            "(3) Kapitaen Schwarzbart segelte in der Ostsee.\n"
            "(4) Weil Schwarzbart mit seiner Mannschaft ein beruehmtes "
            "italienisches Handelsschiff ueberfiel, wurde er zur Belohnung "
            "Kapitaen.\n"
            "(5) Weil Schwarzbart bei seinen Ueberfaellen immer sehr grausam "
            "aussah, ergaben sich die Leute oft von selbst.\n"
            "(6) Klaus Stoertebeker wurde erhaengt.\n"
            "(7) Angeblich lief Klaus Stoertebeker ohne Kopf noch an elf Maennern "
            "vorbei.\n"
            "(8) Der Henker stellte Stoertebeker aus Mitleid ein Bein."
        ),
        "answer": "Richtig: (2), (5), (7).",
        "steps": [
            "(1) falsch: Schwarzbart, nicht Schwarzbrot.",
            "(3) falsch: Schwarzbart segelte in der Karibik.",
            "(4) falsch: franzoesisches Handelsschiff (Concorde), nicht italienisches.",
            "(6) falsch: Sein Kopf wurde abgeschlagen.",
            "(8) falsch: Es wurde dem Henker zu bunt, kein Mitleid.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 4,
        "type": "Richtigen Satz ankreuzen",
        "text": (
            "Welcher Satz ist richtig? Kreuze an:\n"
            "(a) Meist waren Piraten Maenner, doch es gab auch weibliche Piraten.\n"
            "(b) Meist waren Piraten maennlich, doch es gab auch weibliche Piraten.\n"
            "(c) Meist waren Piraten Maenner, doch es gab auch Frauen als Piraten."
        ),
        "answer": "Richtig: (a) Meist waren Piraten Maenner, doch es gab auch weibliche Piraten.",
        "steps": [
            "Originalformulierung im Text waehlen.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 5,
        "type": "Schiffstyp identifizieren",
        "text": (
            "Welcher Schiffstyp passt zu einem Piratenschiff? Waehle:\n"
            "Langschiff, Dschunke, Dhau, Galeere, Schoner."
        ),
        "answer": "Schoner.",
        "steps": [
            "Piraten benutzten oft Schoner: schnelle, wendige Schiffe mit zwei Masten.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 6,
        "type": "Geheimschrift entziffern",
        "text": (
            "Entziffere die rueckwaerts geschriebene Botschaft:\n"
            "'eheG dnesuat ettirhcS hcan nedorN sib ud ieb ned iewz nemuäB tsib.'"
        ),
        "answer": "Gehe tausend Schritte nach Norden, bis du bei den zwei Bäumen bist.",
        "steps": [
            "Jedes Wort rueckwaerts lesen.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 7,
        "type": "Verschluesselte Botschaft",
        "text": (
            "Entziffere die Botschaft (Grossbuchstaben in der Reihenfolge):\n"
            "'geLan beStä fenhel dir durch den sandTreib.'"
        ),
        "answer": "Lange Stäbe helfen dir durch den Treibsand.",
        "steps": [
            "Grossbuchstaben in jedem Wort markieren und neu zusammensetzen: L+S+T = Lange Staebe ... Treibsand.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 8,
        "type": "Wegbeschreibung mit Bedingungen",
        "text": (
            "Lese die Hinweise (laufen, gehen / schwimmen / Wasser, Fluss, See / "
            "halb / quer / oder) und entscheide, was du tun sollst, um den See zu "
            "umgehen oder zu durchqueren."
        ),
        "answer": "Laufe halb um den See herum oder schwimme quer durch den See.",
        "steps": [
            "Aus den Stichworten entsteht: Laufe halb um den See herum ODER schwimme quer durch.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 9,
        "type": "Vokale ergänzen",
        "text": (
            "Ergaenze die fehlenden Vokale:\n"
            "'D. f.nd.st d.n Sch.tz .n ..n.r H.hl. g.n.. .n d.r M.tt. d.s "
            "v..rt.n B.rg.s.'"
        ),
        "answer": "Du findest den Schatz in einer Höhle genau in der Mitte des vierten Berges.",
        "steps": [
            "Vokale (a, e, i, o, u) sinngemaess einsetzen.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
]

NEW_KNOWLEDGE = []
