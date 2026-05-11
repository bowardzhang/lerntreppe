EXERCISE = {
    "id": "1008",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: ... wird ein Hund (Irmela Bender)",
    "topic": "Leseverstehen, Erzählung, Hund, Hochhaus, Großmutter, Pebowipuckel",
    "publisher": "CATLUX",
    "source_pdf": "1008.pdf",
    "answer_pdf": "1008 (1).pdf",
    "total_points": 24.0,
}

LESETEXT = (
    "... wird ein Hund (Irmela Bender)\n\n"
    "Allmählich hatte Schanett schon überhaupt keine Lust mehr, auf dem Parkplatz "
    "vor ihrem Haus zu spielen – er bot mit der Zeit wirklich nicht viel "
    "Abwechslung; aber hinter dem Haus war der Rasen gewachsen. Schanett "
    "betrachtete ihn jeden Tag und wunderte sich, dass ein Grashalm genau so "
    "aussah wie der andere. Mitten im Rasen schauten drei Flecken Erde heraus, in "
    "die pflanzte der Hausmeister drei Birken, die ihre Äste hochzogen und die "
    "Blätter hängen ließen. Dann rammte der Hausmeister einen Pfahl mit einem "
    "Schild in den Rasen. Schanett war froh, dass sie noch nicht lesen konnte, "
    "sonst hätte sie sich nur noch mehr darüber geärgert. Sie wusste auch so, was "
    "darauf stand: Betreten VERBOTEN! Vielleicht auch: BETRETEN FÜR KINDER VERBOTEN!\n\n"
    "Denn der Hausmeister durfte. Und Hunde, sah Schanett, durften auch. In diesem "
    "Haus lebten viele Hunde; Schanett lernte sie auf der Treppe oder an der "
    "Haustür kennen, aber immer nur flüchtig, denn ihre Besitzer hatten wenig "
    "Zeit. Immerhin stellte Schanett durch viele Aufzugfahrten und Treppengehen "
    "allmählich fest, wo sie wohnten. Im siebten Stock gab es einen Pekinesen, "
    "im fünften einen Boxer und einen Windhund, im zweiten einen Pudel und im "
    "ersten einen Dackel. Alle diese Hunde durften, jeder zu einer anderen Zeit, "
    "auf den Rasen. Der Boxer sabberte darauf, der Pekinese schnupperte am Gras, "
    "der Windhund wälzte sich und der Dackel hob das Bein an einer Birke. "
    "Schanett beobachtete das eine Zeitlang, dann teilte sie der Großmutter mit: "
    "'Ich werde ein Hund.'\n\n"
    "'Welche Rasse?', fragte die Großmutter und legte die Zeitung weg. 'Ein "
    "Pebowipuckel\", sagte Schanett. Sie hatte sich einfach von jedem Hund ein "
    "bisschen Namen geliehen. 'Ein Pebowipuckel – das geht', meinte die "
    "Großmutter nach einigem Überlegen. 'Ein Schäferhund wäre mir nämlich zu "
    "groß. Er frisst auch zu viel.\"\n\n"
    "'Was tut ein Hund?', fragte Schanett.\n\n"
    "'Ich habe wenig Erfahrung', gab die Großmutter zu. 'Manche bellen. Es wäre "
    "schön, wenn Pebowipuckel nicht bellten.\" 'Nur draußen', versprach Schanett "
    "und sie machte ganz leise: 'Wuff!' Seit sie die Hunde beobachtete, wusste "
    "sie, dass sie überhaupt nicht Wau sagen konnten.\n\n"
    "'Kann ich raus?'\n\n"
    "'Du brauchst eine Leine.' Die Großmutter band ihr eine Kette aus roten "
    "Perlen um den Hals und befestigte daran ein ledernes Schuhbändel. 'Und du "
    "musst auf allen vieren gehen. Brauchst du auch einen Maulkorb?\" 'Ich bin "
    "nicht bissig\", sagte Schanett. 'Nur rennig. Sonst noch was?' 'Zieh die "
    "Schuhe aus\", schlug die Großmutter vor. 'Es sieht so ungewöhnlich aus, wenn "
    "du auf allen vieren gehst. Außerdem muss man wohl den Rasen schonen.\" "
    "Schanett zog die Schuhe aus. 'Noch was?' 'Ich weiß nicht – ich meine, da "
    "war noch was. Hm. Vermutlich fällt es mir wieder ein.\" Schanett wartete "
    "noch ein bisschen, ob es der Großmutter vielleicht gleich einfiele. Aber "
    "als die Großmutter im Nachdenken nach der Zeitung griff, trabte Schanett "
    "davon.\n\n"
    "Gerade war der Windhund auf dem Rasen. Er rannte und schnupperte und wälzte "
    "sich und Schanett, der Pebowipuckel, tat es ihm nach. Bald merkte sie, dass "
    "ihr das Richtige eingefallen war: Es war fantastisch, ein Pebowipuckel zu "
    "sein. Die Erde roch ganz anders, wenn man dicht mit der Nase daran kam und "
    "das Gras fühlte sich zwischen den Händen gar nicht so gleichmäßig an. "
    "Schanett schnupperte an einer Birke und atmete aus Versehen eine kleine "
    "Spinne ein, die sie gleich wieder herausnieste. Der Windhund hob kurz den "
    "Kopf und beachtete sie nicht weiter.\n\n"
    "Dafür kam eine Frau, die zu ihm gehörte, und schaute Schanett aufmerksam "
    "zu. Nach einer Weile sagte die Frau: 'Darfst du das?' 'Klar', sagte "
    "Schanett und versuchte mit den Ohren zu schlenkern wie der Windhund – "
    "vergeblich. 'Ich weiß schon, das Schild. Aber ich bin kein Kind, ich bin "
    "ein Hund. Hunde dürfen.\" 'Ach so', sagte die Frau. Man sah ihr an, dass "
    "sie gar nicht sicher war. 'Es stimmt alles', sagte Schanett beruhigend. "
    "'Schauen Sie – ich habe ein Halsband und eine Leine. Falls noch was fehlt, "
    "fällt es meiner Großmutter sicher ein.\""
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Wohnsituation",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "In was für einer Art von Haus wohnt Schanett?"
        ),
        "answer": "Schanett wohnt in einem Hochhaus.",
        "steps": ["Aufzug, viele Stockwerke (1., 2., 5., 7. Stock)."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 2,
        "type": "Schulalter begründen",
        "text": "Ging das Mädchen schon zur Schule? Überlege und begründe deine Meinung!",
        "answer": "Nein, da sie noch nicht lesen konnte.",
        "steps": ["'Schanett war froh, dass sie noch nicht lesen konnte.'"],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 3,
        "type": "Grund für Hundewunsch",
        "text": "Schanett wollte ein Hund sein. Erkläre den Grund für diesen Wunsch!",
        "answer": "Hunde durften den Rasen betreten.",
        "steps": ["Kinder dürfen nicht auf den Rasen, Hunde schon."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 4,
        "type": "Hunderasse ankreuzen",
        "text": (
            "Das Mädchen überlegt sich eine Hunderasse für sich. Sie wollte ein …\n"
            "(a) Bepowipuckel\n"
            "(b) Pebowipuckel\n"
            "(c) Pebowimuckel\n"
            "(d) Pebomipuckel\n"
            "… sein. Kreuze das Richtige an!"
        ),
        "answer": "Richtig: (b) Pebowipuckel.",
        "steps": ["Genauen Namen im Text nachprüfen."],
        "points": 1.0,
        "has_image": True,
        "image": "1008_q4_hunderasse_ankreuzen.png",
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 5,
        "type": "Namensbildung erklären",
        "text": "Erkläre, wie Schanett auf diese Bezeichnung kam! Begründe genau und ausführlich!",
        "answer": (
            "Sie hat sich von den Namen der Hunderassen die Anfangsbuchstaben oder "
            "die Schlussbuchstaben geliehen: Pe vom Pekinesen, Bo vom Boxer, "
            "wi vom Windhund, pu vom Pudel und ckel vom Dackel."
        ),
        "steps": ["Pe + Bo + wi + pu + ckel = Pebowipuckel."],
        "points": 2.5,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 6,
        "type": "Großmutters Hilfe",
        "text": (
            "Die Großmutter half mit, dass ihre Enkelin einem Hund noch mehr ähnelt. "
            "Was machte sie?"
        ),
        "answer": (
            "Sie hat ihr eine Hundeleine aus roten Perlen und einem ledernen "
            "Schuhbändel gebastelt und um den Hals gebunden."
        ),
        "steps": ["Halsband + Leine basteln."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 7,
        "type": "Schuhe ausziehen",
        "text": "Warum meint die Oma, dass Schanett ihre Schuhe ausziehen soll? Nenne zwei Gründe!",
        "answer": (
            "Weil Schuhe ungewöhnlich aussehen, wenn man auf allen Vieren geht, "
            "und man muss den Rasen schonen."
        ),
        "steps": [
            "Grund 1: Aussehen.",
            "Grund 2: Rasen schonen.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 8,
        "type": "Hund auf Rasen",
        "text": (
            "Bei ihrem ersten Versuch ein Hund zu sein, befand sich noch ein Hund "
            "auf dem Rasen. Nenne die Rasse!"
        ),
        "answer": "Es war ein Windhund.",
        "steps": ["'Gerade war der Windhund auf dem Rasen.'"],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 9,
        "type": "Parkplatz langweilig",
        "text": (
            "Schanett hatte keine Lust mehr auf dem Parkplatz vor dem Haus zu "
            "spielen. Was war der Grund?"
        ),
        "answer": "Er bot mit der Zeit keine Abwechslung mehr.",
        "steps": ["'er bot mit der Zeit wirklich nicht viel Abwechslung'."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 10,
        "type": "Schäferhund-Begründung",
        "text": (
            "Die Großmutter ist froh, dass ihre Enkeltochter kein Schäferhund ist. "
            "Erkläre mit zwei Aussagen!"
        ),
        "answer": "Ein Schäferhund ist ihr zu groß und ein Schäferhund frisst zu viel.",
        "steps": ["'zu groß. Er frisst auch zu viel.'"],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 11,
        "type": "Hunde zuordnen",
        "text": (
            "Ordne zu: Wo wohnte welcher Hund?\n"
            "1. Stock: ___\n"
            "2. Stock: ___\n"
            "5. Stock: ___\n"
            "7. Stock: ___"
        ),
        "answer": (
            "1. Stock: Dackel ; "
            "2. Stock: Pudel ; "
            "5. Stock: Boxer und Windhund ; "
            "7. Stock: Pekinese."
        ),
        "steps": ["Aus dem zweiten Absatz."],
        "points": 2.5,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 12,
        "type": "Spinne erzählen",
        "text": "Schanett kam auch mit einem kleinen Tierchen in Berührung. Erzähle!",
        "answer": (
            "Schanett schnupperte an einer Birke und atmete aus Versehen eine "
            "kleine Spinne ein, die sie aber wieder herausnieste."
        ),
        "steps": ["Aus dem vorletzten Absatz."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 13,
        "type": "Sätze zu Absätzen zuordnen",
        "text": (
            "Zu welchem Absatz passen die einzelnen Sätze?\n"
            "(a) Schanett erklärt, dass sie auf den Rasen darf. Absatz: ___\n"
            "(b) Viele Hunde wälzen sich, sabbern und schnuppern am Boden. Absatz: ___\n"
            "(c) Das Mädchen beschließt ein Hund zu werden. Absatz: ___\n"
            "(d) Der Hausmeister stellt ein Schild auf. Absatz: ___"
        ),
        "answer": "(a) Absatz 4 ; (b) Absatz 2 ; (c) Absatz 3 ; (d) Absatz 1.",
        "steps": ["Absätze inhaltlich identifizieren."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 14,
        "type": "Eigene Meinung",
        "text": (
            "Im Text dürfen Kinder die Rasenfläche hinter dem Haus nicht betreten. "
            "Was sagst du dazu? Begründe deine Meinung!"
        ),
        "answer": "Individuelle Lösungen.",
        "steps": ["Eigene Meinung mit Begründung."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
]

NEW_KNOWLEDGE = []
