EXERCISE = {
    "id": "0935",
    "subject": "HSU",
    "grade": 4,
    "title": "Lernzielkontrolle: Deutschland, Bayern",
    "topic": "Bayern, Regierungsbezirke, Staatswappen, Freistaat, Flüsse, Seen, Bundesländer, Einwanderung",
    "publisher": "CATLUX",
    "source_pdf": "0935.pdf",
    "answer_pdf": "0935 (1).pdf",
    "total_points": 41.5,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Kartenaufgabe",
        "text": "Benenne die bayerischen Regierungsbezirke auf der Karte!",
        "answer": (
            "Die 7 Regierungsbezirke Bayerns:\n"
            "Oberbayern, Niederbayern, Oberpfalz, Oberfranken, "
            "Mittelfranken, Unterfranken, Schwaben"
        ),
        "steps": [
            "Bayern hat 7 Regierungsbezirke",
            "Von Nord nach Süd und West nach Ost: "
            "Unterfranken (NW), Mittelfranken (Mitte), Oberfranken (NO), "
            "Oberpfalz (O), Niederbayern (SO), Oberbayern (S), Schwaben (W)",
        ],
        "points": 7.0,
        "has_image": True,
        "image": "0935_q1_karte_regierungsbezirke.png",
        "knowledge": [
            "hsu.klasse4.deutschland.bundeslaender",
        ],
    },
    {
        "n": 2,
        "type": "Staatswappen",
        "text": (
            "Nebenstehend siehst du das kleine bayerische Staatswappen. "
            "Welche Symbole sind im großen bayerischen Staatswappen versteckt "
            "und wofür stehen sie? Nenne 3!"
        ),
        "answer": (
            "Mögliche Antworten (3 nennen):\n"
            "Der goldene Löwe (schwarzes Feld) – steht für die Oberpfalz\n"
            "Der fränkische Rechen (rotes Feld mit weißen Streifen) – steht für Ober-, Unter- und Mittelfranken\n"
            "Der blaue Panther – steht für Ober- und Niederbayern\n"
            "Die drei schwarzen Löwen – stehen für Schwaben\n"
            "Das weiß-blaue Herzschild – steht für Bayern als Ganzes\n"
            "Die Volkskrone – das Volk hat die Macht"
        ),
        "steps": [
            "Goldener Löwe im schwarzen Feld = Oberpfalz",
            "Fränkischer Rechen (weiße Spitzen im roten Feld) = Franken (Ober-, Unter-, Mittelfranken)",
            "Blauer Panther = Ober- und Niederbayern",
            "Drei schwarze Löwen = Schwaben",
            "Weiß-blaues Herzschild = ganz Bayern",
            "Volkskrone = Volkssouveränität (das Volk hat die Macht)",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "hsu.klasse4.deutschland.bundeslaender",
        ],
    },
    {
        "n": 3,
        "type": "Zuordnen und nummerieren",
        "text": (
            "Verbinde richtig und nummeriere dann! (Beginne mit der größten Einheit!)\n"
            "Deutschland ↔ Bundesland\n"
            "Oberpfalz ↔ Land\n"
            "Bayern ↔ Regierungsbezirk"
        ),
        "answer": (
            "Größte Einheit zuerst:\n"
            "1 = Land → Deutschland\n"
            "2 = Bundesland → Bayern\n"
            "3 = Regierungsbezirk → Oberpfalz"
        ),
        "steps": [
            "Hierarchie von groß nach klein: Land (Deutschland) → Bundesland (Bayern) → Regierungsbezirk (Oberpfalz)",
            "1 = Deutschland (Land), 2 = Bayern (Bundesland), 3 = Oberpfalz (Regierungsbezirk)",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "hsu.klasse4.deutschland.bundeslaender",
        ],
    },
    {
        "n": 4,
        "type": "Geschichte",
        "text": "Wann erhielt Bayern den Titel „Freistaat” und warum?",
        "answer": (
            "Im Jahr 1918, weil Bayern in dieser Zeit nicht mehr von einem König "
            "regiert wurde (Ende der Monarchie durch die Novemberrevolution)."
        ),
        "steps": [
            "Bayern wurde 1918 zum Freistaat (= Republik ohne König)",
            "Hintergrund: Ende des 1. Weltkriegs, Novemberrevolution, König Ludwig III. floh",
            "„Freistaat” bedeutet: Der Staat gehört dem Volk (res publica)",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "hsu.klasse4.deutschland.politik",
            "hsu.klasse4.deutschland.bundeslaender",
        ],
    },
    {
        "n": 5,
        "type": "Flüsse und Seen",
        "text": "Welche Flüsse und Seen kennst du in Bayern? Nenne jeweils 3 Stück!",
        "answer": (
            "Flüsse (3 nennen): Donau, Main, Isar, Lech, Inn\n"
            "Seen (3 nennen): Bodensee, Chiemsee, Ammersee, Starnberger See"
        ),
        "steps": [
            "Wichtige bayerische Flüsse: Donau, Isar, Lech, Inn, Main, Salzach",
            "Wichtige bayerische Seen: Chiemsee, Starnberger See, Ammersee, Bodensee (anteilig)",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "hsu.klasse4.deutschland.geografie",
        ],
    },
    {
        "n": 6,
        "type": "Tabelle ergänzen",
        "text": (
            "Vervollständige die Tabelle (Bundesland ↔ Landeshauptstadt)!\n"
            "Bayern | ___\n"
            "Nordrhein-Westfalen | ___\n"
            "Baden-Württemberg | ___\n"
            "Sachsen | ___\n"
            "Hessen | ___\n"
            "Thüringen | ___\n"
            "Mecklenburg-Vorpommern | ___\n"
            "___ | Saarbrücken\n"
            "___ | Mainz\n"
            "___ | Hannover\n"
            "___ | Kiel\n"
            "___ | Potsdam\n"
            "___ | Magdeburg"
        ),
        "answer": (
            "Bayern | München\n"
            "Nordrhein-Westfalen | Düsseldorf\n"
            "Baden-Württemberg | Stuttgart\n"
            "Sachsen | Dresden\n"
            "Hessen | Wiesbaden\n"
            "Thüringen | Erfurt\n"
            "Mecklenburg-Vorpommern | Schwerin\n"
            "Saarland | Saarbrücken\n"
            "Rheinland-Pfalz | Mainz\n"
            "Niedersachsen | Hannover\n"
            "Schleswig-Holstein | Kiel\n"
            "Brandenburg | Potsdam\n"
            "Sachsen-Anhalt | Magdeburg"
        ),
        "steps": [
            "Bayern – München; NRW – Düsseldorf; BW – Stuttgart; Sachsen – Dresden",
            "Hessen – Wiesbaden; Thüringen – Erfurt; Mecklenburg-Vorpommern – Schwerin",
            "Saarland – Saarbrücken; Rheinland-Pfalz – Mainz; Niedersachsen – Hannover",
            "Schleswig-Holstein – Kiel; Brandenburg – Potsdam; Sachsen-Anhalt – Magdeburg",
        ],
        "points": 6.5,
        "has_image": False,
        "image": None,
        "knowledge": [
            "hsu.klasse4.deutschland.bundeslaender",
        ],
    },
    {
        "n": 7,
        "type": "Zuordnen",
        "text": (
            "An welche Bundesländer grenzen die Stadtstaaten? "
            "Nenne Stadtstaaten und Bundesländer!"
        ),
        "answer": (
            "Berlin – Brandenburg\n"
            "Bremen – Niedersachsen\n"
            "Hamburg – Schleswig-Holstein und Niedersachsen"
        ),
        "steps": [
            "Berlin ist vollständig von Brandenburg umgeben",
            "Bremen (Stadt und Bremerhaven) liegt vollständig in Niedersachsen",
            "Hamburg grenzt an Schleswig-Holstein und Niedersachsen",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "hsu.klasse4.deutschland.bundeslaender",
        ],
    },
    {
        "n": 8,
        "type": "Ankreuzen",
        "text": (
            "Kreuze die Länder an, die nicht an Deutschland angrenzen!\n"
            "☐ Spanien  ☐ Polen\n"
            "☐ Luxemburg  ☐ Portugal\n"
            "☐ Schweiz  ☐ Österreich\n"
            "☐ Italien  ☐ Belgien"
        ),
        "answer": (
            "Nicht an Deutschland angrenzend (ankreuzen):\n"
            "✗ Spanien\n"
            "✗ Portugal\n"
            "✗ Italien"
        ),
        "steps": [
            "Deutschland grenzt an: Dänemark, Niederlande, Belgien, Luxemburg, Frankreich, "
            "Schweiz, Österreich, Tschechien, Polen",
            "Spanien, Portugal und Italien grenzen nicht an Deutschland",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "hsu.klasse4.europa.nachbarlaender",
        ],
    },
    {
        "n": 9,
        "type": "Nachbarland",
        "text": "Nenne ein Nachbarland, in dem auch Deutsch gesprochen wird!",
        "answer": "Österreich (auch möglich: Schweiz, Luxemburg, Liechtenstein)",
        "steps": [
            "Deutschsprachige Nachbarländer Deutschlands: Österreich, Schweiz (teilweise), Luxemburg (teilweise)",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "hsu.klasse4.europa.nachbarlaender",
        ],
    },
    {
        "n": 10,
        "type": "Einwanderung",
        "text": "Nenne vier Gründe, warum Menschen nach Deutschland kommen!",
        "answer": (
            "Sie werden politisch oder religiös verfolgt.\n"
            "Sie suchen Arbeit in Deutschland.\n"
            "Sie kommen durch Heirat nach Deutschland.\n"
            "Sie suchen ein besseres Leben / Sicherheit / Ausbildungsmöglichkeiten."
        ),
        "steps": [
            "Flucht vor politischer oder religiöser Verfolgung",
            "Arbeitsmigration (bessere Jobchancen)",
            "Familienzusammenführung / Heirat",
            "Bessere Lebensbedingungen, Ausbildung, Sicherheit",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "hsu.klasse4.deutschland.politik",
        ],
    },
    {
        "n": 11,
        "type": "Probleme Einwanderer",
        "text": "Welche Probleme können diese Menschen haben? Nenne zwei!",
        "answer": (
            "Keine Wohnung finden / keine Arbeitsstelle bekommen\n"
            "Sprachbarriere / Diskriminierung / fehlende Anerkennung von Abschlüssen"
        ),
        "steps": [
            "Häufige Probleme: Wohnungssuche, Arbeitssuche, Sprachbarrieren, Diskriminierung",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "hsu.klasse4.deutschland.politik",
        ],
    },
    {
        "n": 12,
        "type": "Handlungsmöglichkeiten",
        "text": (
            "Wie kannst du ein ausländisches Kind unterstützen, das neu in eine "
            "deutsche Schule gekommen ist? Nenne zwei Möglichkeiten!"
        ),
        "answer": (
            "Ihm die Sprache beibringen / gemeinsam Deutsch üben.\n"
            "Ihm die Bräuche zeigen und erklären.\n"
            "Es in die Klasse einführen / mit ihm spielen / Freundschaft schließen."
        ),
        "steps": [
            "Sprachhilfe: gemeinsam Deutsch lernen, erklären",
            "Soziale Integration: Bräuche erklären, Freundschaft anbieten, in Spiele einbeziehen",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "hsu.klasse4.deutschland.politik",
        ],
    },
]

NEW_KNOWLEDGE = []
