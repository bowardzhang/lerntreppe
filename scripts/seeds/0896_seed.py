EXERCISE = {
    "id": "0896",
    "subject": "Mathe",
    "grade": 4,
    "title": "Übungsaufgaben: Wahrscheinlichkeit und Häufigkeit (III)",
    "topic": "Wahrscheinlichkeit, relative Haeufigkeit, Kombinatorik, Aussagen",
    "publisher": "CATLUX",
    "source_pdf": "0896.pdf",
    "answer_pdf": "0896 (1).pdf",
    "total_points": 18.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Murmeln-Saeckchen",
        "text": (
            "Thomas zieht aus einem Saeckchen 10 Murmeln, davon 5 blaue. "
            "Christine zieht aus einem anderen Saeckchen 20 Murmeln, davon 7 blaue. "
            "Wer hat den groesseren Anteil blauer Murmeln gezogen?"
        ),
        "answer": (
            "Thomas: 5/10 = 50% blau. Christine: 7/20 = 35% blau. "
            "Thomas hat einen groesseren Anteil blauer Murmeln gezogen."
        ),
        "steps": [
            "Thomas: 5 von 10 = 5/10 = 1/2 = 50%.",
            "Christine: 7 von 20 = 35%.",
            "Vergleich: 50% > 35%, also Thomas.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.wahrscheinlichkeit.haeufigkeit",
        ],
    },
    {
        "n": 2,
        "type": "Aquarium-Fische",
        "text": (
            "In einem Aquarium schwimmen 8 rote, 4 gelbe und 12 blaue Fische. "
            "Welche Farbe wird beim zufaelligen Herausfangen am wahrscheinlichsten "
            "gefangen? Welche am unwahrscheinlichsten?"
        ),
        "answer": (
            "Insgesamt 24 Fische. Wahrscheinlichkeit: blau (12/24=1/2), rot (8/24=1/3), "
            "gelb (4/24=1/6). Am wahrscheinlichsten: blau. Am unwahrscheinlichsten: gelb."
        ),
        "steps": [
            "Gesamt: 8 + 4 + 12 = 24 Fische.",
            "Blau: 12/24 = 1/2 (50%).",
            "Rot: 8/24 = 1/3 (~33%).",
            "Gelb: 4/24 = 1/6 (~17%).",
            "Groesste Wahrscheinlichkeit: blau ; kleinste: gelb.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.wahrscheinlichkeit.chancen",
        ],
    },
    {
        "n": 3,
        "type": "Bonbon-Wahrscheinlichkeit",
        "text": (
            "In einer Tuete sind 5 Erdbeerbonbons, 3 Zitronenbonbons und 2 "
            "Kirschbonbons. Sabine und Tim greifen ohne Hinschauen.\n"
            "a) Wer hat die groessere Chance, einen Erdbeerbonbon zu bekommen, "
            "wenn beide einmal greifen?\n"
            "b) Wer hat die groessere Chance auf einen Zitronenbonbon?\n"
            "c) Tim greift zuerst und zieht einen Erdbeerbonbon. "
            "Wer hat danach groessere Chance auf einen Erdbeerbonbon, wenn "
            "Tim ihn nicht zurueckgibt?"
        ),
        "answer": (
            "a) Beide haben gleiche Chance vor dem Ziehen (5/10). "
            "Sabine zieht zuerst. ; "
            "b) Sabine (3/10 vs. evtl. 3/9 oder 2/9 für Tim, hier zuerst Sabine). ; "
            "c) Da nur noch 4 Erdbeerbonbons in 9 verbleiben (4/9), hat Sabine "
            "die kleinere Chance als Tim sie hatte (5/10 = 1/2). Tim hatte die "
            "groessere Chance gehabt."
        ),
        "steps": [
            "Insgesamt 10 Bonbons (5 + 3 + 2).",
            "a) Erste Person: 5/10 = 50%.",
            "b) Zitrone: 3/10 = 30% beim ersten Griff.",
            "c) Nach Tims Erdbeer-Bonbon: 4 von 9 verbleibend = 4/9 ~ 44%.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.wahrscheinlichkeit.chancen",
        ],
    },
    {
        "n": 4,
        "type": "Stofftiere-Vorhersage",
        "text": (
            "In einem Greifautomaten gibt es 20 Affen, 10 Baeren und 5 Loewen. "
            "Bei jedem Zug wird zufaellig ein Tier gegriffen.\n"
            "a) Sind die Chancen niedriger oder hoeher, einen Affen zu greifen "
            "als einen Loewen?\n"
            "b) Welche Tiere wird man wohl in den ersten 7 Zuegen ueberwiegend bekommen?"
        ),
        "answer": (
            "a) Hoeher (20 von 35 vs. 5 von 35). "
            "b) Ueberwiegend Affen, da deren Anteil mit 20/35 (~57%) am groessten ist."
        ),
        "steps": [
            "Insgesamt 35 Tiere.",
            "Affen: 20/35 ~ 57%. Baeren: 10/35 ~ 29%. Loewen: 5/35 ~ 14%.",
            "Bei 7 Zuegen erwartet man ca. 4 Affen, 2 Baeren, 1 Loewe.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.wahrscheinlichkeit.chancen",
            "mathe.klasse4.wahrscheinlichkeit.haeufigkeit",
        ],
    },
    {
        "n": 5,
        "type": "Ziffernkarten-Aussagen",
        "text": (
            "Auf zehn Karten stehen die Ziffern 0 bis 9. Welche Aussagen sind "
            "richtig (R) oder falsch (F)?\n"
            "a) Wenn ich eine Karte ziehe, ist es sicher eine gerade Zahl.\n"
            "b) Es ist möglich, eine 5 zu ziehen.\n"
            "c) Ich werde unmoeglich eine 11 ziehen.\n"
            "d) Es ist genau gleich wahrscheinlich, eine 0, 1, 2, ... oder 9 zu ziehen."
        ),
        "answer": "a) F ; b) R ; c) R ; d) R",
        "steps": [
            "a) Falsch: ungerade Karten gibt es auch.",
            "b) Richtig: 5 ist eine der Karten.",
            "c) Richtig: 11 ist nicht im Stapel.",
            "d) Richtig: jede Karte hat 1/10 Chance.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.wahrscheinlichkeit.chancen",
        ],
    },
    {
        "n": 6,
        "type": "Zahlen aus 1, 8, 5",
        "text": (
            "Bilde aus den Ziffern 1, 8 und 5 alle möglichen verschiedenen "
            "dreistelligen Zahlen und ordne sie nach Groesse."
        ),
        "answer": "158, 185, 518, 581, 815, 851",
        "steps": [
            "3 Ziffern -> 3! = 6 Möglichkeiten.",
            "Mit 1 vorne: 158, 185.",
            "Mit 5 vorne: 518, 581.",
            "Mit 8 vorne: 815, 851.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.wahrscheinlichkeit.kombinatorik",
            "mathe.klasse4.sachaufgaben.zahlenraetsel",
        ],
    },
    {
        "n": 7,
        "type": "Dosenwerfen",
        "text": (
            "Beim Dosenwerfen stehen 7 Dosen aufgestapelt. Marco trifft mit "
            "einem Wurf 3 Dosen. Wie viele Dosen stehen noch und wie groß ist "
            "der Anteil der getroffenen Dosen?"
        ),
        "answer": "Noch 4 Dosen stehen. Anteil: 3 von 7 = 3/7 (~43%).",
        "steps": [
            "Stehengeblieben: 7 - 3 = 4 Dosen.",
            "Anteil getroffen: 3/7 ~ 43%.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.wahrscheinlichkeit.haeufigkeit",
        ],
    },
    {
        "n": 8,
        "type": "Fahrradschloss Anne (Kombinatorik)",
        "text": (
            "Anne hat ein Zahlenschloss mit 4 Stellen. Sie weiß, dass die erste "
            "Ziffer eine 1 ist, die zweite eine gerade Ziffer (0, 2, 4, 6 oder 8 - "
            "nur 2 Möglichkeiten merkt sie) und die letzten beiden Ziffern "
            "ungerade Ziffern (1, 3, 5, 7, 9 - nur 7 mal 7 Optionen) sind. "
            "Wie viele mögliche Kombinationen muss sie durchprobieren?"
        ),
        "answer": "1 · 2 · 7 · 7 = 98 Möglichkeiten.",
        "steps": [
            "Stelle 1: 1 Möglichkeit (genau die 1).",
            "Stelle 2: 2 Möglichkeiten (gerade Ziffern, eingeschraenkt).",
            "Stellen 3 & 4: je 7 Möglichkeiten.",
            "Gesamt: 1 · 2 · 7 · 7 = 98.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.wahrscheinlichkeit.kombinatorik",
            "mathe.klasse4.sachaufgaben.zahlenraetsel",
        ],
    },
]

NEW_KNOWLEDGE = []
