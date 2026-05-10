EXERCISE = {
    "id": "0667",
    "subject": "HSU",
    "grade": 4,
    "title": "Lernzielkontrolle Abwasser und Kläranlage",
    "topic": "Abwasser, Kläranlage, Grundwasserschutz, Wasserkreislauf",
    "publisher": "CATLUX",
    "source_pdf": "0667.pdf",
    "answer_pdf": "0667_Lösung.pdf",
    "total_points": 20.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Bild beschreiben und Folgen nennen",
        "text": (
            "Betrachte die Bilder! Beschreibe, warum hier Gefahren für das Grundwasser entstehen "
            "und nenne Folgen, die bald danach eintreten können! (Sätze)"
        ),
        "answer": (
            "Wenn Öl in Gewässer läuft, kann das ökologische Gleichgewicht gestört werden. "
            "Das Wasser kann „umkippen”. Wenn das Öl in das Grundwasser eindringt und wir es trinken, "
            "können wir uns selbst vergiften. "
            "Wenn Pflanzenschutzmittel in das Grundwasser eindringt und Lebewesen davon trinken oder darin schwimmen, "
            "können sie krank werden. "
            "Das Gift aus Pflanzenschutzmitteln kann mit dem Regen wieder herunterkommen und ins Grundwasser gelangen."
        ),
        "steps": [
            "Öl oder Pflanzenschutzmittel gelangen in Boden oder Gewässer.",
            "Stoffe versickern und erreichen das Grundwasser.",
            "Folgen: ökologisches Ungleichgewicht, Vergiftung von Mensch und Tier, Gewässer kippt um.",
        ],
        "points": 4.0,
        "has_image": True,
        "image": "0667_q1_gefahrenbilder.png",
        "knowledge": ["hsu.klasse4.umwelt.naturschutz", "hsu.klasse3.wasser.gewaesser"],
    },
    {
        "n": 2,
        "type": "Richtig / Falsch ankreuzen",
        "text": (
            "Kreuze die richtigen Antworten an!\n"
            "1. Wenn sich Stoffe am Boden sammeln, nennt man das Absetzen.\n"
            "2. Öl kann man durch Sieben aus dem Abwasser entfernen.\n"
            "3. Abwasser filtern kann man auch mit Sand.\n"
            "4. Holz und Steine schwimmen immer an der Wasseroberfläche."
        ),
        "answer": (
            "Richtig: 1 (Absetzen) und 3 (Filtern mit Sand).\n"
            "Falsch: 2 (Öl lässt sich nicht sieben) und 4 (Steine schwimmen nicht)."
        ),
        "steps": [
            "Absetzen = Stoffe sinken zu Boden: richtig.",
            "Öl durch Sieben entfernen: falsch – Öl schwimmt oben, wird abgeschöpft.",
            "Sand als Filtermedium: richtig.",
            "Holz schwimmt, Steine sinken: falsch – nicht immer, Steine sinken.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse4.umwelt.naturschutz"],
    },
    {
        "n": 3,
        "type": "Zuordnen",
        "text": (
            "Das Abwasser aus den Haushalten wird in einer richtigen Kläranlage gereinigt. "
            "Ordne die Station des Klärwerks der richtigen Aufgabe zu! (mit Lineal)\n\n"
            "Stationen: Grobrechen, Sandfang, Faulbehälter\n\n"
            "Aufgaben:\n"
            "– Zu ihm wird der Schlamm aus Vor- und Nachklärbecken mit Pumpen befördert.\n"
            "– Kies und Material, das nicht schwimmt, sinkt zu Boden.\n"
            "– Toilettenpapier und Äste werden entfernt."
        ),
        "answer": (
            "Grobrechen → Toilettenpapier und Äste werden entfernt.\n"
            "Sandfang → Kies und Material, das nicht schwimmt, sinkt zu Boden.\n"
            "Faulbehälter → Zu ihm wird der Schlamm aus Vor- und Nachklärbecken mit Pumpen befördert."
        ),
        "steps": [
            "Grobrechen: grobste Feststoffe (Äste, Papier) heraussieben.",
            "Sandfang: Sand und Kies setzen sich ab.",
            "Faulbehälter: nimmt den Klärschlamm auf.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse4.umwelt.naturschutz"],
    },
    {
        "n": 4,
        "type": "Erklären",
        "text": "Was geschieht in der Station „Belebungsbecken”? Erkläre die Vorgänge in ganzen Sätzen!",
        "answer": (
            "Im Belebungsbecken fressen Bakterien die meisten Schmutzteilchen auf. "
            "Damit sich die Bakterien richtig wohlfühlen und vermehren können, wird ständig Luft in das Becken geblasen. "
            "Die Bakterien brauchen dazu Sauerstoff."
        ),
        "steps": [
            "Bakterien bauen organische Schmutzstoffe ab.",
            "Luft wird eingeblasen, um Bakterien mit Sauerstoff zu versorgen.",
            "Bakterien vermehren sich und reinigen das Wasser biologisch.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse4.umwelt.naturschutz"],
    },
    {
        "n": 5,
        "type": "Erklären",
        "text": "Was geschieht mit dem Klärschlamm? Erkläre ausführlich!",
        "answer": (
            "Der Klärschlamm kommt in die Faultürme. Dort bleibt er viele Tage lang. "
            "Faulbakterien zersetzen den Schlamm ohne Luft und bei einer Temperatur von 37 °C "
            "in Gas, Wasser und Feststoffe. "
            "Die Feststoffe können in der Landwirtschaft als Dünger verwendet oder nach weiterer Entwässerung verbrannt werden. "
            "Das entstehende Gas wird in einem großen Gasbehälter gesammelt und kann z. B. zur Stromerzeugung verwendet werden."
        ),
        "steps": [
            "Klärschlamm gelangt in Faultürme.",
            "Faulbakterien zersetzen ihn ohne Luft bei 37 °C.",
            "Entstehende Produkte: Gas (Energie), Wasser, Feststoffe (Dünger oder Verbrennung).",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse4.umwelt.naturschutz"],
    },
    {
        "n": 6,
        "type": "Erklären",
        "text": "Warum wird das geklärte Wasser in Flüsse und nicht in die Haushalte geleitet?",
        "answer": (
            "Das geklärte Wasser ist noch kein Trinkwasser, enthält aber nur noch wenige Verunreinigungen. "
            "Der Fluss wird dadurch nicht belastet. In der Natur wird das Wasser weiter gereinigt, "
            "zum Beispiel durch die Filterwirkung des Bodens. "
            "Das Wasser kann dann wieder als Rohwasser im Wasserwerk verwendet werden."
        ),
        "steps": [
            "Geklärtes Wasser erfüllt noch nicht die Trinkwasserqualität.",
            "Im Fluss und im Boden findet weitere natürliche Reinigung statt.",
            "Anschließend kann es als Rohwasser für Wasserwerke genutzt werden.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf", "hsu.klasse4.umwelt.naturschutz"],
    },
    {
        "n": 7,
        "type": "Begründen",
        "text": (
            "Warum brauchen wir eigentlich Kläranlagen? Die sind doch teuer und müssen ständig erneuert werden! "
            "Begründe! (Sätze)"
        ),
        "answer": (
            "Das Schmutzwasser wird gereinigt und kann so dem Wasserkreislauf wieder zugeführt werden. "
            "Somit bleibt das Gleichgewicht erhalten. "
            "Würden wir dies nicht tun, hätten wir irgendwann kein Trinkwasser mehr, "
            "da das gesamte Wasser und damit die Umwelt verschmutzt wäre."
        ),
        "steps": [
            "Kläranlagen reinigen Schmutzwasser und führen es dem Kreislauf zurück.",
            "Ohne Kläranlagen: Gewässer und Grundwasser würden verschmutzen.",
            "Folge: kein sauberes Trinkwasser mehr verfügbar.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse4.umwelt.naturschutz", "hsu.klasse3.wasser.kreislauf"],
    },
]

NEW_KNOWLEDGE = []
