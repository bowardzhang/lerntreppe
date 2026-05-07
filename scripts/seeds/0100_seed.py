EXERCISE = {
    "id": "0100",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Alarm im Wespennest",
    "topic": "Leseverstehen, Erzählung, Friedhof, Wespen, Forellenteich",
    "publisher": "CATLUX",
    "source_pdf": "0100.pdf",
    "answer_pdf": "0100 (1).pdf",
    "total_points": 22.0,
}

LESETEXT = (
    "Alarm im Wespennest (Auszug)\n\n"
    "Mein Freund Dieter und ich spielten oft auf dem alten Friedhof am Rande "
    "des Dorfes. Wir hatten keinen anderen Spielplatz, kein Geld und kein "
    "anderes Spielzeug, aber dort war es immer geheimnisvoll.\n\n"
    "Es rauschte im Wind, das Gras zischelte und die Kopfweiden knarrten. "
    "Asta, mein Hund, lief uns immer hinterher.\n\n"
    "Eines Tages wollten wir am Forellenteich angeln. Wir brauchten Wuermer "
    "als Koeder. Direkt am schiefen Eisenkreuz mit den Rosen sollte es welche "
    "geben. Der alte Bauer Jost hatte uns das gesagt: Dort hat er frueher "
    "selbst Wuermer gefunden.\n\n"
    "Doch als wir zu graben anfingen, schwirrte es ploetzlich um uns: ein "
    "ganzer Wespenschwarm! Die stechlustigen Brummer kamen aus dem Boden "
    "geschossen. Wir liefen Hals ueber Kopf zum Forellenteich und sprangen "
    "hinein. Wir tauchten unter, bis die Wespen weg waren. Asta hatten viele "
    "Stiche bekommen. Sie schuettelte sich die Ohren, rieb die Schnauze am "
    "Boden, sauste im Kreis herum und scharrte sich. Wir spritzten sie mit "
    "Wasser nass, damit die Wespen weggingen.\n\n"
    "Dieter hat schon einen alten abgelatschten Stiefel und eine alte "
    "Geldboerse mit zehn Pfennigen aus dem Teich geangelt. Heute aber griff "
    "er mit blossen Haenden eine Forelle. Wir grillten sie und gaben Asta "
    "die Graeten."
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Tiere im Text nennen",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Mit welchen Tieren hatten die Kinder bei ihrem Ausflug zu tun? "
            "Nenne nur Tiere, die sie tatsaechlich sahen."
        ),
        "answer": "Hund (Asta), Wespen, Forellen.",
        "steps": [
            "Im Text suchen: Asta, Wespenschwarm, Forelle.",
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
        "type": "Gründe nennen",
        "text": (
            "Der Friedhof ist ein ungewoehnlicher Platz zum Spielen. Warum "
            "spielten die Kinder trotzdem dort? Nenne drei Gruende."
        ),
        "answer": "(1) Sie hatten keinen anderen Spielplatz. (2) Sie hatten kein Geld. (3) Sie hatten kein anderes Spielzeug.",
        "steps": [
            "Im ersten Absatz nachlesen.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 3,
        "type": "Geräusche aufzählen",
        "text": "Welche Geraeusche nahmen die Kinder auf dem Friedhof wahr?",
        "answer": "Das Rauschen des Windes, das Zischeln des Grases und das Knarren der Kopfweiden.",
        "steps": [
            "Im zweiten Absatz nachlesen.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 4,
        "type": "Wo Würmer suchen",
        "text": (
            "An welcher Stelle wollten die Kinder Wuermer zum Angeln suchen? "
            "Warum glaubten sie, ausgerechnet dort welche zu finden?"
        ),
        "answer": "Am schiefen Eisenkreuz mit den Rosen, weil der alte Bauer Jost dort frueher selbst Wuermer gefunden hatte.",
        "steps": [
            "Begruendung: Bauer Jost hatte den Tipp gegeben.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 5,
        "type": "Was statt der Würmer?",
        "text": "Was fanden die Kinder anstatt der Wuermer vor?",
        "answer": "Einen Wespenschwarm.",
        "steps": [
            "Klar im Text genannt.",
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
        "type": "Dieters Schätze aus dem Teich",
        "text": (
            "Welche 'Schaetze' hatte Dieter bisher aus dem Teich geangelt?\n"
            "(a) ein Auto und eine Pistole\n"
            "(b) einen abgelatschten Stiefel und eine alte Geldboerse mit zehn Pfennigen\n"
            "(c) ein Buch und eine Brille\n"
            "(d) eine Brille und einen Hut"
        ),
        "answer": "(b) einen abgelatschten Stiefel und eine alte Geldboerse mit zehn Pfennigen.",
        "steps": [
            "Letzter Absatz im Lesetext.",
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
        "type": "Rettung der Kinder",
        "text": "Wie und wohin konnten sich die Kinder retten?",
        "answer": "Sie liefen zum Forellenteich, sprangen hinein und tauchten unter, bis die Wespen weg waren.",
        "steps": [
            "Wespen vermeiden durch Untertauchen.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 8,
        "type": "Wie Asta sich gegen die Stiche wehrte",
        "text": "Was tat Asta gegen das Jucken der Wespenstiche?",
        "answer": "Sie schuettelte sich die Ohren, rieb die Schnauze am Boden, sauste im Kreis herum und scharrte sich.",
        "steps": [
            "4 Reaktionen aus dem Text auflisten.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 9,
        "type": "Synonym für Wespen",
        "text": "Im Text wird fuer die Wespen auch noch dieses Wort verwendet:",
        "answer": "Stechlustige Brummer.",
        "steps": [
            "Synonym aus dem Text identifizieren.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 10,
        "type": "Helfen zwischen Mensch und Tier",
        "text": (
            "In der Geschichte geht es um das Helfen zwischen Mensch und Tier. "
            "Wer hilft wem? Wie sieht diese Hilfe aus?"
        ),
        "answer": "Die Menschen helfen dem Tier: Sie spritzen Asta mit Wasser nass, um die Wespen zu vertreiben.",
        "steps": [
            "Hilfe-Handlung im Text suchen.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
]

NEW_KNOWLEDGE = []
