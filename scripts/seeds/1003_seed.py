EXERCISE = {
    "id": "1003",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Bitterbitterkalt – Schule und Thermometer",
    "topic": "Leseverstehen, Ich-Erzählung, Winter, Thermometer, Schule, Prüfungsangst",
    "publisher": "CATLUX",
    "source_pdf": "1003.pdf",
    "answer_pdf": "1003 (1).pdf",
    "total_points": 28.0,
}

LESETEXT = (
    "Als ich ein kleiner Junge war, gab es in jedem Winter viele Wochen lang Eis "
    "und Schnee. Oft war es bitterkalt, und ein böser Wind pfiff durch die Stadt. "
    "Wenn es bitterbitterkalt war, brauchte ich nicht zur Schule. Mein Vater hatte "
    "gesagt: 'Wenn es bitterbitterkalt ist, ist es draußen zu gefährlich. Da können "
    "Finger und Zehen und Nasen tot frieren.\"\n\n"
    "Einmal sagte ich morgens früh: 'Papa, draußen ist es bitterbitterkalt. Ich "
    "gehe wieder ins Bett.\" Mein Vater antwortete: 'Augenblick mal.' Er ging ans "
    "Fenster, um auf das Thermometer zu sehen. Wir hatten zwei Fenster "
    "hintereinander, weil es im Winter so kalt war. Die hießen Doppelfenster. "
    "(Als ich ein kleiner Junge war, gab es noch keine Fenster mit doppeltem Glas.) "
    "Mein Vater machte das erste Fenster auf. Das zweite war vereist. Er kratzte "
    "daran, um auf das Thermometer draußen vor dem Fenster sehen zu können. Dann "
    "machte er das Fenster wieder zu. Er sagte: 'Es sind nur zehn Grad unter Null. "
    "Das ist nur bitterkalt. Deshalb musst du zur Schule.\" 'Und wann ist es "
    "bitterbitterkalt?\", fragte ich. Er sagte: 'Wenn es mindestens zwanzig Grad "
    "unter Null sind.\"\n\n"
    "Ich wartete viele Wochen. Aber es war nie bitterbitterkalt. Eines Tages sagte "
    "unser Lehrer: 'Morgen früh prüfe ich euch im Kopfrechnen.' Ich konnte nicht "
    "gut Kopfrechnen. Darum hatte ich Angst vor der Prüfung.\n\n"
    "Am Nachmittag hatte ich Bauchschmerzen. Als ich am Abend ins Bett ging, hatte "
    "ich immer noch Bauchschmerzen. Ich konnte nicht einschlafen. Ich musste immer "
    "wieder an die Prüfung im Kopfrechnen denken. Ich dachte: Ich möchte krank "
    "werden, damit ich nicht in die Schule muss. Aber so schnell wird kein Kind "
    "krank. Dann dachte ich: Ich möchte, dass der Lehrer krank wird. Aber der war "
    "immer schrecklich gesund. Dann fiel mir etwas ein: Ich dachte: Ich möchte, "
    "dass es morgen bitterbitterkalt ist. In diesem Winter war es noch nie "
    "bitterbitterkalt gewesen. Plötzlich dachte ich: Morgen wird es bestimmt "
    "bitterbitterkalt. Dabei konnte ich das gar nicht wissen. Als ich ein kleiner "
    "Junge war, gab es nämlich noch kein Fernsehen und Wetterberichte im Radio "
    "auch nicht. Aber ich war ganz sicher, dass es bitterbitterkalt werden würde. "
    "Da hörten meine Bauchschmerzen auf. Ich merkte gar nicht, dass ich einschlief.\n\n"
    "Am Morgen war ich als erster in unserer Familie wach. Ich dachte sofort an "
    "die Kopfrechen-Prüfung, krabbelte aus meinem Bett und lief mit nackten Füßen "
    "ins Wohnzimmer. Es war noch dunkel. Ich machte das Licht an. Ich lief zum "
    "Doppelfenster. Ich stieg auf einen Stuhl und öffnete das erste Fenster. Dann "
    "kratzte ich das Eis vom zweiten und hauchte auf die Scheibe. Es waren 19 "
    "Grad unter Null. Ein Grad fehlte. Ein einziges, klitzekleines Grädchen. Es "
    "war nur bitterkalt, nicht bitterbitterkalt.\n\n"
    "Da kam mein Vater. Er fragte: 'Hast du nach dem Thermometer gesehen?' Ich "
    "sagte: 'Ja.' 'Und?' 'Ein Grad fehlt.' Mein Vater sagte nichts. Er ging zum "
    "Fenster. Man konnte sehen, dass er nachdachte. Dann sagte er: 'Hast du hier "
    "vors Fenster gehaucht?\" 'Ja', sagte ich. 'Ich habe das Eis weggehaucht.' Mein "
    "Vater sagte: 'Atem ist warm. Deshalb ist das Thermometer etwas gestiegen. "
    "Ich glaube, ohne Hauchen sind es bestimmt 20 Grad. Es ist bitterbitterkalt. "
    "Du brauchst nicht zur Schule. Ich schreibe dir eine Entschuldigung. Geh "
    "schnell wieder ins warme Bett. Du frierst ja.\""
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Lesestrategie nennen",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Vor dem Lesen!\n"
            "Welche Lesestrategie könnte dir am meisten helfen, die Fragen zum Text "
            "zu beantworten?"
        ),
        "answer": "Die Sätze so zu lesen, dass ich sie sinngemäß verstehe.",
        "steps": ["Sinnentnehmendes Lesen wählen."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 2,
        "type": "Begründung Lesestrategie",
        "text": "Erkläre genau, warum du dich für diese Lesestrategie entschieden hast!",
        "answer": "So kann ich die Wörter, die ich nicht kenne, durch den Text entschlüsseln.",
        "steps": ["Unbekannte Wörter aus dem Kontext erschließen."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 3,
        "type": "Schulregel",
        "text": (
            "Welche Regel gab es bei dem Jungen in der Geschichte? "
            "Wann musste er nicht in die Schule gehen?"
        ),
        "answer": "Er brauchte dann nicht zur Schule gehen, wenn es bitterbitterkalt war.",
        "steps": ["Aus dem ersten Absatz."],
        "points": 1.5,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 4,
        "type": "Begründung Vater",
        "text": "Warum wollte der Vater des Jungen dann nicht, dass er zur Schule ging?",
        "answer": (
            "Der Vater meinte, dass durch die Kälte Finger und Zehen und Nasen "
            "tot frieren können."
        ),
        "steps": ["'Da können Finger und Zehen und Nasen tot frieren.'"],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 5,
        "type": "Multiple Choice Gegenstand",
        "text": (
            "Was hing draußen vor dem Fenster?\n"
            "(a) ein Barometer\n"
            "(b) eine Wetterstation\n"
            "(c) ein Thermometer"
        ),
        "answer": "Richtig: (c) ein Thermometer.",
        "steps": ["'um auf das Thermometer zu sehen'."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 6,
        "type": "Doppelfenster erklären",
        "text": "Was sind Doppelfenster? Erkläre!",
        "answer": (
            "Zwei Fenster, die hintereinander angebracht (eingebaut) sind, "
            "nennt man Doppelfenster."
        ),
        "steps": ["'Wir hatten zwei Fenster hintereinander.'"],
        "points": 1.5,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 7,
        "type": "Bitterbitterkalt definieren",
        "text": "Wann ist es laut Aussage des Vaters bitterbitterkalt?",
        "answer": "Es ist bei mindestens zwanzig Grad unter Null bitterbitterkalt.",
        "steps": ["'mindestens zwanzig Grad unter Null'."],
        "points": 1.5,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 8,
        "type": "Angst vor Prüfung",
        "text": "Warum hatte der Junge Angst vor der Prüfung?",
        "answer": "Der Junge hatte Angst, da er nicht gut Kopfrechnen konnte.",
        "steps": ["'Ich konnte nicht gut Kopfrechnen.'"],
        "points": 1.5,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 9,
        "type": "Drei Wünsche",
        "text": (
            "Was wünschte sich der Junge, damit er am Tag der Prüfung nicht zur "
            "Schule müsste? Nenne seine drei verschiedenen Wünsche!"
        ),
        "answer": (
            "Zuerst wollte er krank werden. Zweitens wollte er, dass der Lehrer "
            "krank werden würde, und drittens wollte er, dass es bitterbitterkalt "
            "werden sollte."
        ),
        "steps": ["Drei Wünsche aus dem vierten Absatz."],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 10,
        "type": "Wörter im Text suchen",
        "text": (
            "Suche die Wörter im Text und schreibe die Zeile auf, in der sie stehen!\n"
            "gefährlich: ___\n"
            "Grädchen: ___\n"
            "weggehaucht: ___\n"
            "Kopfrechen-Prüfung: ___"
        ),
        "answer": (
            "gefährlich → Zeile 5 ; "
            "Grädchen → Zeile 37 ; "
            "weggehaucht → Zeile 42 ; "
            "Kopfrechen-Prüfung → Zeile 33."
        ),
        "steps": ["Wörter im Text finden und Zeilen notieren."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 11,
        "type": "Wettervorhersage damals",
        "text": (
            "Warum konnte der Junge nicht wissen, ob es am nächsten Tag tatsächlich "
            "bitterbitterkalt sein würde? Begründe mit Hilfe des Textes!"
        ),
        "answer": (
            "In dieser Zeit gab es weder Fernsehen noch einen Wetterbericht im "
            "Radio. Deshalb konnte der Junge nicht wissen, ob es wirklich so kalt "
            "werden würde."
        ),
        "steps": ["Es gab damals noch kein Fernsehen und keinen Wetterbericht im Radio."],
        "points": 2.5,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 12,
        "type": "Satz ankreuzen",
        "text": (
            "Welcher Satz steht genauso im Text? Kreuze an!\n"
            "(a) Ich dachte sofort an die Kopfrechen-Prüfung, krabbelte aus meinem "
            "Bett und lief mit nackten Füßen ins Wohnzimmer.\n"
            "(b) Ich dachte sofort an die Kopfrechen-Prüfung, sprang aus meinem "
            "Bett und lief mit nackten Füßen ins Wohnzimmer.\n"
            "(c) Ich dachte sofort an die Kopfrechen-Prüfung, krabbelte aus dem "
            "Bett und lief mit nackten Füßen ins Wohnzimmer."
        ),
        "answer": "Richtig: (a).",
        "steps": ["Wortlaut genau prüfen: 'krabbelte aus meinem Bett'."],
        "points": 1.5,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 13,
        "type": "Erklärung des Vaters",
        "text": (
            "Warum meinte der Vater, dass es doch Minus 20 Grad hatte, obwohl das "
            "Thermometer erst 19 Grad unter Null zeigte? Erkläre mit Hilfe des Textes!"
        ),
        "answer": (
            "Der Junge hatte vorher ans Fenster gehaucht. Deshalb meinte der Vater, "
            "dass Atem warm ist und es tatsächlich nicht 19 Grad sondern bestimmt "
            "20 Grad unter Null hätte. (Somit ist das Thermometer kurz auf 19 Grad "
            "gestiegen.)"
        ),
        "steps": ["'Atem ist warm. Deshalb ist das Thermometer etwas gestiegen.'"],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 14,
        "type": "Eigene Stellungnahme",
        "text": (
            "Bob meint: 'Der Vater hat doch geschwindelt!' "
            "Gru erwidert: 'Nein ganz sicher nicht! Es war wirklich 20 Grad minus.' "
            "Wem würdest du zustimmen? Erkläre und begründe!"
        ),
        "answer": (
            "Ich stimme Gru zu. Durch das Hauchen und das Weghauchen des Eises ist "
            "das Thermometer auf 19 Grad gestiegen, um dann später wieder auf "
            "zwanzig Grad minus zu fallen."
        ),
        "steps": ["Begründung mit dem warmen Atem."],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
]

NEW_KNOWLEDGE = []
