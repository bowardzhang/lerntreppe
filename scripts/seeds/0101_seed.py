EXERCISE = {
    "id": "0101",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Das Märchen vom Igel",
    "topic": "Leseverstehen, Märchen, Freundschaft, Dürre",
    "publisher": "CATLUX",
    "source_pdf": "0101.pdf",
    "answer_pdf": "0101 (1).pdf",
    "total_points": 15.0,
}

LESETEXT = (
    "Das Märchen vom Igel (von Can Göknil)\n\n"
    "Einst lebte ein Igel im Wald. Der hatte so viele Stacheln, dass ihn "
    "niemand zum Freund haben wollte. Er spazierte ganz allein im Wald "
    "umher. 'Vielleicht finde ich einen Freund', dachte er sich.\n\n"
    "Als die Giraffe ihn sah, sagte sie: 'Um Himmels willen! Verstecken wir "
    "uns schnell!' Das Nilpferd meinte: 'Tun wir, als ob wir diesen "
    "stacheligen Igel nicht bemerken!' Sogar der Regenwurm verbarg sich "
    "hinter einem Baum. Die Schildkroete und die Schnecke verkrochen sich in "
    "ihren Haeusern; der Ruesselkaefer vergrub sich in der Erde. Der Uhu "
    "sagte: 'Bitte, belaestigen Sie mich nicht, ich bin müde.' Der Igel "
    "kehrte nach Hause zurück. Die ganze Nacht über war er traurig: 'Ich "
    "bin so allein, so allein', dachte er.\n\n"
    "Im Land, in dem der Igel wohnte, hatte es lange, lange Zeit nicht "
    "geregnet. Als der Tag anbrach, standen die Enten betruebst vor dem "
    "ausgetrockneten See, in dem sie nun nicht mehr schwimmen konnten. Der "
    "Elefant, benommen von der starken Hitze, war an das Seeufer gekommen, "
    "um sich zu duschen; aber am Seegrund war nur mehr so wenig Wasser, dass "
    "sein Ruessel voll Schlamm und Erde wurde.\n\n"
    "Ein alter Vogel sagte: 'Unsere Lage ist sehr ernst. Wir müssen ein "
    "Mittel gegen diese Duerre finden.' Da kam dem Igel eine Idee. Muehsam "
    "kletterte er auf die Spitze des hoechsten Berges. Dann stellte er seine "
    "Stacheln hoch und sprang und huepfte mit aller Kraft, bis er am Himmel "
    "viele Loecher gemacht hatte. Und aus diesen Loechern begann es "
    "tatsaechlich in großen Tropfen zu regnen. Der Regen wurde immer "
    "heftiger. Es regnete und regnete, mehrere Tage lang. Die Tiere waren "
    "sehr erleichtert. 'Der Igel hat uns geholfen', sagten sie. 'Es ist doch "
    "nuetzlich, wenn man Stacheln hat', sagte der alte Vogel, und von dem "
    "Tag hatte der Igel viele Freunde."
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Autor nennen",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Wie heißt der Autor dieses Märchens?"
        ),
        "answer": "Can Göknil.",
        "steps": [
            "Autorenangabe im Text lesen.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 2,
        "type": "Erstes Tier nennen",
        "text": "Auf welches Tier trifft der Igel im Wald zuerst?",
        "answer": "Die Giraffe.",
        "steps": [
            "Im zweiten Absatz nachlesen.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 3,
        "type": "Verhalten begründen",
        "text": "Warum verbarg sich der Regenwurm hinter einem Baum?",
        "answer": "Er wollte den Igel nicht treffen (er hatte Angst vor den Stacheln).",
        "steps": [
            "Aus dem Verhalten der anderen Tiere schliessen.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 4,
        "type": "Traurigkeit begründen",
        "text": "Warum war der Igel so traurig?",
        "answer": "Er war traurig, weil er so allein war.",
        "steps": [
            "Aus dem Text: 'Ich bin so allein, so allein'.",
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
        "type": "Land beschreiben",
        "text": "In welchem Land lebte der Igel?",
        "answer": "In einem Land, in dem es lange, lange Zeit nicht geregnet hatte.",
        "steps": [
            "Aus dem dritten Absatz.",
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
        "type": "Betrübnis der Enten",
        "text": "Warum standen die Enten betruebst vor dem ausgetrockneten See?",
        "answer": "Sie konnten nicht mehr schwimmen, weil der See ausgetrocknet war.",
        "steps": [
            "Aus dem dritten Absatz.",
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
        "type": "Ernsthaftigkeit der Lage",
        "text": "Warum glaubt der alte Vogel, dass die Lage der Tiere ernst ist?",
        "answer": "Weil eine Duerre herrschte: kein Wasser mehr im See, extreme Hitze.",
        "steps": [
            "Aus dem letzten Absatz.",
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
        "type": "Hilfe des Igels erklären",
        "text": "Wie hilft der Igel allen aus der Notlage?",
        "answer": (
            "Der Igel klettert auf den hoechsten Berg, stellt seine Stacheln hoch "
            "und springt, bis er Loecher in den Himmel macht, aus denen es regnet."
        ),
        "steps": [
            "Schritte: auf Berg klettern, Stacheln hochstellen, springen, Loecher machen, Regen.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 9,
        "type": "Satzanfänge vervollständigen",
        "text": (
            "Vollende folgende Satzanfaenge sinnvoll:\n"
            "(a) Der Igel spazierte im Wald, um ___\n"
            "(b) Der Uhu behauptete, er sei zu müde, weil ___"
        ),
        "answer": (
            "(a) Der Igel spazierte im Wald, um Freunde zu finden. ; "
            "(b) Der Uhu behauptete, er sei zu müde, weil er den Igel nicht mochte."
        ),
        "steps": [
            "(a) Ziel des Igels aus dem Text.",
            "(b) Vorwand des Uhus erschliessen.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 10,
        "type": "Lehre ankreuzen",
        "text": (
            "Kreuze die Sätze an, die die Lehre der Geschichte enthalten:\n"
            "(a) Traue deinen Freunden nicht!\n"
            "(b) Nur der hat Freunde, der sich für sie auch einsetzt.\n"
            "(c) Habe keine Vorurteile!\n"
            "(d) Auf Freunde kann man sich nicht verlassen."
        ),
        "answer": "Richtig: (b) und (c).",
        "steps": [
            "(b) Der Igel setzt sich für alle ein und bekommt dafuer Freunde.",
            "(c) Die Tiere hatten Vorurteile wegen der Stacheln.",
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
