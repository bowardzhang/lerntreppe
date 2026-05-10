EXERCISE = {
    "id": "MQA02",
    "subject": "Mathe",
    "grade": 3,
    "title": "Magische Quadrate A 02",
    "topic": "Magisches Quadrat 3\u00d73: Zeilen, Spalten und Diagonalen haben dieselbe Summe",
    "publisher": "CATLUX",
    "source_pdf": "Magische Quadrate A 02.pdf",
    "answer_pdf": None,
    "total_points": 18.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Magisches Quadrat (3×3)",
        "text": (
            '___ | ___ | ___\n'
            '___ |  30 | ___\n'
            '___ |  33 |  20\n'
            'Mag. Zahl: 90'
        ),
        "answer": (
            ' 40 |  27 |  23\n'
            ' 13 |  30 |  47\n'
            ' 37 |  33 |  20'
        ),
        "steps": [
            'Mag. Zahl S = 90.',
            'Mitte 30 bereits gegeben (S ÷ 3 = 30).',
            'Zeile 3: 33 + 20 + ___ = 90  →  ___ = 37.',
            'Spalte 2: 30 + 33 + ___ = 90  →  ___ = 27.',
            'Hauptdiagonale: 30 + 20 + ___ = 90  →  ___ = 40.',
            'Nebendiagonale: 30 + 37 + ___ = 90  →  ___ = 23.',
            'Spalte 1: 40 + 37 + ___ = 90  →  ___ = 13.',
            'Spalte 3: 23 + 20 + ___ = 90  →  ___ = 47.',
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse3.schriftlich.addition",
            "mathe.klasse3.schriftlich.subtraktion",
            "mathe.klasse4.sachaufgaben.zahlenraetsel",
        ],
    },
    {
        "n": 2,
        "type": "Magisches Quadrat (3×3)",
        "text": (
            '___ | ___ |  36\n'
            '___ |  20 |   2\n'
            '  4 | ___ | ___\n'
            'Mag. Zahl: 60'
        ),
        "answer": (
            ' 18 |   6 |  36\n'
            ' 38 |  20 |   2\n'
            '  4 |  34 |  22'
        ),
        "steps": [
            'Mag. Zahl S = 60.',
            'Mitte 20 bereits gegeben (S ÷ 3 = 20).',
            'Zeile 2: 20 + 2 + ___ = 60  →  ___ = 38.',
            'Spalte 1: 38 + 4 + ___ = 60  →  ___ = 18.',
            'Spalte 3: 36 + 2 + ___ = 60  →  ___ = 22.',
            'Zeile 1: 18 + 36 + ___ = 60  →  ___ = 6.',
            'Zeile 3: 4 + 22 + ___ = 60  →  ___ = 34.',
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse3.schriftlich.addition",
            "mathe.klasse3.schriftlich.subtraktion",
            "mathe.klasse4.sachaufgaben.zahlenraetsel",
        ],
    },
    {
        "n": 3,
        "type": "Magisches Quadrat (3×3)",
        "text": (
            ' 19 | ___ | ___\n'
            ' 62 | ___ |   2\n'
            ' 15 | ___ | ___\n'
            'Mag. Zahl: 96'
        ),
        "answer": (
            ' 19 |  28 |  49\n'
            ' 62 |  32 |   2\n'
            ' 15 |  36 |  45'
        ),
        "steps": [
            'Mag. Zahl S = 96.',
            'Mitte = S ÷ 3 = 96 ÷ 3 = 32.',
            'Hauptdiagonale: 19 + 32 + ___ = 96  →  ___ = 45.',
            'Nebendiagonale: 32 + 15 + ___ = 96  →  ___ = 49.',
            'Zeile 1: 19 + 49 + ___ = 96  →  ___ = 28.',
            'Zeile 3: 15 + 45 + ___ = 96  →  ___ = 36.',
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse3.schriftlich.addition",
            "mathe.klasse3.schriftlich.subtraktion",
            "mathe.klasse4.sachaufgaben.zahlenraetsel",
        ],
    },
    {
        "n": 4,
        "type": "Magisches Quadrat (3×3)",
        "text": (
            ' 23 | ___ | ___\n'
            '___ | ___ | ___\n'
            ' 20 | ___ |  23\n'
            'Mag. Zahl: 69'
        ),
        "answer": (
            ' 23 |  20 |  26\n'
            ' 26 |  23 |  20\n'
            ' 20 |  26 |  23'
        ),
        "steps": [
            'Mag. Zahl S = 69.',
            'Mitte = S ÷ 3 = 69 ÷ 3 = 23.',
            'Zeile 3: 20 + 23 + ___ = 69  →  ___ = 26.',
            'Spalte 1: 23 + 20 + ___ = 69  →  ___ = 26.',
            'Spalte 2: 23 + 26 + ___ = 69  →  ___ = 20.',
            'Nebendiagonale: 23 + 20 + ___ = 69  →  ___ = 26.',
            'Zeile 2: 26 + 23 + ___ = 69  →  ___ = 20.',
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse3.schriftlich.addition",
            "mathe.klasse3.schriftlich.subtraktion",
            "mathe.klasse4.sachaufgaben.zahlenraetsel",
        ],
    },
    {
        "n": 5,
        "type": "Magisches Quadrat (3×3)",
        "text": (
            '___ | ___ |  38\n'
            '___ |  28 | ___\n'
            '___ | ___ |  25\n'
            'Mag. Zahl: 84'
        ),
        "answer": (
            ' 31 |  15 |  38\n'
            ' 35 |  28 |  21\n'
            ' 18 |  41 |  25'
        ),
        "steps": [
            'Mag. Zahl S = 84.',
            'Mitte 28 bereits gegeben (S ÷ 3 = 28).',
            'Spalte 3: 38 + 25 + ___ = 84  →  ___ = 21.',
            'Hauptdiagonale: 28 + 25 + ___ = 84  →  ___ = 31.',
            'Nebendiagonale: 38 + 28 + ___ = 84  →  ___ = 18.',
            'Zeile 1: 31 + 38 + ___ = 84  →  ___ = 15.',
            'Zeile 2: 28 + 21 + ___ = 84  →  ___ = 35.',
            'Zeile 3: 18 + 25 + ___ = 84  →  ___ = 41.',
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse3.schriftlich.addition",
            "mathe.klasse3.schriftlich.subtraktion",
            "mathe.klasse4.sachaufgaben.zahlenraetsel",
        ],
    },
    {
        "n": 6,
        "type": "Magisches Quadrat (3×3)",
        "text": (
            ' 10 | ___ | ___\n'
            '___ |   7 | ___\n'
            '  8 | ___ |   4\n'
            'Mag. Zahl: 21'
        ),
        "answer": (
            ' 10 |   5 |   6\n'
            '  3 |   7 |  11\n'
            '  8 |   9 |   4'
        ),
        "steps": [
            'Mag. Zahl S = 21.',
            'Mitte 7 bereits gegeben (S ÷ 3 = 7).',
            'Zeile 3: 8 + 4 + ___ = 21  →  ___ = 9.',
            'Spalte 1: 10 + 8 + ___ = 21  →  ___ = 3.',
            'Spalte 2: 7 + 9 + ___ = 21  →  ___ = 5.',
            'Nebendiagonale: 7 + 8 + ___ = 21  →  ___ = 6.',
            'Zeile 2: 3 + 7 + ___ = 21  →  ___ = 11.',
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse3.schriftlich.addition",
            "mathe.klasse3.schriftlich.subtraktion",
            "mathe.klasse4.sachaufgaben.zahlenraetsel",
        ],
    },
    {
        "n": 7,
        "type": "Magisches Quadrat (3×3)",
        "text": (
            ' 41 | ___ | ___\n'
            '___ |  22 | ___\n'
            ' 22 | ___ |   3\n'
            'Mag. Zahl: 66'
        ),
        "answer": (
            ' 41 |   3 |  22\n'
            '  3 |  22 |  41\n'
            ' 22 |  41 |   3'
        ),
        "steps": [
            'Mag. Zahl S = 66.',
            'Mitte 22 bereits gegeben (S ÷ 3 = 22).',
            'Zeile 3: 22 + 3 + ___ = 66  →  ___ = 41.',
            'Spalte 1: 41 + 22 + ___ = 66  →  ___ = 3.',
            'Spalte 2: 22 + 41 + ___ = 66  →  ___ = 3.',
            'Nebendiagonale: 22 + 22 + ___ = 66  →  ___ = 22.',
            'Zeile 2: 3 + 22 + ___ = 66  →  ___ = 41.',
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse3.schriftlich.addition",
            "mathe.klasse3.schriftlich.subtraktion",
            "mathe.klasse4.sachaufgaben.zahlenraetsel",
        ],
    },
    {
        "n": 8,
        "type": "Magisches Quadrat (3×3)",
        "text": (
            '___ | ___ | ___\n'
            '___ |  25 | ___\n'
            '___ |   6 |  29\n'
            'Mag. Zahl: 75'
        ),
        "answer": (
            ' 21 |  44 |  10\n'
            ' 14 |  25 |  36\n'
            ' 40 |   6 |  29'
        ),
        "steps": [
            'Mag. Zahl S = 75.',
            'Mitte 25 bereits gegeben (S ÷ 3 = 25).',
            'Zeile 3: 6 + 29 + ___ = 75  →  ___ = 40.',
            'Spalte 2: 25 + 6 + ___ = 75  →  ___ = 44.',
            'Hauptdiagonale: 25 + 29 + ___ = 75  →  ___ = 21.',
            'Nebendiagonale: 25 + 40 + ___ = 75  →  ___ = 10.',
            'Spalte 1: 21 + 40 + ___ = 75  →  ___ = 14.',
            'Spalte 3: 10 + 29 + ___ = 75  →  ___ = 36.',
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse3.schriftlich.addition",
            "mathe.klasse3.schriftlich.subtraktion",
            "mathe.klasse4.sachaufgaben.zahlenraetsel",
        ],
    },
    {
        "n": 9,
        "type": "Magisches Quadrat (3×3)",
        "text": (
            ' 21 | ___ | ___\n'
            ' 43 | ___ |  17\n'
            ' 26 | ___ | ___\n'
            'Mag. Zahl: 90'
        ),
        "answer": (
            ' 21 |  35 |  34\n'
            ' 43 |  30 |  17\n'
            ' 26 |  25 |  39'
        ),
        "steps": [
            'Mag. Zahl S = 90.',
            'Mitte = S ÷ 3 = 90 ÷ 3 = 30.',
            'Hauptdiagonale: 21 + 30 + ___ = 90  →  ___ = 39.',
            'Nebendiagonale: 30 + 26 + ___ = 90  →  ___ = 34.',
            'Zeile 1: 21 + 34 + ___ = 90  →  ___ = 35.',
            'Zeile 3: 26 + 39 + ___ = 90  →  ___ = 25.',
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse3.schriftlich.addition",
            "mathe.klasse3.schriftlich.subtraktion",
            "mathe.klasse4.sachaufgaben.zahlenraetsel",
        ],
    },
]

NEW_KNOWLEDGE = [
    {
        "id": "mathe.klasse4.sachaufgaben.zahlenraetsel",
        "label": "Magische Quadrate (3×3)",
        "description": "3×3-Gitter, in dem jede Zeile, Spalte und Diagonale dieselbe Summe ergibt.",
        "parent": "mathe.klasse3",
    },
]
