EXERCISE = {
    "id": "0711",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Durchs wilde Afrika (Alfred Brehm)",
    "topic": "Leseverstehen, Sachtext, Afrika, Steppe, Fata Morgana, Karawane, Brand",
    "publisher": "CATLUX",
    "source_pdf": "0711.pdf",
    "answer_pdf": "0711 (1).pdf",
    "total_points": 21.0,
}

LESETEXT = (
    "Durchs wilde Afrika\n\n"
    "Im Jahre 1847, als weite Teile Afrikas bei uns noch unbekannt waren, "
    "begaben sich Alfred Brehm und Baron Johann Wilhelm von Müller auf eine "
    "Forschungsreise. Sie zogen durch die Grasländer – auch Steppen genannt – "
    "und Wüsten des nördlichen Afrika, sie erlebten Fata Morganas – "
    "Luftspiegelungen, die sich durch die Hitze hervorgerufen wurden – und "
    "sahen zahlreiche wilde Tiere. Die Erfahrungen des damals 18-jährigen "
    "Alfred Brehm hatten zur Folge, dass aus dem jungen Mann ein sehr bekannter "
    "Tierforscher wurde.\n\n"
    "Am frühen Morgen, als die Karawane aufbrach, hatte man den großartigen "
    "Anblick einer Fata Morgana. Die Sonne schien schon recht warm und eine "
    "Fata Morgana war ein Zeichen, dass im Laufe des Tages noch mit großer "
    "Hitze zu rechnen war. Schon mehrmals hatte Alfred auf seinen Fahrten durch "
    "die Wüsten und Steppen Afrikas solche Luftspiegelungen gesehen, aber noch "
    "niemals von gleicher Pracht wie an diesem Morgen. Über der flimmernden "
    "Steppe stand am Himmel das Bild weiter, sattgrüner Wälder, hinter denen "
    "sich die blauen, fast violett erscheinenden Umrisse von Gebirgen "
    "abzeichneten. Ein Bild von eigenartiger, zauberhafter Schönheit, wie von "
    "der Hand eines großen Malers entworfen.\n\n"
    "Die Reittiere wurden gesattelt, die Lasten auf die Kamele verladen. "
    "Alfred und der Baron bestiegen ihre Hedjihns und ritten ihrem Tagesziel "
    "zu. Vor ihren Augen hatten sie den Anblick der prachtvollen Fata Morgana, "
    "die mehr und mehr mit der strahlenden Sonne verblasste. Obwohl die "
    "Regenzeit vor der Tür stand und in den Tagen vorher auch schon leichtere "
    "Regenfälle niedergegangen waren, hatte die Sonne den Boden der Steppe in "
    "kurzer Zeit wieder ausgetrocknet. Gegen Mittag erhob sich ein leichter "
    "Wind, der vom Süden kam und mit heißem Hauch über das Land strich.\n\n"
    "Wie üblich, rastete man, weil die Hitze des Tages ihren Höhepunkt erreicht "
    "hatte, und wartete auf die nachfolgenden Lasttiere. Während die "
    "eingeborenen Diener am Feuer die Keule einer am Tage zuvor erlegten "
    "Antilope als Mittagsmahl für Alfred und den Baron brieten, ruhten die "
    "beiden Forscher im Schatten eines schnell aufgeschlagenen Sonnensegels. "
    "Alfred sah, wie einer der Eingeborenen sich vom Feuer erhob, einige "
    "Schritte machte, stehen blieb und seine Nase witternd in die Luft hob. "
    "Da erscholl auch schon sein Ruf: 'Feuer!' Die Steppe brannte.\n\n"
    "Die Forscher sprangen auf und blickten in die Richtung, in welche die "
    "Eingeborenen wiesen. Alfred Brehm nahm sein Fernrohr ans Auge und sah, "
    "dass ein breiter Streifen gierig leckender Flammen am Horizont auftauchte "
    "und sich rasch über die Steppe bewegte. Das ausgedörrte Gras und das "
    "Reisig brannten lichterloh. Das Feuer konnte durch Blitzschlag oder "
    "Unachtsamkeit entstanden sein, aber oftmals pflegten auch die "
    "Eingeborenen selbst, in den heißen Tagen vor der Regenzeit, die Steppe "
    "anzuzünden, damit der folgende Regen die Asche in den Boden trieb und "
    "diesen für neuen Graswuchs fruchtbar machen sollte. Das Feuer wanderte "
    "stetig auf die Forscher und ihre Begleiter zu, dichte Rauchschwaden "
    "trieben über dem Land dahin, und schon kamen die ersten, schreckerfüllten "
    "Tiere der Steppe, die ihr bedrohtes Leben zu retten suchten."
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Landschaft erkennen",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Von welcher Landschaft handelt der Text? Kreuze an!\n"
            "(a) Der Text handelt von einer Steppe.\n"
            "(b) Der Text handelt vom afrikanischen Urwald.\n"
            "(c) Das steht nicht im Text."
        ),
        "answer": "Richtig: (a) Der Text handelt von einer Steppe.",
        "steps": ["Im Text mehrfach von 'Steppe' die Rede."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 2,
        "type": "Bedeutung Fata Morgana",
        "text": (
            "Worauf deutet die Fata Morgana im Text hin?\n"
            "(a) Sie zeigt an, dass eine Oase in der Nähe ist.\n"
            "(b) Sie zeigt an, dass ein Feuer ausbrechen wird.\n"
            "(c) Sie zeigt an, dass es heiß werden wird.\n"
            "(d) Sie deutet darauf hin, dass es bald regnen wird."
        ),
        "answer": "Richtig: (c) Sie zeigt an, dass es heiß werden wird.",
        "steps": ["'mit großer Hitze zu rechnen war'."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 3,
        "type": "Jahreszeit + Zeile",
        "text": (
            "Welche Jahreszeit 'steht vor der Tür'? Kreuze an und gib die Zeile an!\n"
            "(a) Das steht nicht im Text.\n"
            "(b) Sommer\n"
            "(c) Ende der Trockenzeit\n"
            "(d) Regenzeit"
        ),
        "answer": "Richtig: (d) Regenzeit. Zeile: 13.",
        "steps": ["'Obwohl die Regenzeit vor der Tür stand'."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 4,
        "type": "Richtig/Falsch/Nicht zu beantworten",
        "text": (
            "Entscheide bei jedem Satz, ob seine Aussage richtig, falsch oder aus "
            "dem Text nicht zu beantworten ist.\n"
            "(1) Am Morgen zieht die Karawane durch weite, sattgrüne Wälder.\n"
            "(2) Alfred und der Baron lassen sich von den Eingeborenen Essen zubereiten.\n"
            "(3) Eingeborene haben das Gras angezündet.\n"
            "(4) Das Feuer kommt auf die Karawane zu."
        ),
        "answer": (
            "(1) falsch ; "
            "(2) richtig ; "
            "(3) aus dem Text nicht zu beantworten ; "
            "(4) richtig."
        ),
        "steps": ["Genau im Text nachlesen."],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 5,
        "type": "Satzergänzung",
        "text": (
            "Kreuze die richtige Fortsetzung an!\n"
            "(I) Die Karawane brach auf,\n"
            "  (a) damit man rechtzeitig am Tagesziel ankam.\n"
            "  (b) obwohl es schon sehr heiß war.\n"
            "  (c) weil ein Feuer drohte.\n"
            "  (d) als es noch früh am Morgen war.\n"
            "(II) Es hatte leichte Regenfälle gegeben,\n"
            "  (a) sodass das Gras wieder wuchs.\n"
            "  (b) und deshalb war es heiß.\n"
            "  (c) aber der Boden war bald wieder ausgetrocknet.\n"
            "  (d) und die Eingeborenen hatten wieder Wasser."
        ),
        "answer": "(I) (d) als es noch früh am Morgen war. ; (II) (c) aber der Boden war bald wieder ausgetrocknet.",
        "steps": ["Genau im Text nachlesen."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 6,
        "type": "Grund mittägliche Rast",
        "text": (
            "Nenne den Grund für die mittägliche Rast der Karawane!\n"
            "(a) Sie rastet mittags, weil die Reittiere Futter brauchen.\n"
            "(b) Sie rastet mittags, um auf die nachfolgenden Lasttiere zu warten.\n"
            "(c) Sie rastet mittags, weil die Menschen hungrig sind.\n"
            "(d) Sie rastet mittags, weil es zu heiß zum Weiterreiten ist."
        ),
        "answer": "Richtig: (d) Sie rastet mittags, weil es zu heiß zum Weiterreiten ist.",
        "steps": ["'die Hitze des Tages ihren Höhepunkt erreicht hatte'."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 7,
        "type": "Feuer bemerken",
        "text": (
            "Woran merkt einer der Eingeborenen, dass sich ein Feuer entzündet hat?\n"
            "(a) Er hört es. (b) Er riecht es. (c) Er schmeckt es. (d) Er fühlt es."
        ),
        "answer": "Richtig: (b) Er riecht es.",
        "steps": ["'seine Nase witternd in die Luft hob'."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 8,
        "type": "Wortbedeutung 'lichterloh'",
        "text": (
            "Was ist mit 'Das ausgedörrte Gras und das Reisig brannten lichterloh.' "
            "(Z. 27) am ehesten gemeint?\n"
            "(a) Das Feuer bewegte sich sehr schnell.\n"
            "(b) Gras und Reisig brannten langsam vor sich hin.\n"
            "(c) Durch den Brand entstand eine dichte, schwarze Rauchwolke.\n"
            "(d) Gras und Reisig brannten hell und heftig."
        ),
        "answer": "Richtig: (d) Gras und Reisig brannten hell und heftig.",
        "steps": ["lichterloh = hell und heftig brennend."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 9,
        "type": "Grund für Feuerlegen",
        "text": (
            "Wie wird im Text begründet, warum die Eingeborenen oft absichtlich Feuer legen?\n"
            "(a) Das Feuer erleichtert die Jagd auf flüchtende Tiere.\n"
            "(b) Auf diese Weise wird der Boden gedüngt.\n"
            "(c) Das Feuer zieht den Regen an."
        ),
        "answer": "Richtig: (b) Auf diese Weise wird der Boden gedüngt.",
        "steps": ["'damit der folgende Regen die Asche in den Boden trieb und diesen für neuen Graswuchs fruchtbar machen sollte'."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 10,
        "type": "Was sah Brehm",
        "text": (
            "Was sah Alfred Brehm durch sein Fernrohr?\n"
            "(a) Tiere, die auf der Flucht waren.\n"
            "(b) Ein Feuer, das sich schnell ausbreitete.\n"
            "(c) Eingeborene, die das Gras anzündeten.\n"
            "(d) Ein Gewitter, das am Horizont aufzog."
        ),
        "answer": "Richtig: (b) Ein Feuer, das sich schnell ausbreitete.",
        "steps": ["'ein breiter Streifen gierig leckender Flammen ... sich rasch über die Steppe bewegte'."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 11,
        "type": "Eigene Meinung",
        "text": "Warum lohnt es sich, fremde Länder zu bereisen und zu erforschen? Nenne einen Grund!",
        "answer": "Man kann Neues erfahren, lernen, fremde Kulturen kennenlernen.",
        "steps": ["Eigene Begründung."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 12,
        "type": "Wörter im Text finden",
        "text": (
            "Gib die Zeile/n an, in der die folgenden Wörter im Text zu finden sind:\n"
            "Hedjihns: ___\n"
            "Eingeborenen: ___\n"
            "Sonnensegels: ___\n"
            "Graswuchs: ___"
        ),
        "answer": (
            "Hedjihns → Z. 11 ; "
            "Eingeborenen → Z. 21, 24, 29 ; "
            "Sonnensegels → Z. 21 ; "
            "Graswuchs → Z. 31."
        ),
        "steps": ["Wörter im Text suchen."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 13,
        "type": "Synonyme finden",
        "text": (
            "Finde ein anderes Wort mit gleicher Bedeutung:\n"
            "zahlreich – ___\n"
            "großartig – ___\n"
            "erscholl – ___"
        ),
        "answer": (
            "zahlreich → viele ; "
            "großartig → toll / herrlich ; "
            "erscholl → erklang / ertönte."
        ),
        "steps": ["Synonyme finden."],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
]

NEW_KNOWLEDGE = []
