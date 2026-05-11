EXERCISE = {
    "id": "0255",
    "subject": "HSU",
    "grade": 4,
    "title": "Lernzielkontrolle: Fahrrad, Verkehrsschilder, Fahrradprüfung, Verkehrserziehung",
    "topic": "Fahrrad, Verkehrsschilder, Fahrradprüfung, Verkehrserziehung",
    "publisher": "CATLUX",
    "source_pdf": "0255.pdf",
    "answer_pdf": "0255 (1).pdf",
    "total_points": 46.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Ankreuzaufgabe Fahrradausrüstung",
        "text": (
            "Als Radfahrer bist du für die Verkehrssicherheit deines Fahrrades verantwortlich. "
            "Kreuze die vorgeschriebenen Ausrüstungsgegenstände an!\n"
            "- Luftpumpe\n"
            "- Scheinwerfer und rotes Schlusslicht mit Rückstrahler\n"
            "- Bremsen für Vorder- und Hinterrad\n"
            "- helltönende Glocke\n"
            "- Tacho und Rückspiegel\n"
            "- weißer Frontrückstrahler, Speichenreflektoren, Pedalrückstrahler und roter Großflächenrückstrahler"
        ),
        "answer": (
            "Vorgeschrieben (anzukreuzen):\n"
            "✓ Scheinwerfer und rotes Schlusslicht mit Rückstrahler\n"
            "✓ Bremsen für Vorder- und Hinterrad\n"
            "✓ helltönende Glocke\n"
            "✓ weißer Frontrückstrahler, Speichenreflektoren, Pedalrückstrahler und roter Großflächenrückstrahler\n"
            "Nicht vorgeschrieben: Luftpumpe, Tacho und Rückspiegel"
        ),
        "steps": [
            "Die gesetzlich vorgeschriebene Fahrradausrüstung umfasst: Bremsen, Beleuchtung, Glocke und Reflektoren.",
            "Luftpumpe und Tacho sind nützlich, aber nicht gesetzlich vorgeschrieben.",
            "Rückspiegel ist ebenfalls nicht vorgeschrieben.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 2,
        "type": "Verkehrszeichen erklären",
        "text": (
            "Was bedeuten diese Verkehrszeichen? Schreibe die genaue Bedeutung auf! "
            "(4 Zeichen abgebildet)"
        ),
        "answer": (
            "1. Andreaskreuz: Schienenverkehr hat Vorrang ; "
            "2. Getrennter Rad- und Fußweg ; "
            "3. Verbot für Fahrzeuge aller Art ; "
            "4. Vorfahrt gewähren"
        ),
        "steps": [
            "Andreaskreuz (X-förmiges weißes Schild mit rotem Rand) = Bahnübergang, Schienenverkehr hat Vorrang.",
            "Blaues rundes Schild mit Fahrrad und Fußgänger durch Linie getrennt = getrennter Rad- und Fußweg.",
            "Rundes Schild mit rotem Rand ohne Bild = Verbot für Fahrzeuge aller Art.",
            "Umgekehrtes weißes Dreieck mit rotem Rand = Vorfahrt gewähren.",
        ],
        "points": 8.0,
        "has_image": True,
        "image": "0255_q2_zeichen.png",
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 3,
        "type": "Verhalten am Zebrastreifen beschreiben",
        "text": (
            "Du fährst mit deinem Fahrrad auf der Straße und kommst zu einem Zebrastreifen. "
            "Wie musst du dich hier richtig verhalten? Erkläre!"
        ),
        "answer": (
            "Vor dem Zebrastreifen anhalten, die Fußgänger vorbeilassen und erst dann wieder losfahren."
        ),
        "steps": [
            "Am Zebrastreifen haben Fußgänger immer Vorrang.",
            "Als Radfahrer auf der Straße musst du vor dem Zebrastreifen anhalten und warten.",
            "Erst wenn alle Fußgänger den Überweg passiert haben, darfst du weiterfahren.",
        ],
        "points": 3.0,
        "has_image": True,
        "image": "0255_q3_verhalten_am_zebrastreife.png",
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 4,
        "type": "Reihenfolge beim Linksabbiegen aufschreiben",
        "text": (
            "Du möchtest an einer Kreuzung links abbiegen. "
            "Schreibe in der richtigen Reihenfolge auf, was du tun musst!"
        ),
        "answer": (
            "1. umsehen ; "
            "2. ein Handzeichen nach links geben ; "
            "3. einordnen zur Mitte ; "
            "4. Vorfahrtsregelung beachten ; "
            "5. Gegenverkehr beachten ; "
            "6. nochmals umsehen ; "
            "7. in weitem (großen) Bogen abbiegen ; "
            "8. auf Fußgänger achten"
        ),
        "steps": [
            "Schritt 1: umsehen (Verkehr hinter dir prüfen).",
            "Schritt 2: Handzeichen nach links geben.",
            "Schritt 3: zur Fahrbahnmitte einordnen.",
            "Schritt 4: Vorfahrtsregelung an der Kreuzung beachten.",
            "Schritt 5: Gegenverkehr beachten.",
            "Schritt 6: nochmals umsehen.",
            "Schritt 7: in weitem Bogen abbiegen.",
            "Schritt 8: auf Fußgänger achten.",
        ],
        "points": 8.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 5,
        "type": "Reihenfolge nummerieren",
        "text": (
            "Du willst an einem parkenden Auto vorbeifahren. "
            "Nummeriere in der richtigen Reihenfolge, was du tun musst!\n"
            "- Umschauen\n"
            "- Gegenverkehr beachten\n"
            "- Handzeichen geben und wieder nach rechts einordnen\n"
            "- Einordnen\n"
            "- Handzeichen geben\n"
            "- Seitenabstand halten"
        ),
        "answer": (
            "1 – Umschauen ; "
            "2 – Handzeichen geben ; "
            "3 – Einordnen ; "
            "4 – Gegenverkehr beachten ; "
            "5 – Seitenabstand halten ; "
            "6 – Handzeichen geben und wieder nach rechts einordnen"
        ),
        "steps": [
            "Zuerst umschauen, ob von hinten ein Fahrzeug kommt.",
            "Handzeichen geben (links), um das Ausscheren anzuzeigen.",
            "Nach links einordnen.",
            "Gegenverkehr beachten.",
            "Seitenabstand zum parkenden Auto halten (mind. 1 Meter).",
            "Nach dem Vorbeifahren Handzeichen geben und wieder nach rechts einordnen.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 6,
        "type": "Gefahrensituation mit LKW beschreiben",
        "text": (
            "Du näherst dich einer Kreuzung und wirst von einem LKW überholt. "
            "Womit musst du rechnen? Wie verhältst du dich?"
        ),
        "answer": (
            "Bremsbereit bleiben bzw. bremsen, da durch den LKW die Sicht versperrt wird und man nicht sieht, "
            "was an der Kreuzung los ist. "
            "Der LKW sieht den Radfahrer nicht, wenn dieser im toten Winkel ist. "
            "Der LKW könnte abrupt bremsen oder kurz vor dem Radfahrer auf dessen Spur ziehen."
        ),
        "steps": [
            "Der LKW verdeckt die Sicht auf die Kreuzung → bremsbereit bleiben.",
            "Radfahrer im toten Winkel des LKW sind für den Fahrer unsichtbar.",
            "LKW könnte plötzlich bremsen oder die Spur wechseln → sicheren Abstand halten.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 7,
        "type": "Vorfahrtregelung an Kreuzung erklären",
        "text": (
            "Flo kommt mit seinem Fahrrad an die Kreuzung. "
            "Er sieht folgende Situation – was kannst du dazu sagen (Vorfahrtsregelung)?"
        ),
        "answer": (
            "In dieser Situation führt die Anwendung der Regel 'rechts vor links' zu keiner Lösung, "
            "da die Fahrzeuge gleichberechtigt sind und jeder dem von rechts kommenden Vorfahrt gewähren muss. "
            "Es besteht Verständigungspflicht. Die Lösung heißt 'Dem Linken winken': "
            "Ein Fahrzeug verzichtet auf die Vorfahrt und winkt das von links kommende Fahrzeug durch. "
            "Da der Radfahrer der Schwächste ist, sollte er auf seine Vorfahrt verzichten."
        ),
        "steps": [
            "Alle vier Fahrzeuge kommen gleichzeitig – rechts vor links führt zu einer Blockade.",
            "Lösung: 'Dem Linken winken' – ein Fahrer zeigt auf das linke Fahrzeug und winkt es durch.",
            "Sobald ein Fahrzeug die Kreuzung passiert hat, gilt wieder rechts vor links.",
            "Der Radfahrer sollte als Schwächster auf seine Vorfahrt verzichten.",
        ],
        "points": 4.0,
        "has_image": True,
        "image": "0255_q7_kreuzung.png",
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 8,
        "type": "Reihenfolge an Kreuzungen nummerieren",
        "text": (
            "Wer darf zuerst fahren? Nummeriere in der richtigen Reihenfolge! "
            "(zwei Kreuzungssituationen mit je Rad, Auto, Lastwagen)"
        ),
        "answer": (
            "Situation 1: Lastwagen zuerst (1), dann Rad (2), dann Auto (3). "
            "Situation 2: Rad zuerst (1), dann Auto (2), dann Lastwagen (3)."
        ),
        "steps": [
            "Die Reihenfolge richtet sich ausschließlich nach der Himmelsrichtung/Seite, von der die Fahrzeuge kommen – nicht nach der Fahrzeugart.",
            "Das von rechts kommende Fahrzeug hat Vorfahrt, unabhängig ob Rad, Auto oder Lastwagen.",
        ],
        "points": 6.0,
        "has_image": True,
        "image": "0255_q8_kreuzung.png",
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 9,
        "type": "Lücke ergänzen",
        "text": "Der Sicherheitsabstand bei Radfahrern beträgt ___.",
        "answer": "5 Meter",
        "steps": [
            "Der vorgeschriebene Sicherheitsabstand zwischen zwei Radfahrern beträgt 5 Meter (ca. 3 Fahrradlängen).",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 10,
        "type": "Verkehrszeichen einzeichnen und benennen",
        "text": (
            "Dieses Schild befindet sich am Anfang einer Straße. "
            "Zeichne auf, wie das Schild aussieht, wenn man am anderen Ende der Straße hineinfahren möchte. "
            "Schreibe darunter, wie es heißt!"
        ),
        "answer": (
            "Das Gegenschild heißt 'Verbot der Einfahrt' (rundes rotes Schild mit weißem Balken)."
        ),
        "steps": [
            "Am Anfang der Straße steht das Schild 'Einbahnstraße' (weißer Pfeil auf blauem Grund).",
            "Wer am anderen Ende in diese Straße einfahren möchte, sieht das Schild 'Verbot der Einfahrt' – rundes rotes Schild mit weißem Balken.",
        ],
        "points": 3.0,
        "has_image": True,
        "image": "0255_q10_einbahnstrasse.png",
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 11,
        "type": "Verhaltensregeln für Radgruppen nennen",
        "text": (
            "Wie verhält sich eine Gruppe von Fahrradfahrern richtig? "
            "Nenne zwei verschiedene Dinge!"
        ),
        "answer": (
            "1. Die Gruppe sollte ausreichend Abstand zueinander halten. "
            "2. Sie sollte immer bremsbereit sein."
        ),
        "steps": [
            "Ausreichend Abstand halten: mindestens 5 Meter Sicherheitsabstand zum Vordermann.",
            "Bremsbereit fahren: jederzeit auf unerwartete Situationen reagieren können.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
]

NEW_KNOWLEDGE = []
