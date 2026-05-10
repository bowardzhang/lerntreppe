EXERCISE = {
    "id": "0934",
    "subject": "HSU",
    "grade": 4,
    "title": "Lernzielkontrolle: Deutschland, Bayern",
    "topic": "Deutschland, Bayern, Bundesländer, Regierungsbezirke, Nachbarländer, Geografie, Nationalparks",
    "publisher": "CATLUX",
    "source_pdf": "0934.pdf",
    "answer_pdf": "0934 (1).pdf",
    "total_points": 32.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Lückensätze",
        "text": (
            "Vervollständige die Sätze!\n"
            "Deutschland ist ohne die Stadtstaaten in ___ Bundesländer eingeteilt.\n"
            "Die Stadtstaaten heißen: ___.\n"
            "Die meisten Einwohner hat das Bundesland ___.\n"
            "Die wenigsten Einwohner befinden sich in ___.\n"
            "___ (3) haben eine Grenze zu Frankreich.\n"
            "___ (3) haben eine Grenze zu Polen.\n"
            "Das Bundesland ___ produziert viel Milch.\n"
            "___ umringt als Bundesland Berlin.\n"
            "Das kleinste Bundesland außer den Stadtstaaten ist ___."
        ),
        "answer": (
            "Deutschland ist ohne die Stadtstaaten in 13 Bundesländer eingeteilt.\n"
            "Die Stadtstaaten heißen: Bremen, Hamburg, Berlin.\n"
            "Die meisten Einwohner hat das Bundesland Nordrhein-Westfalen.\n"
            "Die wenigsten Einwohner befinden sich in Bremen.\n"
            "Baden-Württemberg, Rheinland-Pfalz, Saarland haben eine Grenze zu Frankreich.\n"
            "Mecklenburg-Vorpommern, Brandenburg, Sachsen haben eine Grenze zu Polen.\n"
            "Das Bundesland Schleswig-Holstein produziert viel Milch.\n"
            "Brandenburg umringt als Bundesland Berlin.\n"
            "Das kleinste Bundesland außer den Stadtstaaten ist Saarland."
        ),
        "steps": [
            "16 Bundesländer gesamt – 3 Stadtstaaten = 13 Flächenländer",
            "Stadtstaaten: Berlin, Bremen, Hamburg",
            "Bevölkerungsreichstes Bundesland: Nordrhein-Westfalen; bevölkerungsärmstes: Bremen",
            "Grenze zu Frankreich: Baden-Württemberg, Rheinland-Pfalz, Saarland",
            "Grenze zu Polen: Mecklenburg-Vorpommern, Brandenburg, Sachsen",
            "Milchwirtschaft: Schleswig-Holstein",
            "Brandenburg umschließt Berlin vollständig",
            "Kleinstes Flächenland: Saarland",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "hsu.klasse4.deutschland.bundeslaender",
            "hsu.klasse4.europa.nachbarlaender",
        ],
    },
    {
        "n": 2,
        "type": "Kartenaufgabe",
        "text": (
            "Beschrifte auf dieser Deutschlandkarte genau folgende Städte und Gebiete! "
            "Notiere dabei jeweils ihren Namen.\n"
            "a) Die deutsche Hauptstadt\n"
            "b) Das Bundesland, in dem wir leben\n"
            "c) Die Landeshauptstadt unseres Bundeslandes"
        ),
        "answer": (
            "a) Berlin (deutsche Hauptstadt) in die Karte einzeichnen\n"
            "b) Bayern (Bundesland) in die Karte einzeichnen\n"
            "c) München (Landeshauptstadt Bayerns) in die Karte einzeichnen\n"
            "(Hinweis: Lösung ist auf Bayern ausgerichtet; für andere Bundesländer entsprechend anpassen)"
        ),
        "steps": [
            "Berlin liegt im Nordosten Deutschlands",
            "Bayern liegt im Südosten Deutschlands",
            "München liegt im Süden Bayerns",
        ],
        "points": 3.0,
        "has_image": True,
        "image": "0934_q2_karte_deutschland.png",
        "knowledge": [
            "hsu.klasse4.deutschland.bundeslaender",
        ],
    },
    {
        "n": 3,
        "type": "Geschichte",
        "text": "Welche sechs Bundesländer waren vor 1989 Teile von Ost-Deutschland?",
        "answer": (
            "Mecklenburg-Vorpommern, Brandenburg, Berlin, "
            "Sachsen-Anhalt, Sachsen, Thüringen"
        ),
        "steps": [
            "Die 5 neuen Bundesländer plus Ost-Berlin: "
            "Mecklenburg-Vorpommern, Brandenburg, Berlin, Sachsen-Anhalt, Sachsen, Thüringen",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "hsu.klasse4.deutschland.politik",
            "hsu.klasse4.deutschland.bundeslaender",
        ],
    },
    {
        "n": 4,
        "type": "Geografie",
        "text": "An welches Meer und zu welchem Gebirge kannst du in Deutschland fahren?",
        "answer": "Meere: Nordsee, Ostsee; Gebirge: Alpen",
        "steps": [
            "Meere in Deutschland: Nordsee (im Nordwesten) und Ostsee (im Nordosten)",
            "Gebirge: Die Alpen im Süden (Bayerische Alpen)",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "hsu.klasse4.deutschland.geografie",
        ],
    },
    {
        "n": 5,
        "type": "Nachbarländer",
        "text": "Wie viele Nachbarländer hat Deutschland? Schreibe alle auf!",
        "answer": (
            "Deutschland hat 9 Nachbarländer:\n"
            "Frankreich, Dänemark, Luxemburg, Belgien, Niederlande, "
            "Polen, Schweiz, Österreich, Tschechien"
        ),
        "steps": [
            "9 Nachbarländer: Dänemark (N), Niederlande (NW), Belgien (W), "
            "Luxemburg (W), Frankreich (SW), Schweiz (S), Österreich (S/SO), "
            "Tschechien (O), Polen (O/NO)",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "hsu.klasse4.europa.nachbarlaender",
        ],
    },
    {
        "n": 6,
        "type": "Tabelle ergänzen",
        "text": (
            "Vervollständige die Tabelle!\n"
            "Regierungsbezirk | Regierungssitz\n"
            "___ | Bayreuth\n"
            "___ | München\n"
            "___ | Regensburg\n"
            "___ | Ansbach\n"
            "Unterfranken | ___\n"
            "Schwaben | ___\n"
            "Niederbayern | ___"
        ),
        "answer": (
            "Oberfranken | Bayreuth\n"
            "Oberbayern | München\n"
            "Oberpfalz | Regensburg\n"
            "Mittelfranken | Ansbach\n"
            "Unterfranken | Würzburg\n"
            "Schwaben | Augsburg\n"
            "Niederbayern | Landshut"
        ),
        "steps": [
            "Oberfranken – Bayreuth",
            "Oberbayern – München",
            "Oberpfalz – Regensburg",
            "Mittelfranken – Ansbach",
            "Unterfranken – Würzburg",
            "Schwaben – Augsburg",
            "Niederbayern – Landshut",
        ],
        "points": 3.5,
        "has_image": False,
        "image": None,
        "knowledge": [
            "hsu.klasse4.deutschland.bundeslaender",
        ],
    },
    {
        "n": 7,
        "type": "Nachbarbundesländer",
        "text": "Nenne alle Nachbarbundesländer von Bayern!",
        "answer": "Baden-Württemberg, Hessen, Thüringen, Sachsen",
        "steps": [
            "Bayern grenzt an die deutschen Bundesländer: "
            "Baden-Württemberg (W), Hessen (NW), Thüringen (N), Sachsen (NO)",
            "Außerdem grenzt Bayern an Österreich und Tschechien (internationale Grenzen)",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "hsu.klasse4.deutschland.bundeslaender",
        ],
    },
    {
        "n": 8,
        "type": "Fluss",
        "text": (
            "Welcher bayerische Fluss fließt durch zwei Regierungshauptstädte? "
            "Nenne den Fluss und die beiden Städte!"
        ),
        "answer": "Die Isar fließt durch München und Landshut.",
        "steps": [
            "Die Isar fließt von den Alpen nach Norden",
            "Sie durchfließt München (Regierungssitz Oberbayern) und Landshut (Regierungssitz Niederbayern)",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "hsu.klasse4.deutschland.geografie",
        ],
    },
    {
        "n": 9,
        "type": "Ortsnamen",
        "text": "Welchen Bestandteil haben viele Ortsnamen in Bayern, die ein Kurort sind?",
        "answer": "Bad … (z. B. Bad Kissingen, Bad Tölz)",
        "steps": [
            "Bayerische Kurorte beginnen häufig mit „Bad”, z. B. Bad Kissingen, Bad Tölz, Bad Reichenhall",
        ],
        "points": 1.5,
        "has_image": False,
        "image": None,
        "knowledge": [
            "hsu.klasse4.deutschland.geografie",
        ],
    },
    {
        "n": 10,
        "type": "Nationalparks",
        "text": "Wie heißen die zwei Nationalparks in Bayern?",
        "answer": (
            "1. Nationalpark Bayerischer Wald\n"
            "2. Nationalpark Berchtesgaden"
        ),
        "steps": [
            "Nationalpark Bayerischer Wald (ältester Nationalpark Deutschlands)",
            "Nationalpark Berchtesgaden (einziger Alpen-Nationalpark Deutschlands)",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "hsu.klasse4.deutschland.geografie",
        ],
    },
    {
        "n": 11,
        "type": "Lückentext",
        "text": (
            "Vervollständige den Text!\n"
            "Der höchste Berg in Bayern ist die ___. Die ___ teilt unser Bundesland "
            "in das nördliche und südliche Bayern. Die berühmteste Touristenattraktion "
            "ist das ___. Im Herzen Bayerns liegt das Hopfenland ___."
        ),
        "answer": (
            "Der höchste Berg in Bayern ist die Zugspitze. "
            "Die Donau teilt unser Bundesland in das nördliche und südliche Bayern. "
            "Die berühmteste Touristenattraktion ist das Schloss Neuschwanstein. "
            "Im Herzen Bayerns liegt das Hopfenland Hallertau."
        ),
        "steps": [
            "Höchster Berg in Bayern: Zugspitze (2962 m)",
            "Die Donau fließt von West nach Ost durch Bayern und teilt es in Nord und Süd",
            "Bekannteste Sehenswürdigkeit: Schloss Neuschwanstein (Schwangau)",
            "Hallertau = größtes zusammenhängendes Hopfenanbaugebiet der Welt, in Niederbayern/Oberbayern",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "hsu.klasse4.deutschland.geografie",
            "hsu.klasse4.deutschland.bundeslaender",
        ],
    },
]

NEW_KNOWLEDGE = []
