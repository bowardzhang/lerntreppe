EXERCISE = {
    "id": "2127",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Emil sucht Freunde (Marienkäfer)",
    "topic": "Leseverstehen, Erzählung, Marienkäfer, Freundschaft, Akzeptanz",
    "publisher": "CATLUX",
    "source_pdf": "2127.pdf",
    "answer_pdf": "2127 (1).pdf",
    "total_points": 30.0,
}

LESETEXT = (
    "Emil sucht Freunde\n\n"
    "In einem kleinen Wald, nahe einer großen Wiese, lebte eine "
    "Marienkäferfamilie. Sie waren alle sehr glücklich, bis auf den Jüngsten – "
    "Emil – der hatte nämlich kein einziges Pünktchen auf seinem Rücken und "
    "darum wollte auch keiner mit ihm spielen.\n\n"
    "So flog er oft alleine über die große Wiese und beobachtete die Anderen "
    "dabei, wenn sie ihren Spaß hatten. Gerne wollte er dazugehören, doch nach "
    "einer Weile wurde ihm das alles gleichgültig. Der kleine Marienkäfer "
    "entdeckte nämlich ein Haus in der Nähe der Wiese wo es viel lustiger war "
    "als bei seinen Artgenossen.\n\n"
    "Ein alter Mann lebte in dem Häuschen, zusammen mit seiner Enkelin Klara, "
    "die gerne malte. Dabei sah ihr der Kleine dann oft zu. Es war aufregend, "
    "wenn sie ganze Landschaften auf ein Stück Leinwand zauberte, oder eben "
    "nur eine Sonnenblume malte. Er konnte stundenlang beobachten, wenn sie "
    "die Farben miteinander mischte und den Pinsel über das Papier tanzen "
    "ließ.\n\n"
    "Einmal setzte sich Emil der Marienkäfer auf den rechten, oberen Rand des "
    "Bildes. Von dort aus konnte er alles wunderbar überblicken. Nach einer "
    "Weile entdeckte ihn das Mädchen und fragte: 'Ja, was machst denn Du hier? "
    "Siehst Du mir zu?\". Emil nickte mit seinem kleinen Köpfchen. Weiter "
    "bemerkte sie: 'Ooooh, Du hast ja gar keine Pünktchen, soll ich Dir welche "
    "aufmalen?\" Der Marienkäfer flog auf ihre linke Hand und schlug aufgeregt "
    "mit seinen Flügeln auf und ab. Daraufhin holte das Mädchen ihren "
    "kleinsten Pinsel aus der Tasche, tunkte ihn vorsichtig in schwarze Farbe "
    "und tupfte ihm 8 Punkte auf seinen Rücken. Emil war überglücklich und "
    "flog wieder nach Hause zurück.\n\n"
    "Als er bei seiner Familie angekommen war, da staunten sie über das "
    "kleine Wunder. Danach flog Emil munter auf die Wiese zu. Dort wurde er "
    "auch zum ersten Male von den anderen Marienkäfern zum Mitspielen "
    "eingeladen. Plötzlich hatte der Kleine viele Freunde, bis eines Tages "
    "ein Gewitter aufzog und es zu regnen begann. Emil spielte gerade mit "
    "den Anderen auf der Wiese, als die ersten Regentropfen vom Himmel fielen. "
    "Schnell flogen alle heim, doch als Emil zu Hause ankam, da war er bereits "
    "so nass, dass alle seine Pünktchen vom Regen weggewaschen waren. Am "
    "nächsten Tag, als die Sonne wieder zum Vorschein kam, trafen sich die "
    "kleinen Käfer auf der großen Wiese. Emil jedoch blieb zu Hause, denn er "
    "hatte Angst zu den anderen zu fliegen.\n\n"
    "Seine Mutter sah ihn an und sprach: 'Weißt Du, wenn die Anderen Dich "
    "nicht so mögen wie Du bist, dann sind das keine Freunde\".\n\n"
    "Also flog er wieder los und seine schlimmsten Befürchtungen wurden wahr. "
    "Niemand wollte ihn dabei haben. Alle ignorierten ihn. Er grübelte "
    "darüber nach wieder zu dem Mädchen zu fliegen, aber er dachte auch an "
    "die Worte seiner Mutter. Nach langem hin- und her flog er jedoch zu dem "
    "kleinen Häuschen in dem der Großvater mit seiner Enkelin wohnte. Das "
    "Mädchen saß auch wieder an ihrem Platz und malte. Emil war neugierig und "
    "wollte sehen was sie diesmal auf die Leinwand zauberte und war ganz "
    "erstaunt. Sie hatte ein Bild von ihm gemalt – ohne Pünktchen, einfach so "
    "wie er war.\n\n"
    "Emil setzte sich an den Bildrand. 'Ach da bist Du ja wieder kleiner "
    "Käfer. Na, Deine Punkte hat wohl der Regen weggespült.\" Emil nickte mit "
    "seinem Köpfchen. 'Ach sei nicht traurig, Du bist viel hübscher so' Der "
    "Käfer war verlegen, freute sich jedoch über diese Worte und noch viel "
    "mehr über das Bild. Endlich wurde ihm bewusst, dass er keinen Grund "
    "hatte unglücklich zu sein."
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Überschrift finden",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Finde eine passende Überschrift für diese Geschichte!"
        ),
        "answer": "Emil sucht Freunde.",
        "steps": ["Hauptthema der Geschichte."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 2,
        "type": "Aussagen ankreuzen",
        "text": (
            "Was erfährst du über Emil? Kreuze an!\n"
            "(a) Emil ist ein Maikäfer.\n"
            "(b) Emil ist ein Kartoffelkäfer.\n"
            "(c) Emil ist ein Marienkäfer.\n"
            "(d) Emil ist das älteste Kind in der Käferfamilie.\n"
            "(e) Emil ist das jüngste Kind in der Käferfamilie.\n"
            "(f) Emil ist das dickste Kind in der Käferfamilie.\n"
            "(g) Emil entdeckt eine schöne Blume auf der Wiese.\n"
            "(h) Emil entdeckt ein Haus in der Nähe des Waldes.\n"
            "(i) Emil entdeckt ein Haus in der Nähe der Wiese."
        ),
        "answer": "Richtig: (c), (e), (i).",
        "steps": ["Im Text nachprüfen."],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 3,
        "type": "Grund Ablehnung",
        "text": "Warum wollten die anderen Kinder nicht mit Emil spielen?",
        "answer": "Emil hatte keine Punkte auf dem Rücken.",
        "steps": ["Aus dem 1. Absatz."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 4,
        "type": "Tätigkeit Emil",
        "text": "Was machte Emil oft, wenn er alleine war? (mit Zeilenangabe)",
        "answer": (
            "Er flog über die große Wiese und beobachtete die anderen beim Spielen. "
            "Zeile: 4."
        ),
        "steps": ["Aus dem 2. Absatz."],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 5,
        "type": "Adjektive Synonyme",
        "text": (
            "Finde andere passende Wörter:\n"
            "(a) gleichgültig\n"
            "(b) munter\n"
            "(c) verlegen"
        ),
        "answer": (
            "(a) gleichgültig → egal, einerlei ; "
            "(b) munter → heiter, fröhlich ; "
            "(c) verlegen → verschämt, beschämt, schüchtern."
        ),
        "steps": ["Synonyme finden."],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 6,
        "type": "Gegenteile",
        "text": (
            "Nenne das Gegenteil zu den unterstrichenen Wörtern!\n"
            "(a) Es war aufregend, wenn sie ganze Landschaften zauberte ...\n"
            "(b) Von dort aus konnte er alles wunderbar überblicken."
        ),
        "answer": "(a) aufregend → langweilig ; (b) wunderbar → schlecht.",
        "steps": ["Gegenteile finden."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 7,
        "type": "Klara Mitbewohner",
        "text": "Mit wem lebt Klara zusammen?",
        "answer": "Klara lebte mit einem alten Mann zusammen. Er war ihr Opa.",
        "steps": ["Aus dem 3. Absatz."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 8,
        "type": "Beobachtung",
        "text": "Emil beobachtete Klara. Wobei sah er ihr zu?",
        "answer": "Er sah zu, wie Klara ein Bild malte.",
        "steps": ["Aus dem 3. Absatz."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 9,
        "type": "Fehler korrigieren",
        "text": (
            "Wie steht der Satz im Text? Streiche Falsches durch und verbessere!\n"
            "'Nach einer Weile sah ihn das Mädchen und fragte: Ja, was machst du "
            "denn hier? Schaust du mir zu?\""
        ),
        "answer": (
            "sah → entdeckte ; du denn → denn Du ; Schaust → Siehst."
        ),
        "steps": ["Wortlaut prüfen."],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 10,
        "type": "Begründung Mitspielen",
        "text": "Eines Tages durfte Emil mit den anderen spielen. Begründe warum!",
        "answer": "Er hatte jetzt schwarze Punkte und sah aus wie alle anderen.",
        "steps": ["Klara hatte ihm Punkte aufgemalt."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 11,
        "type": "Gewitter",
        "text": "Was passierte mit Emil, als ein Gewitter aufzog und Regentropfen fielen?",
        "answer": "Emil wurde nass und seine Punkte wurden weggewaschen.",
        "steps": ["Aus dem 5. Absatz."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 12,
        "type": "Angst nach Gewitter",
        "text": "Emil hatte nach dem Gewitter Angst, zu den anderen zu fliegen. Begründe!",
        "answer": "Seine Punkte waren weg und er hatte Angst, dass ihn dann alle ausschließen würden.",
        "steps": ["Schluss aus der Geschichte."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 13,
        "type": "Spruch der Mutter",
        "text": (
            "Erkläre, was die Mutter mit folgendem Satz meinte: 'Wenn die anderen "
            "dich nicht so mögen wie du bist, dann sind das keine Freunde.\""
        ),
        "answer": (
            "Wahre Freunde mögen einen so wie man ist, egal wie man aussieht. "
            "Man muss sich nicht verstellen, um anderen zu gefallen."
        ),
        "steps": ["Bedeutung erklären."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 14,
        "type": "Zeile Abweisung",
        "text": "Nenne die Zeilennummer, in der Emil erneut von den anderen Marienkäfern abgewiesen wird!",
        "answer": "Zeile 34.",
        "steps": ["'Niemand wollte ihn dabei haben'."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 15,
        "type": "Karlas Bild",
        "text": "Was malte Klara, als Emil sie erneut besuchte?",
        "answer": "Sie malte ein Bild von Emil ohne Punkte.",
        "steps": ["Aus dem vorletzten Absatz."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 16,
        "type": "Bewusstwerden",
        "text": "Wann wurde Emil bewusst, dass er nicht traurig sein muss?",
        "answer": "Als Klara ihm sagte, er sei viel hübscher ohne Punkte.",
        "steps": ["Aus dem letzten Absatz."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
]

NEW_KNOWLEDGE = []
