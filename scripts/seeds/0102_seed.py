EXERCISE = {
    "id": "0102",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Der vergessene Hund",
    "topic": "Leseverstehen, Erzählung, Hund, Kaufhaus, Gefühle",
    "publisher": "CATLUX",
    "source_pdf": "0102.pdf",
    "answer_pdf": "0102 (1).pdf",
    "total_points": 14.0,
}

LESETEXT = (
    "Der vergessene Hund\n\n"
    "Der kleine, braungefleckte Hund drueckt sich aengstlich an die Hauswand. "
    "Er liegt neben einem Papierkorb, festgebunden an einem Eisenring.\n\n"
    "Rechts von ihm befindet sich der Eingang in ein grosses Kaufhaus, links "
    "ist die Einfahrt zu einer Autowerkstatt.\n\n"
    "Staendig laufen unzaehlige Menschenbeine an ihm vorbei. Sie laufen in das "
    "Kaufhaus rein und wieder raus. Und immer hofft der Hund, dass zwei Beine "
    "kommen und vor ihm stehen bleiben werden. Zwei Beine, die zu einem "
    "Maedchen gehoeren, das er von ganzem Herzen liebt.\n\n"
    "Das junge Maedchen hat den Hund aber vergessen. Im Kaufhaus hat sie nicht "
    "bekommen, was sie wollte, und deshalb ist sie in ein naechstes und "
    "uebernaechstes Kaufhaus und immer weiter gelaufen.\n\n"
    "Erst hat dem Hund das Warten nichts ausgemacht. Er hat dem vertrauten "
    "Geruch des Maedchens hinterher geschnueffelt und sich dann abwartend auf "
    "seine Hinterpfoten gesetzt. Sich hinzulegen, hat er nicht gewagt, weil er "
    "die Rueckkehr des Maedchens auf keinen Fall verpassen wollte. Am Anfang "
    "hat er die Nase noch neugierig gegen die hin- und herlaufenden Menschen "
    "ausgestreckt, denn ein Hund lernt die Welt ja hauptsaechlich durch seine "
    "Nase kennen, nicht durch seine Augen.\n\n"
    "Dann aber hat der kleine Hund ein paar schlimme Hiebe durch schwere "
    "Plastiktueten und Einkaufstaschen mitten auf die Schnauze gekriegt und "
    "sich verstoert zurueckgezogen. Irgendwann ist ein stinkendes Auto gekommen "
    "und hat beinahe die Wand gestreift, an der der Hund liegt. Seitdem "
    "zittert er vor Angst.\n\n"
    "Manchmal bleibt von den vorbeilaufenden Menschen jemand bei dem Hund "
    "stehen und sagt ihm ein freundliches Wort. Dann streckt der Hund seinen "
    "Kopf zum Eingang des Kaufhauses und winselt klaerglich. Da er sich im "
    "Uebrigen von keinem anfassen laesst, verliert, wer auf ihn aufmerksam "
    "wird, schnell die Lust, sich laenger mit ihm zu befassen.\n\n"
    "So liegt der kleine, braungefleckte Hund nach vielen Stunden noch immer "
    "auf der Strasse, eng an die Wand gepresst und zitternd. Es beginnt dunkel "
    "zu werden. Jetzt weint und winselt der vergessene Hund laengst nicht mehr. "
    "Er liegt nur da, zittert und seufzt manchmal so tief, wie nur einer "
    "seufzen kann, der den schlimmsten Kummer ganz allein aushalten muss.\n\n"
    "Da trippeln ploetzlich eilige Schritte naeher und naeher und eine helle "
    "Stimme, in der Verzweiflung mitschwingt und Hoffnung, ruft: 'Puenktchen, "
    "mein Puenktchen - bist du noch hier?'\n\n"
    "Da springt der kleine braungefleckte Hund vor Freude so hoch, dass seine "
    "Leine wie von Geisterhand geloest aus dem Eisenring rutscht. Und dann "
    "rennt, nein fliegt der kleine Hund dem Maedchen entgegen."
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Name des Hundes",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Wie heisst der Hund?"
        ),
        "answer": "Er heisst Puenktchen.",
        "steps": [
            "Am Ende des Textes: 'Puenktchen, mein Puenktchen'.",
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
        "type": "Name erklärt",
        "text": "Warum wird er so genannt?",
        "answer": "Er hat braune Flecken (Punkte) auf seinem Fell.",
        "steps": [
            "Aus dem Text: 'braungefleckt' => Puenktchen.",
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
        "type": "Warum vergessen?",
        "text": "Warum hat das Maedchen den Hund vor dem Kaufhaus vergessen?",
        "answer": (
            "Im Kaufhaus hat sie nicht bekommen was sie wollte und ist deshalb "
            "in ein naechstes und uebernaechstes Kaufhaus weitergegangen."
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
        "n": 4,
        "type": "Warum nicht hinterherlaufen?",
        "text": "Warum laeuft der Hund dem Maedchen nicht einfach hinterher?",
        "answer": "Er war festgebunden (an einem Eisenring).",
        "steps": [
            "Aus dem ersten Absatz.",
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
        "type": "Nur Beine bemerken",
        "text": (
            "Warum bemerkt der Hund nur die Beine der Menschen, als er vor "
            "dem Kaufhaus wartet?"
        ),
        "answer": "Er ist sehr klein und sitzt auf dem Boden, deshalb sieht er nur Beine.",
        "steps": [
            "Schlussfolgerung aus der Beschreibung.",
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
        "type": "Satz unterstreichen",
        "text": (
            "Fuer den Hund ist die Nase wichtiger als das Auge. "
            "Unterstreiche den passenden Satz im Text!"
        ),
        "answer": (
            "'Am Anfang hat er die Nase noch neugierig gegen die hin- und "
            "herlaufenden Menschen ausgestreckt, denn ein Hund lernt die Welt "
            "ja hauptsaechlich durch seine Nase kennen, nicht durch seine Augen.'"
        ),
        "steps": [
            "Im fuenften Absatz nachschauen.",
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
        "type": "Schlimme Dinge benennen",
        "text": (
            "'Erst hat dem Hund das Warten nichts ausgemacht.' Doch dann "
            "passieren schlimme Dinge und 'seitdem zittert er vor Angst.' "
            "Was ist geschehen? Nenne zwei Ereignisse."
        ),
        "answer": (
            "1. Er bekam Hiebe durch schwere Plastiktueten auf die Schnauze. ; "
            "2. Ein stinkendes Auto kam und streifte beinahe die Wand, an der er liegt."
        ),
        "steps": [
            "Aus dem sechsten Absatz: Tueten und Auto.",
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
        "type": "Multiple Choice: warum niemand hilft",
        "text": (
            "Manche Leute kuemmern sich um den ungluecklichen Hund. Warum gibt "
            "sich keiner lange mit ihm ab? Kreuze den passenden Satz an:\n"
            "(a) Er laesst sich von keinem anfassen.\n"
            "(b) Der Hund bellt unertraeglich.\n"
            "(c) Die Menschen verstehen nicht, warum der Hund winselt.\n"
            "(d) Der Hund ist furchtbar schmutzig und voller Floehe."
        ),
        "answer": "Richtig: (a).",
        "steps": [
            "Aus dem siebten Absatz: 'da er sich im Uebrigen von keinem anfassen laesst'.",
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
        "type": "Verben unterstreichen",
        "text": (
            "Der Hund ist ungluecklich, als er so lange warten muss. "
            "Unterstreiche 4 passende Verben im Text!"
        ),
        "answer": "zittert, winselt, weint, seufzt.",
        "steps": [
            "Verben, die Unglueck/Leid ausdruecken.",
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
        "type": "Gefühle der Stimme",
        "text": (
            "Als das Maedchen zum Hund zurueckkommt, kann man aus ihrer "
            "Stimme zwei Gefuehle hoeren. Welche?"
        ),
        "answer": "1. Verzweiflung. 2. Hoffnung.",
        "steps": [
            "Aus dem Text: 'in der Verzweiflung mitschwingt und Hoffnung'.",
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
