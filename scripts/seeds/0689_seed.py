EXERCISE = {
    "id": "0689",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Wie die kleine Wasserspinne das Feuer holte",
    "topic": "Leseverstehen, Märchen/Fabel, Tiere, Wortarten",
    "publisher": "CATLUX",
    "source_pdf": "0689.pdf",
    "answer_pdf": "0689 (1).pdf",
    "total_points": 28.0,
}

LESETEXT = (
    "Wie die kleine Wasserspinne das Feuer holte (Auszug)\n\n"
    "Am Anfang gab es kein Feuer und die Welt war kalt. Alle Tiere froren ganz "
    "entsetzlich. Eines Tages tobte ein fuerchterliches Gewitter über der "
    "Erde, grelle Blitze zuckten über den Himmel und der Donner grollte. "
    "Ploetzlich schlug ein Blitz in eine alte, abgestorbene Eiche ein, die "
    "trockene Rinde entzuendete sich und der Baum stand sofort in lodernden "
    "Flammen.\n\n"
    "Nun freuten sich die Tiere und sagten: 'Von dieser brennenden Eiche werden "
    "wir uns Feuer holen. Endlich werden wir uns waermen können.' Dieser Baum "
    "stand jedoch auf einer Insel und die Tiere konnten wegen des tiefen "
    "Wassers nicht herankommen.\n\n"
    "Der Rabe flog als erster und versengte sich die Federn, bis sie ganz "
    "schwarz waren. Die kleine Schleiereule blickte in den hohlen Baum, ein "
    "heisser Luftstrom brannte ihr beinahe die Augen aus - ihre Augen sind rot "
    "bis auf den heutigen Tag. Die Barteule und die Horneule kehrten ohne Feuer "
    "zurück; weisse Ringe um ihre Augen blieben. Auch die schwarze Schlange "
    "und die gruene Natter scheiterten.\n\n"
    "Endlich erklaerte sich die kleine Wasserspinne bereit: 'Ich weiß, wie ich "
    "es mache.' Sie spann einen Faden aus ihrem Körper und webte eine kleine, "
    "runde Tasche, die sie auf ihrem Ruecken befestigte. Dann schwamm sie zur "
    "Insel, legte ein winziges Stueckchen gluehende Holzkohle in ihre Tasche "
    "und kam damit eilends zurück. Nun konnten sich die Tiere endlich waermen."
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Tiere in der Geschichte ankreuzen",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Welche Tiere kommen in der Geschichte vor? Kreuze an:\n"
            "(a) Rabe ; (b) Fische ; (c) Schleiereule ; (d) Hornnatter"
        ),
        "answer": "Richtig: (a) Rabe und (c) Schleiereule.",
        "steps": [
            "(a) Rabe: ja, kommt vor.",
            "(b) Fische: nein.",
            "(c) Schleiereule: ja.",
            "(d) Hornnatter: nein (es kommen Horneule und gruene Natter vor, aber keine Hornnatter).",
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
        "type": "Warum wollten die Tiere das Feuer?",
        "text": "Warum wuenschten sich die Tiere das Feuer? Begruende in ganzen Sätzen.",
        "answer": "Die Tiere froren, weil es kalt war, und sie wollten sich waermen.",
        "steps": [
            "Aus dem Anfang des Textes: 'Am Anfang gab es kein Feuer und die Welt war kalt. Alle Tiere froren'.",
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
        "type": "Warum scheiterte der Rabe?",
        "text": "Warum konnte der grosse, starke Rabe das Feuer nicht holen?",
        "answer": "Weil er sich beim Annaehern an die Flammen die Federn versengte und sich fuerchtete.",
        "steps": [
            "Hinweis im Text: 'als sich die Flammen naeherten, versengte er sich die Federn'.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 4,
        "type": "Wie kam das Feuer?",
        "text": (
            "Wo kam das Feuer ploetzlich her? Kreuze die richtige Antwort an:\n"
            "(a) Die Tiere fanden ein Feuerholz.\n"
            "(b) Der Rabe brachte es den Tieren.\n"
            "(c) Ein Blitz schlug in einen Baum ein, der sofort zu brennen begann."
        ),
        "answer": "Richtig: (c) Ein Blitz schlug in einen Baum ein, der sofort zu brennen begann.",
        "steps": [
            "Direkt aus dem Text: 'schlug ein Blitz in eine alte, abgestorbene Eiche ein'.",
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
        "type": "Zitat aus dem Text",
        "text": (
            "Was sagten die Tiere, als sie das Feuer sahen? Schreibe ganze "
            "Sätze aus dem Text."
        ),
        "answer": (
            "'Von dieser brennenden Eiche werden wir uns Feuer holen. Endlich "
            "werden wir uns waermen können.'"
        ),
        "steps": [
            "Originalzitate verwenden.",
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
        "type": "Schwierigkeit erklären",
        "text": "Warum war es so schwer, Feuer von dem brennenden Baum zu holen?",
        "answer": "Der brennende Baum stand auf einer Insel. Die Tiere mussten durch tiefes Wasser, das viele Tiere nicht durchqueren konnten.",
        "steps": [
            "Lokales Hindernis: Insel und tiefes Wasser.",
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
        "type": "Eulen mit weißen Ringen",
        "text": (
            "Warum haben die Eulen, wenn man der Geschichte glaubt, grosse "
            "weisse Ringe um die Augen?"
        ),
        "answer": "Weil der Wind die heisse Asche um ihre Augen blies.",
        "steps": [
            "Aus dem Text: 'Die heisse Asche, die der Wind hinauf blies, machte weisse Ringe um ihre Augen.'",
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
        "type": "Richtige Sätze ankreuzen",
        "text": (
            "Kreuze die richtigen Sätze an:\n"
            "(1) Der Rabe versuchte als erster Feuer zu holen.\n"
            "(2) Die Schleiereule hatte keine Lust, das Feuer zu holen.\n"
            "(3) Der brennende Baum stand in einem tiefen Sumpf.\n"
            "(4) Die Spinne webte sich eine Tasche, in die sie ein Stueck "
            "Holzkohle tat.\n"
            "(5) Die Augen der Horneule sind rot bis auf den heutigen Tag."
        ),
        "answer": "Richtig: (1) und (4).",
        "steps": [
            "(2) falsch: Die Schleiereule wollte gehen.",
            "(3) falsch: Der Baum stand auf einer Insel.",
            "(5) falsch: Die Augen der Schleiereule sind rot, nicht der Horneule.",
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
        "type": "Wer holte das Feuer und wie?",
        "text": (
            "Wer schafft es schließlich, das Feuer zu holen? Wie gelingt das? "
            "Erklaere in ganzen Sätzen."
        ),
        "answer": (
            "Die kleine Wasserspinne holt das Feuer. Sie webt eine kleine Tasche "
            "aus ihrem Faden und befestigt sie auf ihrem Ruecken. Dann schwimmt "
            "sie zur Insel, legt ein winziges Stueckchen gluehende Holzkohle in "
            "die Tasche und kommt damit zurück."
        ),
        "steps": [
            "Schritte: weben, schwimmen, Holzkohle holen, zurueckkehren.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 10,
        "type": "Ausdrücke erklären",
        "text": (
            "(a) Erklaere die Bedeutung von '...versengte sich die Federn'.\n"
            "(b) Was sind 'vierfuessige Tiere'? Nenne 2 Beispiele."
        ),
        "answer": (
            "(a) Der Rabe verbrannte sich die Federn (sie wurden angesengt). ; "
            "(b) Tiere mit 4 Beinen, z. B. Wolf, Katze, Tiger, Hund."
        ),
        "steps": [
            "(a) 'versengen' = leicht verbrennen.",
            "(b) 'vierfuessig' = 4 Beine.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 11,
        "type": "Wer sagt was?",
        "text": (
            "'Ich weiß, wie ich es mache' - Wer sagt das und was ist damit "
            "gemeint?"
        ),
        "answer": (
            "Die Wasserspinne sagt das. Sie meint damit, dass sie einen Weg "
            "kennt, das Feuer zu holen (mit ihrer gewebten Tasche)."
        ),
        "steps": [
            "Direkt im Text identifizieren.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 12,
        "type": "Gegenteile finden",
        "text": (
            "Finde im Text das Wort, das das Gegenteil bedeutet:\n"
            "(a) jung\n"
            "(b) feige\n"
            "(c) wertlos"
        ),
        "answer": "(a) alt ; (b) mutig ; (c) kostbar",
        "steps": [
            "Suche im Text Synonyme bzw. Gegenteile.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
            "deutsch.klasse4.grammatik.wortarten",
        ],
    },
    {
        "n": 13,
        "type": "Wortarten unterstreichen",
        "text": (
            "Unterstreiche in der Geschichte 2 Nomen (gruen), 2 Verben (blau) "
            "und 2 Adjektive (gelb)."
        ),
        "answer": (
            "Beispiele: Nomen: 'Wasserspinne', 'Feuer'. "
            "Verben: 'froren', 'tobte'. "
            "Adjektive: 'kalt', 'grelle'."
        ),
        "steps": [
            "Nomen: Lebewesen, Dinge, Ideen.",
            "Verben: Taetigkeitswoerter.",
            "Adjektive: Eigenschaftswoerter.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.wortarten",
        ],
    },
    {
        "n": 14,
        "type": "Aussage der Geschichte",
        "text": "Was zeigt uns die Geschichte?",
        "answer": (
            "Auch jemand, der klein ist (nicht groß und stark), kann grosse "
            "Taten vollbringen."
        ),
        "steps": [
            "Lehre/Moral der Fabel formulieren.",
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
