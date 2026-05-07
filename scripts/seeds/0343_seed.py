EXERCISE = {
    "id": "0343",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Das verflixte E",
    "topic": "Leseverstehen, Fantasiegeschichte, Buchstaben, Gespenst",
    "publisher": "CATLUX",
    "source_pdf": "0343.pdf",
    "answer_pdf": "0343 (1).pdf",
    "total_points": 45.0,
}

LESETEXT = (
    "Das verflixte E (nach Mira Lobe)\n\n"
    "Es gibt reizende Gespenster. Leider gehoerte das Gespenst Eene-Meene-Peene "
    "nicht dazu. Es war eine widerwaertige Person: boshaft, habgierig und eitel. "
    "Stundenlang sass es vorm Spiegel und sagte, eigentlich sei es gar kein "
    "Gespenst, sondern eine Fee. Eine bildschoene, suesse, sanfte, reizende Fee! "
    "Alle lachten es aus - und das machte das Gespenst Eene-Meene-Peene noch "
    "boeser, als es ohnehin schon war. Schlupp - hexte es saemtliche E in seinen "
    "Gespensterkoffer und machte sich davon.\n\n"
    "Es baute sich ein E-Werk mit Fenstern und Erkern, mit Kellern und Kerkern "
    "und rechteckigen Wendeltreppen. Neben dem E-Werk ebnete es zehnmal zehn "
    "Wege, setzte Erdbeeren und Ebereschen, legte zehn Seen an mit Egeln und "
    "Segeln; und weil es immer noch eine Menge E im Sack hatte, hexte es eine "
    "Herde See-Elefanten und fuetterte sie mit Seesternen und Schneesternen, bis "
    "er leer war, der Sack.\n\n"
    "Jetzt gab es kein einziges E mehr auf der Welt. Kinr konnt kinn vrsthn. "
    "All Lut warn vrzwiflt.\n\n"
    "Zum Beispiel: Braut und Braeutigam stehen in der Kirche und wollen heiraten. "
    "Aber ohne E kann man keine Ehe schliessen. Di Braut wint und hult. Dr "
    "Braeutigam schrit und ztrt. Der Mesner sperrt die Kirche zu.\n\n"
    "Oder: Tante Adelheid hat ihren Neffen Emil eingeladen. 'Libr Nff mil!' sagt "
    "sie. 'Kaff odr T? Und in paar lckr Kks dazu?' 'Lib Tant Adlhid, din Frnshr "
    "ist ntzwi. Soll ich nicht dn lkrtikr bstlln?' 'Sit gstrn ght das Tlfon "
    "nicht mhr. Schrcklich!'\n\n"
    "Oder: Der Buergermeister muss eine Festrede in der Feuerwehrhalle halten. "
    "Zwoelf Feuerwehrlehrlinge haben heute ihren Feuertest bestanden. 'Vrhrt "
    "Fstgmind!' beginnt der Buergermeister feierlich. Die Lehrlinge kichern. "
    "Der Buergermeister bricht seine Rede ab und sperrt das Rathaus zu.\n\n"
    "Nur in der Schule wollen es ein paar unermuedliche Lehrer noch immer nicht "
    "aufgeben. Der Rechenlehrer Immerfleis zum Beispiel. 'Tho!' ruft er. 'Wivil "
    "ist schs und nun und ins?' Theo steht auf: 'Ich wiss nicht, Hrr Rchnlhrr ...' "
    "'Schzhn!' ruft Herr Immerfleis. In den anderen Faechern ist es nicht besser: "
    "in Dutsch und rdkund, in Schribn und Lsn - von nglisch ganz zu schwign. "
    "Also wird auch die Schule geschlossen.\n\n"
    "Da beschliessen alle, zum E-Werk zu ziehen und die E von dem Gespenst "
    "zurueckzuholen. 'Gib uns unsr ... widr!'\n\n"
    "Das Gespenst Eene-Meene-Peene sitzt an seinem schoensten Erkerfenster und "
    "haelt sich die Seiten vor Lachen. 'Krisch nicht, du schusslichs Gspnst!' "
    "rufen die Leute empoert.\n\n"
    "'Was bin ich?', kreischt das Gespenst und spruehte Funken vor Zorn.\n\n"
    "Funken sind in einem E-Werk streng verboten, wie jeder weiss. Rrrums! gibt "
    "es einen Kurzschluss, und das ganze Haus mit Fenstern und Erkern, mit "
    "Kellern und Kerkern fliegt in die Luft. Es wirbelt nur so von E.\n\n"
    "Theo faengt sich eins und ist wieder Theo. Das Brautpaar sinkt sich seelig "
    "in die Arme. Alle Kinder, die heute getauft werden, heissen Helene oder "
    "Engelbert. Das Gespenst Eene-Meene-Peene verschwindet auf Nimmerwiedersehen.\n\n"
    "Bis eines Tages der Kobold Oone-Moone-Poone auftaucht und alle O stiehlt. "
    "Er traegt sie frt zu einem rt - und was das fuer Flgen hat, denkt euch "
    "gefaelligst selbst aus."
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Adjektive nennen",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Beschreibe das Gespenst mit Adjektiven!\n"
            "(a) Die Leute finden es ...\n"
            "(b) Es findet sich selbst ..."
        ),
        "answer": (
            "(a) Die Leute finden es: boshaft, habgierig, eitel. ; "
            "(b) Es findet sich selbst: bildschoen, suess, sanft, reizend."
        ),
        "steps": [
            "Aus dem ersten Abschnitt.",
        ],
        "points": 3.5,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 2,
        "type": "Wohnort",
        "text": "Wo wohnt das Gespenst?",
        "answer": "Im E-Werk.",
        "steps": [
            "Aus dem zweiten Abschnitt.",
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
        "type": "Falsche Wörter streichen",
        "text": (
            "Streiche die falschen Woerter durch!\n"
            "Nahe dem E-Werk ebnete es zehnmal zwei Wege, setzte Ebereschen und "
            "Erdbeeren, legte zehn Seen mit Egeln und Segeln an, und da es immer "
            "noch jede Menge E im Sack hat, hexte es eine Herde See-Elefanten und "
            "fuetterte sie mit Schneesternen und Seesternen, bis er leer war, der "
            "Sack."
        ),
        "answer": (
            "Durchstreichen: 'zwei' (richtig: zehn), 'Ebereschen und Erdbeeren' "
            "(richtig: Erdbeeren und Ebereschen), 'da' (richtig: weil), "
            "'jede Menge' (richtig: eine Menge), 'Schneesternen und Seesternen' "
            "(richtig: Seesternen und Schneesternen)."
        ),
        "steps": [
            "Originaltext genau pruefen und Abweichungen markieren.",
        ],
        "points": 5.5,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 4,
        "type": "Text übersetzen",
        "text": "Uebersetze richtig! Was sagt Tante Adelheid zu ihrem Neffen Emil?",
        "answer": (
            "'Lieber Neffe Emil!' ; "
            "'Kaffee oder Tee? Und ein paar leckere Kekse dazu?'"
        ),
        "steps": [
            "E-lose Schreibweise mit E ersetzen.",
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
        "type": "Kaputte Geräte",
        "text": "Was ist bei Tante Adelheid kaputt?",
        "answer": "Der Fernseher und das Telefon.",
        "steps": [
            "Aus dem Abschnitt mit Tante Adelheid.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 6,
        "type": "Grund der Feier",
        "text": "Warum fand eine Feier in der Feuerwehrhalle statt?",
        "answer": "Weil zwoelf Feuerwehrlehrlinge ihren Feuertest bestanden hatten.",
        "steps": [
            "Aus dem Abschnitt ueber den Buergermeister.",
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
        "type": "Rechenaufgabe",
        "text": "Welche Rechenaufgabe stellte der Rechenlehrer Immerfleis? Schreibe sie mit Zahlen!",
        "answer": "6 + 9 + 1 = 16.",
        "steps": [
            "'schs und nun und ins' = 6 + 9 + 1.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 8,
        "type": "Schulfächer benennen",
        "text": "In welchen Faechern konnte man in der Schule nichts mehr lernen?",
        "answer": "Deutsch, Erdkunde, Schreiben, Lesen, Englisch.",
        "steps": [
            "Aus dem Absatz ueber die Schule.",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 9,
        "type": "Geschlossene Gebäude",
        "text": "Welche Gebaeude mussten geschlossen werden?",
        "answer": "Das Rathaus, die Kirche, die Schule.",
        "steps": [
            "Aus dem Text: Kirche (Mesner), Rathaus (Buergermeister), Schule.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 10,
        "type": "E-Werk Verbot",
        "text": "Was ist in einem E-Werk strengstens verboten?",
        "answer": "Funken sind in einem E-Werk strengstens verboten.",
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
        "n": 11,
        "type": "Namen ankreuzen",
        "text": (
            "Kreuze die richtigen Namen an! Alle Kinder, die heute getauft "
            "werden, heissen ...\n"
            "(a) Theo\n"
            "(b) Helene\n"
            "(c) Engelbert"
        ),
        "answer": "Richtig: (b) Helene und (c) Engelbert.",
        "steps": [
            "Aus dem letzten Teil der Geschichte.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 12,
        "type": "Kleidung der Braut",
        "text": "Was traegt die Braut?",
        "answer": "Ganz in Weiss mit Schleppe und Schleier.",
        "steps": [
            "Aus dem Abschnitt ueber Braut und Braeutigam.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 13,
        "type": "Motiv des Gespenstes",
        "text": "Warum stiehlt das Gespenst alle E?",
        "answer": (
            "Es stiehlt alle E, weil es von allen ausgelacht wird. Das Gespenst "
            "behauptet, eine schoene Fee zu sein, doch die Leute lachen es aus."
        ),
        "steps": [
            "Aus dem ersten Absatz: ausgelacht werden => Rache durch E-Diebstahl.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 14,
        "type": "Zitat mit Zeile",
        "text": (
            "Was sagen die Leute zu dem Gespenst, das es dazu bringt, vor Zorn "
            "Funken zu spruehen? Nenne genau den Satz!"
        ),
        "answer": "'Kreisch nicht, du scheussliches Gespenst!'",
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
        "n": 15,
        "type": "Anderer Begriff finden",
        "text": (
            "Das Gespenst lacht sich total schlapp. Finde einen anderen Begriff "
            "dafuer im Text."
        ),
        "answer": "Sich die Seiten vor Lachen halten.",
        "steps": [
            "Synonym fuer 'sich schlappachen' im Text suchen.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 16,
        "type": "Folgen des Kurzschlusses",
        "text": "Was passiert, als das Gespenst vor Zorn Funken spruehte?",
        "answer": (
            "Es gibt einen Kurzschluss und das ganze E-Werk mit Fenstern und "
            "Erkern, mit Kellern und Kerkern fliegt in die Luft. Alle E kehren "
            "zurueck."
        ),
        "steps": [
            "Funken => Kurzschluss => Explosion => E kehren zurueck.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 17,
        "type": "Nachfolger des Gespenstes",
        "text": "Wer nimmt den Platz des Gespenstes ein? Was wird diesmal gestohlen?",
        "answer": "Der Kobold Oone-Moone-Poone; er stiehlt alle O.",
        "steps": [
            "Aus dem letzten Absatz.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 18,
        "type": "Satz abschreiben",
        "text": "Schreibe den letzten Satz vollstaendig und richtig ab.",
        "answer": (
            "'Er traegt sie fort zu einem Ort - und was das fuer Folgen hat, "
            "denkt euch gefaelligst selbst aus.'"
        ),
        "steps": [
            "O-lose Schreibweise korrigieren: 'frt'=>'fort', 'rt'=>'Ort', 'Flgen'=>'Folgen'.",
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
