EXERCISE = {
    "id": "0873",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Die Wette des Freiherrn Karl von Drais (Laufrad)",
    "topic": "Leseverstehen, Sachtext, Karl von Drais, Laufrad, Erfindung, Wette, Fahrrad",
    "publisher": "CATLUX",
    "source_pdf": "0873.pdf",
    "answer_pdf": "0873 (1).pdf",
    "total_points": 39.0,
}

LESETEXT = (
    "Die Wette des Freiherrn Karl von Drais\n\n"
    "Am Stammtisch im Goldenen Schwan ist wieder einmal ein heftiger Streit "
    "ausgebrochen. 'Ich bin schneller als jeder Wanderer', hört man eine laute "
    "Stimme. 'Das kann nicht sein! Das ist unmöglich! Wie willst du das machen?' "
    "rufen die anderen dazwischen. Es geht um die neue Erfindung des "
    "Forstmeisters Karl Friedrich Christian Ludwig von Drais, Freiherr von "
    "Sauerbronn. Diesmal hat er sich etwas ganz Besonderes ausgedacht: ein "
    "Laufrad. Er versucht, seine Erfindung zu erklären: 'Mein Laufrad hat viele "
    "Vorteile. Man kommt schneller vorwärts, als wenn man einfach geht. "
    "Außerdem ist es nicht so anstrengend. Eine schwere Last ist auf einem "
    "Karren mit Rädern eben leichter zu transportieren, als wenn man sie tragen "
    "muss.\" 'Hört! Hört! Der Radläufer!', ruft einer der Herren. Schallendes "
    "Gelächter erhebt sich. Verärgert ergreift Karl von Drais wieder das Wort: "
    "'Ihr wisst ganz genau, dass mit Rädern alles leichter geht. Auf Rädern "
    "kann der Mensch auch sein eigenes Gewicht leichter bewegen, als wenn er "
    "es auf zwei Beinen bewegt.\" 'Du mit deinen Rädern', ist die Antwort 'das "
    "geht doch nicht.\" Nun wird es dem Freiherrn zu bunt, krachend schlägt "
    "seine geballte Faust auf den Tisch: 'Ich wette, dass ich mit meinem "
    "Laufrad nur vier Stunden von Karlsruhe bis zum Rhein brauche!\"\n\n"
    "Plötzlich wird es ganz still in dem Saal. Auch die anderen Gäste haben "
    "gehört, was da gesagt wurde. 'In vier Stunden von Karlsruhe bis zum "
    "Rhein.\" Dann bricht ein Tumult los. Alle rufen und schreien durcheinander. "
    "'Jetzt ist er übergeschnappt!' 'Unmöglich!' 'Die Wette hat er schon "
    "verloren!\" 'Das kann er nicht schaffen!' 'Ich bin in vier Stunden am "
    "Rhein\", ruft Karl von Drais noch einmal in die Runde. 'Die Wette gilt!' "
    "rufen einige Herren. Das wird ein Spektakel, das man sich nicht entgehen "
    "lassen kann. So etwas hat man schon lange nicht mehr erlebt in Karlsruhe. "
    "Schon wird über den Wetteinsatz und die Bedingungen dieses ungewöhnlichen "
    "Wettkampfes verhandelt. Am nächsten Sonntag soll er stattfinden. "
    "Schiedsrichter sollen in Karlsruhe und am Rhein die Start- und "
    "Ankunftszeit kontrollieren.\n\n"
    "In den nächsten Tagen werden die besten Wanderer aufgerufen, sich an dem "
    "Wettkampf zu beteiligen. Junge kräftige Burschen melden sich. Sie haben "
    "den Weg schon oft gemacht und wissen genau, wie lange ein Wanderer dafür "
    "braucht. Sie sind sich ganz sicher, diese Wette haben sie schon in der "
    "Tasche. Deshalb lächeln sie auch nur spöttisch, als Karl von Drais mit "
    "seinem Laufrad erscheint.\n\n"
    "Zuversichtlich sitzt er auf dem Holzgestell mit zwei Rädern. Seine Hände "
    "umfassen ein Querholz, mit dem er das vorderere Rad nach rechts und links "
    "bewegen kann. 'Ist das dein neues Pferd?' 'Hast du dein Pferd auch gut "
    "gefüttert?\" Solche und andere spöttischen Zurufe muss der Erfinder über "
    "sich ergehen lassen. Viele Menschen haben sich versammelt, um den Beginn "
    "dieser abenteuerlichen Wette mitzuerleben. Überall wird lebhaft "
    "diskutiert, weitere Wetten werden abgeschlossen.\n\n"
    "Dann wird es still. Gespannt schauen alle auf die Wettkämpfer. Der "
    "vereinbarte Zeitpunkt für den Start ist gekommen. Auf ein Zeichen hin "
    "setzen sie sich in Bewegung. Mit kräftigen Tritten stößt sich Karl von "
    "Drais vom Boden ab. Er kommt in Fahrt. Immer schneller rollt er mit "
    "seinem Laufrad davon. Durch die holprigen Straßen und Gassen geht es. "
    "Mit gleichmäßigen Stößen hält er sein Laufrad in Schwung. Schon bald hat "
    "er die Wanderer weit hinter sich gelassen. Nach vier Stunden erreicht der "
    "Laufrad-Erfinder das vereinbarte Ziel. Zwölf Stunden später kommen auch "
    "die Wanderer an. Verschwitzt mit Blasen an den Füßen betreten sie "
    "erschöpft das Gasthaus, wo der Freiherr schon wartet. 'Wo kommt ihr denn "
    "her? Habt ihr unterwegs Blumen gepflückt?\" spöttelt er.\n\n"
    "Dies geschah im Jahre 1817. Karl von Drais hat die Wette gewonnen. Durch "
    "diese Fahrt wurde die Laufmaschine bekannt. Aber es dauerte noch über "
    "fünfzig Jahre, bis aus seiner Idee unser heutiges Fahrrad mit Pedalen, "
    "Kettenantrieb und Luftbereifung wurde."
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Erfindung benennen",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Was hat Karl von Drais erfunden?"
        ),
        "answer": "Er hat ein Laufrad erfunden.",
        "steps": ["Im 1. Absatz."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 2,
        "type": "Drei Vorteile",
        "text": "Welche drei Vorteile seiner Erfindung nennt Drais?",
        "answer": (
            "1. Man kommt schneller vorwärts. ; "
            "2. Es ist nicht so anstrengend. ; "
            "3. Man kann eine schwere Last besser transportieren als wenn man sie tragen muss."
        ),
        "steps": ["Aus Absatz 1."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 3,
        "type": "Wette",
        "text": "Wie lautet die Wette?",
        "answer": "Er wettet, dass er mit seinem Laufrad nur 4 Stunden von Karlsruhe bis zum Rhein braucht.",
        "steps": ["Direkt aus dem Text."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 4,
        "type": "Glauben der Gäste",
        "text": "Glauben die anderen Gäste, dass von Drais seine Wette gewinnt?",
        "answer": "Nein, sie glauben nicht, dass er die Wette gewinnt.",
        "steps": ["'Jetzt ist er übergeschnappt!' usw."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 5,
        "type": "Aufgabe Schiedsrichter",
        "text": "Was ist die Aufgabe der Schiedsrichter?",
        "answer": "Sie sollen in Karlsruhe und am Rhein die Start- und Ankunftszeit kontrollieren.",
        "steps": ["Aus Absatz 2."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 6,
        "type": "Andere Wettkämpfer",
        "text": "Wer – außer Karl von Drais – beteiligt sich am Wettkampf?",
        "answer": "Kräftige, junge Burschen und die besten Wanderer.",
        "steps": ["Aus Absatz 3."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 7,
        "type": "Fortbewegung",
        "text": "Wie bewegt von Drais sich fort?",
        "answer": "Er bewegte sich mit gleichmäßigen, kräftigen Fußstößen fort.",
        "steps": ["Aus Absatz 5."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 8,
        "type": "Zeitpunkt Drais am Ziel",
        "text": "Wie viel Zeit ist vergangen, als er sein Ziel erreicht?",
        "answer": "Nach 4 Stunden erreicht er das Ziel.",
        "steps": ["Aus Absatz 5."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 9,
        "type": "Zeitbedarf Wanderer",
        "text": "Wie viel Zeit brauchten seine Wettgegner?",
        "answer": "Die Wettgegner brauchten 16 Stunden (12 Stunden später als Drais).",
        "steps": ["Drais nach 4h, Wanderer 12h später → 16h."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 10,
        "type": "Datum",
        "text": "Diese Geschichte ist wirklich passiert. Wann war das?",
        "answer": "Das war 1817 an einem Sonntag.",
        "steps": ["Aus dem letzten Absatz."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 11,
        "type": "Bekanntheit Laufrad",
        "text": "Wie wurde das Laufrad bekannt?",
        "answer": (
            "Durch die Wette mit den Herren, dass er in vier Stunden von Karlsruhe "
            "bis zum Rhein mit dem Laufrad braucht, die Karl von Drais gewonnen hat."
        ),
        "steps": ["Aus dem letzten Absatz."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 12,
        "type": "Laufrad beschreiben",
        "text": "Beschreibe das Laufrad von Karl von Drais!",
        "answer": (
            "Es ist ein Holzgestell mit zwei Rädern und einem Querholz, mit dem "
            "er das vordere Rad nach links und rechts bewegen kann."
        ),
        "steps": ["Aus Absatz 4."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 13,
        "type": "Wer/Was pro Abschnitt",
        "text": "Finde zu jedem der 5 Abschnitte das wichtigste Wer oder Was!",
        "answer": (
            "Abschnitt 1: Karl von Drais, das Laufrad und die Herren vom Stammtisch ; "
            "Abschnitt 2: Die Wette zwischen Drais und den Herren ; "
            "Abschnitt 3: Die besten Wanderer und der Laufrad-Erfinder ; "
            "Abschnitt 4: Karl von Drais, die Wette und die Wanderer ; "
            "Abschnitt 5: Karl von Drais, Laufrad und Fahrrad."
        ),
        "steps": ["Hauptperson/Hauptthema jedes Absatzes finden."],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 14,
        "type": "Wichtigstes pro Abschnitt",
        "text": "Finde das Wichtigste über das Wer oder Was in jedem der 5 Abschnitte!",
        "answer": (
            "1: Erfinder des Laufrads, schneller als zu Fuß. ; "
            "2: Drais wettet 4 Stunden, Herren halten dagegen. ; "
            "3: Wanderer treten an und verspotten ihn. ; "
            "4: Drais lässt sie hinter sich, kommt nach 4 Std. an, Wanderer 12 Std. später. ; "
            "5: 1817 gewann er, später wurde daraus das Fahrrad."
        ),
        "steps": ["Wichtigste Aussage je Abschnitt zusammenfassen."],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 15,
        "type": "Zusammenfassung in Sätzen",
        "text": "Schreibe zu jedem Abschnitt ein bis zwei zusammenfassende Sätze!",
        "answer": (
            "1: Karl von Drais stellt im Wirtshaus seine Erfindung das Laufrad vor und schließt eine Wette ab. ; "
            "2: Die Wette: in 4 Stunden von Karlsruhe zum Rhein. ; "
            "3: Am Tag der Wette wird Drais von den besten Wanderern verspottet. ; "
            "4: Drais gewinnt die Wette in 4 Stunden, Wanderer kommen erst 12 Stunden später. ; "
            "5: Drais gewinnt 1817; über 50 Jahre später entstand daraus das Fahrrad."
        ),
        "steps": ["Inhaltliche Zusammenfassung pro Abschnitt."],
        "points": 9.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 16,
        "type": "Zusammenfassung beurteilen",
        "text": (
            "Beurteile vorgegebene Zusammenfassungen nach den Kriterien: "
            "kurz / eigene Worte / das Wichtigste. Streiche, was nicht zutrifft!"
        ),
        "answer": (
            "Zusammenfassungen aller 5 Abschnitte sind kurz, in eigenen Worten und "
            "enthalten das Wichtigste. Alle drei Kriterien sind angekreuzt."
        ),
        "steps": ["Alle drei Kriterien prüfen."],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
]

NEW_KNOWLEDGE = []
