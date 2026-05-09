EXERCISE = {
    "id": "2143",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Eisbären – Könige der Arktis",
    "topic": "Leseverstehen, Sachtext, Eisbär, Arktis, Tiere, Naturschutz",
    "publisher": "CATLUX",
    "source_pdf": "2143.pdf",
    "answer_pdf": "2143 (1).pdf",
    "total_points": 32.0,
}

LESETEXT = (
    "Eisbären – Könige der Arktis\n\n"
    "Die Meere und das Festland rund um den Nordpol werden Arktis genannt. "
    "Dazu gehören auch Teile von Kanada, Grönland, Skandinavien, Russland und "
    "Alaska. Das Zentrum der Arktis bildet eine riesige Insel, die durch und "
    "durch aus Eis besteht. Diese Eisplatte ist zwischen vier und sechs Meter "
    "dick, bis zu 1 600 Kilometer breit und liegt auf dem arktischen Ozean. "
    "Mitten in dieser Eiswüste befindet sich der Nordpol. Die Insel ist von "
    "Packeis umgeben. Das sind dicke Eisschichten, die zum Teil am Meeresboden "
    "oder an den Kontinenten festgefroren sind. An den Küsten rund um den "
    "arktischen Ozean verschwindet das Eis im Sommer für wenige Monate. Für "
    "alle Pflanzen und Tiere, die es dort gibt, ist das ein großes Glück – "
    "sonst würden sie nicht überleben können. In der Arktis leben viele "
    "verschiedene Tierarten: Robben, Walrosse, Wale, Polarwölfe, Polarfüchse "
    "und natürlich die Eisbären.\n\n"
    "Eisbären leben auf dem Eis und im Meer rund um den Nordpol. (Arktis) "
    "Der Körper der Eisbären ist gut an das Leben in der Kälte und im Wasser "
    "angepasst. In der Arktis kann es bis zu minus 70 Grad kalt sein! Deshalb "
    "haben Eisbären ein sehr dickes Fell und eine zehn Zentimeter dicke "
    "Fettschicht, damit sie nicht erfrieren. Außerdem sind ihre einzelnen "
    "Haare hohl. Dadurch wird das Fell nicht so schwer, wenn der Bär im "
    "eisigen Wasser schwimmt. Auch die langen Haare zwischen den Fußballen "
    "wirken isolierend gegen die Kälte. Außerdem sind die Haare des Fells "
    "durchlässig für wärmende Sonnenstrahlen. Sie haben scharfe gebogene "
    "Krallen, mit denen sie Halt auf dem Eis finden und ihre Beute festhalten "
    "können. Das Fell der Eisbären ist weiß bis gelblich, damit sie beim "
    "Heranschleichen an die Beute nicht entdeckt werden.\n\n"
    "Der Eisbär ist tatsächlich eines der größten Landraubtiere, die es "
    "gibt: Er kann bis zu drei Meter lang werden, erreicht eine Schulterhöhe "
    "von einem Meter fünfzig und wiegt bis zu 850 Kilogramm. Die Weibchen "
    "sind meistens kleiner und leichter. Die Männchen sind außer während der "
    "Paarungszeit Einzelgänger, sind also lieber allein. In der Paarungszeit "
    "vom Mai bis Juni kämpfen sie heftig um die Weibchen.\n\n"
    "Eisbärweibchen bringen meist zwei Junge (Babys) zur Welt, um die sie "
    "sich zwei bis drei Jahre kümmern. Eisbärmütter haben eine enge Bindung "
    "zu ihren Jungen. Dies hängt mit der völligen Hilflosigkeit der "
    "Neugeborenen zusammen, deren Augen sich erst nach 40 Lebenstagen öffnen. "
    "Außerdem müssen die Jungen im Abstand von wenigen Stunden gesäugt "
    "werden, um zu überleben. Eisbären sind hervorragende Schwimmer. Die "
    "steifen Haare an den Vorderbeinen und die breiten Vorderfüße wirken beim "
    "Schwimmen wie Ruder. Mit ihrem stromlinienförmigen Körper können sie "
    "leicht durch das Wasser gleiten. Sie sind aber auch sehr gute und "
    "schnelle Läufer, weil sie einen großen Teil ihres Lebens an Land oder "
    "auf dem Eis verbringen. Bei der Jagd legen sie riesige Entfernungen "
    "zurück. Manchmal verfolgen sie ihre Beute über Hunderte von Kilometern. "
    "Beim Laufen erreichen sie Geschwindigkeiten von über 40 km/h. Außerdem "
    "können sie prima schwimmen und tauchen. Zur Erholung lassen sie sich "
    "aber auch mal auf einer Eisscholle treiben. Pro Jahr wandert ein Eisbär "
    "etwa 15 000 Kilometer.\n\n"
    "Eisbären sind gute Jäger und ernähren sich hauptsächlich von Robben. "
    "Sie jagen aber auch Fische und junge Walrosse. Wenn im Sommer das Eis "
    "schmilzt und sie auf das Festland ziehen, jagen sie dort kleine "
    "Säugetiere und Vögel oder fressen Gras, Moos und Beeren. Da die Tiere "
    "sehr neugierig sind, dringen sie auf der Suche nach Nahrung auch immer "
    "wieder in menschliche Siedlungen ein und suchen dort in Abfällen "
    "Nahrungsmittel. Bei solchen Gelegenheiten werden immer wieder Tiere "
    "erschossen, obwohl sie unter Naturschutz stehen. Eisbären stehen heute "
    "unter Naturschutz, weil sie in früheren Zeiten wegen ihres Fells von "
    "Pelzjägern gnadenlos gejagt und fast ausgerottet wurden."
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Packeis erklären",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Erkläre, was Packeis ist!"
        ),
        "answer": (
            "Packeis sind dicke Eisschichten, die zum Teil am Meeresboden oder an "
            "den Kontinenten festgefroren sind."
        ),
        "steps": ["Aus Absatz 1."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 2,
        "type": "Überlebensgrund Tiere",
        "text": "Die Tiere und Pflanzen in der Arktis können nur aus einem ganz bestimmten Grund überleben. Welcher?",
        "answer": "Sie überleben, weil das Eis im Sommer an den Küsten für wenige Monate ganz verschwindet.",
        "steps": ["Aus Absatz 1."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 3,
        "type": "Wo leben Eisbären",
        "text": "Wo leben Eisbären? Antworte genau in ganzen Sätzen!",
        "answer": "Eisbären leben auf dem Eis und im Meer rund um den Nordpol (Arktis).",
        "steps": ["Aus Absatz 2."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 4,
        "type": "Fettschicht",
        "text": "Wie dick ist die Fettschicht der Eisbären? (mit Zeile)",
        "answer": "10 cm — Zeile 17.",
        "steps": ["Im Text suchen."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 5,
        "type": "Fellfarbe",
        "text": "Welche Farbe hat das Fell der Eisbären und warum ist das so? Antworte in vollständigen Sätzen!",
        "answer": (
            "Eisbären haben ein weiß bis gelbliches Fell, damit sie beim "
            "Heranschleichen an die Beute nicht entdeckt werden."
        ),
        "steps": ["Aus Absatz 2."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 6,
        "type": "Drei Anpassungen",
        "text": "Wie ist der Eisbär an das Leben in der Kälte und im Wasser angepasst? Nenne drei Merkmale!",
        "answer": (
            "1. Dickes Fell + 10 cm Fettschicht + lange Haare zwischen den Fußballen ; "
            "2. Scharfe gebogene Krallen für Halt und Beutefang ; "
            "3. Hohle Haare, damit das Fell beim Schwimmen nicht zu schwer wird."
        ),
        "steps": ["Aus Absatz 2."],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 7,
        "type": "Lückentext Eisbär",
        "text": (
            "Fülle die Lücken!\n"
            "Eisbärmännchen können eine Körperlänge von fast ___ erreichen und bis "
            "zu ___ schwer werden. Die Weibchen sind meistens ___ und ___."
        ),
        "answer": "drei Metern / 850 Kilogramm / kleiner / leichter.",
        "steps": ["Aus Absatz 3."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 8,
        "type": "Bindung Mutter-Junge",
        "text": "Warum haben Eisbärmütter eine enge Bindung zu ihren Jungen? Nenne 2 Gründe!",
        "answer": (
            "1. Die Neugeborenen sind anfangs hilflos, weil sich die Augen erst "
            "nach 40 Tagen öffnen. ; "
            "2. Die Jungen müssen im Abstand von wenigen Stunden gesäugt werden, "
            "um zu überleben."
        ),
        "steps": ["Aus Absatz 4."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 9,
        "type": "Schwimmer",
        "text": "Warum sind Eisbären hervorragende Schwimmer? (2 Merkmale)",
        "answer": (
            "Sie haben einen stromlinienförmigen Körper, und die Vorderbeine und "
            "die breiten Vorderfüße wirken beim Schwimmen wie Ruder."
        ),
        "steps": ["Aus Absatz 4."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 10,
        "type": "Nahrung Eisbären",
        "text": "Zähle auf, wovon sich Eisbären ernähren! Nenne alles aus dem Text!",
        "answer": (
            "Eisbären ernähren sich von Robben, Fischen, jungen Walrossen, "
            "kleinen Säugetieren und Vögeln, Gras, Moos und Beeren sowie Abfällen "
            "aus menschlichen Siedlungen."
        ),
        "steps": ["Aus dem letzten Absatz."],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 11,
        "type": "Erschießen erklären",
        "text": "Warum werden Eisbären heute manchmal erschossen, obwohl sie unter Naturschutz stehen?",
        "answer": "Weil sie öfters in menschliche Siedlungen eindringen und dort im Abfall nach Nahrung suchen.",
        "steps": ["Aus dem letzten Absatz."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 12,
        "type": "Naturschutz Begründung",
        "text": "Warum stehen Eisbären heute unter Naturschutz?",
        "answer": "Sie wurden früher wegen ihres Pelzes gejagt und fast ausgerottet.",
        "steps": ["Aus dem letzten Absatz."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 13,
        "type": "Richtige Sätze ankreuzen",
        "text": (
            "Kreuze richtige Sätze an!\n"
            "(a) Pro Jahr wandert ein Eisbär etwa 15 000 Kilometer.\n"
            "(b) Eisbären sind hervorragende Schwimmer aber schlechte Läufer.\n"
            "(c) Die Paarungszeit der Eisbären dauert von Juli bis Dezember.\n"
            "(d) In der Arktis kann es bis zu minus 90 Grad kalt sein."
        ),
        "answer": "Richtig: (a) Pro Jahr wandert ein Eisbär etwa 15 000 Kilometer.",
        "steps": ["Im Text prüfen."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 14,
        "type": "Eisbären im Zoo",
        "text": (
            "Was hältst du davon, dass es Eisbären in vielen deutschen Zoos gibt? "
            "Begründe deine Meinung!"
        ),
        "answer": (
            "Individuelle Lösungen. Z. B. Pro: man kann Eisbären aus der Nähe "
            "sehen, große Schwimmbecken, Nachwuchs ; Contra: wenig Platz, keine "
            "Jagdmöglichkeit, wenig Bewegung gegenüber freier Natur."
        ),
        "steps": ["Eigene Meinung mit Begründung."],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
]

NEW_KNOWLEDGE = []
