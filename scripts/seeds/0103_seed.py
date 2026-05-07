EXERCISE = {
    "id": "0103",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Von Teufelsvögeln und Unglücksraben",
    "topic": "Leseverstehen, Sachtext, Raben, Krähen, Aberglaube",
    "publisher": "CATLUX",
    "source_pdf": "0103.pdf",
    "answer_pdf": "0103 (1).pdf",
    "total_points": 15.0,
}

LESETEXT = (
    "Von Teufelsvögeln und Ungluecksraben\n\n"
    "Kraehen und Raben gehoeren zu den Tieren, die im Laufe der Jahrhunderte "
    "besonders stark vom Menschen verfolgt wurden. Mangelndes Wissen ueber die "
    "Lebensweise dieser Voegel war ein Grund dafuer. Obwohl der Kolkrabe zu "
    "den gefaehrdeten Tierarten gehoert, versuchten noch vor wenigen Jahren "
    "Schafer in Baden-Wuerttemberg die Jagd auf diesen Rabenvogel wieder "
    "durchzusetzen. Die Schafer behaupteten, ein Schwarm junger Kolkraben "
    "haette zahlreiche Laemmer getoetet und ausgewachsenen Schafen die Augen "
    "ausgehackt. Eine wissenschaftliche Untersuchung brachte schliesslich den "
    "Beweis: An den Vorwuerfen war nichts dran. Die Raben waren gerettet.\n\n"
    "Einigermaassen gut kamen Raben bei uns Menschen nur manchmal weg. Ein "
    "seltenes Beispiel hierfuer gibt es in der Religion der alten Germanen. "
    "In ihrer Vorstellung hatte der Goetterchef Odin zwei Raben, Huginn und "
    "Muninn, die jeden Morgen durch die Welt flogen, um fuer ihren Herrn nach "
    "dem Rechten zu sehen.\n\n"
    "Haeufig jedoch waren die rabenschwarzen Voegel bei den aberglaeubischen "
    "Leuten in frueheren Zeiten regelrecht verhasst. Man hielt sie fuer "
    "Teufelsvoegel, die mit dem Boesen im Bunde waren. Nicht zufaellig tauchen "
    "deshalb in zahlreichen alten Sagen und Maerchen Raben als Begleiter des "
    "Teufels auf. Und auch die boesen Hexen haben in diesen Geschichten "
    "zuweilen einen Raben als Gefaehrten.\n\n"
    "Raben galten ausserdem als Ungluecksbringer. Die alten Roemer hielten sie "
    "sogar fuer Todesboten: Setzte sich ein Rabe auf das Hausdach, musste man "
    "befuerchten, dass einer der Bewohner demnaechst sterben wuerde.\n\n"
    "Der schlechte Ruf der Raben hing hauptsaechlich mit ihrer Lebensweise "
    "zusammen: Rabenkraehen haben zum Beispiel die Angewohnheit, Feinden und "
    "toten Tieren die Augen auszuhacken. Hinzu kommt, dass Raben und Kraehen "
    "als Aasfresser natuerlich auch vor dem Fleisch toter Menschen nicht Halt "
    "machen. Deswegen waren sie haeufig auf Schlachtfeldern anzutreffen. Und "
    "auch auf Hinrichtungsstaetten konnte man meist zahlreiche Raben beobachten, "
    "daher der Name 'Galgenvogel'.\n\n"
    "Es ist also kein Wunder, dass der Mensch Rabenvoegel in erster Linie mit "
    "Unglueck, Krieg und Tod in Verbindung brachte. Sie wurden als 'boese "
    "Voegel' abgestempelt, die man ohne Gnade verfolgen und toeten konnte.\n\n"
    "Wie sehr dieses negative Bild vom Ungluecksraben noch bis heute in den "
    "Koepfen der Menschen spukt, zeigt Alfred Hitchcocks beruhmter Gruselfilm "
    "'Die Voegel'. Wohl jedem, der diesen Film einmal gesehen hat, wird etwas "
    "unheimlich, wenn er bei Windstille in der herbstlichen Natur spazieren geht "
    "und ploetzlich merkt, dass die zuvor kahlen Baeume schwarz geworden sind. "
    "Denn unbemerkt haben sich Hunderte von Kraehen auf den Zweigen "
    "niedergelassen. Still sitzen sie auf den Baeumen. Nur hin und wieder ist "
    "ein schnarrender Laut zu hoeren oder ein Rascheln des Gefieders ..."
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Aussage im Text ankreuzen",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Beinahe haetten vor wenigen Jahren Schafer aus Baden-Wuerttemberg "
            "den Kolkraben ein grosses Unrecht angetan. Kreuze an, was richtig "
            "ist (nur was ganz genau so im Text steht):\n"
            "(a) Die Schafer behaupten, der Kolkrabe sei ein Killer.\n"
            "(b) Die Schafer behaupteten, ein Schwarm junger Kolkraben haette "
            "zahlreiche Laemmer getoetet.\n"
            "(c) Die Schafer behaupteten, ein Schwarm junger Kolkraben haette "
            "zahlreiche Schafe getoetet.\n"
            "(d) Politiker setzten sich fuer die Raben ein, damit diese nicht "
            "getoetet werden konnten.\n"
            "(e) Man ging mit Gift und Gewehren gegen die Raben vor.\n"
            "(f) Die Raben hatten in Wirklichkeit nur ein einziges Tier der "
            "Herde getoetet, weil sie hungrig waren."
        ),
        "answer": "Richtig: (b).",
        "steps": [
            "Wortlaut genau pruefen: 'Laemmer' nicht 'Schafe'; (d) falsch: Politiker setzten sich fuer Schafer ein.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 2,
        "type": "Namen der Raben",
        "text": (
            "Wie heissen in der Religion der alten Germanen die beiden Raben "
            "des Gottes Odin? Kreuze an:\n"
            "(a) Hugin und Mumin\n"
            "(b) Hginn und Munnin\n"
            "(c) Hugginn und Muninn\n"
            "(d) Huginn und Muninn\n"
            "(e) Hugin und Munin"
        ),
        "answer": "Richtig: (d) Huginn und Muninn.",
        "steps": [
            "Exakten Wortlaut im Text pruefen.",
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
        "type": "Aufgabe der Raben",
        "text": "Welche Aufgabe hatten die Raben Odins?",
        "answer": (
            "Sie flogen jeden Morgen durch die Welt, um fuer Odin nach dem "
            "Rechten zu sehen (zu berichten, was geschah)."
        ),
        "steps": [
            "Aus dem zweiten Absatz.",
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
        "type": "Raben in Märchen",
        "text": (
            "Woran erkennt man beim Lesen von Maerchen und Sagen, wie sehr "
            "aberglaeubische Menschen die Raben fuerchten oder sogar hassen?"
        ),
        "answer": (
            "In Sagen und Maerchen tauchen Raben als Begleiter des Teufels und "
            "boesen Hexen auf."
        ),
        "steps": [
            "Aus dem dritten Absatz.",
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
        "type": "Römer und Todesboten",
        "text": "Inwiefern hielten die alten Roemer Raben fuer Todesboten?",
        "answer": (
            "Wenn sich ein Rabe auf ein Hausdach setzte, musste man befuerchten, "
            "dass einer der Bewohner demnaechst sterben wuerde."
        ),
        "steps": [
            "Aus dem vierten Absatz.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 6,
        "type": "Verbindung mit Krieg und Tod",
        "text": "Weshalb verbinden Menschen Raben oft mit Krieg und Tod?",
        "answer": (
            "Weil Raben und Kraehen als Aasfresser auch vor dem Fleisch toter "
            "Menschen nicht Halt machen und haeufig auf Schlachtfeldern und "
            "Hinrichtungsstaetten anzutreffen waren."
        ),
        "steps": [
            "Aus dem fuenften Absatz: Aasfresser auf Schlachtfeldern.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 7,
        "type": "Bester Ruf bei welchem Volk?",
        "text": "Bei welchem Volk hatten Raben den besten Ruf? Begruende!",
        "answer": (
            "Bei den Germanen, weil Odin zwei Raben (Huginn und Muninn) als "
            "Boten hatte und sie respektvoll behandelte."
        ),
        "steps": [
            "Aus dem zweiten Absatz: Germanen/Odin.",
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
        "type": "Meinung begründen",
        "text": (
            "Koennte man auch verstehen, dass sich manche Menschen vor dem "
            "Verhalten der Raben gruseln? Begruende deine Meinung mit Hilfe "
            "einer Textstelle!"
        ),
        "answer": (
            "Ja, den Leuten spukt noch immer das Bild vom Ungluecks- oder "
            "Galgenvogel in den Koepfen. Im Text: Alfred Hitchcocks Gruselfilm "
            "'Die Voegel' zeigt, wie das negative Bild bis heute fortlebt."
        ),
        "steps": [
            "Eigene Meinung + Textstelle angeben.",
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
