EXERCISE = {
    "id": "0250",
    "subject": "Deutsch",
    "grade": 4,
    "title": "2. Lernzielkontrolle: Sprachbetrachtung, die 4 Fälle",
    "topic": "Kasus: Nominativ, Genitiv, Dativ, Akkusativ",
    "publisher": "CATLUX",
    "source_pdf": "0250.pdf",
    "answer_pdf": "0250 (1).pdf",
    "total_points": 38.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Fälle der unterstrichenen Wörter bestimmen",
        "text": (
            "Bestimme den Fall der unterstrichenen Wörter.\n"
            "1. Wir bauen ein Haus. → Haus: ___. Fall\n"
            "2. Ich helfe meiner Mutter. → Mutter: ___. Fall\n"
            "3. Es regnet heute. → es: ___. Fall\n"
            "4. Das ist die Tasche meiner Schwester. → Tasche meiner Schwester: Tasche: ___. Fall, Schwester: ___. Fall\n"
            "5. Erwin geht in die Schule. → Erwin: ___. Fall\n"
            "6. Das ist das Teilstück des Weges. → Teilstück: ___. Fall"
        ),
        "answer": (
            "1. Haus = 4. Fall (Akkusativ) ; "
            "2. Mutter = 3. Fall (Dativ) ; "
            "3. es = 1. Fall (Nominativ) ; "
            "4. Tasche = 1. Fall (Nominativ), Schwester = 2. Fall (Genitiv) ; "
            "5. Erwin = 1. Fall (Nominativ) ; "
            "6. Teilstück = 1. Fall (Nominativ), Weges = 2. Fall (Genitiv)"
        ),
        "steps": [
            "Haus: Objekt von 'bauen' → 4. Fall (Akkusativ).",
            "Mutter: Objekt von 'helfen' (Dativverb) → 3. Fall (Dativ).",
            "es: Subjekt des Satzes → 1. Fall (Nominativ).",
            "Tasche: Subjekt → 1. Fall; meiner Schwester: Genitivattribut → 2. Fall.",
            "Erwin: Subjekt → 1. Fall (Nominativ).",
            "Teilstück: Subjekt → 1. Fall; des Weges: Genitivattribut → 2. Fall.",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.kasus",
        ],
    },
    {
        "n": 2,
        "type": "Fälle in Sätzen unterstreichen und bestimmen",
        "text": (
            "a) Unterstreiche die Wörter im angegebenen Fall.\n"
            "1. (1. Fall) Der fleißige Schüler löst die schwere Aufgabe.\n"
            "2. (4. Fall) Mama kauft einen roten Pullover.\n"
            "3. (3. Fall) Der Lehrer gibt dem guten Schüler ein Lob.\n"
            "4. (2. Fall) Das Fahrrad meines Freundes ist kaputt.\n\n"
            "b) Unterstreiche die Endungen und bestimme den Fall.\n"
            "1. Das ist ihrer Mutter Hut. → Fall: ___\n"
            "2. Er kauft einen feinen Anzug. → Fall: ___\n"
            "3. Sie sieht einige Freundinnen. → Fall: ___\n"
            "4. Sie hilft dem alten Mann. → Fall: ___\n"
            "5. Das ist ein tolles Fest. → Fall: ___\n"
            "6. Das Haus unserer Nachbarn ist groß. → Fall der unterstrichenen Gruppe: ___"
        ),
        "answer": (
            "a) 1. Der fleißige Schüler (Nominativ) ; "
            "2. einen roten Pullover (Akkusativ) ; "
            "3. dem guten Schüler (Dativ) ; "
            "4. meines Freundes (Genitiv) ; "
            "b) 1. ihrer Mutter = 2. Fall (Genitiv) ; "
            "2. einen feinen = 4. Fall (Akkusativ) ; "
            "3. einige Freundinnen = 4. Fall (Akkusativ) ; "
            "4. dem = 3. Fall (Dativ) ; "
            "5. tolles = 4. Fall (Akkusativ) ; "
            "6. unserer Nachbarn = 2. Fall (Genitiv)"
        ),
        "steps": [
            "a1) Der fleißige Schüler = Subjekt → 1. Fall / Nominativ.",
            "a2) einen roten Pullover = Akkusativobjekt → 4. Fall / Akkusativ.",
            "a3) dem guten Schüler = Dativobjekt → 3. Fall / Dativ.",
            "a4) meines Freundes = Genitivattribut → 2. Fall / Genitiv.",
            "b1) ihrer Mutter → Endung '-er' Genitiv Femininum → 2. Fall.",
            "b2) einen feinen → unbestimmter Artikel Mask. Akk. → 4. Fall.",
            "b3) einige Freundinnen → Akkusativ Plural → 4. Fall.",
            "b4) dem → Dativartikel → 3. Fall.",
            "b5) tolles → Adjektivendung Nominativ Neutrum → 1. Fall.",
            "b6) unserer Nachbarn → Genitivattribut → 2. Fall.",
        ],
        "points": 16.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.kasus",
        ],
    },
    {
        "n": 3,
        "type": "Sätze mit 3. Fall bilden",
        "text": (
            "Bilde zwei Sätze, in denen ein Nomen im 3. Fall (Dativ) vorkommt."
        ),
        "answer": "Beispiel: Ich helfe meinem Bruder. / Er gibt der Lehrerin ein Geschenk.",
        "steps": [
            "Dativobjekt: nach Verben wie helfen, geben, schenken, danken, gehören …",
            "Beispiel 1: Ich helfe meinem Bruder.",
            "Beispiel 2: Er gibt der Lehrerin ein Geschenk.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.kasus",
        ],
    },
    {
        "n": 4,
        "type": "Sätze mit 3. und 4. Fall ankreuzen",
        "text": (
            "Kreuze die Sätze an, die sowohl einen 3. Fall als auch einen 4. Fall enthalten.\n"
            "1. Der Hund bellt laut.\n"
            "2. Mama kauft dem Kind ein Eis.\n"
            "3. Das Mädchen liest ein Buch.\n"
            "4. Er schenkt seiner Schwester einen Blumenstrauß.\n"
            "5. Der Lehrer lobt den fleißigen Schüler."
        ),
        "answer": "Sätze 2 und 4 (beide enthalten einen 3. und einen 4. Fall).",
        "steps": [
            "Satz 1: nur Subjekt (1. Fall) + Adverbiale → kein 3./4. Fall.",
            "Satz 2: dem Kind (Dativ, 3. Fall) + ein Eis (Akkusativ, 4. Fall) → ✓",
            "Satz 3: ein Buch (4. Fall), aber kein 3. Fall → ✗",
            "Satz 4: seiner Schwester (Dativ, 3. Fall) + einen Blumenstrauß (Akkusativ, 4. Fall) → ✓",
            "Satz 5: den fleißigen Schüler (4. Fall), aber kein 3. Fall → ✗",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.kasus",
        ],
    },
    {
        "n": 5,
        "type": "Satz mit vorgegebenen Wörtern bilden",
        "text": (
            "Bilde einen Satz mit den Wörtern: Florian – Schuhe – Kinder.\n"
            "Verteile die Fälle so: 1. Fall, 3. Fall, 4. Fall."
        ),
        "answer": "Beispiel: Florian gibt den Kindern die Schuhe.",
        "steps": [
            "1. Fall (Nominativ/Subjekt): Florian.",
            "3. Fall (Dativ): den Kindern.",
            "4. Fall (Akkusativ): die Schuhe.",
            "Satz: Florian gibt den Kindern die Schuhe.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.kasus",
        ],
    },
    {
        "n": 6,
        "type": "Endungen ergänzen und Fälle unterstreichen",
        "text": (
            "Ergänze die Endungen und unterstreiche jeweils den Fall.\n"
            "1. das Haus mein___ Nachbarn → ___. Fall\n"
            "2. Er hilft sein___ Vater. → ___. Fall\n"
            "3. Sie kauft ein___ neuen Rock. → ___. Fall\n"
            "4. Ein___ gut___ Schüler arbeitet fleißig. → ___. Fall\n"
            "5. Ich sehe d___ kleinen Hund. → ___. Fall\n"
            "6. Er dankt d___ Ärztin. → ___. Fall\n"
            "7. Das Spielzeug d___ Kindes ist kaputt. → ___. Fall\n"
            "8. Er bringt sein___ Freundin Blumen. → ___. Fall"
        ),
        "answer": (
            "1. meines Nachbarn = 2. Fall (Genitiv) ; "
            "2. seinem Vater = 3. Fall (Dativ) ; "
            "3. einen neuen Rock = 4. Fall (Akkusativ) ; "
            "4. Ein guter Schüler = 1. Fall (Nominativ) ; "
            "5. den kleinen Hund = 4. Fall (Akkusativ) ; "
            "6. der Ärztin = 3. Fall (Dativ) ; "
            "7. des Kindes = 2. Fall (Genitiv) ; "
            "8. seiner Freundin = 3. Fall (Dativ)"
        ),
        "steps": [
            "1. mein-es Nachbarn → Genitiv Maskulinum → 2. Fall.",
            "2. sein-em Vater → Dativ Maskulinum → 3. Fall.",
            "3. ein-en neuen Rock → Akkusativ Maskulinum → 4. Fall.",
            "4. Ein-  gut-er Schüler → Nominativ Maskulinum → 1. Fall.",
            "5. d-en kleinen Hund → Akkusativ Maskulinum → 4. Fall.",
            "6. d-er Ärztin → Dativ Femininum → 3. Fall.",
            "7. d-es Kindes → Genitiv Neutrum → 2. Fall.",
            "8. sein-er Freundin → Dativ Femininum → 3. Fall.",
        ],
        "points": 8.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.kasus",
        ],
    },
]

NEW_KNOWLEDGE = []
