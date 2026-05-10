EXERCISE = {
    "id": "0533",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Die kranke Prinzessin",
    "topic": "Leseverstehen, Märchen, Prinzessin, Hexen, Heilung",
    "publisher": "CATLUX",
    "source_pdf": "0533.pdf",
    "answer_pdf": "0533 (1).pdf",
    "total_points": 24.0,
}

LESETEXT = (
    "Die kranke Prinzessin (Italienisches Märchen)\n\n"
    "Es war einmal eine Hauptstadt eines großen Reiches, in der herrschte "
    "grosse Trauer. Kam ein Fremder und fragte nach der Ursache, so gaben ihm "
    "die Einwohner zur Antwort, die schoene und einzige Tochter ihres geliebten "
    "Königs liege schwer krank danieder - sie ruehre sich nicht mehr und esse "
    "und trinke nichts, so dass man nur aus dem schwachen Atem entnehmen koenne, "
    "sie sei noch am Leben. Die Aerzte seien schon zu Hunderten gerufen worden "
    "und haetten Tausende von Mitteln versucht, aber alles sei umsonst. Und "
    "wenn der Fremde dies gehoert hatte, so brauchte er nur noch an den "
    "Strassenecken stehen zu bleiben und zu lesen: Da stand ueberall gedruckt, "
    "der König wolle seine Tochter demjenigen zur Frau geben, der sie retten "
    "wuerde - und damit niemand an der Richtigkeit dieses Versprechens zweifle, "
    "hatte der König selbst seine Unterschrift beigefuegt.\n\n"
    "Fern von der Hauptstadt wanderte ein Juengling seiner Wege. Er war gar "
    "sittsam und schoen gewachsen mit frischroten Wangen und froehlichem Sinne, "
    "obwohl er elternlos in der Welt allein stand. Eines Tages geriet er in "
    "einen Wald, verirrte sich und fand keinen Ausweg. Abends sah er neben "
    "einem großen Baum eine Einsiedlerklause. Er bat den alten weissbaertigen "
    "Einsiedler um Nachtherberge. Dieser sagte: 'Recht gerne, allein ich habe "
    "über meiner Klause nur einen Dachboden mit weichem Mooslager, wo du dich "
    "hinlegen kannst. Da magst du wohl weich schlafen, aber ich will dir auch "
    "sagen, dass da schon Mancher abends auf der Leiter hinaufgestiegen und "
    "morgens nicht wieder zurueckgekommen ist.' 'Ich fuerchte mich nicht', sagte "
    "der Juengling, 'ich hab ein reines Gewissen.' Der Einsiedler teilte mit dem "
    "Gaste den kaerlichen Abendimbiss aus einem Kanten Brot und einem Kruge "
    "schlechten lauen Regenwassers, dann fuehrte er ihn zur Leiter, wo der "
    "Juengling hinaufstieg und müde wie er war, bald einschlief.\n\n"
    "Um Mitternacht erwachte er. Auf dem großen Baum neben der Klause sassen "
    "viele Hexen und hatten sich gar viel zu erzaehlen. 'Aber wo bleibt denn "
    "heute unsere Pantoffel?', fragten mehrere. Und sogleich erschien auch die "
    "gerufene gar kleine und haessliche Hexe und erzaehlte mit boshafter "
    "Schadenfreude, wie sie in der Stadt die Tochter des Königs so behext habe, "
    "dass sie wohl bald sterben muesse.\n\n"
    "'Und waere denn gar kein Mittel mehr?', fragten die anderen. 'Oh ja', "
    "erwiderte die Kleine. 'Man muss nur diesen Baum hier neben der Klause "
    "ausgraben und eine Wurzel davon in dem Wasser der Quelle sieden, die unter "
    "dem Baum fliesst. Gaebe man dieses Wasser dann der Prinzessin zu trinken, "
    "wuerde sie noch in derselben Stunde gesund sein.' Sie sprachen noch vieles, "
    "bis im Osten der Tag graute. Dann flogen sie schwirrend davon.\n\n"
    "Der Juengling hatte sich alles wohl gemerkt. Er versprach dem Einsiedler "
    "eine reiche Quelle, wenn er ihm erlaube, jenen Baum vor der Klause "
    "auszugraben. Der Alte gab nach. Bald fiel der Baum um. Waehrend der Baum "
    "noch fiel, sprang auch schon eine volle reiche Quelle frischen Trinkwassers "
    "empor. Der Juengling schnitt einige Wurzelenden ab, liess sich ein "
    "Flaeschchen geben, fuellte es mit Wasser, verbarg beides an seinem Leibe "
    "und machte sich auf den Weg.\n\n"
    "Am Morgen des dritten Tages stand er an der Treppe der Königssburg. Der "
    "König liess ihn vor und gestattete ihm den Heilungsversuch. Der Juengling "
    "liess sich in die Küche führen, tat was er zu tun hatte, trat in das "
    "Zimmer der Kranken und flosste ihr einige Tropfen des Wunderwassers in den "
    "Mund. Sogleich schlug sie die Augen auf und hatte bald frisch und gesund "
    "ihr Schmerzenslager verlassen.\n\n"
    "Der König hielt sein Versprechen um so lieber, je mehr der Juengling auch "
    "der Prinzessin gefiel, und bald wurde eine so lustige Hochzeit gehalten, "
    "wie im ganzen weiten Reiche nie eine war."
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Fragen in ganzen Sätzen",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Beantworte in ganzen Sätzen:\n"
            "(a) Was ist der einzige Hinweis dafuer, dass die Prinzessin noch am "
            "Leben ist?\n"
            "(b) Was verspricht der König demjenigen, der seine Tochter heilen kann?\n"
            "(c) Wo laesst der Einsiedler den Juengling schlafen?\n"
            "(d) Welche wichtige Information erhaelt der Juengling, als er das "
            "Gespraech der Hexen belaauscht?"
        ),
        "answer": (
            "(a) Der einzige Hinweis ist der schwache Atem der Prinzessin. ; "
            "(b) Der König verspricht demjenigen, der sie heilen kann, seine "
            "Tochter zur Frau. ; "
            "(c) Auf seinem vermoosten Dachboden. ; "
            "(d) Er erfaehrt, mit welchem Mittel man die Prinzessin heilen kann "
            "(Wurzel des Baumes in Quellwasser sieden)."
        ),
        "steps": [
            "Alle vier Teile im Text nachlesen.",
        ],
        "points": 8.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 2,
        "type": "Im Text unterstreichen",
        "text": (
            "Unterstreiche im Text in den richtigen Farben:\n"
            "(rot) Warum hat der König auf den Plakaten seine Unterschrift beigefuegt?\n"
            "(blau) Aus was besteht der Abendimbiss des Einsiedlers?\n"
            "(gelb) Wie sieht die Hexe Pantoffel aus?\n"
            "(gruen) Wie viel von der Medizin trinkt die Prinzessin?"
        ),
        "answer": (
            "Rot: '...damit niemand an der Richtigkeit dieses Versprechens zweifle.' ; "
            "Blau: 'aus einem Kanten Brot und einem Kruge schlechten lauen Regenwassers.' ; "
            "Gelb: 'gar kleine und haessliche Hexe.' ; "
            "Gruen: 'einige Tropfen des Wunderwassers.'"
        ),
        "steps": [
            "Stellen im Text farblich markieren.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 3,
        "type": "Satz ankreuzen",
        "text": (
            "Kreuze an, welcher Satzausschnitt tatsaechlich im Text vorkommt:\n"
            "(a) Er war gar sittsam und schoen gewachsen mit frischroten Lippen "
            "und froehlichem Sinne, obwohl er elternlos in der Welt allein stand...\n"
            "(b) Er war gar sittsam und schoen gewachsen mit frischroten Wangen "
            "und froehlichem Sinne, obwohl er elternlos in der Welt allein stand...\n"
            "(c) Er war gar sittsam und schoen gewachsen mit frischroten Wangen "
            "und froehlichem Sinne, obwohl er elternlos in der Welt stand..."
        ),
        "answer": "Richtig: (b).",
        "steps": [
            "Wortlaut genau pruefen: 'Wangen' (nicht Lippen), 'allein' nicht vergessen.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 4,
        "type": "Richtige Aussagen ankreuzen",
        "text": (
            "Kreuze an, was richtig ist:\n"
            "(1) In der Hauptstadt herrschte einmal grosse Freude.\n"
            "(2) Der Einsiedler befuerchtet, dass der Juengling die Nacht auf "
            "dem Dachboden nicht ueberleben könnte.\n"
            "(3) Pantoffel ist in diesem Märchen der Name einer Hexe.\n"
            "(4) Der Juengling erwacht, weil er laute Schreie und Gebruell hoert.\n"
            "(5) Der Juengling braucht vier Tage, bis er an der Königssburg ankommt.\n"
            "(6) Die Aerzte sind zu Tausenden gerufen worden und haben Hunderte "
            "von Mitteln versucht.\n"
            "(7) Der Juengling hat keine Angst auf dem Dachboden zu schlafen, "
            "weil er glaubt wegen seines reinen Gewissens koenne ihm nichts passieren.\n"
            "(8) Als die Prinzessin aufwacht, gefaellt ihr der Juengling nicht."
        ),
        "answer": "Richtig: (2), (3), (7).",
        "steps": [
            "(1) F: grosse Trauer, nicht Freude.",
            "(4) F: Er hoerte Fluesstern und Kichern.",
            "(5) F: drei Tage.",
            "(6) F: umgekehrt: zu Hunderten / Tausende Mittel.",
            "(8) F: der Juengling gefiel ihr.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 5,
        "type": "Fragen in ganzen Sätzen",
        "text": (
            "Antworte in ganzen Sätzen:\n"
            "(a) Was braucht der Juengling, um die Medizin für die Prinzessin "
            "herzustellen?\n"
            "(b) Wie könnte sich der König fühlen, als seine Tochter wieder "
            "gesund aufwacht?\n"
            "(c) Ist der Einsiedler ein grosszuegiger Mensch? Begruende deine Meinung!"
        ),
        "answer": (
            "(a) Er braucht eine Wurzel vom Baum neben der Klause und Wasser der "
            "Quelle, die unter dem Baum fliesst. ; "
            "(b) Er könnte sich sehr gluecklich und erleichtert fühlen. ; "
            "(c) Ja, er ist grosszuegig; er hat den Juengling bei sich schlafen "
            "lassen und ihm geholfen, den Baum auszugraben."
        ),
        "steps": [
            "(a) Aus dem Hexengespraech: Wurzel + Quellwasser.",
            "(b) Eigene Schluessfolgerung.",
            "(c) Begruendung aus dem Text.",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 6,
        "type": "Märchenmerkmale nennen",
        "text": "Nenne 3 Merkmale, an denen du erkennst, dass es sich um ein Märchen handelt.",
        "answer": (
            "Z. B.: (1) Die Geschichte beginnt mit 'Es war einmal'. ; "
            "(2) Es kommen uebernatuerliche Wesen vor (Hexen). ; "
            "(3) Die Geschichte hat ein gutes Ende."
        ),
        "steps": [
            "Typische Maerchenmerkmale: 'Es war einmal', Zauberei, gutes Ende.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
]

NEW_KNOWLEDGE = []
