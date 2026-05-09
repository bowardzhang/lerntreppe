EXERCISE = {
    "id": "2129",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Muränen im Korallenriff",
    "topic": "Leseverstehen, Sachtext, Muräne, Korallenriff, Raubfisch, Tiere",
    "publisher": "CATLUX",
    "source_pdf": "2129.pdf",
    "answer_pdf": "2129 (1).pdf",
    "total_points": 28.0,
}

LESETEXT = (
    "Muränen im Korallenriff\n\n"
    "Korallenriffe mit ihrer bunten Fisch- und Pflanzenwelt sind beliebte "
    "Tauchreviere für Sporttaucher. Es ist spannend und faszinierend die "
    "unbekannte Unterwasserwelt zu erforschen – doch allzu Neugierige sollten "
    "vorsichtig sein. Wer mit den Händen unvorsichtig Spalten und Höhlen "
    "erkundet, kann schnell Bekanntschaft mit einem typischen Bewohner des "
    "Korallenriffs machen. Zwar greifen Muränen im freien Wasser kaum an, doch "
    "können sie es gar nicht leiden, wenn jemand sie in ihren gemütlichen "
    "Behausungen überrascht.\n\n"
    "Muränen können giftig sein\n"
    "In die Enge getrieben, schießen sie wie ein Torpedo aus ihrem Versteck "
    "hervor. Den unvorsichtigen Unterwassertouristen erwartet ein "
    "schmerzhafter Biss. Die Raubfische haben ein kräftiges Gebiss mit spitzen "
    "Zähnen, das schlimme Wunden verursacht. Einige Muränenarten sind außerdem "
    "giftig: Ihre Giftdrüsen sitzen in der Mundschleimhaut hinter den "
    "Hakenzähnen und entleeren sich bei einem Biss direkt in die Wunde.\n\n"
    "Keine Angst: Die Muräne will nur atmen\n"
    "Kein Wunder also, dass Muränen bei Tauchern einen nicht besonders guten "
    "Ruf haben und Begegnungen mit ihnen schon mal Gänsehaut verursachen. "
    "Sehr freundlich sehen sie ja auch nicht aus, wenn sie da aus ihren "
    "Höhlen lugen und ihr Maul langsam öffnen und schließen. Was wie eine "
    "Drohgebärde aussieht, ist aber nur die regelmäßige Atembewegung einer "
    "Muräne. Eine Muräne, die sich bedroht fühlt, weicht dagegen ein Stück "
    "zurück und reißt das Maul weit auf. In dieser Stellung verharrt sie, bis "
    "sie merkt, dass keine Gefahr mehr droht.\n\n"
    "Brauchen Muränen eine Brille?\n"
    "Werden Muränen nicht belästigt, sind sie sogar sehr ruhige und scheue "
    "Tiere. Sie liegen den ganzen Tag gemütlich in ihrer Nische auf der Lauer "
    "und warten, bis ein Beutetier vorbeigeschwommen kommt. Dann wird "
    "blitzschnell zugeschlagen. Am liebsten fressen Muränen kleine Fische, "
    "Krebse und Kraken. Bei der Jagd hilft den Raubfischen ihre gute Nase und "
    "ihr gutes Hörvermögen. Die Augen sind dagegen eher nutzlos, alle Muränen "
    "sind stark kurzsichtig. Nur nachts wagen Muränen sich aus ihren "
    "Stammhöhlen. Dann gehen sie auch mal frei schwimmend auf die Jagd, "
    "halten sich jedoch immer in der Nähe ihrer Korallen und des Meeresbodens "
    "auf.\n\n"
    "Fischdelikatessen bei den Römern\n"
    "Muränen leben nur dort wo es schön warm ist, im Mittelmeer oder im "
    "Indischen Ozean zum Beispiel. Auch im Sommerurlaub in Italien könnt ihr "
    "Muränen begegnen, dort lebt nämlich die Mittelmeermuräne. Diese Tiere "
    "können bis zu eineinhalb Meter lang und sechs Kilogramm schwer werden. "
    "Im alten Rom mästeten die Menschen Muränen als Speisefische, die "
    "Raubfische galten als echte Delikatesse. Damit sich die Menschen an "
    "dieser Fischspeise nicht vergifteten, mussten Muränen bei hohen "
    "Temperaturen zubereitet werden. Nur dadurch wurde das Gift in Blut, Haut "
    "und Giftdrüsen der Mittelmeermuräne unwirksam."
)

