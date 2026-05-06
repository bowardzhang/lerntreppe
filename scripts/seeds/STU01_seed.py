EXERCISE = {
    "id": "STU01",
    "subject": "Mathe",
    "grade": 4,
    "title": "Sachaufgaben: Textstellen unterstreichen",
    "topic": "Wichtige Textstellen erkennen, ueberfluessige Informationen ignorieren",
    "publisher": "Online-Übungen",
    "source_pdf": "Textstellen unterstreichen_Textaufgaben Grundschule.pdf",
    "answer_pdf": "Textstellen unterstreichen_Textaufgaben Grundschule_Lösung.pdf",
    "total_points": 5.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Sportfest Weitsprung-Unterschied",
        "text": (
            "Unterstreiche die wichtigen Textstellen und beantworte die Frage:\n"
            "'Am Freitag findet in der Waldschule das Sportfest statt. Kira "
            "springt beim Weitsprung 265 cm weit. Beim Sprint rennt sie 50 m in "
            "9,7 s. Im Hochsprung schafft sie 117 cm. Steven springt beim "
            "Weitsprung 257 cm weit. Beim Sprint benoetigt er 9,2 s und im "
            "Hochsprung schafft er 118,5 cm.'\n"
            "Wie gross ist der Unterschied zwischen Kira und Steven im Weitsprung?"
        ),
        "answer": "265 cm - 257 cm = 8 cm. Kira sprang 8 cm weiter als Steven.",
        "steps": [
            "Wichtig: Kira Weitsprung 265 cm, Steven Weitsprung 257 cm.",
            "Differenz: 265 - 257 = 8 cm.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.groessen.laenge",
        ],
    },
    {
        "n": 2,
        "type": "Fahrrad in der Werkstatt",
        "text": (
            "Tim gibt sein Fahrrad am Freitag um 16 Uhr in die Werkstatt. Er muss "
            "18 EUR fuer einen neuen Reifen und 12 EUR fuer ein neues Licht "
            "bezahlen. Er bezahlt die Reparatur von seinem Taschengeld. Einen Tag "
            "spaeter holt er es um 10 Uhr ab.\n"
            "Frage: Wie viele Stunden stand das Fahrrad in der Werkstatt?"
        ),
        "answer": "18 Stunden.",
        "steps": [
            "Freitag 16 Uhr bis Mitternacht: 8 h.",
            "Mitternacht bis Samstag 10 Uhr: 10 h.",
            "8 + 10 = 18 h.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.groessen.zeit",
        ],
    },
    {
        "n": 3,
        "type": "Frau Meiers Einkauf ohne Getränke",
        "text": (
            "Frau Meier geht um 16 Uhr einkaufen. Um 18 Uhr trifft sie sich mit "
            "Frau Mueller. Sie kauft Aepfel fuer 3 EUR, Getraenke fuer 5 EUR, "
            "Brotbelag fuer 8 EUR und Haferflocken fuer 0,50 EUR. An der Kasse "
            "bezahlt sie mit einem 20-EUR-Schein.\n"
            "Frage: Wie viel haette sie ohne die Getraenke bezahlt?"
        ),
        "answer": "3 EUR + 8 EUR + 0,50 EUR = 11,50 EUR. Sie haette 11,50 EUR bezahlt.",
        "steps": [
            "Ohne Getraenke: Aepfel 3 + Brotbelag 8 + Haferflocken 0,50.",
            "Summe: 11,50 EUR.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.groessen.geld",
        ],
    },
    {
        "n": 4,
        "type": "Tiger und Hyäne (Gewichtsdifferenz)",
        "text": (
            "Woelfe werden ungefaehr 80 cm gross und wiegen ungefaehr 40 kg. "
            "Tiger wiegen sogar 120 kg, obwohl sie nur eine Koerperhoehe von "
            "75 cm haben. Loewen sind ungefaehr 100 cm hoch. Sie wiegen "
            "150 - 250 kg. Hyaenen sind mit ca. 35 kg am leichtesten. Ihre "
            "Schulterhoehe kann jedoch 60 cm betragen.\n"
            "Frage: Wie viele Kilogramm ist ein Tiger schwerer als eine Hyaene?"
        ),
        "answer": "120 kg - 35 kg = 85 kg. Ein Tiger ist 85 kg schwerer als eine Hyaene.",
        "steps": [
            "Tiger: 120 kg ; Hyaene: 35 kg.",
            "Differenz: 120 - 35 = 85 kg.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.groessen.gewicht",
        ],
    },
    {
        "n": 5,
        "type": "Radtour-Dauer (mit Pause)",
        "text": (
            "Hans und Franz machen eine 160 km lange Radtour. Sie fahren um "
            "8:00 Uhr los. Fuer 20 km brauchen sie eine Stunde. Um 12:00 Uhr "
            "machen sie eine Stunde Mittagspause.\n"
            "Frage: Wie lang dauert die Radtour insgesamt?"
        ),
        "answer": "160 : 20 = 8 h Fahrtzeit + 1 h Pause = 9 h. Die Radtour dauert 9 h.",
        "steps": [
            "Reine Fahrtzeit: 160 km : 20 km/h = 8 h.",
            "Mit Pause: 8 h + 1 h = 9 h.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.groessen.zeit",
            "mathe.klasse4.groessen.laenge",
        ],
    },
]

NEW_KNOWLEDGE = []
