EXERCISE = {
    "id": "0008",
    "subject": "HSU",
    "grade": 4,
    "title": "Lernzielkontrolle: Fahrrad und Verkehrsschilder",
    "topic": "Fahrrad, Verkehrsschilder",
    "publisher": "CATLUX",
    "source_pdf": "0008.pdf",
    "answer_pdf": "0008 (1).pdf",
    "total_points": 52.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Gefahrenzeichen benennen",
        "text": "Wie heißen diese Gefahrenzeichen? (6 Zeichen sind abgebildet)",
        "answer": (
            "Einseitig rechts verengte Fahrbahn ; "
            "Unebene Fahrbahn ; "
            "Kurve rechts ; "
            "Gegenverkehr ; "
            "Baustelle ; "
            "Gefahrenstelle"
        ),
        "steps": [
            "Gefahrenzeichen sind dreieckig mit rotem Rand.",
            "Die sechs abgebildeten Zeichen heißen: Einseitig rechts verengte Fahrbahn, Unebene Fahrbahn, Kurve rechts, Gegenverkehr, Baustelle, Gefahrenstelle.",
        ],
        "points": 6.0,
        "has_image": True,
        "image": "0008_q1_gefahrenzeichen.png",
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 2,
        "type": "Verkehrszeichen erklären",
        "text": "Was sagen dir diese Zeichen? (4 Zeichen sind abgebildet)",
        "answer": (
            "Fahrradstraße: hier dürfen nur Radfahrer fahren ; "
            "Vorfahrtstraße, die knickt ab ; "
            "Verbot der Einfahrt, aber Radfahrer dürfen in diese Richtung fahren (= fahrradfrei) ; "
            "Halt – Vorfahrt gewähren, ich muss stehen bleiben"
        ),
        "steps": [
            "Blaues Schild mit Fahrrad = Fahrradstraße.",
            "Gelbes Schild mit Pfeil = Vorfahrtstraße, die abknickt.",
            "Rotes Einfahrt-verboten-Schild mit Zusatz 'Radfahrer frei' = Einfahrt verboten, Radfahrer dürfen entgegen fahren.",
            "STOP-Schild = Halt, Vorfahrt gewähren.",
        ],
        "points": 4.0,
        "has_image": True,
        "image": "0008_q2_zeichen_bedeutung.png",
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 3,
        "type": "Begründung schreiben",
        "text": "Dürfen Radfahrer entgegen der Einbahnstraße fahren? Begründe!",
        "answer": (
            "Bei einer normalen, nicht extra gekennzeichneten Einbahnstraße nein. "
            "Bei einer Einbahnstraße mit dem Zusatzschild 'Fahrrad frei' ja – Radfahrer dürfen dann entgegen der Fahrtrichtung fahren."
        ),
        "steps": [
            "Einbahnstraßen gelten grundsätzlich für alle Fahrzeuge in eine Richtung.",
            "Ausnahme: Ist das Zusatzschild 'Radfahrer frei' angebracht, dürfen Radfahrer entgegen der Einbahnstraße fahren.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 4,
        "type": "Verkehrsregel als Satz aufschreiben",
        "text": (
            "Welche Verkehrsregel gilt, wenn an der Kreuzung die Vorfahrt durch keine "
            "Verkehrszeichen geregelt ist? Schreibe einen Satz!"
        ),
        "answer": "Hier gilt die Regel: rechts vor links.",
        "steps": [
            "Ohne Verkehrszeichen oder Ampel gilt an einer Kreuzung die Grundregel: rechts vor links.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 5,
        "type": "Verhalten in der Spielstraße beschreiben",
        "text": (
            "Wie musst du dich als Radfahrer in einer Spielstraße (verkehrsberuhigter Bereich) verhalten?"
        ),
        "answer": (
            "Ich muss bremsbereit sein, ich muss langsam fahren und ich muss auf Fußgänger achten."
        ),
        "steps": [
            "In einer Spielstraße gilt: langsam fahren, immer bremsbereit sein, Fußgänger haben Vorrang.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 6,
        "type": "Begründung schreiben",
        "text": "Dürfen in einer Spielstraße auch Autos fahren? Begründe!",
        "answer": (
            "Ja, sie dürfen, aber nur in Schrittgeschwindigkeit (4–7 km/h)."
        ),
        "steps": [
            "Autos dürfen in eine Spielstraße einfahren.",
            "Sie müssen jedoch Schrittgeschwindigkeit fahren (ca. 4–7 km/h) und auf Fußgänger und spielende Kinder Rücksicht nehmen.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 7,
        "type": "Fahrradausrüstung aufzählen",
        "text": (
            "Welche Gegenstände an deinem Fahrrad gehören zur vorgeschriebenen Ausrüstung? "
            "– Verkehrssicherheit – (10 Gegenstände)"
        ),
        "answer": (
            "Vorderradbremse, Hinterradbremse, weißer Frontreflektor, "
            "roter Großflächenrückstrahler, rote Schlussleuchte, "
            "hell tönende Glocke, Scheinwerfer, Dynamo, "
            "Speichenrückstrahler (gelb), gelbe Pedalrückstrahler"
        ),
        "steps": [
            "Bremsen: Vorderradbremse und Hinterradbremse.",
            "Beleuchtung: Scheinwerfer (vorne) und Dynamo als Stromquelle.",
            "Rückleuchte: rote Schlussleuchte.",
            "Reflektoren: weißer Frontreflektor, roter Großflächenrückstrahler, gelbe Speichenrückstrahler, gelbe Pedalrückstrahler.",
            "Signalgerät: hell tönende Glocke.",
        ],
        "points": 10.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 8,
        "type": "Verkehrszeichen einfärben (grün/gelb/rot)",
        "text": (
            "Bei welchen Verkehrszeichen:\n"
            "- darfst du weiterfahren? Male das Kästchen grün an\n"
            "- musst du aufpassen? Male das Kästchen gelb an\n"
            "- darfst du nicht fahren? Male das Kästchen rot an\n"
            "(8 Zeichen sind abgebildet)"
        ),
        "answer": (
            "Grün (weiterfahren): Zeichen ohne Fahrverbot, z. B. Richtungspfeil, Fahrradweg. "
            "Gelb (aufpassen): Gefahrenzeichen (Dreieck), Vorfahrt gewähren, Baustelle. "
            "Rot (nicht fahren): Einfahrt verboten, Fahrverbot, Stoppschild."
        ),
        "steps": [
            "Grüne Kästchen: Gebots- oder Freigabeschilder (z. B. Fahrradstraße, Richtungspfeil).",
            "Gelbe Kästchen: Gefahrenzeichen (Dreieck) oder Vorfahrtschilder.",
            "Rote Kästchen: Verbotsschilder (rund mit rotem Rand oder roter Schrift).",
        ],
        "points": 8.0,
        "has_image": True,
        "image": "0008_q8_zeichen_farben.png",
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 9,
        "type": "Abstände nennen",
        "text": (
            "a) Wie groß ist der Sicherheitsabstand zwischen 2 Rädern?\n"
            "b) Wie groß ist der Seitenabstand beim Überholen?"
        ),
        "answer": (
            "a) 3 Fahrradlängen (5 Meter) ; "
            "b) 1,5 m"
        ),
        "steps": [
            "Sicherheitsabstand zum vorausfahrenden Rad: mindestens 3 Fahrradlängen bzw. 5 Meter.",
            "Seitenabstand beim Überholen: mindestens 1,5 Meter.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 10,
        "type": "Verkehrszeichen einzeichnen und Reihenfolge bestimmen",
        "text": (
            "Zeichne die fehlenden Verkehrszeichen ein! "
            "Wann darf der Radfahrer fahren? Kreuze an! (zwei Kreuzungssituationen)"
        ),
        "answer": (
            "Situation 1: Radfahrer fährt als Vierter. "
            "Situation 2: Radfahrer fährt als Erster."
        ),
        "steps": [
            "Vorfahrtsregel rechts vor links anwenden und die Reihenfolge der Fahrzeuge an der Kreuzung bestimmen.",
            "Situation 1: Radfahrer muss warten – er darf als Vierter fahren.",
            "Situation 2: Der Radfahrer hat Vorfahrt – er darf als Erster fahren.",
        ],
        "points": 4.0,
        "has_image": True,
        "image": "0008_q10_kreuzung.png",
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 11,
        "type": "Verkehrsschilder in Gruppen einteilen",
        "text": "In welche Gruppen kannst du die Verkehrsschilder einteilen?",
        "answer": (
            "Richtzeichen ; "
            "Vorschriftszeichen ; "
            "Gefahrenzeichen"
        ),
        "steps": [
            "Gefahrenzeichen: dreieckige Schilder mit rotem Rand – warnen vor Gefahren.",
            "Vorschriftszeichen: runde Schilder – Gebote (blau) oder Verbote (rot).",
            "Richtzeichen: rechteckige Schilder – geben Orientierung und Information.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 12,
        "type": "Altersgrenzen nennen",
        "text": (
            "Ab wann darfst du nicht mehr auf dem Bürgersteig fahren und musst die Straße "
            "benutzen (Alter)?"
        ),
        "answer": (
            "Zwischen acht und zehn Jahren darf ich selbst entscheiden, ob ich den Radweg oder die Straße benutze. "
            "Ab zehn Jahren muss ich die Straße bzw. den Radweg benutzen."
        ),
        "steps": [
            "Kinder bis 8 Jahre müssen den Bürgersteig benutzen.",
            "Von 8 bis 10 Jahren: Wahlrecht zwischen Bürgersteig und Fahrbahn.",
            "Ab 10 Jahren: Bürgersteig ist verboten, es muss die Fahrbahn/der Radweg genutzt werden.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 13,
        "type": "Physikalischen Zusammenhang erklären",
        "text": (
            "Deine Mutter fährt mit dem Auto durch eine 30er-Zone. Plötzlich sieht sie, dass am "
            "rechten Fahrbahnrand ein Kind auf die Straße läuft. "
            "Warum gelingt es deiner Mutter nicht sofort, das Auto vollständig abzubremsen?"
        ),
        "answer": (
            "Das Auto hat auch bei Tempo 30 einen Bremsweg von ca. 14 Metern. "
            "Zwischen dem Sehen des Kindes und dem Treten der Bremse vergeht noch Reaktionszeit, "
            "sodass das Auto erst nach einer längeren Strecke vollständig zum Stehen kommt."
        ),
        "steps": [
            "Reaktionszeit: Die Zeit vom Erkennen der Gefahr bis zum Treten der Bremse (ca. 1 Sekunde).",
            "Bremsweg: Bei 30 km/h ca. 9 Meter.",
            "Anhalteweg = Reaktionsweg + Bremsweg ≈ 14 Meter.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 14,
        "type": "Gefahren benennen",
        "text": "Welche Gefahren musst du beim Radfahren im Herbst besonders berücksichtigen?",
        "answer": (
            "Man kann schlechter gesehen werden, weil es früher und schneller dunkel wird. "
            "Die Sicht kann durch Nebel und starken Regen eingeschränkt sein. "
            "Es besteht Ausrutschgefahr durch nasse Blätter oder frühen Frost."
        ),
        "steps": [
            "Sichtbarkeit: Früher Einbruch der Dunkelheit → Licht einschalten, reflektierende Kleidung tragen.",
            "Sichtverhältnisse: Nebel und Regen verringern die Sicht.",
            "Rutschgefahr: Nasse Blätter auf dem Boden und früher Frost machen das Fahren gefährlich.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
]

NEW_KNOWLEDGE = []