QUESTIONS = [
    {
        "n": 1,
        "type": "W-Fragen",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Wie stellt ein Leseprofi eine gute Frage? Nenne vier Beispiele!"
        ),
        "answer": "Mit den W-Fragen: Wer, Wie, Was, Warum.",
        "steps": ["W-Fragen kennen."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 2,
        "type": "Fragen beurteilen",
        "text": (
            "Beurteile folgende Fragen. Begründe!\n"
            "(a) Wie alt werden Muränen?\n"
            "(b) Kann man Muränen essen?\n"
            "(c) Wo leben Muränen?"
        ),
        "answer": (
            "(a) Unpassende Frage – steht nicht im Text. ; "
            "(b) Unpassende Frage – Ja/Nein-Frage, sollte mit ganzem Satz beantwortbar sein. ; "
            "(c) Richtige Frage! Kann nicht mit ja/nein beantwortet werden und braucht einen ganzen Satz."
        ),
        "steps": ["Fragequalität prüfen."],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 3,
        "type": "Fragen zu Antworten",
        "text": (
            "Finde passende Fragen zu diesen Antworten!\n"
            "(a) 'Die Giftdrüsen sitzen in der Mundschleimhaut.'\n"
            "(b) 'Sie weicht zurück und reißt das Maul auf.'\n"
            "(c) 'Weil sie mit giftigem Schleim bedeckt sind.'"
        ),
        "answer": (
            "(a) Wo befinden sich die Giftdrüsen? ; "
            "(b) Was macht die Muräne, wenn sie sich bedroht fühlt? ; "
            "(c) Warum können sich Muränen in einer Höhle nicht verletzen?"
        ),
        "steps": ["W-Fragen formulieren."],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 4,
        "type": "Eigene Fragen",
        "text": (
            "Stelle zu jedem Abschnitt selbst eine sinnvolle Frage!\n"
            "(a) Muränen im Korallenriff\n"
            "(b) Keine Angst: Die Muräne will nur atmen\n"
            "(c) Brauchen Muränen eine Brille?\n"
            "(d) Fischdelikatessen bei den Römern"
        ),
        "answer": (
            "(a) Wem können Taucher begegnen, wenn sie in Spalten greifen? ; "
            "(b) Wie sieht die Muräne aus, wenn sie sich bedroht fühlt? ; "
            "(c) Was hilft den Muränen bei der Jagd? ; "
            "(d) Wo galt die Muräne als Delikatesse?"
        ),
        "steps": ["Eigene Fragen pro Abschnitt."],
        "points": 8.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 5,
        "type": "Sätze ankreuzen",
        "text": (
            "Welche Sätze stehen so im Text?\n"
            "(a) Ihre Giftdrüsen sitzen in der Mundschleimhaut hinter den Hakenzähnen "
            "und entleeren sich bei einem Biss direkt in die Wunde.\n"
            "(b) Dann wird schnell zugeschlagen.\n"
            "(c) Nur nachts trauen sie sich aus ihren Stammhöhlen.\n"
            "(d) Kein Wunder also, dass Muränen bei Tauchern einen nicht besonders "
            "guten Ruf haben und Begegnungen mit ihnen schon mal Gänsehaut verursachen."
        ),
        "answer": "Richtig: (a) und (d).",
        "steps": ["Wortlaut prüfen."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 6,
        "type": "Gegenteile",
        "text": (
            "Nenne das Gegenteil!\n"
            "kräftig: ___\n"
            "nutzlos: ___"
        ),
        "answer": "kräftig → schwach ; nutzlos → sinnvoll (nützlich).",
        "steps": ["Antonyme finden."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 7,
        "type": "Synonym verharren",
        "text": (
            "'In dieser Stellung verharrt sie, bis sie merkt, dass keine Gefahr "
            "mehr droht.\" Nenne ein Wort mit derselben Bedeutung für 'verharren'!"
        ),
        "answer": "innehalten / bleiben / aushalten.",
        "steps": ["Synonym finden."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 8,
        "type": "Eigene Überschrift",
        "text": "Denke dir eine eigene Überschrift für Absatz 4: 'Brauchen Muränen eine Brille?' aus!",
        "answer": "Z. B.: Haben Muränen eine Sehschwäche? / Sehen Muränen schlecht? / Sind Muränen blind?",
        "steps": ["Eigene Überschrift formulieren."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
]

NEW_KNOWLEDGE = []
