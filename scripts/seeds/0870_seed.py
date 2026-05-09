EXERCISE = {
    "id": "0870",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Wie Eulenspiegel in einem Bienenkorb schlief",
    "topic": "Leseverstehen, Schwank, Till Eulenspiegel, Bienenkorb, Diebe",
    "publisher": "CATLUX",
    "source_pdf": "0870.pdf",
    "answer_pdf": "0870 (1).pdf",
    "total_points": 23.0,
}

LESETEXT = (
    "Wie Eulenspiegel in einem Bienenkorb schlief\n\n"
    "Einmal war Till mit seiner Mutter in einem Nachbardorf zur Kirchweih. "
    "Schließlich wurde er müde und suchte sich ein schattiges Plätzchen zum "
    "Schlafen.\n\n"
    "Dabei geriet er in einen stillen Garten, in dem viele Bienenkörbe standen. "
    "Es waren auch leere Stöcke darunter, und in einen der leeren Bienenstöcke "
    "legte er sich und schlief ein. Er schlief von Mittag bis gegen Mitternacht. "
    "Und Frau Eulenspiegel, die ihren Herrn Sohn überall auf dem "
    "Kirchweihrummel gesucht hatte, dachte, er sei schon längst nach Hause "
    "gegangen. Stattdessen lag er, wie gesagt, in dem leeren Bienenkorb und "
    "schlief. Gegen Mitternacht kamen zwei Diebe in den stillen abgelegenen "
    "Garten und wollten einen Bienenkorb stehlen, um dann den Honig zu "
    "verkaufen. 'Wir werden den schwersten Korb nehmen', sagte der eine Dieb. "
    "'Je schwerer der Korb ist, umso mehr Honig hat er.' 'In Ordnung', sagte "
    "der andere. Und dann hoben sie die Körbe der Reihe nach hoch. Der "
    "schwerste war natürlich der, in dem Eulenspiegel lag. Und deshalb nahmen "
    "sie den, luden ihn sich auf die Schultern, schleppten ihn aus dem Garten "
    "auf die Straße hinaus und wanderten stöhnend und schwitzend ihrem Dorf zu.\n\n"
    "Eulenspiegel war natürlich aufgewacht und ärgerte sich, dass ihn die "
    "beiden Kerle geweckt und nun auch noch nachts in ein Dorf schleppten, in "
    "dem er gar nicht wohnte. Als sie ihn so eine Weile getragen hatten, griff "
    "er vorsichtig aus dem Bienenkorb heraus und zog den Vorderen furchtbar an "
    "den Haaren.\n\n"
    "'Aua', schrie der Dieb. 'Bist du denn ganz verrückt geworden?' Er dachte "
    "selbstverständlich, der andere Dieb sei es gewesen und schimpfte "
    "schauderhaft. Der andere wusste nicht, was los war und sagte: 'Du bist "
    "wohl übergeschnappt! Ich schleppe an dem Bienenkorb wie ein Möbelträger, "
    "und du bildest dir ein, ich hätte Zeit und Lust, dich an den Haaren zu "
    "ziehen! Zu dumm!\"\n\n"
    "Eulenspiegel amüsierte sich königlich, und nach einer Weile rupfte er den "
    "Hintermann am Haar, und zwar derartig, dass ihm ein Büschel Haare in der "
    "Hand blieb. 'Nun wird's mir aber auch zu bunt!', brüllte der Dieb. 'Erst "
    "träumst du, ich hätte dich an den Haaren gezogen. Und nun reißt du mir "
    "fast die Kopfhaut runter!\" So eine Frechheit!\" 'Blödsinn!', knurrte der "
    "andere. 'Es ist so dunkel, dass ich die Straße kaum sehen kann, und ich "
    "halte den Korb mit beiden Händen fest, und da soll ich noch hinter mich "
    "greifen und dir Haare herausziehen können? Bei dir piept's ja!\"\n\n"
    "Sie stritten, fluchten und ächzten, dass Till Eulenspiegel beinahe laut "
    "gelacht hätte. Aber das ging natürlich nicht. Stattdessen riss er, fünf "
    "Minuten später, den Vordermann derartig am Haar, dass der mit dem Schädel "
    "an den Bienenkorb krachte, den Korb fallen ließ, sich umdrehte und den "
    "Hintermann wütend mit beiden Fäusten ins Gesicht schlug. Nun ließ auch "
    "dieser Dieb den Korb fallen und warf sich mit aller Wucht auf den "
    "Vorderen. Im nächsten Augenblick lagen beide am Boden und rangen und "
    "schlugen und kratzten sich, bis sie schließlich so übereinander "
    "wegpurzelten, dass sie, so wütend waren sie, sich im Dunkeln überhaupt "
    "nicht wieder fanden. Eulenspiegel aber blieb gemütlich in seinem Korb "
    "liegen und schlief weiter, bis ihn am Morgen die Sonne weckte."
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Textgattung",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Zu welcher Textgattung gehört die Geschichte?\n"
            "(a) Gedicht (b) Fabel (c) Schwank (d) Sachtext"
        ),
        "answer": "Richtig: (c) Schwank.",
        "steps": ["Schwank: lustige, kurze Geschichte mit Pointe."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 2,
        "type": "Merkmale Schwank",
        "text": "Nenne zwei Merkmale dieser Textgattung, die auf diese Geschichte zutreffen!",
        "answer": "Z. B.: Übertreibungen, Streiche, Dummheiten, witziger Schluss.",
        "steps": ["Typische Schwank-Merkmale."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 3,
        "type": "Personen nennen",
        "text": "Nenne alle Personen, die in der Geschichte vorkommen!",
        "answer": "Till Eulenspiegel, seine Mutter (Frau Eulenspiegel) und zwei Diebe.",
        "steps": ["Aus dem Text alle Figuren benennen."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 4,
        "type": "Grund Nachbardorf",
        "text": "Warum geht Till ins Nachbardorf?",
        "answer": "Im Nachbardorf ist Kirchweih.",
        "steps": ["'in einem Nachbardorf zur Kirchweih'."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 5,
        "type": "Grund Bienenstock",
        "text": "Warum kriecht er in den Bienenstock? (Lies genau nach!)",
        "answer": "Er kriecht in den Bienenstock, weil er müde ist und ein schattiges Plätzchen sucht.",
        "steps": ["'wurde er müde und suchte sich ein schattiges Plätzchen'."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 6,
        "type": "Vermutung der Mutter",
        "text": "Wo vermutet Frau Eulenspiegel ihren Sohn?",
        "answer": "Frau Eulenspiegel vermutet, dass Till schon nach Hause gegangen ist.",
        "steps": ["'dachte, er sei schon längst nach Hause gegangen'."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 7,
        "type": "Plan der Diebe",
        "text": "Was wollten die Diebe mit einem Bienenstock tun? (Antworte ausführlich)",
        "answer": "Sie wollten den Honig der Bienen klauen, um diesen zu verkaufen.",
        "steps": ["'einen Bienenkorb stehlen, um dann den Honig zu verkaufen'."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 8,
        "type": "Schwerster Korb",
        "text": "Warum nehmen die Diebe den Korb mit Eulenspiegel mit?",
        "answer": "Die Diebe vermuten, dass in dem schwersten Korb der meiste Honig ist.",
        "steps": ["'Je schwerer der Korb ist, umso mehr Honig hat er.'"],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 9,
        "type": "Zeilen suchen",
        "text": (
            "Suche die Zeilen:\n"
            "(a) …wanderten stöhnend und…\n"
            "(b) …wie ein Möbelträger…\n"
            "(c) …schlugen und kratzten…\n"
            "(d) '…Erst träumst du…'"
        ),
        "answer": "(a) Zeile 13 ; (b) Zeile 21 ; (c) Zeile 34 ; (d) Zeile 25.",
        "steps": ["Textstellen mit Zeilenangabe."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 10,
        "type": "Ärger Eulenspiegel",
        "text": "Warum ärgert sich Eulenspiegel über die Diebe? Suche zwei Gründe im Text!",
        "answer": (
            "Eulenspiegel ärgert sich, weil sie ihn geweckt haben und ihn in ein "
            "anderes Dorf schleppten."
        ),
        "steps": ["Zwei Gründe aus dem Text."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 11,
        "type": "Wehr Eulenspiegel",
        "text": "Wie wehrt sich Eulenspiegel?",
        "answer": "Er zog sie abwechselnd an den Haaren.",
        "steps": ["Vorderen und Hintermann am Haar gezogen."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 12,
        "type": "Streit der Diebe",
        "text": "Warum beginnen die Diebe zu streiten?",
        "answer": "Beide denken, der andere zieht ihnen an den Haaren.",
        "steps": ["Missverständnis durch Eulenspiegels Streich."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 13,
        "type": "Synonyme finden",
        "text": (
            "Finde andere, passende Worte aus dem Text:\n"
            "Räuber: ___\n"
            "tragen: ___"
        ),
        "answer": "Räuber → Diebe ; tragen → schleppen.",
        "steps": ["Synonyme im Text suchen."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 14,
        "type": "Ausdrücke erklären",
        "text": (
            "Was bedeutet dieser Ausdruck?\n"
            "(a) 'Du bist wohl übergeschnappt!' (Z. 20)\n"
            "(b) '…mit aller Wucht…' (Z. 33)"
        ),
        "answer": "(a) Du bist wohl verrückt. ; (b) mit aller Kraft.",
        "steps": ["Redewendungen erklären."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 15,
        "type": "Andere Schwankhelden",
        "text": (
            "Du kennst noch mehr Geschichten dieser Textgattung. "
            "Wie heißen ihre 'Helden' (Figuren)?"
        ),
        "answer": "Baron von Münchhausen, Max und Moritz und die Schildbürger.",
        "steps": ["Bekannte Schwankfiguren."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 16,
        "type": "Name erklären",
        "text": "Erkläre den Namen 'Eulenspiegel'!",
        "answer": "Ich halte euch den Spiegel vor, zeige euch eure Fehler.",
        "steps": ["Name = Spiegel der menschlichen Schwächen."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
]

NEW_KNOWLEDGE = []
