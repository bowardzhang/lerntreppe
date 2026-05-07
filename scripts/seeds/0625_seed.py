EXERCISE = {
    "id": "0625",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Thema Legenden – Elisabeth von Thüringen",
    "topic": "Leseverstehen, Legende, Elisabeth, Wunder, Heilige",
    "publisher": "CATLUX",
    "source_pdf": "0625.pdf",
    "answer_pdf": "0625 (1).pdf",
    "total_points": 29.0,
}

LESETEXT = (
    "Thema Legenden: Elisabeth von Thüringen\n\n"
    "Elisabeth, die junge Frau des Landgrafen Ludwig von Thueringen, war ganz "
    "erfuellt von christlicher Liebe. Sie pflegte selbst die Kranken und "
    "Aussaetzigen und baute ihnen ein Spital. Tag fuer Tag speiste sie viele "
    "Notleidende. Ja, sie verkaufte sogar ihre Juwelen und kostbaren Kleider, "
    "um den Armen helfen zu koennen.\n\n"
    "Die Hofleute auf der stolzen Wartburg liebten ein prunkvolles, ueppiges "
    "Leben. Diese Leute beklagten sich oft bei Landgraf Ludwig ueber die "
    "Verschwendung der Fuerstin. Um das Elend im Land kuemmerten sie sich "
    "wenig.\n\n"
    "Doch der Landgraf liebte seine heitere, freigebige Frau. Er lachte nur: "
    "'Mag sie den Armen Gutes tun! Wenn sie uns nur die Wartburg laesst.'\n\n"
    "Aber einmal, so erzaehlt die Legende, soll er doch unwillig geworden sein. "
    "Es war zur Winterzeit. Ludwig kehrte eben von einem Ritt auf die Wartburg "
    "zurueck. Da begegnete ihm Elisabeth. Sie trug im hochgerafften Mantel "
    "Brote, die sie den Armen bringen wollte. 'Was traegst du wieder fort?' "
    "fragte Ludwig barsch. Elisabeth oeffnete ihren Mantel. Da war er mitten im "
    "Winter voll weisser und roter Rosen. Ludwig staunte und freute sich ueber "
    "dieses Wunder. Von da an liebte er Elisabeth noch mehr.\n\n"
    "Gross war Elisabeths Schmerz, als ihr Gatte auf einem Kreuzzug starb. Nun "
    "widmete sie sich noch mehr den Armen und Kranken. Schliesslich lebte sie "
    "ganz bei ihnen. Der Ruf ihrer Barmherzigkeit und Milde verbreitete sich im "
    "ganzen Land.\n\n"
    "Elisabeth starb im Jahre 1231 mit vierundzwanzig Jahren. Schon vier Jahre "
    "spaeter wurde sie heiliggesprochen. Ueber ihrem Grab in Marburg wurde die "
    "erste gotische Kirche in Deutschland gebaut.\n\n"
    "Worterlaeuterungen: Spital = Krankenhaus; Aussaetzige = Menschen, die von "
    "einer lebensgefaehrlichen, ansteckenden Krankheit befallen sind."
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Person nennen",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Von wem handelt diese Legende?"
        ),
        "answer": "Elisabeth von Thueringen.",
        "steps": [
            "Aus dem Titel und ersten Satz.",
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
        "type": "Weitere Legenden nennen",
        "text": "Nenne drei weitere Legenden!",
        "answer": "Z. B.: Die heilige Barbara, der heilige Nikolaus, die heilige Lucia, der heilige Martin.",
        "steps": [
            "Bekannte Heiligenlegenden.",
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
        "type": "Legendenmerkmale mit Textstellen",
        "text": (
            "Woran erkennt man bei diesem Text, dass es sich um eine Legende "
            "handelt? Nenne drei Merkmale von Legenden und beschreibe, wo du sie "
            "in diesem Text findest (Zeilennummer angeben)."
        ),
        "answer": (
            "(1) Wunder: Mitten im Winter blühen die Rosen (Z. 15-16). ; "
            "(2) Religiöse, gottesglaebige Figur: Elisabeth war erfuellt von "
            "christlicher Liebe (Z. 1-2). ; "
            "(3) Heilige: Elisabeth wurde vier Jahre nach ihrem Tod "
            "heiliggesprochen (Z. 22-23)."
        ),
        "steps": [
            "Merkmale einer Legende: Wunder, religiöse Figur, Heiligsprechung.",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 4,
        "type": "Wunder beschreiben",
        "text": "Welches Wunder passiert in dieser Legende? Beschreibe!",
        "answer": (
            "Die Brote der Elisabeth haben sich mitten im Winter in bluehende "
            "weisse und rote Rosen verwandelt, als sie den Mantel oeffnete."
        ),
        "steps": [
            "Aus dem vierten Absatz.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 5,
        "type": "Weitere Wunder",
        "text": "Nenne zwei weitere Wunder, die du aus anderen Legenden kennst!",
        "answer": (
            "Z. B.: Lucia - ihre todkranke Mutter wurde geheilt. ; "
            "Barbara - ein Zweig blueht mitten im Winter. ; "
            "Nikolaus - er hilft den Hungernden."
        ),
        "steps": [
            "Wunder aus bekannten Heiligenlegenden.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 6,
        "type": "Vorbildliches Verhalten",
        "text": (
            "Die Menschen von denen Legenden handeln, sollen uns Vorbilder sein.\n"
            "(a) Warum ist das Verhalten der Frau in dieser Legende vorbildhaft? "
            "Nenne drei Beispiele.\n"
            "(b) Nenne zwei weitere Menschen, von denen Legenden handeln, und "
            "erklaere, warum deren Verhalten fuer uns ein Vorbild sein soll."
        ),
        "answer": (
            "(a) Z. B.: Sie pflegte die Kranken und Aussaetzigen. ; "
            "Sie baute ein Spital. ; "
            "Sie verkaufte ihre Juwelen, um den Armen zu helfen. ; "
            "(b) Z. B.: Barbara - liess sich in der Zeit der Christenverfolgung "
            "taufen. ; Nikolaus - half den hungernden Menschen."
        ),
        "steps": [
            "(a) Drei Beispiele aus dem Text.",
            "(b) Vorbildliche Handlungen anderer Heiliger.",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 7,
        "type": "Legenden und Bräuche",
        "text": (
            "Wir kennen zahlreiche Braeuche, die auf Legenden zurueckgehen. "
            "Nenne die Legende und den zugehoerigen Brauch! (3 Beispiele)"
        ),
        "answer": (
            "Barbara: Wir stellen im Winter einen Kirschzweig ins Wasser. ; "
            "Nikolaus: Wir stellen einen Schuh vor die Tuere. ; "
            "St. Martin: Wir veranstalten einen St. Martins Zug."
        ),
        "steps": [
            "Bekannte Brauchtumstraditionen mit Heiligenlegenden verknuepfen.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 8,
        "type": "Kreatives Schreiben",
        "text": (
            "Elisabeth trug im hochgerafften Mantel Brote. Ludwig fragte barsch: "
            "'Was traegst du wieder fort?' Elisabeth oeffnete ihren Mantel. Was "
            "nun? Soll sie die Wahrheit sagen und dafuer den Tadel ihres Mannes "
            "in Kauf nehmen? Soll sie sich herausreden? Schreibe deine Meinung "
            "auf! Du kannst dir auch ein kleines Gespraech ausdenken."
        ),
        "answer": "Individuelle Loesungsansaetze (freies Schreiben).",
        "steps": [
            "Eigene Gedanken und Argumentation formulieren.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
]

NEW_KNOWLEDGE = []
