EXERCISE = {
    "id": "2117",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Der Kuckuck",
    "topic": "Leseverstehen, Sachtext, Kuckuck, Vögel, Brutparasit, Klimawandel",
    "publisher": "CATLUX",
    "source_pdf": "2117.pdf",
    "answer_pdf": "2117 (1).pdf",
    "total_points": 24.0,
}

LESETEXT = (
    "Der Kuckuck\n\n"
    "Der große graue Vogel hat dunkle Streifen auf der Brust. Durch seine "
    "auffallende Größe kann er auf den ersten Blick auch mit einem Raubvogel "
    "verwechselt werden. Er sieht zwar ganz gewöhnlich aus, doch sein Ruf, "
    "nach dem er auch benannt wurde, ist sehr berühmt. Dieser Ruf ist so "
    "einprägsam, dass Uhrenmacher auf die Idee kamen, ihn für ihre Uhren zu "
    "nutzen. Spätestens jetzt weißt du sicherlich, dass es sich um unseren "
    "Kuckuck handelt.\n\n"
    "Der Kuckuck ist ein ziemlich komischer Vogel, denn er macht fast nichts "
    "wie andere Vögel. Er ernährt sich zum Beispiel von giftigen Raupen, "
    "andere Vögel rühren diese nicht an. Die Vorliebe für giftige, haarige "
    "Raupen ist wahrscheinlich der Grund, warum der Kuckuck seine Jungen "
    "nicht aufziehen kann, denn der frisch ausgeschlüpfte kleine Kuckuck "
    "verträgt diese Nahrung noch nicht.\n\n"
    "Vor Millionen von Jahren hat der Kuckuck sich darauf spezialisiert, "
    "seine Eier anderen Vögeln unterzuschieben. Nest bauen und brüten – das "
    "hat er verlernt. Für die Kuckuckseltern ist das kein Problem. Sie bauen "
    "kein eigenes Nest, sondern legen ihre Eier in ein fremdes ab. Mit einem "
    "heimtückischen Plan gelingt ihnen das. Der Kuckucksmann fliegt "
    "angriffslustig auf das Nest einer kleineren Vogelart zu. Wegen seiner "
    "Größe denken diese Vögel dann, sie würden von einem Raubvogel bedroht. "
    "Während sie sich in Sicherheit bringen und ihre Brutstätte verlassen, "
    "legt das Kuckucksweibchen ein Ei in das fremde Nest. Wenn das Vogelpaar "
    "nach einiger Zeit erschöpft wieder zurückkehrt, merkt es normalerweise "
    "nicht, dass ein neues Ei dazugekommen ist.\n\n"
    "Kuckucksdame und Kuckucksherr verbringen einen ruhigen Sommer, während "
    "sich die anderen Vogeleltern für das Kuckucksbaby abschuften. Die "
    "kleinen Kuckucke sind sehr gefräßig. Eine überaus empfindliche Haut "
    "haben sie auch und deshalb ertragen sie es nicht, von ihren "
    "Stiefgeschwistern berührt zu werden. So versucht das Kuckucksbaby mit "
    "aller Kraft, Eier und Stiefgeschwister aus dem Nest zu stoßen. In der "
    "Regel hat es Erfolg und so bekommt es die besten Häppchen ganz für sich "
    "alleine. Während die fremden Eltern eifrig nach Futter suchen, wächst "
    "und wächst der kleine Kuckuck und wird ungefähr dreimal so groß wie "
    "seine Stiefeltern.\n\n"
    "Der bekannte Kuckucksruf ist heute immer seltener zu hören, weil die "
    "Zahl der Kuckucke abnimmt. Deshalb haben der Naturschutzbund und der "
    "Landesbund für Vogelschutz den Kuckuck im Jahr 2008 zum Vogel des "
    "Jahres erklärt. Mit dieser Aktion wollte man auf die bedrohte Vogelart "
    "und ihre besonderen Lebensumstände aufmerksam machen. Warum aber ist "
    "unser Kuckuck in Gefahr?\n\n"
    "Der Klimawandel bewirkt, dass die meisten Zugvögel inzwischen eher aus "
    "ihren südlichen Winterquartieren in ihre nördliche Heimat zurückfliegen. "
    "Nur der Kuckuck und ein paar andere Vogelarten kümmern sich nicht um "
    "die Klimaveränderung. Er reist wie gewohnt, erst Mitte April an. Doch "
    "das kann ihm zum Verhängnis werden. Denn wenn in den fremden Vogelnestern "
    "bereits die ersten Eier ausgebrütet worden sind, kann das "
    "Kuckucksweibchen sein Ei nicht mehr unbemerkt in das fremde Nest "
    "schmuggeln."
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Bild ankreuzen",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Kreuze an, welches Bild einen Kuckuck abbildet."
        ),
        "answer": "Bild des Kuckucks ankreuzen (großer grauer Vogel mit dunklen Streifen auf der Brust).",
        "steps": ["Beschreibung aus Z. 1."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 2,
        "type": "Aussehen abschreiben",
        "text": "Schreibe den Satz aus dem Text vollständig ab, der das Aussehen des Kuckucks genau wiedergibt.",
        "answer": "Der große graue Vogel hat dunkle Streifen auf der Brust.",
        "steps": ["Z. 1."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 3,
        "type": "Synonym Nest",
        "text": "Schreibe das Wort auf, das im Text anstelle von 'Nest' verwendet wird.",
        "answer": "Brutstätte.",
        "steps": ["Z. 19 / 21."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 4,
        "type": "Wörter durchstreichen",
        "text": (
            "In jedem Satz wurde ein Wort hinzugefügt. Streiche es durch!\n"
            "(a) Wegen seiner Größe denken diese Vögel dann, sie würden von einem gefährlichen Raubvogel bedroht.\n"
            "(b) So versucht das Kuckucksbaby mit aller Kraft, Eier und Stiefgeschwister schnell aus dem Nest zu stoßen."
        ),
        "answer": "(a) 'gefährlichen' streichen ; (b) 'schnell' streichen.",
        "steps": ["Mit Originaltext vergleichen."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 5,
        "type": "Zeilenangaben",
        "text": (
            "Lies im Text nach und gib die jeweils richtige Zeile an.\n"
            "(a) In Zeile ___ liest du zum ersten Mal, wie der Vogel heißt.\n"
            "(b) In Zeile ___ wird berichtet, was der Kuckucksmann unternimmt.\n"
            "(c) In Zeile ___ erfährst du zum ersten Mal, was der Kuckuck frisst."
        ),
        "answer": "(a) Z. 5 ; (b) Z. 17 ; (c) Z. 8.",
        "steps": ["Wörter im Text suchen."],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 6,
        "type": "Wortbedeutung ankreuzen",
        "text": (
            "Was bedeutet das Wort im Text?\n"
            "(I) 'gewöhnlich' (Z. 2-3): unauffällig / ungewohnt / interessant\n"
            "(II) 'heimtückischen' (Z. 16): umständlichen / heimlichen / hinterlistigen\n"
            "(III) 'eifrig' (Z. 28-30): mühsam / abwechselnd / fleißig"
        ),
        "answer": "(I) unauffällig ; (II) hinterlistigen ; (III) fleißig.",
        "steps": ["Im Kontext deuten."],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 7,
        "type": "Zwei richtige Aussagen",
        "text": (
            "Kreuze die zwei Aussagen an, die laut Text eindeutig richtig sind.\n"
            "(1) Der Kuckuck ist ein Raubvogel von auffallender Größe.\n"
            "(2) Der Kuckuck könnte sich jederzeit ein Nest bauen, wenn er nicht zu bequem wäre.\n"
            "(3) Die Vogeleltern, die ein Kuckucksjunges großziehen, sind deutlich kleiner als ein ausgewachsenes Kuckucksjunges.\n"
            "(4) Auch andere Vogelarten richten sich nicht nach dem veränderten Klima.\n"
            "(5) Viele Uhrmacher verwenden die Federn des Kuckucks für ihre Uhren.\n"
            "(6) Jedes Jahr machen Naturschützer darauf aufmerksam, dass es immer weniger Kuckucke gibt."
        ),
        "answer": "Richtig: (3) und (4).",
        "steps": ["Im Text nachprüfen."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 8,
        "type": "Zwei Gründe Kuckucksbaby",
        "text": (
            "Warum wirft das Kuckucksbaby die anderen Eier und die Stiefgeschwister "
            "aus dem Nest? Schreibe zwei Gründe auf!"
        ),
        "answer": (
            "1. Weil es wegen seiner empfindlichen Haut die Berührung der "
            "Stiefgeschwister nicht ertragen kann. ; "
            "2. Es ist sehr gefräßig und bekommt so die besten Häppchen ganz "
            "für sich alleine."
        ),
        "steps": ["Aus Absatz 4."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 9,
        "type": "Klimawandel Problem",
        "text": (
            "Der Kuckuck hat ein Problem, wenn er erst Mitte April in seine "
            "nördliche Heimat zurückkommt. Warum? Nenne 2 Gründe."
        ),
        "answer": (
            "1. Die meisten Zugvögel fliegen jetzt schon früher in ihre nördliche "
            "Heimat zurück. ; "
            "2. Wenn in den fremden Vogelnestern bereits die ersten Eier "
            "ausgebrütet sind, kann das Kuckucksweibchen sein Ei nicht mehr "
            "unbemerkt in das fremde Nest legen."
        ),
        "steps": ["Aus dem letzten Absatz."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 10,
        "type": "Sätze verbinden",
        "text": (
            "Bilde sinnvolle Sätze (zwei Kästchen bleiben übrig).\n"
            "(a) Der Kuckuck ist ein ziemlich komischer Vogel\n"
            "(b) Das andere Vogelpaar merkt es normalerweise nicht, dass ein neues Ei im Nest liegt\n"
            "(c) Die Vorliebe für giftige Raupen ist wahrscheinlich der Grund, warum der Kuckuck seine Jungen nicht aufziehen kann\n"
            "(d) Das Kuckucksweibchen kann sein Ei nicht mehr unbemerkt schmuggeln"
        ),
        "answer": (
            "(a) → er unterscheidet sich stark von anderen Vögeln. ; "
            "(b) → wenn es später müde zum Nest zurückkommt. ; "
            "(c) → denn einem kleinen Kuckuck können sie noch nicht als Nahrung dienen. ; "
            "(d) → wenn die ersten Vogeljungen aus dem Ei geschlüpft sind."
        ),
        "steps": ["Inhaltlich passende Satzteile verbinden."],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 11,
        "type": "Pronomenbezug",
        "text": (
            "Wofür stehen die unterstrichenen Wörter?\n"
            "(a) Mit ihr wollte man auf die bedrohte Vogelart aufmerksam machen.\n"
            "(b) In der Regel hat es Erfolg."
        ),
        "answer": "(a) ihr → Aktion ; (b) es → Kuckucksbaby.",
        "steps": ["Bezugswort im Text suchen."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 12,
        "type": "Überschrift finden",
        "text": "Schreibe eine passende Überschrift auf die Zeile über dem Text.",
        "answer": "Z. B.: 'Der Kuckuck' / 'Der Kuckuck und sein Verhalten' / 'Vogel des Jahres'.",
        "steps": ["Eigene Überschrift finden."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
]

NEW_KNOWLEDGE = []
