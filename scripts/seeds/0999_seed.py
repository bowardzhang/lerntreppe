EXERCISE = {
    "id": "0999",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Schullandheim Nürnberg (Fahrpläne)",
    "topic": "Leseverstehen, Sachtext, Schullandheim, Nürnberg, Fahrpläne, Klassenfahrt",
    "publisher": "CATLUX",
    "source_pdf": "0999.pdf",
    "answer_pdf": "0999 (1).pdf",
    "total_points": 38.0,
}

LESETEXT = (
    "Schullandheim Nürnberg\n\n"
    "Das Schuljahr ist bald zu Ende und die lange ersehnten Sommerferien nahen. "
    "Die Viertklässler der Grundschule Weißenburg freuen sich schon sehr auf "
    "die kommenden Wochen, da für diese Zeit noch einiges geplant ist. So "
    "steht noch die Fahrradprüfung der Verkehrswacht an, für die sie derzeit "
    "fleißig üben. Außerdem finden die Bundesjugendspiele in wenigen Tagen "
    "statt und der ein oder andere Ausflug steht auch noch bevor. Ganz "
    "besonders freuen sich die Kinder allerdings auf ihre Reise ins "
    "Schullandheim. Gemeinsam mit ihrem Klassenlehrer Herr Schlaumeier und "
    "ihrer Musiklehrerin Fr. Meise machen sie sich montags mit dem Bus auf "
    "den Weg nach Nürnberg. Dort übernachten sie in der Jugendherberge "
    "Nürnberg, die früher eine Burg mit Stallungen gewesen ist. Nachdem sie "
    "den ersten Tag die mittelalterliche Burg erkunden wollen und am Dienstag "
    "eine Führung durch die Altstadt von Nürnberg bekommen, besuchen sie am "
    "Mittwoch den Nürnberger Tiergarten. Um ihn zu erreichen, werden sie den "
    "Weg bis zum Nürnberger Hauptbahnhof laufen und steigen dort in die "
    "Straßenbahn Nr. 6 ein. Am Donnerstag wollen sie in das Nordostbad gehen. "
    "Dafür müssen sie mit der U-Bahn Nr. 2 bis zum Nordostbahnhof fahren und "
    "steigen am gleichen Bahnhof wie am Tag vorher ein. Der letzte Tag wird "
    "der Freitag sein, an dem sie dann wieder die Rückreise antreten müssen.\n\n"
    "U-Bahn U2 (Röthenbach – Hauptbahnhof – Flughafen) – relevante Halte:\n"
    "Hauptbahnhof ab: 9.41, 9.46, 9.51, 9.56, 10.01, 10.06\n"
    "Nordostbahnhof an: 9.48, 9.53, 9.58, 10.03, 10.08, 10.13\n"
    "(Fahrt Hauptbahnhof → Nordostbahnhof: 7 Minuten; U-Bahn fährt alle 5 Minuten)\n\n"
    "Straßenbahn Nr. 6 (Christuskirche – Hauptbahnhof – Tiergarten):\n"
    "Hauptbahnhof ab: 9.46, 9.56, 10.06, 10.16, 10.26, 10.36\n"
    "Tiergarten an: 10.01, 10.11, 10.21, 10.31, 10.41, 10.51\n"
    "(Fahrt Hauptbahnhof → Tiergarten: 15 Minuten; Straßenbahn fährt alle 10 Minuten)"
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Aussagen ankreuzen",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Kreuze die richtigen Aussagen an!\n"
            "(a) Die Kinder gehen in die Realschule.\n"
            "(b) Die Kinder gehen in die 3. Klasse.\n"
            "(c) Die Kinder gehen in die 4. Klasse.\n"
            "(d) Die Kinder wohnen in Würzburg.\n"
            "(e) Die Kinder gehen in die Grundschule."
        ),
        "answer": "Richtig: (c) Die Kinder gehen in die 4. Klasse. ; (e) Die Kinder gehen in die Grundschule.",
        "steps": ["Viertklässler der Grundschule Weißenburg."],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 2,
        "type": "Drei Aktivitäten",
        "text": "Nenne drei Dinge, die die Schüler noch vor den Sommerferien unternehmen!",
        "answer": (
            "Die Schüler werden noch eine Fahrradprüfung machen, an den "
            "Bundesjugendspielen mitmachen und ins Schullandheim fahren."
        ),
        "steps": ["Aus dem Text."],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 3,
        "type": "Lehrernamen",
        "text": "Wie heißen die beiden Lehrer, welche die Schülerinnen und Schüler auf ihre Reise begleiten?",
        "answer": "Die Lehrer heißen Herr Schlaumeier und Frau Meise.",
        "steps": ["Aus dem Text."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 4,
        "type": "Name Musiklehrerin",
        "text": "An was erinnert dich der Name der Musiklehrerin?",
        "answer": "Der Name der Musiklehrerin erinnert mich an einen Vogel (Meise).",
        "steps": ["Meise = Vogel."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 5,
        "type": "Fehlersuche",
        "text": (
            "Vergleiche den Satz mit dem Text. Streiche Falsches durch und schreibe "
            "die verbesserten Wörter!\n"
            "'Nachdem sie am ersten Tag die mittelalterliche Burgmauer erkunden "
            "wollen und am Diensag eine Führung durch die Altstadt bekommen, "
            "betrachten sie am Mittwoch den Nürnburger Tiergarten.\""
        ),
        "answer": (
            "Burgmauer → Burg ; Diensag → Dienstag ; Altstadt → Altstadt von Nürnberg ; "
            "betrachten → besuchen ; Nürnburger → Nürnberger."
        ),
        "steps": ["Genauen Wortlaut prüfen."],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 6,
        "type": "Verkehrsmittel",
        "text": "Mit welchen Verkehrsmitteln bewegen sich die Schüler fort?",
        "answer": "Sie bewegen sich mit dem Bus, der Straßenbahn Nr. 6 und der U-Bahn 2 fort.",
        "steps": ["Aus dem Text."],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 7,
        "type": "Bahnhöfe markieren",
        "text": (
            "Markiere in den beiden Fahrplänen den Startbahnhof der Schüler blau "
            "und den Zielbahnhof orange!"
        ),
        "answer": (
            "Mittwoch: Start = Hauptbahnhof (blau), Ziel = Tiergarten (orange) ; "
            "Donnerstag: Start = Hauptbahnhof (blau), Ziel = Nordostbahnhof (orange)."
        ),
        "steps": ["In beiden Fahrplänen markieren."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 8,
        "type": "Synonyme + Zeile",
        "text": (
            "Finde Synonyme im Text und gib die Zeile an!\n"
            "Zoo: ___ ; Schullandheim: ___ ; Heimfahrt: ___ ; momentan: ___"
        ),
        "answer": (
            "Zoo → Tiergarten (Z. 14) ; "
            "Schullandheim → Jugendherberge (Z. 10) ; "
            "Heimfahrt → Rückreise (Z. 19) ; "
            "momentan → derzeit (Z. 4)."
        ),
        "steps": ["Synonyme im Text suchen."],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 9,
        "type": "Mittwoch-Abfahrten",
        "text": (
            "Die Schüler wollen am Mittwoch zwischen halb 10 und 10 Uhr am "
            "Hauptbahnhof losfahren. Welche Möglichkeiten haben sie?"
        ),
        "answer": "Sie können am Hauptbahnhof um 9:46, 9:56 oder 10:06 Uhr mit Straßenbahn Nr. 6 losfahren.",
        "steps": ["Fahrplan Straßenbahn Nr. 6 ablesen."],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 10,
        "type": "Fahrtdauer Tiergarten",
        "text": "Wie lange dauert die Fahrt zum Nürnberger Tiergarten?",
        "answer": "Die Fahrt dauert 15 Minuten.",
        "steps": ["Hauptbahnhof ab 9:46, Tiergarten an 10:01."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 11,
        "type": "U-Bahn-Wahl Donnerstag",
        "text": (
            "Am Donnerstag öffnet das Schwimmbad um 10 Uhr. Welche U-Bahn sollten "
            "die Schüler nehmen? Begründe!"
        ),
        "answer": (
            "Sie sollten die U-Bahn um 9:51 Uhr nehmen, dann sind sie um 9:58 Uhr "
            "da (2 Minuten vor 10 Uhr). Die nächste U-Bahn um 9:56 würde erst um "
            "10:03 ankommen, also 3 Minuten zu spät."
        ),
        "steps": ["Fahrplan U2 prüfen."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 12,
        "type": "Sätze vervollständigen",
        "text": (
            "Vervollständige die folgenden Sätze:\n"
            "(a) Wenn sie mit der U2 um 9.56 Uhr am Hauptbahnhof losfahren, kommen sie um ___ am Zielbahnhof an.\n"
            "(b) Wenn sie mit der Straßenbahn Nr. 6 um 10.41 Uhr am Tiergarten sein wollen, müssen sie um ___ am Hauptbahnhof losfahren.\n"
            "(c) Die Straßenbahn Nr. 6 fährt ___ als die U2.\n"
            "(d) Die Musiklehrerin meint: 'Es ist nicht schlimm, wenn wir eine U-Bahn verpassen, weil ___\n"
            "(e) Die Fahrt am Mittwoch dauert ___ als die Fahrt am Donnerstag."
        ),
        "answer": (
            "(a) 10:03 Uhr ; "
            "(b) 10:26 Uhr ; "
            "(c) seltener ; "
            "(d) die U-Bahn alle 5 Minuten fährt. ; "
            "(e) 8 Minuten länger."
        ),
        "steps": ["Mit Fahrplänen rechnen."],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 13,
        "type": "Vollständige Sätze",
        "text": "Du hast in vollständigen Sätzen geantwortet.",
        "answer": "Formpunkte für vollständige Sätze über die ganze Aufgabe.",
        "steps": ["Sprachliche Korrektheit."],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
]

NEW_KNOWLEDGE = []
