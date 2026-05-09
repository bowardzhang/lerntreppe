EXERCISE = {
    "id": "0816",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Leben am Nordpol – Die Inuit",
    "topic": "Leseverstehen, Sachtext, Inuit, Arktis, Iglu, Nordpol, Eskimo",
    "publisher": "CATLUX",
    "source_pdf": "0816.pdf",
    "answer_pdf": "0816 (1).pdf",
    "total_points": 20.0,
}

LESETEXT = (
    "Leben am Nordpol – Die Inuit\n\n"
    "Die Arktis ist der nördlichste Teil der Erde. In ihrer Mitte liegen das "
    "eisbedeckte Nordpolarmeer und der Nordpol. Schaut man sich die Arktis auf "
    "dem Globus an, kann man kaum glauben, dass dort, sozusagen am oberen Rand "
    "der Erde, Menschen leben. Im Winter ist es sehr kalt, die Temperaturen "
    "sinken bis auf -50 Grad Celsius. Im Sommer wird es selten wärmer als +10 "
    "Grad Celsius. Dazu fegt häufig ein schneidender Wind über die Eisfläche. "
    "Außerdem breitet heftiges Schneegestöber ein weißes Tuch über die "
    "winterliche Landschaft.\n\n"
    "Seit etwa 5000 Jahren besiedeln Menschen die Arktis. Früher wurden die "
    "Ureinwohner der arktischen Gebiete Eskimos genannt. Wörtlich übersetzt "
    "bedeutet Eskimo 'Rohfleischesser' – aber weil das für die Inuit ein "
    "Schimpfwort ist, nennt man sie heute Inuit. Inuit bedeutet 'Mensch'. Um "
    "dort in Eis und Schnee überleben zu können, haben sie sich den "
    "schwierigen Bedingungen angepasst.\n\n"
    "Die Inuit entwickelten ganz besondere Häuser aus Eis: die Iglus. In diesen "
    "'Eishäusern' wohnten sie vor allem, wenn sie monatelang auf der Robbenjagd "
    "unterwegs waren. Um ein Iglu zu bauen, werden Eisblöcke wie Bauklötze "
    "übereinander geschichtet. Die Ritzen werden anschließend mit Schnee "
    "abgedichtet. Anstelle einer Tür wird ein kleiner Eistunnel gebaut, der "
    "mit einem Eisblock verschlossen werden kann. In so einem Iglu lässt es "
    "sich auch bei der größten Kälte gut aushalten. Dort wird es immerhin +5 "
    "Grad Celsius warm, während es draußen das Thermometer schon mal unter "
    "-40 Grad Celsius sinkt.\n\n"
    "Um auf die Jagd zu gehen und sich dabei auf dem Eis gut fortbewegen zu "
    "können, haben die Inuit niedrige, lange Schlitten erfunden, die von "
    "Huskys gezogen werden. Huskys sind Hunde, die von den Polarwölfen "
    "abstammen. Sie lieben den Schnee und vertragen die eisige Kälte gut. "
    "Jahrtausendelang waren die Hundeschlitten das einzige Fortbewegungsmittel "
    "der Inuit. Doch inzwischen sind die Hundeschlitten zum größten Teil durch "
    "Motorboote und Motorschlitten ersetzt. Auch die traditionellen Iglus "
    "werden heute nur noch selten gebaut. Immer weniger der rund 22000 Inuit "
    "in der Arktis leben nach den alten Traditionen ihrer Vorfahren.\n\n"
    "Der Lebensraum der Inuit hat sich durch die Umweltbedingungen sehr "
    "verändert. Wegen des wärmeren Klimas schmilzt das Eis und der "
    "Wasserspiegel steigt. Viele der Holzhäuser, in denen die Inuit die meiste "
    "Zeit leben, drohen umzukippen, weil der Boden unter ihnen wegtaut. "
    "Außerdem fischen große Fangflotten die Meere leer. Deshalb gehen die "
    "Inuit immer seltener auf die Jagd. Doch dadurch haben sie weniger zu "
    "essen und weniger Geld, weil sie nichts zum Verkaufen oder Tauschen haben.\n\n"
    "Viele Inuit sind daher heute arbeitslos und deswegen auf finanzielle "
    "Unterstützung vom Staat, beispielsweise von Kanada, angewiesen. Dauerhafte "
    "Arbeitsplätze bieten nur einige Fischfabriken an der Küste. In den "
    "Sommermonaten gibt es die Möglichkeit, auf Fischkuttern Arbeit zu finden. "
    "Andere Inuit verdienen sich einige Dollars als Jagdführer von Touristen "
    "oder als Begleiter von Reisegruppen, die Eisbären und andere Tiere im "
    "arktischen Eis fotografieren wollen."
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Wortbedeutung 'traditionellen'",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Welches Wort passt? 'traditionellen'\n"
            "(a) eisigen (b) herkömmlichen (c) warmen"
        ),
        "answer": "Richtig: (b) herkömmlichen.",
        "steps": ["traditionell = herkömmlich, alt überliefert."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 2,
        "type": "Wortbedeutung 'entwickelten'",
        "text": (
            "Welches Wort passt? 'entwickelten'\n"
            "(a) bewohnten (b) besaßen (c) erfanden"
        ),
        "answer": "Richtig: (c) erfanden.",
        "steps": ["entwickeln = erfinden."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 3,
        "type": "Metaphern erklären",
        "text": (
            "Kreuze an, was diese Aussagen bedeuten:\n"
            "(I) 'Dazu fegt häufig ein schneidender Wind über die Eisfläche.'\n"
            "  (a) Der Wind bläst kalt und eisig.\n"
            "  (b) Der Wind zerschneidet die Kleidung.\n"
            "  (c) Das Eis wird vom Wind weggeblasen.\n"
            "(II) 'Außerdem breitet Schneegestöber ein weißes Tuch über die winterliche Landschaft.'\n"
            "  (a) Inuit trocknen Wäsche im Freien.\n"
            "  (b) Hundeschlitten wirbeln Schnee auf.\n"
            "  (c) Eine dicke Schneedecke legt sich über das Land."
        ),
        "answer": "(I) (a) Der Wind bläst kalt und eisig. ; (II) (c) Eine dicke Schneedecke legt sich über das Land.",
        "steps": ["Bildhafte Sprache deuten."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 4,
        "type": "Eskimo - Schimpfwort",
        "text": "Erkläre genau, warum die Inuit nicht 'Eskimos' heißen wollen.",
        "answer": (
            "Für diese Menschen bedeutet das Wort 'Eskimo' ein Schimpfwort "
            "('Rohfleischesser'). Deshalb nennt man sie heute 'Inuit', was so "
            "viel wie 'Mensch' heißt."
        ),
        "steps": ["Aus dem 2. Absatz."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 5,
        "type": "Iglu-Bau ordnen",
        "text": (
            "Nummeriere in der richtigen Reihenfolge!\n"
            "(a) Bau eines kleinen Eistunnels\n"
            "(b) Abdichten der Ritzen mit Schnee\n"
            "(c) Eisblöcke übereinander schichten\n"
            "(d) Eisblock zum Verschließen"
        ),
        "answer": "(c) 1. ; (b) 2. ; (a) 3. ; (d) 4.",
        "steps": ["Reihenfolge laut Text."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 6,
        "type": "Beantwortbare Fragen",
        "text": (
            "Welche Fragen kannst du jeweils mit Hilfe des Textes beantworten? "
            "Setze pro Kasten zwei Kreuze.\n"
            "(1) Wie hoch ist die Anzahl der arbeitslosen Inuit heute?\n"
            "(2) Wie dick ist das Eis in der Arktis?\n"
            "(3) Welche Temperatur herrscht in einem Iglu?\n"
            "(4) Wann arbeiten die Inuit auf Fischkuttern?\n"
            "(5) Welche Teile verzehrten die Inuit von einem erlegten Wal?\n"
            "(6) Wie begrüßen sich die Inuit?\n"
            "(7) Seit wann leben Menschen in der Arktis?\n"
            "(8) Wie hoch sind die Niederschläge am Nordpol?\n"
            "(9) Warum steigt der Wasserspiegel?\n"
            "(10) Mit welchen Waffen gehen die Inuit auf Jagd?"
        ),
        "answer": "Beantwortbar: (3), (4), (7), (9).",
        "steps": ["Fragen mit dem Text abgleichen."],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 7,
        "type": "Huskys",
        "text": "Was erfährst du im Text über die Abstammung, die Vorlieben und die Aufgabe der Huskys?",
        "answer": (
            "Abstammung: Sie stammen von den Polarwölfen ab. ; "
            "Vorlieben: Sie lieben den Schnee und vertragen die eisige Kälte. ; "
            "Aufgabe: Sie ziehen die Schlitten der Inuit."
        ),
        "steps": ["Aus dem 4. Absatz."],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 8,
        "type": "Richtig/Falsch/Nicht enthalten",
        "text": (
            "Kreuze an, ob die Aussage richtig, falsch oder nicht enthalten ist!\n"
            "(1) Die Inuit lebten in Iglus, wenn sie auf Robbenjagd waren.\n"
            "(2) Wegen des wärmeren Klimas drohen Holzhäuser umzukippen.\n"
            "(3) Heute arbeiten fast alle Inuit für Touristen.\n"
            "(4) Schuld an der Erwärmung der Erde sind die Treibhausgase.\n"
            "(5) Robbenjäger müssen oft mit Motorbooten gerettet werden."
        ),
        "answer": "(1) richtig ; (2) richtig ; (3) falsch ; (4) nicht enthalten ; (5) nicht enthalten.",
        "steps": ["Im Text nachprüfen."],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 9,
        "type": "Fernsehsendung empfehlen",
        "text": (
            "Welche Fernsehsendung würdest du deinem Freund empfehlen, der sich "
            "für die Arktis interessiert?\n"
            "(a) Fischfang im Mittelmeer\n"
            "(b) Abenteuer am Polarmeer\n"
            "(c) Geheimnisvolle Eiskeller\n"
            "(d) Schlittenbau im Fichtelgebirge"
        ),
        "answer": "Richtig: (b) Abenteuer am Polarmeer.",
        "steps": ["Polarmeer = Arktis."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
]

NEW_KNOWLEDGE = []
