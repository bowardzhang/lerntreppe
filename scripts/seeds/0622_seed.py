EXERCISE = {
    "id": "0622",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Der Löwe, der Esel und der Fuchs",
    "topic": "Leseverstehen, Fabel, Aesop, Tiere, Löwenanteil",
    "publisher": "CATLUX",
    "source_pdf": "0622.pdf",
    "answer_pdf": "0622 (1).pdf",
    "total_points": 28.0,
}

LESETEXT = (
    "Der Loewe, der Esel und der Fuchs (nach Aesop)\n\n"
    "Ein Loewe, ein Fuchs und ein Esel gingen miteinander auf die Jagd. Als sie "
    "nun reichlich Beute gemacht hatten, befahl der Loewe dem Esel, diese zu "
    "verteilen. Dieser gehorchte und zerlegte alles in drei gleich grosse Teile. "
    "Dann forderte er den Koenig der Tiere auf, selbst einen Teil auszuwaehlen. "
    "Da aber wurde der Loewe wild, zerriss den Esel und befahl nun dem Fuchs zu "
    "teilen. Dieser haeufte alles zusammen, legte den Esel obenauf und erbat "
    "sich nur etwas Weniges fuer seine Muehe. 'Schoen, mein Freund', sagte der "
    "Loewe schmunzelnd, 'sage mir doch, wer hat dich so schoen teilen gelehrt?' "
    "Der listige Fuchs antwortete: 'Nun, das Schicksal des Esels.'"
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Adjektive finden",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "In der Geschichte kommen verschiedene Tiere vor. Finde je zwei "
            "Adjektive, die sie beschreiben!\n"
            "Loewe: ___ / ___\n"
            "Esel: ___ / ___\n"
            "Fuchs: ___ / ___"
        ),
        "answer": (
            "Loewe: unfreundlich, gebieterisch (herrisch, wild). ; "
            "Esel: gutmutig, dumm (naiv, gehorssam). ; "
            "Fuchs: schlau, listig (clever, klug)."
        ),
        "steps": [
            "Adjektive aus dem Verhalten der Tiere ableiten.",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 2,
        "type": "Verteilung des Esels",
        "text": "Der Esel bekommt den Auftrag, die Beute zu verteilen. Wie macht er das genau?",
        "answer": "Er gehorcht und zerlegt alles in drei gleich grosse Teile.",
        "steps": [
            "Direkt aus dem Text.",
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
        "type": "Reaktion des Löwen",
        "text": (
            "(a) Nenne einen Grund, warum der Loewe wuetend wurde.\n"
            "(b) Wie reagierte er?"
        ),
        "answer": (
            "(a) Er wollte selbst am meisten haben / der Esel hat fair geteilt, "
            "was dem Loewen nicht passte. ; "
            "(b) Er wurde wild und zerriss den Esel."
        ),
        "steps": [
            "Aus dem Text: gerechte Teilung gefiel dem Loewen nicht.",
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
        "type": "Verteilung des Fuchses",
        "text": "Wie verteilt der Fuchs die Beute?",
        "answer": "Er gibt fast alles dem Loewen und behaelt fuer sich nur wenig.",
        "steps": [
            "Aus dem Text: 'haeufte alles zusammen ... erbat sich nur etwas Weniges'.",
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
        "type": "Stimmung des Löwen",
        "text": (
            "(a) In welcher Stimmung ist jetzt der Loewe?\n"
            "(b) Warum schmunzelt er?"
        ),
        "answer": (
            "(a) Der Loewe ist zufrieden. ; "
            "(b) Weil er am meisten bekommt und sich fuer sehr schlau haelt."
        ),
        "steps": [
            "Aus dem Text: 'Der Loewe schmunzelnd'.",
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
        "type": "Zufriedenheit begründen",
        "text": (
            "Waren Loewe und Fuchs mit der Teilung am Schluss zufrieden? "
            "Nenne fuer jedes Tier einen Grund."
        ),
        "answer": (
            "Der Loewe war zufrieden, weil er am meisten bekommen hat. ; "
            "Der Fuchs war zufrieden, weil er noch am Leben ist."
        ),
        "steps": [
            "Beider Motivation aus dem Text erschliessen.",
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
        "type": "Lehre des Fuchses",
        "text": "Was lernt der Fuchs aus dem Verhalten des Loewens?",
        "answer": (
            "Dass man dem Maechtigsten nicht widersetzen darf und auf sich selbst "
            "achten muss (man kann niemanden blind vertrauen)."
        ),
        "steps": [
            "Moral der Fabel: 'Das Schicksal des Esels' war sein Lehrer.",
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
        "type": "Textsorte erkennen",
        "text": (
            "(a) Diese Geschichte gehoert in der Literatur zur Gruppe der ...\n"
            "(b) Kennst du noch andere solche Geschichten? Nenne 2!\n"
            "(c) Nenne die Kennzeichen dieser Textsorte."
        ),
        "answer": (
            "(a) Fabel. ; "
            "(b) Z. B. 'Der Fuchs und die Katze', 'Der Rabe und der Fuchs', "
            "'Der Hase und der Igel'. ; "
            "(c) Tiere koennen sprechen und denken; Tiere haben menschliche "
            "Eigenschaften; kurzer Text; hat eine Lehre (Moral)."
        ),
        "steps": [
            "Merkmale einer Fabel: sprechende Tiere, Moral, kurz.",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 9,
        "type": "Erzählerabsicht",
        "text": "Der Erzaehler dieser Geschichte beabsichtigt bei den Zuhoerern zweierlei. Was?",
        "answer": "Unterhaltung und eine Lehre (Moral) vermitteln.",
        "steps": [
            "Typische Funktionen von Fabeln.",
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
        "type": "Löwenanteil erklären",
        "text": (
            "Jetzt weisst du, warum wir auch heute noch manchmal von einem "
            "'Loewenanteil' sprechen. Was meinen wir damit?"
        ),
        "answer": "Wenn man von etwas das Meiste bekommt, also den groessten Anteil.",
        "steps": [
            "Aus der Geschichte ableiten: Loewe bekommt am meisten.",
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
