EXERCISE = {
    "id": "0378",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Die Schrift der Prinzessin",
    "topic": "Leseverstehen, Märchen, Geheimschrift, Prinzessin, Alphabet",
    "publisher": "CATLUX",
    "source_pdf": "0378.pdf",
    "answer_pdf": "0378 (1).pdf",
    "total_points": 17.0,
}

LESETEXT = (
    "Die Schrift der Prinzessin (Katrin Behrend)\n\n"
    "Nun hoert mal zu! Es war naemlich einmal eine allerliebste kleine "
    "Prinzessin, heiter und schoen wie die Fruehlingssonne, freundlich und "
    "gut, wie eben nur Prinzessinnen sein koennen. Aber sie hatte es trotz "
    "ihrer Freundlichkeit und Schoenheit nicht gut; denn ihre Eltern waren "
    "gestorben, und sie lebte nun mit ihrem alten Onkel in ihrem Schloss. "
    "Der grimmige Mann aber war nicht fuersorglich zu ihr, denn der Vater der "
    "Prinzessin hatte in seinem Testament bestimmt, dass er nicht laenger als "
    "bis zum 21. Lebensjahr seiner Tochter im Schloss bleiben duerfe; dann "
    "sollten das Schloss und Land der Prinzessin Gisa allein gehoeren. Das "
    "mochte aber der muerrische Onkel ganz und gar nicht.\n\n"
    "Kurz vor ihrem 21. Geburtstag wollte Gisa das Schreiben erlernen. Der "
    "Onkel hatte einen boesen Gedanken: Er brachte ihr das Alphabet rueckwaerts "
    "bei (z = a; y = b ...). Da hoerte er ploetzlich eine Stimme: 'Z ist a.' "
    "Der weisse Schlossrabe sass vor ihm auf dem Tisch. In hoechstem Zorn warf "
    "er ein Buch nach dem Tier; aber das entwischte durch das offene Fenster.\n\n"
    "Der boese Onkel machte mit Gisa eine Wette: Wenn sie bis zu ihrem "
    "Geburtstag so schreibt, dass alle Leute es verstehen, verlaesst er das "
    "Schloss. Gisa lernte fleissig, konnte aber nur falsch schreiben. Am Abend "
    "vor ihrem Geburtstag schrieb sie: 'An meinem einundzwanzigsten Geburtstage "
    "soll grosses Volksfest sein. Prinzessin Gisa.' Der Zettel wurde an allen "
    "Strassenecken angeschlagen. Die Leute lasen: 'Zn ovrnvo vrnfnwadznarthgvn "
    "Tvyfighgztv hmpp timhavh Empqhuvhg hvrn. Lirnavhhrn Trhz.' Sie glaubten "
    "erst, es sei ein Spass, dann dachten sie, die Prinzessin sei irrsinnig.\n\n"
    "Manch schoener Prinz sah ihr Bild und sagte: 'Schade um sie!' Nur ein "
    "Prinz zweifelte: 'Wer so kluge Augen hat, kann doch nicht irrsinnig sein!' "
    "Er reiste in das Land. Sein Knappe ging voraus, um im Schloss anzufragen. "
    "Er brachte ein Brieflein: 'Qmoog fnw svpug ori. Rsi hvrw drppqmoovn! Trhz.' "
    "Da hoerte der Prinz eine schnarrende Stimme: 'Z ist a.' Ein weisser Rabe "
    "sass auf dem Kopf seines Pferdes und huepfte auf seine Hand. 'Z ist a!', "
    "sagte der Rabe immer wieder. 'Das scheint mir ja hier ein schreckliches "
    "Land zu sein', sagte er, 'selbst dieser Vogel hat einen Vogel.'\n\n"
    "Doch mit einem Mal wurde er aufmerksam: 'Wie? Z ist a? Sollte der Vogel "
    "das Raetsel loesen koennen?' Schnell schrieb er sich das ABC auf, und dann "
    "noch einmal rueckwaerts darunter, und konnte lesen: 'Kommt und helft mir! "
    "Ihr seid willkommen! Gisa.'\n\n"
    "Der Prinz liess nicht locker, bis der boese Onkel gestand; dann liess er "
    "den Uebeltaeter in Ketten legen. Die Prinzessin wurde die Gemahlin ihres "
    "Befreiers. Am naechsten Morgen prangte an allen Strassenecken: 'An meinem "
    "Hochzeitstag soll grosses Volksfest sein! Gisa' - und sie feierten, bis "
    "kein Mensch mehr feiern konnte."
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Testament des Vaters",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Was stand in dem Testament, das der Vater fuer die Prinzessin "
            "geschrieben hatte?\n"
            "(a) Was durfte der Onkel nicht?\n"
            "(b) Was sollte danach gehoeren?"
        ),
        "answer": (
            "(a) Der Onkel durfte nicht laenger als bis zum 21. Lebensjahr seiner "
            "Tochter im Schloss bleiben. ; "
            "(b) Dann sollten das Schloss und das Land der Prinzessin Gisa allein "
            "gehoeren."
        ),
        "steps": [
            "Aus dem ersten Absatz: Testamentinhalt.",
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
        "type": "Trick des Onkels",
        "text": (
            "Welchen Trick verwendete der boese Onkel, damit die Prinzessin "
            "nicht richtig schreiben lernte?"
        ),
        "answer": "Er lehrte die Prinzessin das Alphabet rueckwaerts (z = a, y = b ...).",
        "steps": [
            "Aus dem zweiten Absatz.",
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
        "type": "Reaktion der Untertanen",
        "text": (
            "Was glaubten die Untertanen der Prinzessin, als sie das Schild lasen?\n"
            "(a) Erste Reaktion:\n"
            "(b) Spaetere Reaktion:"
        ),
        "answer": (
            "(a) Sie glaubten, dass sich jemand einen Spass erlaubt haette. ; "
            "(b) Sie glaubten, dass die Prinzessin irrsinnig geworden sei."
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
        "n": 4,
        "type": "Der kluge Prinz",
        "text": (
            "Was sagte der eine Prinz, als er noch einmal ihr Bild ansah?\n"
            "(a) Was erkannte er?\n"
            "(b) Was beschloss er?"
        ),
        "answer": (
            "(a) 'Wer so kluge Augen hat, kann doch nicht irrsinnig sein!' ; "
            "(b) 'Ich werde mich mal aufmachen und sie mir anschauen.'"
        ),
        "steps": [
            "Direktes Zitat aus dem vierten Absatz.",
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
        "type": "Geänderte Wörter unterstreichen",
        "text": (
            "Dieser Satz steht etwas anders im Lesetext. Unterstreiche die "
            "geaenderten Woerter:\n"
            "'...schickte er einen Knappen hinaus, der im Schloss nachfragen "
            "sollte...'"
        ),
        "answer": (
            "'einen' (im Text: 'seinen'), 'hinaus' (im Text: 'voraus'), "
            "'nachfragen' (im Text: 'anfragen')."
        ),
        "steps": [
            "Satz im Text suchen und Abweichungen finden.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 6,
        "type": "Behauptung des Onkels",
        "text": (
            "Der Onkel behauptete, dass die Prinzessin das Schreiben nicht "
            "lernen koenne. Welchen Grund nannte er ihr?"
        ),
        "answer": "Er sagte ihr, sie sei schon zu alt dazu.",
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
        "type": "Fehlende Wörter ergänzen",
        "text": (
            "Ergaenze die fehlenden Woerter:\n"
            "(a) 'Was ___ du denn da immer vor dich hin?'\n"
            "(b) 'Das scheint mir ja hier ein ___ Land zu sein, ...'\n"
            "(c) '...selbst dieser Vogel hat einen ___.' "
        ),
        "answer": "(a) plapperst ; (b) schreckliches ; (c) Vogel.",
        "steps": [
            "Aus dem vierten Absatz: Gespraech des Prinzen mit dem Raben.",
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
        "type": "Dauer der Feier",
        "text": "Wie lange dauerte die Hochzeitsfeier von Gisa und dem Prinzen?",
        "answer": "Sie feierten, bis kein Mensch mehr feiern konnte.",
        "steps": [
            "Aus dem letzten Absatz.",
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
        "type": "Bedeutung von Gemahlin",
        "text": (
            "Kreuze an, welches Wort die gleiche Bedeutung wie 'Gemahlin' besitzt:\n"
            "(a) Fraeulein ; (b) Ehefrau ; (c) Freundin ; (d) Braut ; (e) Hausfrau"
        ),
        "answer": "Richtig: (b) Ehefrau.",
        "steps": [
            "Bedeutung von 'Gemahlin' = Ehefrau.",
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
        "type": "Geheimschrift entschlüsseln",
        "text": (
            "Gisa hat eine Nachricht fuer dich. Kannst du sie entschluesseln?\n"
            "Tipp: Das Alphabet rueckwaerts: z=a, y=b, x=c, w=d, v=e, u=f, "
            "t=g, s=h, r=i, q=j, p=k, o=l, n=m, m=n, l=o, k=p, j=q, i=r, "
            "h=s, g=t, f=u, e=v, d=w, c=x, b=y, a=z"
        ),
        "answer": "Viel Erfolg! (eigene Nachricht entschluesseln - Alphabet rueckwaerts anwenden).",
        "steps": [
            "Jeden Buchstaben durch den Gegenbuchstaben ersetzen.",
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
