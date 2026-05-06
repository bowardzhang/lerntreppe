EXERCISE = {
    "id": "0572",
    "subject": "Deutsch",
    "grade": 4,
    "title": "3. Lernzielkontrolle: Wortarten, Fälle, Adjektivsteigerung, Konjunktionen, Zeiten",
    "topic": "Zusammensetzungen, Kasus, wie/als, Adjektivsteigerung, Satzglieder, Zeitformen",
    "publisher": "CATLUX",
    "source_pdf": "0572.pdf",
    "answer_pdf": "0572 (1).pdf",
    "total_points": 43.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Wortarten zusammengesetzter Nomen",
        "text": (
            "Aus welchen Wortarten sind diese Nomen zusammengesetzt? "
            "Schreibe die Grundformen und Wortarten auf.\n"
            "Bienenhonig: ___\n"
            "Turnstunde: ___\n"
            "Spitzmaus: ___\n"
            "Schwimmbad: ___"
        ),
        "answer": (
            "Bienenhonig: die Biene + der Honig (Nomen + Nomen) ; "
            "Turnstunde: turnen + die Stunde (Verb + Nomen) ; "
            "Spitzmaus: spitz + die Maus (Adjektiv + Nomen) ; "
            "Schwimmbad: schwimmen + das Bad (Verb + Nomen)"
        ),
        "steps": [
            "Bienenhonig = Biene (N) + Honig (N).",
            "Turnstunde = turnen (V) + Stunde (N).",
            "Spitzmaus = spitz (Adj) + Maus (N).",
            "Schwimmbad = schwimmen (V) + Bad (N).",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.rechtschreibung.zusammensetzungen",
            "deutsch.klasse4.grammatik.wortarten",
        ],
    },
    {
        "n": 2,
        "type": "Zusammengesetzte Adjektive",
        "text": (
            "Schreibe je zwei zusammengesetzte Adjektive auf:\n"
            "Nomen + Adjektiv: ___, ___\n"
            "Adjektiv + Adjektiv: ___, ___"
        ),
        "answer": (
            "Nomen + Adjektiv: z.B. eiskalt, messerscharf ; "
            "Adjektiv + Adjektiv: z.B. hellgelb, dunkelrot"
        ),
        "steps": [
            "Nomen+Adj: Eis+kalt=eiskalt, Messer+scharf=messerscharf.",
            "Adj+Adj: hell+gelb=hellgelb, dunkel+rot=dunkelrot.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.rechtschreibung.zusammensetzungen",
            "deutsch.klasse4.grammatik.wortarten",
        ],
    },
    {
        "n": 3,
        "type": "Fragen nach Nomen stellen und Fall bestimmen",
        "text": (
            "Stelle Fragen nach den unterstrichenen Nomen, antworte und bestimme "
            "den Fall.\n"
            "Der Hund lauft auf der Strasse. "
            "Ein Junge ruft den Hund bei seinem Namen. "
            "Das Fell des Hundes ist sehr schoen. "
            "Der Junge gibt dem Hund eine Wurst."
        ),
        "answer": (
            "Wer oder was laeuft? -> Der Hund (1. Fall) ; "
            "Wen oder was ruft der Junge? -> Den Hund (4. Fall) ; "
            "Wessen Fell ist sehr schoen? -> Des Hundes (2. Fall) ; "
            "Wem gibt der Junge eine Wurst? -> Dem Hund (3. Fall)"
        ),
        "steps": [
            "Hund als Subjekt -> 1. Fall / Nominativ.",
            "Hund als Akkusativobjekt (rufen, Wen?) -> 4. Fall.",
            "des Hundes = Genitivattribut (Wessen?) -> 2. Fall.",
            "dem Hund = Dativobjekt (geben, Wem?) -> 3. Fall.",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.kasus",
        ],
    },
    {
        "n": 4,
        "type": "Fall der unterstrichenen Nomen bestimmen",
        "text": (
            "Bestimme den Fall der unterstrichenen Nomen:\n"
            "Neulich machte unsere Klasse (_) einen Ausflug (_) in den Zoo. "
            "Am Eingang gaben wir unserer Lehrerin (_) das Geld fuer die "
            "Eintrittskarten (_). Wegen des schlechten Wetters (_) besuchten "
            "wir zuerst das Schlangenhaus (_). Dann standen wir lange bei den "
            "Affen (_) und fuetterten sie. Bald war die Brotzeit vieler "
            "Kinder (_) weg."
        ),
        "answer": (
            "Klasse = 1. Fall ; Ausflug = 4. Fall ; Lehrerin = 3. Fall ; "
            "Eintrittskarten = 4. Fall ; Wetters = 2. Fall ; Schlangenhaus = 4. Fall ; "
            "Affen = 3. Fall ; Kinder = 2. Fall"
        ),
        "steps": [
            "Klasse: Subjekt -> 1. Fall.",
            "Ausflug: Akkusativobjekt (machte was?) -> 4. Fall.",
            "Lehrerin: Dativobjekt (gaben wem?) -> 3. Fall.",
            "Eintrittskarten: fuer + Akkusativ -> 4. Fall.",
            "Wetters: Genitivattribut (wegen) -> 2. Fall.",
            "Schlangenhaus: Akkusativobjekt (besuchten was?) -> 4. Fall.",
            "Affen: bei + Dativ -> 3. Fall.",
            "Kinder: Genitivattribut (Brotzeit wessen?) -> 2. Fall.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.kasus",
        ],
    },
    {
        "n": 5,
        "type": "wie oder als einsetzen",
        "text": (
            "Setze 'wie' oder 'als' richtig ein:\n"
            "Krapfen schmecken suesser ___ Brot. "
            "Altes Brot ist so hart ___ Stein. "
            "Die Zitrone ist sauerer ___ eine Orange. "
            "Aber sie ist kleiner ___ diese. "
            "Ich mag Orangen genauso gerne ___ Mandarinen. "
            "Obst ist gesuender ___ Kuchen."
        ),
        "answer": "als ; wie ; als ; als ; wie ; als",
        "steps": [
            "'suesser als' = Komparativ -> als.",
            "'so hart wie' = Gleichheitsvergleich -> wie.",
            "'sauerer als' = Komparativ -> als.",
            "'kleiner als' = Komparativ -> als.",
            "'genauso gerne wie' = Gleichheitsvergleich -> wie.",
            "'gesuender als' = Komparativ -> als.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.steigerung",
        ],
    },
    {
        "n": 6,
        "type": "Adjektive steigern",
        "text": (
            "Suche 4 Adjektive aus dem vorherigen Text und steigere sie "
            "(Grundform, Komparativ, Superlativ)."
        ),
        "answer": (
            "suess - suesser - am suessesten ; "
            "hart - haerter - am haertesten ; "
            "alt - aelter - am aeltesten ; "
            "sauer - saurer - am sauersten"
        ),
        "steps": [
            "suess -> suesser -> am suessesten.",
            "hart -> haerter -> am haertesten.",
            "alt -> aelter -> am aeltesten.",
            "sauer -> saurer -> am sauersten.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.steigerung",
        ],
    },
    {
        "n": 7,
        "type": "Wortarten bestimmen",
        "text": (
            "Bestimme die Wortart jedes Wortes (Nomen, Verb, Adjektiv, Konjunktion):\n"
            "fliessen | gut | Fluss | weil | bevor | dass | eisig | sicher | "
            "nachdem | Jaeger | obwohl | kalt | sehen | mittelblau | "
            "Freude | waehrend | Luft | toll | rasen | wenn"
        ),
        "answer": (
            "fliessen=Verb ; gut=Adjektiv ; Fluss=Nomen ; weil=Konjunktion ; "
            "bevor=Konjunktion ; dass=Konjunktion ; eisig=Adjektiv ; sicher=Adjektiv ; "
            "nachdem=Konjunktion ; Jaeger=Nomen ; obwohl=Konjunktion ; kalt=Adjektiv ; "
            "sehen=Verb ; mittelblau=Adjektiv ; "
            "Freude=Nomen ; waehrend=Konjunktion ; Luft=Nomen ; toll=Adjektiv ; "
            "rasen=Verb ; wenn=Konjunktion"
        ),
        "steps": [
            "Verben (Taetigkeiten): fliessen, sehen, rasen.",
            "Nomen (mit Artikel vorstellbar): Fluss, Jaeger, Freude, Luft.",
            "Adjektive (Eigenschaften): gut, eisig, sicher, kalt, mittelblau, toll.",
            "Konjunktionen (verbinden Saetze): weil, bevor, dass, nachdem, obwohl, waehrend, wenn.",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.wortarten",
        ],
    },
    {
        "n": 8,
        "type": "Konjunktionen einsetzen",
        "text": (
            "Setze in jede Luecke eine passende Konjunktion ein:\n"
            "1. Peter geht heute in die Schule, ___ er stark erkaeltet ist.\n"
            "2. ___ ich einschlafe, lese ich noch ein paar Seiten.\n"
            "3. Erika isst ein Stueck Kuchen, ___ er ihr gut schmeckt.\n"
            "4. Ich darf am Wochenende zelten, ___ es nicht regnet."
        ),
        "answer": "1. obwohl ; 2. Bevor ; 3. weil ; 4. wenn",
        "steps": [
            "1. Gegensatz (krank, geht trotzdem) -> obwohl.",
            "2. zeitlich vorher -> bevor.",
            "3. Begruendung -> weil.",
            "4. Bedingung -> wenn.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.wortarten",
        ],
    },
    {
        "n": 9,
        "type": "Satzgegenstand und Satzaussage + Grundformen",
        "text": (
            "Unterstreiche den Satzgegenstand rot und die Satzaussage blau. "
            "Schreibe dann alle Satzaussagen in der Grundform auf.\n"
            "Mutter liest Peter am Abend eine Geschichte vor. "
            "Der Junge reibt sich die Augen. "
            "Er kaempft mit dem Schlaf. "
            "Die Augen fallen ihm zu. "
            "Vorsichtig traegt Vater ihn ins Bett."
        ),
        "answer": (
            "Satzgegenstaende: Mutter, Der Junge, Er, Die Augen, Vater. "
            "Satzaussagen: liest vor, reibt, kaempft, fallen zu, traegt. "
            "Grundformen: vorlesen, reiben, kaempfen, zufallen, tragen."
        ),
        "steps": [
            "Wer liest? Mutter -> Sg; was tut sie? liest vor -> Sa.",
            "Wer reibt? Der Junge -> Sg; reibt -> Sa.",
            "Wer kaempft? Er -> Sg; kaempft -> Sa.",
            "Was faellt zu? Die Augen -> Sg; fallen zu -> Sa.",
            "Wer traegt? Vater -> Sg; traegt -> Sa.",
            "Grundformen: vorlesen, reiben, kaempfen, zufallen, tragen.",
        ],
        "points": 7.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.satzglieder",
            "deutsch.klasse4.grammatik.wortarten",
        ],
    },
    {
        "n": 10,
        "type": "Verben in Zeiten konjugieren",
        "text": (
            "Setze die Verben in der entsprechenden Person in die verschiedenen Zeiten:\n"
            "Grundform | Gegenwart | 1. Vergangenheit | 2. Vergangenheit\n"
            "giessen   | es        | ___              | ___\n"
            "schenken  | ich       | ___              | ___\n"
            "beobachten| du        | ___              | ___\n"
            "rennen    | ihr       | ___              | ___"
        ),
        "answer": (
            "giessen: es giesst / es goss / es hat gegossen ; "
            "schenken: ich schenke / ich schenkte / ich habe geschenkt ; "
            "beobachten: du beobachtest / du beobachtetest / du hast beobachtet ; "
            "rennen: ihr rennt / ihr ranntet / ihr seid gerannt"
        ),
        "steps": [
            "giessen (stark): giesst, goss, hat gegossen.",
            "schenken (schwach): schenke, schenkte, habe geschenkt.",
            "beobachten (schwach): beobachtest, beobachtetest, hast beobachtet.",
            "rennen (unregelmaessig): rennt, ranntet, seid gerannt.",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.zeiten",
        ],
    },
]

NEW_KNOWLEDGE = []
