EXERCISE = {
    "id": "0623",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Der Fuchs und die Katze",
    "topic": "Leseverstehen, Fabel, Grimm, Fuchs, Katze, Hochmut",
    "publisher": "CATLUX",
    "source_pdf": "0623.pdf",
    "answer_pdf": "0623 (1).pdf",
    "total_points": 28.0,
}

LESETEXT = (
    "Der Fuchs und die Katze (Gebrüder Grimm)\n\n"
    "Es trug sich zu, dass die Katze in einem Walde dem Herrn Fuchs begegnete. "
    "Weil sie dachte, er ist gescheit und wohl erfahren und gilt viel in der "
    "Welt, so begruesste sie ihn artig: 'Guten Tag, lieber Herr Fuchs, wie "
    "geht's? Wie steht's? Wie schlaegt ihr Euch durch in dieser teuren Zeit?'\n\n"
    "Der Fuchs, voller Hochmut, musterte die Katze von Kopf bis Fuss und "
    "ueberlegte, ob er eine Antwort geben sollte. Endlich sprach er: 'O du "
    "armseliger Bartputzer, du buntscheckiger Narr, du Hungerleider und "
    "Maeusejager, was kommt dir in den Sinn? Du unterstehst dich zu fragen, wie "
    "es mir gehe? Was hast du gelernt? Wie viel Kuenste verstehst du?' 'Ich "
    "verstehe nur eine einzige', antwortete bescheiden die Katze. 'Was für eine "
    "Kunst ist das?', fragte der Fuchs. 'Wenn die Hunde hinter mir her sind, so "
    "kann ich auf einen Baum springen und mich retten.' 'Das ist alles?', fragte "
    "der Fuchs, 'ich bin Herr über hundert Kuenste und habe ueberdies noch einen "
    "Sack voll Listen. Du jammerst mich, komm mit mir, ich will dich lehren, wie "
    "man den Hunden entgeht.'\n\n"
    "Indessen kam ein Jäger mit vier Hunden daher. Die Katze sprang behende auf "
    "einen Baum und kletterte in den Gipfel, wo Aeste und Laubwerk sie voellig "
    "verbargen. 'Bindet den Sack auf, Herr Fuchs, bindet den Sack auf!', rief "
    "ihm die Katze zu, aber die Hunde hatten ihn schon gepackt und hielten ihn "
    "fest. 'Ei, Herr Fuchs!', rief die Katze, 'Ihr bliebt mit Euren hundert "
    "Kuensten stecken. Haettet Ihr heraufklettern können wie ich, so waer's "
    "nicht um Euer Leben geschehen.'"
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Zeilen finden",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Schreibe die Zeilen auf, in denen du folgende Sätze findest:\n"
            "(a) 'Du jammerst mich, komm mit mir ...'\n"
            "(b) 'Die Katze sprang behende auf einen Baum und kletterte...'"
        ),
        "answer": (
            "(a) 'Du jammerst mich, komm mit mir ...' steht in den Zeilen 14-15. ; "
            "(b) 'Die Katze sprang behende...' steht in den Zeilen 16-17."
        ),
        "steps": [
            "Im Text die Zeilen abzaehlen.",
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
        "type": "Lückentext ergänzen",
        "text": (
            "Ergaenze mit passenden Woertern aus dem Text:\n"
            "(a) Der Fuchs, voller ___, musterte die Katze ... und ___, ...\n"
            "(b) ... aber die Hunde hatten ihn schon ___...\n"
            "(c) 'ich bin Herr über hundert ___...'"
        ),
        "answer": "(a) Hochmut / ueberlegte ; (b) gepackt ; (c) Kuenste.",
        "steps": [
            "Luecken direkt aus dem Text fuellen.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 3,
        "type": "Richtige Aussagen ankreuzen",
        "text": (
            "Kreuze die richtigen Aussagen an:\n"
            "(1) Der Fuchs war wuetend über die Katze.\n"
            "(2) Am Anfang der Geschichte denkt die Katze, der Fuchs sei sehr dumm.\n"
            "(3) Die Katze beherrscht die Kunst, die Hunde zu erschrecken.\n"
            "(4) Es kam ein Jäger mit vier Hunden vorbei.\n"
            "(5) Der Fuchs hat einen echten Sack bei sich.\n"
            "(6) Die Katze klettert am Schluss auf einen Baum.\n"
            "(7) Der Fuchs verliert am Ende sein Leben."
        ),
        "answer": "Richtig: (4), (6), (7).",
        "steps": [
            "(1) F: der Fuchs war hochmutig, nicht wuetend.",
            "(2) F: Die Katze dachte, der Fuchs sei sehr gescheit.",
            "(3) F: Die Katze kann auf Baeume klettern.",
            "(5) F: 'Sack voll Listen' ist eine Redewendung.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 4,
        "type": "Schimpfwörter nennen",
        "text": "Nenne die vier Schimpfwoerter, mit denen der Fuchs die Katze beschimpft!",
        "answer": (
            "1. armseliger Bartputzer ; "
            "2. buntscheckiger Narr ; "
            "3. Hungerleider ; "
            "4. Maeusejager."
        ),
        "steps": [
            "Direkt aus dem Text des Fuchses.",
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
        "type": "Adjektive und Wortart",
        "text": (
            "Kreuze an, welche Woerter zur Katze passen, und bestimme die Wortart:\n"
            "(a) hoeflich\n"
            "(b) dumm\n"
            "(c) hinterlistig\n"
            "(d) bescheiden"
        ),
        "answer": "Richtig: (a) hoeflich und (d) bescheiden. Wortart: Eigenschaftswoerter (Adjektive).",
        "steps": [
            "Die Katze begruesst den Fuchs artig und antwortet bescheiden.",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 6,
        "type": "Adjektive zum Fuchs",
        "text": "Schreibe drei Woerter auf, die zum Verhalten des Fuchses passen!",
        "answer": "Z. B.: angeberisch, hochmutig, arrogant (auch: frech, eitel, ueberheblich).",
        "steps": [
            "Aus dem Verhalten des Fuchses erschliessen.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 7,
        "type": "Synonym finden",
        "text": "Ersetze 'behende' durch ein anderes passendes Wort!",
        "answer": "flink, schnell, geschickt, gewandt, rasch (beliebiges Synonym).",
        "steps": [
            "'behende' bedeutet: schnell und geschickt.",
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
        "type": "Ueberlegenheit erklären",
        "text": (
            "Wie kam es dazu, dass am Ende der Geschichte die Katze dem Fuchs "
            "ueberlegen war? Erklaere in ganzen Sätzen!"
        ),
        "answer": (
            "Die Katze hat nicht mit hundert Kuensten geprahlt, sondern besass "
            "die richtige Faehigkeit: auf einen Baum klettern zu können. So "
            "konnten die Hunde sie nicht fangen, waehrend der Fuchs trotz seiner "
            "vielen Listen hilflos war."
        ),
        "steps": [
            "Eine praktische Kunst > hundert unnuetze Listen.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 9,
        "type": "Fabelmerkmal erkennen",
        "text": "Woran erkennst du, dass es sich tatsaechlich um eine Fabel handelt?",
        "answer": (
            "Z. B.: Die Personen sind Tiere und die Tiere können sprechen. "
            "Die Tiere haben menschliche Eigenschaften (Hochmut, Bescheidenheit). "
            "Die Geschichte hat eine Lehre (Moral): Prahlerei hilft nichts."
        ),
        "steps": [
            "Fabelmerkmal: sprechende Tiere + menschliche Eigenschaften + Moral.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
]

NEW_KNOWLEDGE = []
