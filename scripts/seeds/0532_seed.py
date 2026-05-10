EXERCISE = {
    "id": "0532",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Reiter, Retter, Ritter – Das Rittertum im Mittelalter",
    "topic": "Leseverstehen, Sachtext, Ritter, Mittelalter, Geschichte",
    "publisher": "CATLUX",
    "source_pdf": "0532.pdf",
    "answer_pdf": "0532 (1).pdf",
    "total_points": 20.0,
}

LESETEXT = (
    "Reiter, Retter, Ritter – Wie entstand das Rittertum im Mittelalter?\n\n"
    "Das Rittertum im Mittelalter in Europa umfasst in etwa die Zeit vom Jahr "
    "1000 bis zum Jahr 1500. In mehr als fünf Jahrhunderten wurden Maenner "
    "von meist niederem Adel zum Ritter geschlagen, Kriege und Kreuzzuege "
    "gefuehrt, Burgen oder wie in Spanien, Kastelle gebaut.\n\n"
    "In Frankreich heißen die Ritter 'Monsieur', in Spanien 'Don', in "
    "Deutschland 'Herr' und in England 'Sir'. In Asien wurden die japanischen "
    "Ritter 'Samurai' genannt.\n\n"
    "Der Ritterstand bildete sich zu einer Zeit, als Europa in viele "
    "Königreiche aufgeteilt war, die heftige Kriege um jeden Zipfel Land "
    "fuehrten. Die Kriege um Laendereien wurden mit Reitern und Fussoldaten "
    "gefuehrt; die berittenen Soldaten waren dem Fussheer weit ueberlegen.\n\n"
    "Da der Reiter mit seinem Pferd und eigenen Waffen kaempfen musste, "
    "stammten diese Maenner aus adligen Familien, die das dafuer noetige Geld "
    "aufbringen konnten.\n\n"
    "Aus dem bewaffneten Reiterstand entwickelte sich im Laufe der Zeit das "
    "Rittertum mit seiner eigenen Lebensweise und einem Ehrenkodex.\n\n"
    "Drei mal sieben Jahre – der lange Weg vom Knaben zum Ritter\n\n"
    "Kein adliger Junge wurde als Ritter geboren, zum Ritter wurden Jungen in "
    "21 Jahren erzogen. Hoehepunkt war der Empfang der Ritterwuerde durch drei "
    "Schlaege mit dem flachen Schwert auf die Schultern und dem Schwur des "
    "Rittereides.\n\n"
    "Von Geburt bis zum siebten Lebensjahr lebte der Sohn eines Adligen auf "
    "der elterlichen Burg. Mit sieben Jahren wurde er dann auf eine fremde Burg "
    "gebracht. Als Edelknabe wurde er mit hoefischer Sitte, guten Manieren, "
    "biblischer Geschichte, Musik und Gesang vertraut gemacht. Das Erlernen "
    "von Lesen und Schreiben war eher nicht ueblich.\n\n"
    "Mit 14 Jahren wurde der junge Ritteranwaerter zum Schildknaben ernannt. "
    "Damit begann der dritte und haerteste Teil der Ausbildung. Der Knappe war "
    "für die Ruestung und Waffen seines Herrn verantwortlich.\n\n"
    "Hatte der junge Knappe endlich das 21. Lebensjahr vollendet, wurde er in "
    "den Ritterstand erhoben. Er benoeligte jede Menge Geld für die erste "
    "Ruestung - sie kostete in etwa soviel wie ein Bauernhof. Er benoeligte "
    "neben einem Auge 'wie ein Luchs', einem Herz 'wie ein Loewe', der "
    "Tapferkeit 'eines Ebers' und dem Mut 'eines Tigers' auch den Rittereid.\n\n"
    "Den Tag und die Nacht vor der Zeremonie verbrachte der Knappe fastend und "
    "betend. Sein zukuenftiger Herr ueberreichte ihm einen Guertel mit einem "
    "geweihten Ritterschwert. Feierlich kniete der junge Mann vor seinem Herrn "
    "nieder, der ihm den Eid abnahm:\n\n"
    "'Ich, Hartmut von Braunfels, gelobe stets die Wahrheit zu sagen, das "
    "Recht zu wahren, Gott, die Schwachen, die Wehrlosen, die Witwen und "
    "Waisen zu schuetzen, allen gegenueber hoeflich, freimutig und grosszuegig "
    "zu sein, stets meinem Herrn und Kaiser zu dienen, nie im Kampf vor einem "
    "Feind zu fliehen, das Boese immer zu bekaempfen.'\n\n"
    "Nach diesem Schwur erhielt er die drei Schwertschlaege. Noch an diesem Tag "
    "erhielt der junge Ritter ein Pferd als Geschenk. Ab diesem Tag durfte er "
    "im Turnier selbst mitkaempfen und konnte ein Lehen erhalten."
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Fragen in ganzen Sätzen",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Beantworte in ganzen Sätzen:\n"
            "(a) Wann entstand das Rittertum in Europa?\n"
            "(b) Warum stammten die Reiter einer Armee meist aus adligen Familien?\n"
            "(c) Woraus entwickelte sich das Rittertum im Laufe der Zeit?\n"
            "(d) Wie sah die Zeremonie aus, wenn ein Ritter die Ritterwuerde erhielt?"
        ),
        "answer": (
            "(a) Das Rittertum entstand um das Jahr 1000 und dauerte bis etwa 1500. ; "
            "(b) Weil diese genug Geld hatten; der Reiter musste mit eigenem Pferd "
            "und eigenen Waffen kaempfen. ; "
            "(c) Das Rittertum entwickelte sich aus dem bewaffneten Reiterstand. ; "
            "(d) Der zukuenftige Ritter erhielt drei Schlaege mit dem flachen "
            "Schwert auf die Schulter und musste den Rittereid schworen."
        ),
        "steps": [
            "Alle vier Teile im Text nachlesen.",
        ],
        "points": 6.0,
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
            "(rot) Wie viele Jahre dauerte die Ausbildung zum Ritter?\n"
            "(blau) Wie heißen die Ritter in Japan?\n"
            "(gelb) Welchen Eid legte Hartmut von Braunfels ab?\n"
            "(gruen) Welche Geschenke machte der zukuenftige Herr seinem Ritter?"
        ),
        "answer": (
            "Rot: 21 Jahre. ; "
            "Blau: Samurai. ; "
            "Gelb: Der Rittereid ('Ich, Hartmut von Braunfels, gelobe ...'). ; "
            "Gruen: Guertel mit Ritterschwert und Pferd."
        ),
        "steps": [
            "Im Text markieren und auflisten.",
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
            "(a) Dazu benoeligte er neben einem Auge 'wie ein Luchs', einem Herz "
            "'wie ein Loewe', der Tapferkeit 'eines Ebers' und dem Mut 'eines Tigers', ...\n"
            "(b) Dazu benoeligte er neben den Augen 'wie ein Luchs', dem Herz "
            "'wie ein Loewe', der Tapferkeit 'eines Ebers' und dem Mut 'eines Tigers', ...\n"
            "(c) Dazu benoeligte er neben einem Auge 'wie ein Fuchs', einem Herz "
            "'wie ein Loewe', der Tapferkeit 'eines Ebers' und dem Mut 'eines Tigers', ..."
        ),
        "answer": "Richtig: (a).",
        "steps": [
            "Wortlaut genau pruefen: 'Luchs' (nicht Fuchs), 'einem Auge' (nicht 'den Augen').",
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
        "type": "Reihenfolge ordnen",
        "text": (
            "Bringe die Ausbildungsstufen durch Nummerieren in die richtige Reihenfolge:\n"
            "___ Schildknappe\n"
            "___ Edelknabe\n"
            "___ Sohn eines Adligen\n"
            "___ Ritter"
        ),
        "answer": "1. Sohn eines Adligen ; 2. Edelknabe ; 3. Schildknappe ; 4. Ritter.",
        "steps": [
            "Reihenfolge im Text: Geburt - 7 Jahre - 14 Jahre - 21 Jahre.",
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
        "type": "Richtig oder falsch ankreuzen",
        "text": (
            "Kreuze an, was richtig (R) oder falsch (F) ist:\n"
            "(1) Die meisten Ritter konnten lesen und schreiben.\n"
            "(2) In Spanien hiessen die Ritter 'Don'.\n"
            "(3) Europa war damals in viele Königreiche aufgeteilt.\n"
            "(4) Die Ausbildung eines Fussoldaten dauerte länger als die eines Reiters.\n"
            "(5) Die Ritter hatten einen eigenen Ehrenkodex.\n"
            "(6) Nur Könige konnten die Zeremonie der Ritterwuerde durchfuehren.\n"
            "(7) Ein Ritter in der Ausbildung lebte weiterhin bei seinen Eltern.\n"
            "(8) Nachdem ein junger Mann zum Ritter geschlagen wurde, durfte er selbst "
            "an Turnieren teilnehmen.\n"
            "(9) Der junge Ritter erhielt von seinem Herrn ein Haus geschenkt."
        ),
        "answer": "(1) F ; (2) R ; (3) R ; (4) F ; (5) R ; (6) F ; (7) F ; (8) R ; (9) F.",
        "steps": [
            "(1) F: Lesen/Schreiben war nicht ueblich.",
            "(4) F: Reiterausbildung dauerte länger.",
            "(6) F: Jeder Ritter konnte den Ritterschlag vornehmen.",
            "(7) F: Mit 7 Jahren kam er auf eine fremde Burg.",
            "(9) F: Lehen = Nutzungsrecht, kein Eigentum.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 6,
        "type": "Fragen in ganzen Sätzen",
        "text": (
            "Beantworte in ganzen Sätzen:\n"
            "(a) Nenne vier Dinge, die ein werdender Ritter als Edelknabe erlernen musste.\n"
            "(b) Wer bezahlte die Ruestung eines Ritters, wenn er in den Ritterstand "
            "erhoben wurde?\n"
            "(c) Haette dir eine Ausbildung zum Ritter gefallen? Begruende!"
        ),
        "answer": (
            "(a) Hoefische Sitte, gute Manieren, biblische Geschichte, Musik und Gesang. ; "
            "(b) Er selbst musste die Ruestung bezahlen. ; "
            "(c) Individuelle Antwort, z. B. Nein - weil man mit 7 Jahren von der "
            "Familie getrennt wurde; oder Ja - wegen Reiten und Turnier."
        ),
        "steps": [
            "(a) Aus dem Edelknaben-Abschnitt.",
            "(b) Im Text: 'jede Menge Geld für die erste Ruestung'.",
            "(c) Eigene Meinung mit Begruendung.",
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
