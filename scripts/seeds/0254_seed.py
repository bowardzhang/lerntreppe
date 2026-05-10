EXERCISE = {
    "id": "0254",
    "subject": "HSU",
    "grade": 4,
    "title": "Lernzielkontrolle: Fahrrad, Verkehrsschilder, Fahrradprüfung",
    "topic": "Fahrrad, Verkehrsschilder, Fahrradprüfung",
    "publisher": "CATLUX",
    "source_pdf": "0254.pdf",
    "answer_pdf": "0254 (1).pdf",
    "total_points": 44.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Fehlende Fahrradteile benennen und einzeichnen",
        "text": (
            "An diesem Fahrrad fehlen 4 Teile, damit es verkehrssicher wird.\n"
            "a) Schreibe sie auf!\n"
            "b) Zeichne sie ein!"
        ),
        "answer": (
            "1. Glocke ; "
            "2. weißer Scheinwerfer vorn ; "
            "3. weißer Reflektor vorn ; "
            "4. rote Rückleuchte / Rückstrahler"
        ),
        "steps": [
            "Ein verkehrssicheres Fahrrad braucht: Glocke, Scheinwerfer vorn (weiß), Reflektor vorn (weiß) und Rückleuchte/Rückstrahler hinten (rot).",
            "Die vier fehlenden Teile am abgebildeten Fahrrad sind diese vier Ausrüstungsgegenstände.",
        ],
        "points": 8.0,
        "has_image": True,
        "image": "0254_q1_fahrrad.png",
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 2,
        "type": "Verkehrszeichen benennen und ausmalen",
        "text": "Benenne die Zeichen und male sie richtig aus! (4 Zeichen abgebildet)",
        "answer": (
            "Vorfahrtstraße (gelbes Schild mit weißem Rand) ; "
            "Vorfahrt gewähren (umgekehrtes Dreieck, weißes Schild mit rotem Rand) ; "
            "Verbot der Einfahrt (rotes rundes Schild mit weißem Balken) ; "
            "Vorfahrt an der nächsten Kreuzung (weißes Schild mit gelbem Quadrat auf der Spitze, roter Rand)"
        ),
        "steps": [
            "Gelbes Schild mit weißer Umrandung = Vorfahrtstraße.",
            "Umgekehrtes Dreieck (weiß, roter Rand) = Vorfahrt gewähren.",
            "Rundes Schild mit rotem Grund und weißem Balken = Verbot der Einfahrt.",
            "Weißes Schild mit gelbem Quadrat auf Spitze und rotem Rand = Vorfahrt an der nächsten Kreuzung.",
        ],
        "points": 6.0,
        "has_image": True,
        "image": "0254_q2_zeichen.png",
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 3,
        "type": "Ausnahmen der Vorfahrtsregel nennen",
        "text": "Wann gilt die Regel 'Rechts vor links' nicht?",
        "answer": (
            "1. Wenn die Polizei den Verkehr regelt ; "
            "2. Wenn Ampeln den Verkehr regeln ; "
            "3. Wenn Schilder den Verkehr regeln ; "
            "4. Bei einer Grundstücksausfahrt"
        ),
        "steps": [
            "'Rechts vor links' ist die Grundregel ohne weitere Regelung.",
            "Ausnahmen: Verkehrspolizist hat höchste Priorität, dann Ampeln, dann Verkehrsschilder.",
            "Wer aus einem Grundstück auf die Straße fährt, hat keine Vorfahrt – die Grundregel gilt dort nicht.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 4,
        "type": "Reihenfolge nummerieren",
        "text": (
            "Du willst an der Kreuzung links abbiegen. "
            "Nummeriere die folgenden Punkte in der richtigen Reihenfolge!\n"
            "- Ich biege in weitem Bogen ab\n"
            "- Ich schaue nochmals um\n"
            "- Ich beachte die Vorfahrt\n"
            "- Ich gebe ein deutliches Handzeichen links\n"
            "- Ich achte auf Fußgänger\n"
            "- Ich schaue um\n"
            "- Ich achte auf den Gegenverkehr\n"
            "- Ich ordne mich zur Fahrbahnmitte ein"
        ),
        "answer": (
            "1 – Ich schaue um ; "
            "2 – Ich gebe ein deutliches Handzeichen links ; "
            "3 – Ich ordne mich zur Fahrbahnmitte ein ; "
            "4 – Ich beachte die Vorfahrt ; "
            "5 – Ich achte auf den Gegenverkehr ; "
            "6 – Ich schaue nochmals um ; "
            "7 – Ich biege in weitem Bogen ab ; "
            "8 – Ich achte auf Fußgänger"
        ),
        "steps": [
            "Vor dem Abbiegen: umsehen, Handzeichen links geben, zur Fahrbahnmitte einordnen.",
            "An der Kreuzung: Vorfahrt beachten, Gegenverkehr beachten, nochmals umschauen.",
            "Beim Abbiegen: in weitem Bogen abbiegen, auf Fußgänger achten.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 5,
        "type": "Verhalten bei Grundstücksausfahrt beschreiben",
        "text": (
            "Du kommst mit deinem Fahrrad aus einer Grundstückseinfahrt und willst nach "
            "rechts auf die Straße fahren. Was musst du dabei beachten?"
        ),
        "answer": (
            "Die Autos, die bereits auf der Straße fahren, haben Vorrang – du musst warten, bis die Straße frei ist. "
            "Fußgänger auf dem Gehweg haben ebenfalls Vorrang und müssen vorbeigelassen werden. "
            "Du vergewisserst dich, dass kein Fußgänger kommt, fährst bis zur Straße, "
            "gibst mit dem Arm ein Zeichen nach rechts und fährst erst dann auf die Straße."
        ),
        "steps": [
            "Aus einer Grundstückseinfahrt kommend hat man keine Vorfahrt.",
            "Zuerst Fußgänger auf dem Gehweg vorbeilassen.",
            "Dann warten, bis die Fahrbahn frei ist.",
            "Handzeichen nach rechts geben und erst dann einbiegen.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 6,
        "type": "Zeichen des Verkehrspolizisten erklären",
        "text": (
            "Was bedeuten die Zeichen des Verkehrspolizisten? "
            "Schreibe dies zu den Polizisten und male die Ampeln entsprechend aus! "
            "(3 Polizistenstellungen abgebildet)"
        ),
        "answer": (
            "Arme seitlich ausgestreckt = Stopp, Anhalten ; "
            "Eine Hand nach oben = Achtung, bereit halten ; "
            "Arm vorwärts gestreckt / Wink vorwärts = Ich darf fahren"
        ),
        "steps": [
            "Polizist mit beiden Armen seitlich: Querverkehr muss halten → wie rote Ampel.",
            "Polizist hebt eine Hand: Achtung, bald kommt eine Änderung → wie gelbe Ampel.",
            "Polizist winkt vorwärts: Fahrt frei → wie grüne Ampel.",
        ],
        "points": 3.0,
        "has_image": True,
        "image": "0254_q6_polizist.png",
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 7,
        "type": "Rangfolge der Vorfahrtregelung ergänzen",
        "text": (
            "Die Vorfahrt kann verschieden geregelt werden. "
            "Ergänze und schreibe nach der Wichtigkeit auf!\n"
            "1 Verkehrspolizist\n"
            "2 ___\n"
            "3 ___\n"
            "4 ___"
        ),
        "answer": (
            "1. Verkehrspolizist ; "
            "2. Ampel ; "
            "3. Schilder ; "
            "4. rechts vor links"
        ),
        "steps": [
            "Höchste Priorität hat der Verkehrspolizist.",
            "Dann Ampeln.",
            "Dann Verkehrsschilder (z. B. Vorfahrtstraße, Stoppschild).",
            "Wenn nichts anderes geregelt ist: rechts vor links.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
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
            "Situation 1: Auto zuerst (1), dann Rad (2), dann Lastwagen (3). "
            "Situation 2: Rad zuerst (1), dann Auto (2), dann Lastwagen (3)."
        ),
        "steps": [
            "Die Reihenfolge richtet sich nach der Vorfahrtsregel rechts vor links.",
            "Das von rechts kommende Fahrzeug fährt zuerst, unabhängig von der Fahrzeugart.",
        ],
        "points": 6.0,
        "has_image": True,
        "image": "0254_q8_kreuzung.png",
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 9,
        "type": "Gefahrensituation erklären",
        "text": (
            "Warum darfst du an einem LKW, der rechts abbiegen will, "
            "nicht auf der rechten Seite vorbeifahren?"
        ),
        "answer": (
            "Weil man sich dann im sogenannten toten Winkel befindet und der LKW-Fahrer einen nicht sehen kann."
        ),
        "steps": [
            "LKW-Fahrer haben einen großen toten Winkel rechts neben und vor dem Fahrzeug.",
            "Wer rechts neben einem abbiegenden LKW fährt, wird überfahren, weil der Fahrer ihn nicht sieht.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 10,
        "type": "Ankreuzaufgabe Kreisverkehr",
        "text": (
            "Kreuze an, was stimmt! Bei einem Kreisverkehr …\n"
            "- gibt man linkes Handzeichen, wenn man mit dem Fahrrad herausfährt.\n"
            "- gibt man rechtes Handzeichen, wenn man mit dem Fahrrad herausfährt.\n"
            "- gibt man rechtes Handzeichen, wenn man mit dem Fahrrad hineinfährt.\n"
            "- hat der Vorfahrt, der in den Kreis hineinfährt.\n"
            "- hat der Vorfahrt, der im Kreis fährt.\n"
            "- hat der Vorfahrt, der von links kommt.\n"
            "- hat der Vorfahrt, der von rechts kommt."
        ),
        "answer": (
            "Richtig: 'gibt man rechtes Handzeichen, wenn man mit dem Fahrrad herausfährt.' ; "
            "'hat der Vorfahrt, der im Kreis fährt.'"
        ),
        "steps": [
            "Im Kreisverkehr hat der im Kreis fahrende Verkehr Vorfahrt.",
            "Beim Herausfahren aus dem Kreisverkehr gibt man rechtes Handzeichen.",
            "Beim Hineinfahren wird kein Handzeichen gegeben.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 11,
        "type": "Verkehrszeichen einzeichnen und Anzahl bestimmen",
        "text": (
            "Zeichne ein mögliches Verkehrszeichen in der richtigen Farbe! "
            "Wie viele Möglichkeiten gibt es? Kreuze an!\n"
            "- 1\n"
            "- 2\n"
            "- mehr als 2"
        ),
        "answer": "Es gibt genau 1 Möglichkeit.",
        "steps": [
            "Das abgebildete Zeichen (Stoppschild / Vorfahrt gewähren) hat nur eine festgelegte Form und Farbe.",
            "Die Antwort ist: 1.",
        ],
        "points": 2.0,
        "has_image": True,
        "image": "0254_q11_zeichen.png",
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
    {
        "n": 12,
        "type": "Verkehrszeichen im Ausland erklären",
        "text": (
            "Du machst mit deinen Eltern Urlaub in Marokko. Ihr habt eine Fahrradtour geplant, "
            "um die Stadt zu erkunden. Auf dem Weg kommst du an einem Verkehrsschild vorbei, "
            "das mit einem arabischen Wort beschriftet ist. "
            "Welche Bedeutung hat dieses Verkehrszeichen? Erkläre, was du beachten musst."
        ),
        "answer": (
            "Das Verkehrszeichen ist ein Stoppschild. Es ist das einzige Verkehrszeichen mit acht Ecken "
            "und hat in jedem Land die gleiche Bedeutung: Halt! Vorfahrt gewähren! "
            "Man muss vollständig anhalten und den Querverkehr durchlassen."
        ),
        "steps": [
            "Das Stoppschild ist weltweit eindeutig erkennbar: achteckige Form, rote Farbe.",
            "Die Form allein – ohne Schrift lesen zu müssen – zeigt die Bedeutung: Anhalten, Vorfahrt gewähren.",
        ],
        "points": 2.0,
        "has_image": True,
        "image": "0254_q12_stoppschild.png",
        "knowledge": ["hsu.klasse2.verkehr.regeln"],
    },
]

NEW_KNOWLEDGE = []
