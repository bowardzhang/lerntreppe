EXERCISE = {
    "id": "0820",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Der Nachtvogel",
    "topic": "Leseverstehen, Erzaehlung, Angst, Fantasie, Eltern-Kind",
    "publisher": "CATLUX",
    "source_pdf": "0820.pdf",
    "answer_pdf": "0820 (1).pdf",
    "total_points": 26.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Lesetext-Bild",
        "text": (
            "Lesetext: 'Der Nachtvogel' (siehe beigefuegte Abbildung). "
            "Lies den Text genau und beantworte dann die folgenden Fragen "
            "in ganzen Sätzen.\n\n"
            "1.1 Der Junge hatte das Gefuehl, als ob jemand im Zimmer atmete. "
            "Was hoerte er? Was war es tatsaechlich?"
        ),
        "answer": "Er hoerte etwas rauschen. Es war sein eigener Atem.",
        "steps": ["Aus dem Anfang des Textes."],
        "points": 2.0,
        "has_image": True,
        "image": "0820_q1_lesetext_nachtvogel.png",
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 2,
        "type": "Geraeusch unter dem Bett",
        "text": (
            "Dem Jungen kam es so vor, als ob sich etwas unter dem Bett "
            "bewegte. Was hoerte er?"
        ),
        "answer": "Er hoerte ein Rauschen und ein Knacken.",
        "steps": ["Aus dem Text."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 3,
        "type": "Groesste Angst",
        "text": "Wovor hatte der Junge am meisten Angst?",
        "answer": "Vor dem Nachtvogel.",
        "steps": ["Aus dem Text."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 4,
        "type": "Reaktion der Eltern",
        "text": "Wie reagierten die Eltern, als er ihnen von seiner Angst erzaehlte?",
        "answer": (
            "Sie sagten: 'Stell dich doch nicht an! Du bildest dir das alles "
            "nur ein.' Sie glaubten ihm nicht und nahmen ihn nicht ernst, "
            "dass er Angst vor dem Alleinsein hatte."
        ),
        "steps": ["Aus dem Text - Reaktion der Eltern beschreiben."],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 5,
        "type": "Falsche Woerter unterstreichen",
        "text": (
            "Unterstreiche, was in den Sätzen falsch ist (sieben Fehler):\n"
            "- ... es laeutete an der Haustuer. Der Junge wurde steif vor Angst.\n"
            "- Dann kratzte etwas an der Hauswand. Das war der Kater!\n"
            "- Jetzt kletterte er mit seinen Krallen am Fenster hoch.\n"
            "- Jetzt war er an der Fensterbank.\n"
            "- Und jetzt klopfte er mit seinem Schnabel an die Scheibe.\n"
            "- Einmal, zweimal, dreimal, immer lauter, und gleich wuerde das "
            "Fenster zerbrechen, gleich wuerde der Vogel ins Zimmer springen."
        ),
        "answer": (
            "Sieben falsche Woerter (im Text durch das tatsaechliche Geschehen "
            "im Lesetext zu ersetzen): "
            "Haustuer, Hauswand, Kater, Krallen, Fensterbank, Schnabel, Vogel."
        ),
        "steps": [
            "Mit dem Lesetext vergleichen.",
            "Jedes falsche Wort gegen die richtige Aussage abgleichen.",
        ],
        "points": 7.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 6,
        "type": "Verteidigung des Jungen",
        "text": "Wie wehrte sich der Junge gegen die angebliche Gefahr?",
        "answer": (
            "Der Junge packte die Blumenvase vom Tisch neben dem Bett. Er "
            "schleuderte sie zum Fenster. Das Glas zersplitterte. Wind fuhr "
            "ins Zimmer und der Vogel war fort."
        ),
        "steps": ["Aus dem Text."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 7,
        "type": "Schimpfen der Eltern",
        "text": "Warum schimpften die Eltern mit dem Jungen, als sie heimkamen?",
        "answer": (
            "Ihre schoenen Ausgehkleider waren nass vom Blumenwasser und die "
            "Fensterscheibe war kaputt."
        ),
        "steps": ["Folgen der Aktion mit der Vase."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 8,
        "type": "Was war der Nachtvogel",
        "text": "Erklaere: Was war der Nachtvogel?",
        "answer": (
            "Der Nachtvogel existiert nur in der Fantasie des Jungen. In "
            "dieser Nacht laeuteten seine Eltern und klopften mit einer Stange "
            "an sein Fenster. Der Junge dagegen meinte, er habe den "
            "'Nachtvogel' in dieser Nacht selbst vertrieben."
        ),
        "steps": [
            "Zwischen Fantasie und Wirklichkeit unterscheiden.",
            "Erklaeren, was die Eltern wirklich gemacht hatten.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 9,
        "type": "Eltern lassen Jungen allein",
        "text": (
            "Liessen die Eltern den Jungen auch in Zukunft allein? "
            "Unterstreiche die entsprechenden Zeilen gruen!"
        ),
        "answer": (
            "'Aber die Eltern verstanden das nicht. Sie gingen immer wieder "
            "am Abend fort und liessen den Jungen allein.'"
        ),
        "steps": ["Stelle im Text finden und markieren."],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 10,
        "type": "Adjektiv passt nicht",
        "text": (
            "Welches Adjektiv passt nicht zu den Personen in der Geschichte? "
            "Kreuze an:\n"
            "(a) aengstlich (b) aergerlich (c) neidisch"
        ),
        "answer": "(c) neidisch passt nicht.",
        "steps": [
            "Der Junge ist aengstlich.",
            "Die Eltern sind aergerlich (sie schimpfen).",
            "Niemand ist neidisch in der Geschichte.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
]

NEW_KNOWLEDGE = []
