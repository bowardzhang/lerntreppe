EXERCISE = {
    "id": "0698",
    "subject": "Deutsch",
    "grade": 4,
    "title": "2. Lernzielkontrolle: Wortarten, Redesätze, Zeiten, Satzglieder, Pronomen, Bindewörter",
    "topic": "Wortarten bestimmen, wörtliche Rede, Zeitformen, Satzglieder, Pronomen, Konjunktionen",
    "publisher": "CATLUX",
    "source_pdf": "0698.pdf",
    "answer_pdf": "0698 (1).pdf",
    "total_points": 45.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Wortarten bestimmen",
        "text": (
            "Bestimme die Wortarten der unterstrichenen Wörter im Satz:\n"
            "'Heute hatte ich ein paar Minuten verschlafen, deshalb brachte mich "
            "meine Mutter mit dem Auto schnell zur Grundschule.'\n"
            "Ich: ___\n"
            "Minuten: ___\n"
            "brachte: ___\n"
            "meine: ___\n"
            "dem: ___\n"
            "schnell: ___\n"
            "Grundschule: ___"
        ),
        "answer": (
            "Ich = Personalpronomen ; "
            "Minuten = abstraktes Nomen ; "
            "brachte = Verb ; "
            "meine = Possessivpronomen ; "
            "dem = bestimmter Artikel ; "
            "schnell = Adjektiv ; "
            "Grundschule = zusammengesetztes Nomen"
        ),
        "steps": [
            "Ich → Personalpronomen.",
            "Minuten → abstraktes Nomen.",
            "brachte → Verb (Vergangenheit von 'bringen').",
            "meine → Possessivpronomen.",
            "dem → bestimmter Artikel (Dativ).",
            "schnell → Adjektiv.",
            "Grundschule → zusammengesetztes Nomen (Grund + Schule).",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.wortarten",
        ],
    },
    {
        "n": 2,
        "type": "Satzzeichen und Redesätze",
        "text": (
            "a) Setze alle fehlenden Satzzeichen ein.\n"
            "b) Unterstreiche die Redesätze.\n\n"
            "Los mach schnell rief ich ihr zu Doch sie bleibt ganz ruhig und "
            "meinte Hast du Angst zu spät zu kommen"
        ),
        "answer": (
            "„Los, mach schnell!“, rief ich ihr zu. Doch sie bleibt ganz ruhig "
            "und meinte: „Hast du Angst, zu spät zu kommen?“"
        ),
        "steps": [
            "Erster Redesatz endet mit Ausrufezeichen, danach Begleitsatz.",
            "Zweiter Redesatz beginnt nach Doppelpunkt und Anführungszeichen.",
            "Frage am Ende → Fragezeichen.",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.rechtschreibung.gross_klein",
        ],
    },
    {
        "n": 3,
        "type": "Zeitformen umwandeln",
        "text": (
            "'Ich saß sehr unruhig im Auto, doch schließlich waren wir am Ziel.'\n"
            "a) Setze diesen Satz in die Gegenwart.\n"
            "b) Setze diesen Satz in die 2. Vergangenheit.\n"
            "c) Setze diesen Satz in die Zukunft."
        ),
        "answer": (
            "a) Ich sitze sehr unruhig im Auto, doch schließlich sind wir am Ziel. ; "
            "b) Ich bin sehr unruhig im Auto gesessen, doch schließlich sind wir am Ziel gewesen. ; "
            "c) Ich werde sehr unruhig im Auto sitzen, doch schließlich werden wir am Ziel sein."
        ),
        "steps": [
            "Gegenwart: saß → sitze ; waren → sind.",
            "2. Vergangenheit (Perfekt): saß → bin … gesessen ; waren → sind … gewesen.",
            "Zukunft (Futur): saß → werde sitzen ; waren → werden sein.",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.zeiten",
        ],
    },
    {
        "n": 4,
        "type": "Satzglieder bestimmen",
        "text": (
            "Bestimme alle Satzglieder im Satz und markiere sie:\n"
            "'Nun rangierte meine Mutter das Auto vorsichtig in eine Parklücke.'"
        ),
        "answer": (
            "Nun = adverbiale Bestimmung der Zeit ; "
            "rangierte = Satzaussage (Prädikat) ; "
            "meine Mutter = Satzgegenstand (Subjekt, 1. Fall) ; "
            "das Auto = Akkusativobjekt (4. Fall) ; "
            "vorsichtig = adverbiale Bestimmung der Art und Weise ; "
            "in eine Parklücke = adverbiale Bestimmung des Ortes"
        ),
        "steps": [
            "'Wann?' → Nun (Zeit).",
            "Verb 'rangierte' → Satzaussage.",
            "'Wer?' → meine Mutter (Subjekt).",
            "'Wen/was rangierte?' → das Auto (Akkusativ).",
            "'Wie?' → vorsichtig (Art und Weise).",
            "'Wohin?' → in eine Parklücke (Ort).",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.satzglieder",
        ],
    },
    {
        "n": 5,
        "type": "Satzgegenstand und Satzaussage",
        "text": (
            "Bestimme in jedem Satz den Satzgegenstand (blau) und die "
            "Satzaussage (rot):\n"
            "1. Sofort sprang ich aus dem Auto und lief zu meinem Klassenzimmer.\n"
            "2. Zum Glück waren Max und Hansi noch in der Garderobe.\n"
            "3. Schon ertönte schrill die Schulhausglocke.\n"
            "4. Gerade noch rechtzeitig setzten wir uns auf unseren Platz."
        ),
        "answer": (
            "1. Sg: ich ; Sa: sprang … (und) lief. "
            "2. Sg: Max und Hansi ; Sa: waren. "
            "3. Sg: die Schulhausglocke ; Sa: ertönte. "
            "4. Sg: wir ; Sa: setzten (uns)."
        ),
        "steps": [
            "Frage 'Wer/was?' → Satzgegenstand (Subjekt).",
            "Frage 'Was tut/tat …?' → Satzaussage (Prädikat).",
            "Bei mehrteiligem Prädikat alle Teile markieren.",
        ],
        "points": 4.5,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.satzglieder",
        ],
    },
    {
        "n": 6,
        "type": "Zeitentabelle",
        "text": (
            "Vervollständige die Tabelle mit dem richtigen Personalpronomen.\n"
            "Gegenwart            | 1. Vergangenheit | 2. Vergangenheit | Zukunft\n"
            "ich laufe            | ___              | ___              | ___\n"
            "___                  | ___              | er hat geworfen  | ___\n"
            "___                  | du nahmst        | ___              | ___"
        ),
        "answer": (
            "ich laufe / ich lief / ich bin gelaufen / ich werde laufen ; "
            "er wirft / er warf / er hat geworfen / er wird werfen ; "
            "du nimmst / du nahmst / du hast genommen / du wirst nehmen"
        ),
        "steps": [
            "laufen: laufe – lief – bin gelaufen – werde laufen.",
            "werfen: wirft – warf – hat geworfen – wird werfen.",
            "nehmen: nimmst – nahmst – hast genommen – wirst nehmen.",
        ],
        "points": 4.5,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.zeiten",
        ],
    },
    {
        "n": 7,
        "type": "Personal- und Possessivpronomen",
        "text": (
            "Markiere alle Personalpronomen blau und alle Possessivpronomen rot:\n"
            "euer  Sie  die  mein\n"
            "es    unser  du  sei"
        ),
        "answer": (
            "Personalpronomen: Sie, es, du. "
            "Possessivpronomen: euer, mein, unser. "
            "Keines: die (Artikel/Relativpronomen), sei (Verbform)."
        ),
        "steps": [
            "Personalpronomen ersetzen Personen/Dinge: Sie, es, du.",
            "Possessivpronomen zeigen Besitz an: euer, mein, unser.",
            "'die' = Artikel; 'sei' = Imperativ von 'sein'.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.wortarten",
        ],
    },
    {
        "n": 8,
        "type": "Konjunktionen erkennen",
        "text": (
            "Kreise nur die Konjunktionen ein:\n"
            "wenn  und  das  dann  jetzt\n"
            "dass  aber  danach  denn  damit"
        ),
        "answer": (
            "Konjunktionen: wenn, und, dass, aber, denn, damit. "
            "Keine Konjunktionen: das (Artikel/Pronomen), dann, jetzt, danach (Adverbien)."
        ),
        "steps": [
            "Konjunktionen verbinden Sätze oder Satzteile.",
            "wenn, und, dass, aber, denn, damit → ja.",
            "das = Artikel; dann/jetzt/danach = Adverbien.",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.wortarten",
        ],
    },
    {
        "n": 9,
        "type": "Sätze mit passenden Konjunktionen verbinden",
        "text": (
            "Verbinde die Sätze mit einer passenden Konjunktion.\n"
            "1. Sie tranken heißen Kinderpunsch. Ihnen wurde warm.\n"
            "2. Die Mädchen wollten noch etwas bleiben. Es war schon 19 Uhr."
        ),
        "answer": (
            "1. Ihnen wurde warm, weil sie heißen Kinderpunsch tranken. ; "
            "2. Es war schon 19 Uhr, aber die Mädchen wollten noch etwas bleiben."
        ),
        "steps": [
            "1. Kausalzusammenhang → 'weil'.",
            "2. Gegensatz → 'aber'.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.wortarten",
        ],
    },
    {
        "n": 10,
        "type": "Falsche Konjunktionen korrigieren",
        "text": (
            "Streiche die falschen Konjunktionen durch und schreibe den Satz "
            "richtig auf.\n"
            "1. Schokoriegel schmecken gut, denn sie machen dick.\n"
            "2. Kerzen sind gefährlich, denn ich passe gut auf."
        ),
        "answer": (
            "1. Schokoriegel schmecken gut, aber sie machen dick. ; "
            "2. Ich passe gut auf, weil Kerzen gefährlich sind."
        ),
        "steps": [
            "1. Gegensatz statt Begründung → 'aber'.",
            "2. Begründung umkehren und 'weil' verwenden.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.wortarten",
        ],
    },
]

NEW_KNOWLEDGE = []
