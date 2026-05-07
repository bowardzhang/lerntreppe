EXERCISE = {
    "id": "0699",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Vom Fuchs, wie er zwei kleine Bären beschwindelt hat",
    "topic": "Leseverstehen, Fabel, Tiergeschichte, Wortarten, Synonyme",
    "publisher": "CATLUX",
    "source_pdf": "0699.pdf",
    "answer_pdf": "0699 (1).pdf",
    "total_points": 37.0,
}

LESETEXT = (
    "Vom Fuchs, wie er zwei kleine Baeren beschwindelt hat (Fabel)\n\n"
    "In diesem Wald, in diesem undurchdringlichen Dickicht lebte einmal eine "
    "Baerenmutter mit zwei Baerenkindern. Eines Tages, als sie heranwuchsen, "
    "beschlossen die Brueder, sich auf den Weg zu machen. Sie verabschiedeten "
    "sich von ihrer Mutter und nahmen etwas zu essen mit auf den Weg.\n\n"
    "Bald hatten sie ein Stueck Kaese gefunden. 'Ach, Bruederchen, ich moechte "
    "essen!', sagte das juengere Baerlein. Doch sie konnten sich nicht "
    "einigen, wer welches Stueck Kaese bekommen sollte. Sie begannen zu "
    "streiten.\n\n"
    "Da kam der schlaue Gevatter Fuchs daher. 'Was streitet ihr denn, junge "
    "Herren?', fragte er. 'Wir koennen uns nicht einigen, wie wir den Kaese "
    "teilen sollen.' 'Das ist doch ganz einfach', lachte der Fuchs, 'ich werde "
    "teilen!'.\n\n"
    "Der Fuchs brach den Kaese in zwei Stuecke. Doch eine Haelfte war groesser "
    "als die andere. 'Du hast uns aber schoen bedacht!', stoehnte das eine "
    "Baerlein. 'Keine Sorge', sagte der Fuchs, 'ich gleiche das aus.' Er biss "
    "ein Stueck vom groesseren Teil ab - und es wurde kleiner als das andere. "
    "Also biss er auch davon ab. So ging es immer wieder, bis der Fuchs den "
    "ganzen Kaese gegessen hatte.\n\n"
    "Die beiden Baerlein blieben mit leerem Magen zurueck. Der schlaue Fuchs "
    "aber zog vergnuegt davon."
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Richtigen Satz unterstreichen",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Welcher Satz steht im Text? Kreuze an:\n"
            "(a) In jenem Wald, in jenem dichten Gebuesch lebte einmal eine "
            "Baerenmutter mit zwei Baerenkindern.\n"
            "(b) In diesem Wald, in diesem undurchdringlichen Dickicht lebte "
            "einmal eine Baerenmutter mit zwei Baerenkindern.\n"
            "(c) In jenem Wald, in jenem dichten Dickicht lebte einmal eine "
            "Baerenmutter mit zwei Baerenkindern."
        ),
        "answer": "Richtig: (b).",
        "steps": [
            "Originalsatz im Text identifizieren.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 2,
        "type": "Frage des Fuchses",
        "text": "Was fragte der Fuchs die beiden Tiere, als er ihnen begegnete?",
        "answer": "'Was streitet ihr denn, junge Herren?'",
        "steps": [
            "Direkt aus dem Text: 'Was streitet ihr denn, junge Herren?'.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 3,
        "type": "Aussagen ankreuzen",
        "text": (
            "(a) Wo wohnen die Baeren? Kreuze die richtige Antwort an:\n"
            "i) auf einer Wiese ; ii) in einem dichten Wald ; iii) in einer Hoehle\n"
            "(b) Was nehmen die Baeren mit auf den Weg?\n"
            "i) Spielzeug ; ii) etwas zu essen ; iii) Geld"
        ),
        "answer": "(a) ii) in einem dichten Wald ; (b) ii) etwas zu essen.",
        "steps": [
            "Im Text nachlesen.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 4,
        "type": "Vorschlag des Fuchses",
        "text": "Welchen Vorschlag machte der Fuchs, um den Streitfall zu loesen?",
        "answer": "Er schlug vor: 'Das ist doch ganz einfach, ich werde teilen!'",
        "steps": [
            "Direktes Zitat aus dem Text.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 5,
        "type": "Erste Teilung des Käses",
        "text": "Was stellten die Baerenkinder fest, als der Fuchs den Kaese das erste Mal teilte?",
        "answer": "Eine Haelfte war groesser als die andere.",
        "steps": [
            "Beobachtung der Baerlein wiedergeben.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 6,
        "type": "Unzufriedenheit der Bären",
        "text": "Warum waren die beiden Baeren mit dem Handeln des Fuchses staendig unzufrieden?",
        "answer": "Der Fuchs teilte den Kaese nie gerecht auf - die Stuecke waren immer ungleich gross.",
        "steps": [
            "Begruendung: ungerechte Aufteilung.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 7,
        "type": "Wer fraß den Käse?",
        "text": "Wer hat am Ende den Kaese gefressen?",
        "answer": "Der Fuchs hat den ganzen Kaese gefressen.",
        "steps": [
            "Schluss der Geschichte.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 8,
        "type": "Anrede der Bärenkinder",
        "text": "Mit welchem Namen werden die Baerenkinder vom Fuchs angesprochen?",
        "answer": "'Junge Herren'.",
        "steps": [
            "Originalanrede aus dem Text.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 9,
        "type": "Tier mit Namen 'Gevatter'",
        "text": "Welches Tier traegt auch den Namen 'Gevatter'?",
        "answer": "Der Fuchs (Gevatter Fuchs).",
        "steps": [
            "Klassische Anrede in deutschen Fabeln.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 10,
        "type": "Bedeutung erklären",
        "text": (
            "Suche im Text die Aussage '...du hast uns aber schoen bedacht!' "
            "und erklaere sie mit eigenen Worten."
        ),
        "answer": (
            "Der Fuchs hat die beiden Baeren reingelegt. Mit der Aussage meinen "
            "die Baerlein ironisch das Gegenteil: Der Fuchs hat sie nicht gut "
            "bedacht - er hat sie betrogen."
        ),
        "steps": [
            "Ironie erkennen: 'schoen bedacht' = sehr schlecht bedacht.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 11,
        "type": "Adjektive zu Tieren",
        "text": (
            "Nenne je ein passendes Adjektiv fuer das Verhalten der Tiere und "
            "begruende:\n"
            "Baerlein: ___\n"
            "Fuchs: ___"
        ),
        "answer": (
            "Baerlein: dumm/streitsuechtig - sie lassen sich ueberlisten und "
            "streiten um den Kaese. ; "
            "Fuchs: schlau/listig/klug - er ueberlistet beide Baeren und isst "
            "den ganzen Kaese."
        ),
        "steps": [
            "Charaktereigenschaften aus dem Verhalten ableiten.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
            "deutsch.klasse4.grammatik.wortarten",
        ],
    },
    {
        "n": 12,
        "type": "Synonyme im Text",
        "text": (
            "Suche im Text Woerter, die du durch folgende Woerter ersetzen "
            "koenntest:\n"
            "(a) zanken ; (b) kraeftig ; (c) stoehnen"
        ),
        "answer": "(a) streiten ; (b) herzhaft ; (c) seufzen",
        "steps": [
            "Synonyme im Text suchen.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 13,
        "type": "Synonym für seufzte",
        "text": "Ersetze 'seufzte' durch ein anderes passendes Wort.",
        "answer": "stoehnte (oder klagte, jammerte).",
        "steps": [
            "Synonym fuer 'seufzen'.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.wortarten",
        ],
    },
    {
        "n": 14,
        "type": "Wortarten unterstreichen",
        "text": (
            "Unterstreiche in der Geschichte 2 Nomen (gruen), 2 Verben (blau) "
            "und 2 Adjektive (gelb)."
        ),
        "answer": (
            "Beispiele: Nomen: 'Wald', 'Mutter', 'Brueder'. "
            "Verben: 'lebte', 'beschlossen', 'streiten'. "
            "Adjektive: 'samtenen', 'dichter', 'juengere'."
        ),
        "steps": [
            "Wortarten erkennen und farbig markieren.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.wortarten",
        ],
    },
    {
        "n": 15,
        "type": "Textsorte erkennen",
        "text": (
            "(a) Wie nennt man diese Art der Geschichten?\n"
            "(b) Nenne zwei Merkmale dieser Textsorte mit je einem Beispiel.\n"
            "(c) Nenne zwei weitere solche Geschichten.\n"
            "(d) Was kann man aus dieser Geschichte lernen?"
        ),
        "answer": (
            "(a) Eine Fabel. ; "
            "(b) (1) Tiere koennen sprechen/denken (z. B. 'Ach, Bruederchen, "
            "ich moechte essen!'). (2) Tiere haben menschliche Eigenschaften "
            "(der Fuchs lacht und ueberlistet). ; "
            "(c) Beispiele: 'Der Fuchs und die Gaense', 'Der Hase und der Igel', "
            "'Zwei Froesche in der Milch'. ; "
            "(d) Wenn zwei sich streiten, freut sich der Dritte: Der Fuchs hat "
            "am Ende den ganzen Kaese gefressen, weil die Baerlein sich nicht "
            "einigen konnten."
        ),
        "steps": [
            "Fabelmerkmale: sprechende Tiere, Lehre, kurze Erzaehlung.",
            "Lehre formulieren.",
        ],
        "points": 8.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 16,
        "type": "Eigene Überschrift",
        "text": "Denke dir eine weitere Ueberschrift aus, die den Sinn der Geschichte richtig wiedergibt.",
        "answer": "Beispiel: 'Wie der Fuchs die Baeren reinlegte' oder 'Ueberlistet vom Fuchs'.",
        "steps": [
            "Sinn der Geschichte: Schwindel/Ueberlistung.",
            "Knappe, treffende Ueberschrift waehlen.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
]

NEW_KNOWLEDGE = []
