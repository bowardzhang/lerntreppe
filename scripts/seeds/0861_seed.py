EXERCISE = {
    "id": "0861",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Eichhörnchen und Grauhörnchen",
    "topic": "Leseverstehen, Sachtext, Eichhörnchen, Grauhörnchen, Marder, Habicht",
    "publisher": "CATLUX",
    "source_pdf": "0861.pdf",
    "answer_pdf": "0861 (1).pdf",
    "total_points": 40.0,
}

LESETEXT = (
    "Pelzig, possierlich, puschelig: Eichhörnchen stehen in der Beliebtheit der "
    "Menschen ganz oben. Mit ihren fingerartigen Zehen und haarigen Ohren "
    "erinnern die schreckhaften Nager an kleine Kobolde. Bekommt man sie einmal "
    "kurz zu Gesicht, begeistern sie mit tollkühnen Kletterkünsten. Leichtfüßig "
    "springen sie von Ast zu Ast, flitzen kopfüber die Baumstämme herunter, "
    "sammeln Nüsse in ihren Backentaschen und sind im nächsten Augenblick auch "
    "schon wieder im Dickicht verschwunden.\n\n"
    "Aufgrund seiner Geschicklichkeit konnte dem Eichhörnchen bislang kein "
    "anderes Tier wirklich gefährlich werden. Selbst sein ärgster Fressfeind, "
    "der Marder, zieht bei wilden Verfolgungsjagden in den Baumwipfeln am Ende "
    "meist den Schwanz ein – besonders dann, wenn sich das Eichhörnchen ganz "
    "plötzlich von einem hohen Ast in die Tiefe stürzen lässt. Dem Marder bleibt "
    "dann nichts anderes übrig, als zuzusehen, wie das Eichhörnchen – seinen "
    "Puschelschwanz als Fallschirm benutzend – auf dem Waldboden landet und mit "
    "großen Sprüngen davon hüpft.\n\n"
    "Auch vor den scharfen Augen und Krallen größerer Greifvögel, wie dem "
    "Habicht, kann das Eichhörnchen seinen Pelz meist retten. Es turnt nämlich "
    "ringsherum die Stämme der Bäume hinauf. So gelänge es noch nicht einmal "
    "einem Scharfschützen, das flinke Tierchen ins Visier zu nehmen. Warum auch? "
    "Das Zusammenleben zwischen Menschen und Eichhörnchen ist sehr friedlich. "
    "Inzwischen leben sogar mehr Eichhörnchen in städtischen Grünzonen als in "
    "Wäldern. Dennoch ist die Zukunft des europäischen Eichhörnchens ungewiss. "
    "Denn plötzlich droht die Gefahr aus den eigenen Reihen. Der 'Wolf im "
    "Eichhörnchenpelz\" ist grau, fast doppelt so groß wie sein europäischer "
    "Verwandter und sehr gefräßig. In England, wo das amerikanische Grauhörnchen "
    "im 19. Jahrhundert erstmals seine Kralle auf den europäischen Boden setzte, "
    "gibt es heute kaum noch einheimische Hörnchen. Der Hauptgrund ist, dass über "
    "70 Prozent der eingewanderten Grauhörnchen einen Virus übertragen; gegen "
    "den sie zwar selbst immun sind, an dem aber europäische Eichhörnchen "
    "innerhalb weniger Wochen sterben.\n\n"
    "Auch mit seinem Verhalten macht das amerikanische Grauhörnchen dem "
    "europäischen Ureinwohner das Leben schwer. Das europäische Eichhörnchen "
    "ist ein strikter Einzelgänger, der viel Platz für sich allein beansprucht. "
    "Das amerikanische Grauhörnchen dagegen stört sich nicht an anderer "
    "Gesellschaft. Im Gegenteil. Im Herbst macht es sich mit großer Vorliebe "
    "über die Wintervorräte seines europäischen Artgenossen her. Denn während "
    "sich das europäische Hörnchen zu dieser Jahreszeit einer Diät unterzieht "
    "und eifrig Haselnüsse für die kalten Wintermonate verbuddelt, frisst sich "
    "das amerikanische Grauhörnchen zur selben Zeit eine Fettschicht an und "
    "sucht sich dann ein warmes Plätzchen für den Winterschlaf. Das europäische "
    "Eichhörnchen aber kann nicht auf Vorrat fressen und ist im Winter auf "
    "seine zurückgelegten Bodenschätze angewiesen. Keine guten Voraussetzungen "
    "also für eine harmonische Wohngemeinschaft in den Baumwipfeln."
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Satzfortsetzungen ankreuzen",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Kreuze jeweils die passende Fortsetzung an!\n"
            "(I) Die Eichhörnchen lassen sich von einem hohen Ast in die Tiefe stürzen…\n"
            "  (a) um schneller vom Baum zu steigen.\n"
            "  (b) um Flugübungen zu machen.\n"
            "  (c) um dem Marder zu entgehen.\n"
            "  (d) um sich abzukühlen.\n"
            "(II) In England gibt es heute kaum noch Eichhörnchen…\n"
            "  (a) weil die englischen Eichhörnchen ausgewandert sind.\n"
            "  (b) weil die englischen Eichhörnchen durch einen Virus des Grauhörnchens gestorben sind.\n"
            "  (c) weil es in England nur Grauhörnchen gibt.\n"
            "  (d) weil sie gegen den Virus immun sind."
        ),
        "answer": "(I) (c) um dem Marder zu entgehen. ; (II) (b) durch Virus des Grauhörnchens gestorben.",
        "steps": ["Aus Absatz 2 und 3."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 2,
        "type": "Einzige Frage abschreiben",
        "text": "Schreibe die einzige Frage im Text genau auf!",
        "answer": "'Warum auch?'",
        "steps": ["Im 3. Absatz."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 3,
        "type": "Überschriften zuordnen",
        "text": (
            "Welche Überschrift passt zu welchem Abschnitt?\n"
            "(a) Fluchtverhalten des Eichhörnchens am Baum\n"
            "(b) Der eigentliche Hauptfeind des Eichhörnchens\n"
            "(c) Fressverhalten von Grauhörnchen und Eichhörnchen\n"
            "(d) Aussehen und Fressverhalten des Eichhörnchens"
        ),
        "answer": "(a) Absatz 3 ; (b) Absatz 2 ; (c) Absatz 4 ; (d) Absatz 1.",
        "steps": ["Inhalt jedes Absatzes prüfen."],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 4,
        "type": "Synonyme aus dem Text",
        "text": (
            "Suche jeweils ein Wort, das im Text vorkommt und eine ähnliche "
            "Bedeutung hat wie:\n"
            "putzig: ___\n"
            "Gestrüpp: ___\n"
            "Parks: ___\n"
            "Krankheitserreger: ___\n"
            "friedlich: ___"
        ),
        "answer": (
            "putzig → possierlich (süß) ; "
            "Gestrüpp → Dickicht ; "
            "Parks → städtische Grünzonen ; "
            "Krankheitserreger → Virus ; "
            "friedlich → harmonisch."
        ),
        "steps": ["Synonyme im Text finden."],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 5,
        "type": "Habicht-Schutz",
        "text": "Wie kann sich das Eichhörnchen vor dem Habicht retten? Schreibe den Satz aus dem Text genau ab!",
        "answer": "'Es turnt nämlich ringsherum die Stämme der Bäume hinauf.'",
        "steps": ["Im 3. Absatz."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 6,
        "type": "Bedeutungserklärung",
        "text": (
            "Was bedeutet:\n"
            "(a) 'Der Wolf im Eichhörnchen-Pelz ist grau' (Z. 24)\n"
            "  - Wölfe verkleiden sich als Eichhörnchen.\n"
            "  - Wölfe und Eichhörnchen sind grau.\n"
            "  - Der Pelz ähnelt dem des Wolfes.\n"
            "  - Das Eichhörnchen hat in einem Artgenossen einen Feind.\n"
            "(b) 'Keine guten Voraussetzungen für eine harmonische Wohngemeinschaft' (Z. 42)\n"
            "  - Sie vertragen sich besser am Boden.\n"
            "  - Wohngemeinschaften sind gut.\n"
            "  - Eichhörnchen und Grauhörnchen vertragen sich nicht.\n"
            "  - Sie brauchen keine Bedingungen für Wohngemeinschaften."
        ),
        "answer": (
            "(a) Das Eichhörnchen hat in einem Artgenossen einen Feind. ; "
            "(b) Eichhörnchen und Grauhörnchen vertragen sich nicht."
        ),
        "steps": ["Bildhafte Sprache deuten."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 7,
        "type": "Zeilen suchen",
        "text": (
            "Finde die folgenden Wörter im Text und notiere die Zeile!\n"
            "Ureinwohner: ___ ; Geschicklichkeit: ___ ; "
            "Wintervorräte: ___ ; Krallen: ___"
        ),
        "answer": "Ureinwohner: Z. 32 ; Geschicklichkeit: Z. 8 ; Wintervorräte: Z. 36 ; Krallen: Z. 16.",
        "steps": ["Wörter im Text suchen."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 8,
        "type": "Lückentext",
        "text": (
            "Fülle die Lücken!\n"
            "(a) Mit ihren ___ Zehen und haarigen Ohren erinnern die ___ Nager an "
            "kleine ___. (Zeilen ___, Absatz ___)\n"
            "(b) Das europäische ___ ist ein ___ Einzelgänger, der viel Platz für "
            "sich allein ___. (Zeilen ___, Absatz ___)"
        ),
        "answer": (
            "(a) fingerartigen / schreckhaften / Kobolde — Z. 2, Absatz 1. ; "
            "(b) Eichhörnchen / strikter / beansprucht — Z. 32, Absatz 4."
        ),
        "steps": ["Wörter aus dem Text einsetzen."],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 9,
        "type": "Rückwärtswörter",
        "text": (
            "Kannst du die Rückwärtswörter aus dem Text lesen?\n"
            "täiD ___ ; tsbreH ___ ; ssiwegnu ___ ; znawhcslehcsuP ___"
        ),
        "answer": "Diät ; Herbst ; ungewiss ; Puschelschwanz.",
        "steps": ["Wörter rückwärts lesen."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 10,
        "type": "Fremdwörter markieren",
        "text": (
            "Welcher Satz aus der Geschichte ist gesucht? Markiere alle Wörter, "
            "die nicht dazugehören!\n"
            "Leichtfüßig springen sie von Ast zu Ast, flitzen ständig kopfüber die "
            "Baumstämme herunter, sammeln viele Nüsse in ihren kleinen Backentaschen "
            "und sind im nächsten Augenblick auch schon wieder flink im dunklen "
            "Dickicht verschwunden."
        ),
        "answer": "Fremdwörter (zu streichen): ständig, viele, kleinen, flink, dunklen.",
        "steps": ["Mit dem Originaltext (Absatz 1) vergleichen."],
        "points": 2.5,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 11,
        "type": "Wörtliches Zitat ankreuzen",
        "text": (
            "Wie steht es wörtlich im Text? Kreuze an!\n"
            "(a) Das europäische Eichhörnchen kann nicht auf Vorrat fressen ...\n"
            "(b) Das europäische Eichhörnchen aber kann nicht auf Vorrat essen ...\n"
            "(c) Das europäische Eichhörnchen aber kann nicht auf Vorrat fressen ...\n"
            "(d) Das europäische Eichhörnchen kann aber nicht auf Vorrat fressen ..."
        ),
        "answer": "Richtig: (c) 'Das europäische Eichhörnchen aber kann nicht auf Vorrat fressen ...'",
        "steps": ["Wortlaut genau prüfen."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 12,
        "type": "Richtig oder Falsch",
        "text": (
            "Entscheide bei jedem Satz, ob die Aussage richtig oder falsch ist!\n"
            "(1) Eichhörnchen erinnern Menschen an Kobolde.\n"
            "(2) Habichte und Eichhörnchen sind Freunde.\n"
            "(3) Grauhörnchen machen im Herbst eine Fastenkur.\n"
            "(4) Eichhörnchen sammeln Nüsse in ihren Backentaschen."
        ),
        "answer": "(1) richtig ; (2) falsch ; (3) falsch ; (4) richtig.",
        "steps": ["Im Text nachprüfen."],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 13,
        "type": "Frage zu Abschnitt zuordnen",
        "text": (
            "Welche Frage wird in welchem Abschnitt beantwortet?\n"
            "(a) Können Menschen und Eichhörnchen gut zusammenleben?\n"
            "(b) Was macht das Grauhörnchen im Herbst?\n"
            "(c) Warum erwischt der Marder das Eichhörnchen nicht?"
        ),
        "answer": "(a) Absatz 3 ; (b) Absatz 4 ; (c) Absatz 2.",
        "steps": ["Inhalt der Abschnitte zuordnen."],
        "points": 1.5,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 14,
        "type": "Wohnort heute",
        "text": "Wo leben die europäischen Eichhörnchen inzwischen vermehrt und wieso?",
        "answer": (
            "Sie leben im Gegensatz zu früher nicht mehr in Wäldern, sondern in "
            "städtischen Grünzonen, da sie ein harmonisches Zusammenleben mit den "
            "Menschen haben."
        ),
        "steps": ["Aus Absatz 3."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 15,
        "type": "Feind beschreiben",
        "text": "Beschreibe das Aussehen des Feindes des europäischen Eichhörnchens und gib die Zeilennummern an!",
        "answer": (
            "Das amerikanische Grauhörnchen ist grau, fast doppelt so groß wie "
            "sein Artgenosse und sehr gefräßig. (Z. 24)"
        ),
        "steps": ["Aus Absatz 3, Z. 24."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 16,
        "type": "Harmonisches Zusammenleben",
        "text": (
            "Erkläre, was man unter einem harmonischen Zusammenleben zwischen "
            "Mensch und Eichhörnchen verstehen kann!"
        ),
        "answer": (
            "Die Menschen jagen die Eichhörnchen nicht und lassen sie in der "
            "Umgebung leben. Viele Menschen füttern die Eichhörnchen auch und "
            "erleichtern ihnen die Nahrungssuche."
        ),
        "steps": ["Eigene Erklärung."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 17,
        "type": "Verhalten Grauhörnchen",
        "text": (
            "Das europäische Eichhörnchen verbuddelt im Herbst Haselnüsse und "
            "macht eine Diät. Was dagegen macht sein feindlicher Artgenosse?"
        ),
        "answer": (
            "Das Grauhörnchen frisst sich eine Fettschicht an und sucht sich "
            "danach einen warmen Platz für seinen Winterschlaf."
        ),
        "steps": ["Aus Absatz 4."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
]

NEW_KNOWLEDGE = []
