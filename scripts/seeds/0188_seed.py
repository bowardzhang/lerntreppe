EXERCISE = {
    "id": "0188",
    "subject": "Deutsch",
    "grade": 4,
    "title": "1. Lernzielkontrolle: Sprache untersuchen, Zeiten, Wortarten, Fälle",
    "topic": "Zeitformen, Wortarten bestimmen, Wortfelder, Fälle (Kasus)",
    "publisher": "CATLUX",
    "source_pdf": "0188.pdf",
    "answer_pdf": "0188 (1).pdf",
    "total_points": 50.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Zeitentabelle",
        "text": (
            "Fülle die Tabelle aus.\n\n"
            "Grundform | Gegenwart (er/sie) | 1. Vergangenheit (er/sie) | 2. Vergangenheit (er/sie) | vollendete Gegenwart (er/sie) | Zukunft (er/sie)\n"
            "laufen    | ___                | ___                       | ___                       | ___                          | ___\n"
            "suchen    | ___                | ___                       | ___                       | ___                          | ___\n"
            "winken    | ___                | ___                       | ___                       | ___                          | ___\n"
            "lügen     | ___                | ___                       | ___                       | ___                          | ___\n"
            "essen     | ___                | ___                       | ___                       | ___                          | ___\n"
            "backen    | ___                | ___                       | ___                       | ___                          | ___"
        ),
        "answer": (
            "laufen: läuft / lief / ist gelaufen / hat gelaufen / wird laufen ; "
            "suchen: sucht / suchte / hat gesucht / hatte gesucht / wird suchen ; "
            "winken: winkt / winkte / hat gewinkt / hatte gewinkt / wird winken ; "
            "lügen: lügt / log / hat gelogen / hatte gelogen / wird lügen ; "
            "essen: isst / aß / hat gegessen / hatte gegessen / wird essen ; "
            "backen: bäckt / backte / hat gebacken / hatte gebacken / wird backen"
        ),
        "steps": [
            "laufen: Gegenwart=läuft, 1.Vg=lief, 2.Vg=ist gelaufen, vollend.Gw=hat gelaufen, Zukunft=wird laufen.",
            "suchen: Gegenwart=sucht, 1.Vg=suchte, 2.Vg=hat gesucht, vollend.Gw=hatte gesucht, Zukunft=wird suchen.",
            "winken: Gegenwart=winkt, 1.Vg=winkte, 2.Vg=hat gewinkt, vollend.Gw=hatte gewinkt, Zukunft=wird winken.",
            "lügen: Gegenwart=lügt, 1.Vg=log, 2.Vg=hat gelogen, vollend.Gw=hatte gelogen, Zukunft=wird lügen.",
            "essen: Gegenwart=isst, 1.Vg=aß, 2.Vg=hat gegessen, vollend.Gw=hatte gegessen, Zukunft=wird essen.",
            "backen: Gegenwart=bäckt, 1.Vg=backte, 2.Vg=hat gebacken, vollend.Gw=hatte gebacken, Zukunft=wird backen.",
        ],
        "points": 12.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.zeiten",
        ],
    },
    {
        "n": 2,
        "type": "Satz in Zeiten umschreiben",
        "text": (
            "Schreibe den Satz in die angegebenen Zeiten um.\n"
            "Es hört auf zu regnen.\n"
            "2. Vergangenheit: ___\n"
            "Zukunft: ___\n"
            "1. Vergangenheit: ___"
        ),
        "answer": (
            "2. Vergangenheit: Es hat aufgehört zu regnen. ; "
            "Zukunft: Es wird aufhören zu regnen. ; "
            "1. Vergangenheit: Es hörte auf zu regnen."
        ),
        "steps": [
            "2. Vergangenheit (Perfekt): Es hat aufgehört zu regnen.",
            "Zukunft: Es wird aufhören zu regnen.",
            "1. Vergangenheit (Präteritum): Es hörte auf zu regnen.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.zeiten",
        ],
    },
    {
        "n": 3,
        "type": "Zeitstufen bestimmen",
        "text": (
            "Bestimme die Zeitstufe der unterstrichenen Verben.\n"
            "1. Morgen werden wir ins Kino gehen. → ___\n"
            "2. Wir lachen und singen. → ___\n"
            "3. Gestern spielten wir Fußball. → ___"
        ),
        "answer": "1. Zukunft ; 2. Gegenwart ; 3. 1. Vergangenheit",
        "steps": [
            "1. 'werden … gehen' = Futur → Zukunft.",
            "2. 'lachen und singen' = Präsens → Gegenwart.",
            "3. 'spielten' = Präteritum → 1. Vergangenheit.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.zeiten",
        ],
    },
    {
        "n": 4,
        "type": "Wortarten bestimmen",
        "text": (
            "Bestimme die Wortart der unterstrichenen Wörter.\n"
            "1. Der Hund bellt laut. → Der: ___\n"
            "2. Das Mädchen liest ein Buch. → Mädchen: ___\n"
            "3. Die Kinder spielen draußen. → spielen: ___\n"
            "4. Der alte Mann geht langsam. → alte: ___\n"
            "5. Sie hilft ihrer Freundin. → Sie: ___\n"
            "6. Wir müssen die Aufgabe lösen. → lösen: ___"
        ),
        "answer": (
            "1. Der = Artikel ; 2. Mädchen = Nomen ; 3. spielen = Verb ; "
            "4. alte = Adjektiv ; 5. Sie = Pronomen ; 6. lösen = Verb"
        ),
        "steps": [
            "Der → bestimmter Artikel.",
            "Mädchen → Nomen (Substantiv).",
            "spielen → Verb (Tunwort).",
            "alte → Adjektiv (Eigenschaftswort).",
            "Sie → Personalpronomen.",
            "lösen → Verb (Tunwort).",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.wortarten",
        ],
    },
    {
        "n": 5,
        "type": "Wortfelder",
        "text": (
            "Schreibe je vier Wörter zum Wortfeld auf.\n"
            "Wortfeld 'gehen': ___, ___, ___, ___\n"
            "Wortfeld 'sprechen': ___, ___, ___, ___"
        ),
        "answer": (
            "gehen: hüpfen, eilen, rennen, schleichen (Beispiele) ; "
            "sprechen: reden, rufen, plappern, sagen (Beispiele)"
        ),
        "steps": [
            "Wortfeld gehen: schleichen, rennen, hüpfen, eilen, trotten, wandern …",
            "Wortfeld sprechen: reden, rufen, flüstern, plappern, sagen, erzählen …",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.wortarten",
        ],
    },
    {
        "n": 6,
        "type": "Fälle im Text bestimmen",
        "text": (
            "Lies den Text und bestimme die Fälle der unterstrichenen Wörter.\n\n"
            "Ein Wolf und ein Reiher begegneten sich an einem Teich. "
            "Der Wolf hatte einen Knochen im Hals stecken. "
            "Er bat den Reiher um seine Hilfe. "
            "Der Reiher steckte seinen langen Schnabel in den Rachen des Wolfes "
            "und zog den Knochen heraus.\n\n"
            "Bestimme Fall und Nomen:\n"
            "1. Ein Wolf → ___. Fall: ___\n"
            "2. einem Teich → ___. Fall: ___\n"
            "3. einen Knochen → ___. Fall: ___\n"
            "4. den Reiher → ___. Fall: ___\n"
            "5. seinen langen Schnabel → ___. Fall: ___\n"
            "6. des Wolfes → ___. Fall: ___\n"
            "7. dem Reiher → ___. Fall: ___\n"
            "8. den Knochen → ___. Fall: ___"
        ),
        "answer": (
            "1. Wolf = 1. Fall (Nominativ) ; "
            "2. Teich = 3. Fall (Dativ) ; "
            "3. Knochen = 4. Fall (Akkusativ) ; "
            "4. Reiher = 4. Fall (Akkusativ) ; "
            "5. Schnabel = 4. Fall (Akkusativ) ; "
            "6. Wolfes = 2. Fall (Genitiv) ; "
            "7. Reiher = 3. Fall (Dativ) ; "
            "8. Knochen = 4. Fall (Akkusativ)"
        ),
        "steps": [
            "Wolf (Subjekt des Satzes) → 1. Fall / Nominativ.",
            "an einem Teich (Dativ nach 'an' mit Ortsangabe) → 3. Fall / Dativ.",
            "hatte einen Knochen (Akkusativobjekt) → 4. Fall / Akkusativ.",
            "bat den Reiher (Akkusativobjekt) → 4. Fall / Akkusativ.",
            "steckte seinen langen Schnabel (Akkusativobjekt) → 4. Fall / Akkusativ.",
            "des Wolfes (Genitivattribut) → 2. Fall / Genitiv.",
            "dem Reiher (Dativobjekt von 'bat') → 3. Fall / Dativ.",
            "zog den Knochen heraus (Akkusativobjekt) → 4. Fall / Akkusativ.",
        ],
        "points": 8.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.kasus",
        ],
    },
    {
        "n": 7,
        "type": "Verben in 1. Vergangenheit im Lückentext",
        "text": (
            "Setze die Verben in Klammern in die 1. Vergangenheit ein.\n\n"
            "Eines Abends ___ (heimgehen) ein Jäger durch den Wald. "
            "Plötzlich ___ (sehen) er zwei junge Rehe am Boden liegen. "
            "Ein Fuchs ___ (sich nähern) ihnen vorsichtig. "
            "Die Rehe ___ (liegen) still und ___ (bluten) aus einer Wunde. "
            "Die Alten ___ (sich kümmern) nicht mehr um sie. "
            "Bald ___ (kommen) Tierpfleger des Jagdverbands. "
            "Sie ___ (versorgen) die Wunden der Rehe. "
            "Dann ___ (laden) sie die Tiere auf ihr Fahrzeug. "
            "Der Jäger ___ (rasen) mit ihnen zum Tierarzt. "
            "Dieser ___ (lesen) sofort das Blutbild. "
            "Er ___ (tun) alles, um die Rehe zu retten."
        ),
        "answer": (
            "heimging / sah / näherte sich / lagen / bluteten / "
            "kümmerten sich / kamen / versorgten / luden / raste / las / tat"
        ),
        "steps": [
            "heimgehen → heimging (starkes Verb).",
            "sehen → sah (starkes Verb).",
            "sich nähern → näherte sich (schwaches Verb).",
            "liegen → lagen (starkes Verb).",
            "bluten → bluteten (schwaches Verb).",
            "sich kümmern → kümmerten sich (schwaches Verb).",
            "kommen → kamen (starkes Verb).",
            "versorgen → versorgten (schwaches Verb).",
            "laden → luden (starkes Verb).",
            "rasen → raste (schwaches Verb).",
            "lesen → las (starkes Verb).",
            "tun → tat (unregelmäßig).",
        ],
        "points": 12.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.zeiten",
        ],
    },
]

NEW_KNOWLEDGE = []
