EXERCISE = {
    "id": "0665",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Der Wolf und der Fuchs",
    "topic": "Leseverstehen, Fabel, Wolf, Fuchs, Gier, Nimmersatt",
    "publisher": "CATLUX",
    "source_pdf": "0665.pdf",
    "answer_pdf": "0665 (1).pdf",
    "total_points": 24.0,
}

LESETEXT = (
    "Der Wolf und der Fuchs\n\n"
    "Der Wolf hatte den Fuchs bei sich. Was der Wolf wollte, das musste der Fuchs "
    "tun, weil er schwächer war. Der Fuchs wäre gern den Herrn los geworden.\n\n"
    "Es trug sich zu, dass sie beide durch den Wald gingen. Da sprach der Wolf: "
    "'Rotfuchs, schaff mir was zu fressen herbei, oder ich fresse dich selber auf.' "
    "Der Fuchs antwortete: 'Ich weiß einen Bauernhof, wo zwei Lämmlein sind. "
    "Hast du Lust, so wollen wir uns eins holen.\" Dem Wolf war das recht. Sie "
    "gingen hin, und der Fuchs stahl das eine Lämmlein, brachte es dem Wolf und "
    "schlich davon. Da fraß es der Wolf auf, war damit aber noch nicht zufrieden, "
    "sondern wollte das andere auch noch dazu haben. Er ging selbst, es zu holen. "
    "Weil der Wolf aber so ungeschickt war, hört ihn die Mutter des Lämmleins. "
    "Sie fing entsetzlich an zu schreien, so dass die Bauern herbeigelaufen kamen. "
    "Da fanden sie den Wolf und schlugen ihn so erbärmlich, dass er hinkend und "
    "heulend bei dem Fuchs ankam. 'Da hast du mich schön angeführt', sprach er, "
    "'ich wollte das andere Lamm holen. Da haben mich die Bauern erwischt und "
    "haben mich weich geschlagen.\" Der Fuchs antwortete: 'Warum bist du auch so "
    "ein Nimmersatt?\"\n\n"
    "Am anderen Tag gingen sie wieder ins Feld. Wieder sprach der gierige Wolf: "
    "'Rotfuchs, schaff mir was zu fressen herbei, oder ich fresse dich selber auf!' "
    "Da antwortete der Fuchs: 'Ich weiß ein Bauernhaus. Da backt die Frau heute "
    "Abend Pfannkuchen. Wir wollen uns einige holen.\" Sie gingen hin, und der "
    "Fuchs schlich ums Haus herum, guckte und schnupperte so lange, bis er "
    "ausfindig gemacht hatte, wo die Schüssel mit den Leckereien stand. Vorsichtig "
    "zog er sechs Pfannkuchen herab und brachte sie dem Wolf. 'Da hast du zu "
    "fressen\", sprach er zu ihm und ging seiner Wege. Der Wolf hatte die "
    "Pfannkuchen in einem Augenblick verschlungen und sprach: 'Sie schmecken "
    "nach mehr\", ging hin und riss die ganze Schüssel herunter, so dass sie in "
    "Stücke zersprang. Da gab es einen gewaltigen Lärm. Die Bäuerin stürzte "
    "heraus, entdeckte den Wolf und begann zu schreien. Die Leute eilten herbei "
    "und schlugen ihn. Mit zwei lahmen Beinen kam er laut heulend zum Fuchs in "
    "den Wald hinaus. 'Was hast du mich garstig angeführt!', rief er, 'die Bauern "
    "haben mich erwischt und mir die Haut gegerbt.\" Der Fuchs antwortete: 'Warum "
    "bist du auch so ein Nimmersatt?\"\n\n"
    "Am dritten Tag, als der Wolf noch hinkte, sprach er doch wieder: 'Rotfuchs, "
    "schaff mir was zu fressen herbei, oder ich fress dich selber auf.\" Der Fuchs "
    "antwortete: 'Ich weiß einen Mann, der hat geschlachtet, und das gesalzene "
    "Fleisch liegt in einem Fass im Keller. Das wollen wir holen.\" 'Ja', sprach der "
    "Wolf, 'aber ich will gleich mitgehen, damit du mir hilfst, wenn ich nicht fort "
    "kann.\" 'Meinetwegen', sagte der Fuchs und zeigte ihm den Weg, auf dem sie "
    "endlich in den Keller gelangten. Da war nun Fleisch im Überfluss. Der Wolf "
    "machte sich gleich daran und sprach: 'Bis ich aufhöre, hat´s Zeit.' Der Fuchs "
    "ließ es sich auch gut schmecken, blickte aber überall umher und lief oft zu dem "
    "Loch, durch das sie gekommen waren. Er versuchte, ob sein Leib noch schmal "
    "genug sei, durchzuschlüpfen. Der Wolf sprach: 'Lieber Fuchs, sag mir, warum "
    "rennst du so hin und her und springst hinaus und herein?\" 'Ich muss doch "
    "sehen, ob niemand kommt\", antwortete der Listige, 'friss nur nicht zu viel.' "
    "Da sagte der Wolf: 'Ich gehe nicht eher fort, als bis das Fass leer ist.'\n\n"
    "Indessen kam der Bauer, der im Keller Lärm gehört hatte. Als der Fuchs ihn "
    "sah, war er mit einem Satz zum Loch draußen. Der Wolf wollte nach, aber er "
    "hatte sich so dick gefressen, dass er nicht mehr hindurch konnte, sondern "
    "stecken blieb. Da kam der Bauer mit einem Knüppel und schlug ihn tot. Der "
    "Fuchs aber sprang in den Wald und war froh, dass er den Nimmersatt los war."
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Grund nennen",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Warum musste der Fuchs tun, was der Wolf ihm sagte? "
            "Beantworte in einem Satz!"
        ),
        "answer": "Er war schwächer.",
        "steps": [
            "Direkt aus dem Text: 'weil er schwächer war.'",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 2,
        "type": "Wünsche und Drohung des Wolfes",
        "text": (
            "Der Wolf lässt sich vom Fuchs bedienen!\n"
            "(a) Was verlangt der Wolf vom Fuchs? Beantworte in einem Satz!\n"
            "(b) Womit droht der Wolf dem Fuchs, sollte er ihm seinen Wunsch nicht erfüllen? "
            "Beantworte in einem Satz!\n"
            "(c) Wie oft richtete der Wolf seinen Wunsch an den Fuchs? Gib die Zeilen an!"
        ),
        "answer": (
            "(a) Hole mir was zum Fressen oder ich fresse dich selber. ; "
            "(b) Er würde den Fuchs fressen. ; "
            "(c) 3 mal — Zeilen: (3–4), (22), (37–38)."
        ),
        "steps": [
            "(a) Forderung des Wolfes: 'schaff mir was zu fressen herbei'.",
            "(b) Drohung: 'oder ich fresse dich selber auf.'",
            "(c) Dreimal wiederholt: am ersten, zweiten und dritten Tag.",
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
        "type": "Fressen benennen",
        "text": (
            "Welches Fressen besorgt der Fuchs dem Wolf am … (Stichpunkte)\n"
            "(a) ...ersten Tag?\n"
            "(b) ...zweiten Tag?"
        ),
        "answer": (
            "(a) Ein Lämmlein. ; "
            "(b) Sechs Pfannkuchen."
        ),
        "steps": [
            "(a) 'der Fuchs stahl das eine Lämmlein'.",
            "(b) 'zog er sechs Pfannkuchen herab'.",
        ],
        "points": 1.5,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 4,
        "type": "Warum ertappt",
        "text": (
            "Warum wird der Wolf am zweiten Tag beim Stehlen ertappt? "
            "Beantworte in einem Satz!"
        ),
        "answer": (
            "Die Bäuerin hat ihn gesehen und geschrien, nachdem der Wolf vor Gier "
            "die ganze Schüssel runtergerissen hat und dies einen furchtbaren Lärm "
            "verursacht hat."
        ),
        "steps": [
            "Wolf reißt die Schüssel herunter → Lärm → Bäuerin kommt heraus.",
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
        "type": "Strafe unterstreichen",
        "text": (
            "Wie wird der Wolf am zweiten Tag bestraft? "
            "Unterstreiche die Stelle im Text grün!"
        ),
        "answer": (
            "Textstelle zum Unterstreichen: "
            "'Die Leute eilten herbei und schlugen ihn. Mit zwei lahmen Beinen "
            "kam er laut heulend zum Fuchs in den Wald hinaus.'"
        ),
        "steps": [
            "Nach dem Lärm: 'Die Leute eilten herbei und schlugen ihn.'",
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
        "type": "Wortbedeutung erklären",
        "text": (
            "Der Fuchs fragte den Wolf mehrmals: 'Warum bist du auch so ein Nimmersatt?' "
            "Was ist damit gemeint?"
        ),
        "answer": "Der Wolf konnte nie genug bekommen.",
        "steps": [
            "Nimmersatt = jemand, der nie satt wird / nie genug hat.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 7,
        "type": "Grund fürs Mitgehen",
        "text": (
            "Warum will der Wolf am dritten Tag gemeinsam mit dem Fuchs zum Stehlen gehen? "
            "Beantworte in einem Satz!"
        ),
        "answer": "Der Fuchs sollte ihm helfen, falls sie erwischt werden.",
        "steps": [
            "'damit du mir hilfst, wenn ich nicht fort kann.'",
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
        "type": "Fuchs und das Loch",
        "text": (
            "Der Wolf wundert sich, warum der Fuchs so oft zum Loch läuft.\n"
            "(a) Wie erklärt das der Fuchs?\n"
            "(b) Warum läuft er tatsächlich zum Loch?"
        ),
        "answer": (
            "(a) Er muss sehen, ob niemand kommt. ; "
            "(b) Um zu sehen, ob er noch durch das Loch hindurch passt."
        ),
        "steps": [
            "(a) Lüge des Fuchses: 'Ich muss doch sehen, ob niemand kommt.'",
            "(b) Wahrheit: 'Er versuchte, ob sein Leib noch schmal genug sei, durchzuschlüpfen.'",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 9,
        "type": "Keller verlassen",
        "text": (
            "(a) Wann hat der Wolf zunächst vor, den Keller zu verlassen? "
            "Unterstreiche im Text rot!\n"
            "(b) Warum will er dann doch eher fort? Beantworte in einem Satz!"
        ),
        "answer": (
            "(a) Textstelle: 'Ich gehe nicht eher fort, als bis das Fass leer ist.' ; "
            "(b) Er hört den Bauer und er will dem Fuchs hinterher."
        ),
        "steps": [
            "(a) 'Bis ich aufhöre, hat´s Zeit.' / 'als bis das Fass leer ist.'",
            "(b) Der Bauer kommt in den Keller.",
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
        "type": "Fuchs hilft nicht",
        "text": (
            "Der Fuchs hilft dem Wolf nicht, als dieser im Loch festsitzt! "
            "Warum tut er das? Begründe deine Meinung mit eigenen Worten!"
        ),
        "answer": "Er will den Wolf nicht mehr haben / er ist froh, ihn los zu sein.",
        "steps": [
            "'Der Fuchs aber sprang in den Wald und war froh, dass er den Nimmersatt los war.'",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 11,
        "type": "Sätze im Text erkennen",
        "text": (
            "Welche Sätze stehen genauso im Text? Kreuze an!\n"
            "(1) Der Fuchs wäre gern den Herrn los geworden.\n"
            "(2) Dem Wolf war es recht.\n"
            "(3) Die Leute eilten herbei und schlugen ihn.\n"
            "(4) Da ist nur Fleisch im Überfluss.\n"
            "(5) Indessen kam der Bauer, der im Keller Lärm gehört hatte."
        ),
        "answer": (
            "Richtig: (1), (3), (5). ; "
            "(2) falsch: im Text 'Dem Wolf war das recht.' ; "
            "(4) falsch: im Text 'Da war nun Fleisch im Überfluss.'"
        ),
        "steps": [
            "Genauen Wortlaut im Text nachprüfen.",
        ],
        "points": 2.5,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 12,
        "type": "Textsorte und Moral",
        "text": (
            "Das war eine aufregende Futtersuche!\n"
            "(a) Wie nennt man diese Art der Geschichte?\n"
            "(b) Nenne einen Beweis, an dem du es gemerkt hast! (Satz)\n"
            "(c) Meistens kann man aus dieser Art von Geschichten etwas lernen. "
            "Was meinst du, ist es in dieser Geschichte? "
            "Begründe deine Meinung mit eigenen Worten (Satz)."
        ),
        "answer": (
            "(a) Fabel. ; "
            "(b) Die Tiere können sprechen und denken / die Tiere haben menschliche "
            "Eigenschaften / der Leser erhält eine Lehre (Moral). ; "
            "(c) Es kommt nicht immer auf die Stärke an, sondern auf die Intelligenz / "
            "Gier führt ins Verderben."
        ),
        "steps": [
            "(a) Fabel: kurze Erzählung mit Tieren und Moral.",
            "(b) Tiere sprechen und handeln wie Menschen.",
            "(c) Moral aus dem Verhalten von Wolf und Fuchs ableiten.",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
]

NEW_KNOWLEDGE = []
