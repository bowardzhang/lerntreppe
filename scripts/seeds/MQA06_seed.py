EXERCISE = {
    "id": "MQA06",
    "subject": "Mathe",
    "grade": 3,
    "title": "Magische Quadrate A 06",
    "topic": "Magisches Quadrat 3\u00d73: Zeilen, Spalten und Diagonalen haben dieselbe Summe",
    "publisher": "CATLUX",
    "source_pdf": "Magische Quadrate A 06.pdf",
    "answer_pdf": None,
    "total_points": 18.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Magisches Quadrat (3×3)",
        "text": (
            '___ | ___ |  49\n'
            '___ |  31 | ___\n'
            '___ | ___ |  30\n'
            'Mag. Zahl: 93'
        ),
        "answer": (
            ' 32 |  12 |  49\n'
            ' 48 |  31 |  14\n'
            ' 13 |  50 |  30'
        ),
        "steps": [
            'Mag. Zahl S = 93.',
            'Mitte 31 bereits gegeben (S ÷ 3 = 31).',
            'Spalte 3: 49 + 30 + ___ = 93  →  ___ = 14.',
            'Hauptdiagonale: 31 + 30 + ___ = 93  →  ___ = 32.',
            'Nebendiagonale: 49 + 31 + ___ = 93  →  ___ = 13.',
            'Zeile 1: 32 + 49 + ___ = 93  →  ___ = 12.',
            'Zeile 2: 31 + 14 + ___ = 93  →  ___ = 48.',
            'Zeile 3: 13 + 30 + ___ = 93  →  ___ = 50.',
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
            ' 13 | ___ | ___\n'
            '___ | ___ | ___\n'
            ' 16 | ___ |   9\n'
            'Mag. Zahl: 33'
        ),
        "answer": (
            ' 13 |  14 |   6\n'
            '  4 |  11 |  18\n'
            ' 16 |   8 |   9'
        ),
        "steps": [
            'Mag. Zahl S = 33.',
            'Mitte = S ÷ 3 = 33 ÷ 3 = 11.',
            'Zeile 3: 16 + 9 + ___ = 33  →  ___ = 8.',
            'Spalte 1: 13 + 16 + ___ = 33  →  ___ = 4.',
            'Spalte 2: 11 + 8 + ___ = 33  →  ___ = 14.',
            'Nebendiagonale: 11 + 16 + ___ = 33  →  ___ = 6.',
            'Zeile 2: 4 + 11 + ___ = 33  →  ___ = 18.',
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
            '___ | ___ | ___\n'
            '___ |  28 | ___\n'
            '___ |  26 |  24\n'
            'Mag. Zahl: 84'
        ),
        "answer": (
            ' 32 |  30 |  22\n'
            ' 18 |  28 |  38\n'
            ' 34 |  26 |  24'
        ),
        "steps": [
            'Mag. Zahl S = 84.',
            'Mitte 28 bereits gegeben (S ÷ 3 = 28).',
            'Zeile 3: 26 + 24 + ___ = 84  →  ___ = 34.',
            'Spalte 2: 28 + 26 + ___ = 84  →  ___ = 30.',
            'Hauptdiagonale: 28 + 24 + ___ = 84  →  ___ = 32.',
            'Nebendiagonale: 28 + 34 + ___ = 84  →  ___ = 22.',
            'Spalte 1: 32 + 34 + ___ = 84  →  ___ = 18.',
            'Spalte 3: 22 + 24 + ___ = 84  →  ___ = 38.',
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
            '___ | ___ |  37\n'
            '___ |  23 |   2\n'
            '  9 | ___ | ___\n'
            'Mag. Zahl: 69'
        ),
        "answer": (
            ' 16 |  16 |  37\n'
            ' 44 |  23 |   2\n'
            '  9 |  30 |  30'
        ),
        "steps": [
            'Mag. Zahl S = 69.',
            'Mitte 23 bereits gegeben (S ÷ 3 = 23).',
            'Zeile 2: 23 + 2 + ___ = 69  →  ___ = 44.',
            'Spalte 1: 44 + 9 + ___ = 69  →  ___ = 16.',
            'Spalte 3: 37 + 2 + ___ = 69  →  ___ = 30.',
            'Zeile 1: 16 + 37 + ___ = 69  →  ___ = 16.',
            'Zeile 3: 9 + 30 + ___ = 69  →  ___ = 30.',
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
            ' 21 | ___ | ___\n'
            ' 41 | ___ |  11\n'
            ' 16 | ___ | ___\n'
            'Mag. Zahl: 78'
        ),
        "answer": (
            ' 21 |  21 |  36\n'
            ' 41 |  26 |  11\n'
            ' 16 |  31 |  31'
        ),
        "steps": [
            'Mag. Zahl S = 78.',
            'Mitte = S ÷ 3 = 78 ÷ 3 = 26.',
            'Hauptdiagonale: 21 + 26 + ___ = 78  →  ___ = 31.',
            'Nebendiagonale: 26 + 16 + ___ = 78  →  ___ = 36.',
            'Zeile 1: 21 + 36 + ___ = 78  →  ___ = 21.',
            'Zeile 3: 16 + 31 + ___ = 78  →  ___ = 31.',
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
            '___ |  30 | ___\n'
            ' 26 | ___ |  50\n'
            'Mag. Zahl: 90'
        ),
        "answer": (
            ' 10 |  46 |  34\n'
            ' 54 |  30 |   6\n'
            ' 26 |  14 |  50'
        ),
        "steps": [
            'Mag. Zahl S = 90.',
            'Mitte 30 bereits gegeben (S ÷ 3 = 30).',
            'Zeile 3: 26 + 50 + ___ = 90  →  ___ = 14.',
            'Spalte 1: 10 + 26 + ___ = 90  →  ___ = 54.',
            'Spalte 2: 30 + 14 + ___ = 90  →  ___ = 46.',
            'Nebendiagonale: 30 + 26 + ___ = 90  →  ___ = 34.',
            'Zeile 2: 54 + 30 + ___ = 90  →  ___ = 6.',
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
            '___ | ___ | ___\n'
            '___ |  29 | ___\n'
            '___ |  48 |  25\n'
            'Mag. Zahl: 87'
        ),
        "answer": (
            ' 33 |  10 |  44\n'
            ' 40 |  29 |  18\n'
            ' 14 |  48 |  25'
        ),
        "steps": [
            'Mag. Zahl S = 87.',
            'Mitte 29 bereits gegeben (S ÷ 3 = 29).',
            'Zeile 3: 48 + 25 + ___ = 87  →  ___ = 14.',
            'Spalte 2: 29 + 48 + ___ = 87  →  ___ = 10.',
            'Hauptdiagonale: 29 + 25 + ___ = 87  →  ___ = 33.',
            'Nebendiagonale: 29 + 14 + ___ = 87  →  ___ = 44.',
            'Spalte 1: 33 + 14 + ___ = 87  →  ___ = 40.',
            'Spalte 3: 44 + 25 + ___ = 87  →  ___ = 18.',
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
            '  6 | ___ | ___\n'
            '___ |  17 | ___\n'
            ' 20 | ___ |  28\n'
            'Mag. Zahl: 51'
        ),
        "answer": (
            '  6 |  31 |  14\n'
            ' 25 |  17 |   9\n'
            ' 20 |   3 |  28'
        ),
        "steps": [
            'Mag. Zahl S = 51.',
            'Mitte 17 bereits gegeben (S ÷ 3 = 17).',
            'Zeile 3: 20 + 28 + ___ = 51  →  ___ = 3.',
            'Spalte 1: 6 + 20 + ___ = 51  →  ___ = 25.',
            'Spalte 2: 17 + 3 + ___ = 51  →  ___ = 31.',
            'Nebendiagonale: 17 + 20 + ___ = 51  →  ___ = 14.',
            'Zeile 2: 25 + 17 + ___ = 51  →  ___ = 9.',
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
            '___ | ___ |  41\n'
            '___ |  25 |   2\n'
            '  9 | ___ | ___\n'
            'Mag. Zahl: 75'
        ),
        "answer": (
            ' 18 |  16 |  41\n'
            ' 48 |  25 |   2\n'
            '  9 |  34 |  32'
        ),
        "steps": [
            'Mag. Zahl S = 75.',
            'Mitte 25 bereits gegeben (S ÷ 3 = 25).',
            'Zeile 2: 25 + 2 + ___ = 75  →  ___ = 48.',
            'Spalte 1: 48 + 9 + ___ = 75  →  ___ = 18.',
            'Spalte 3: 41 + 2 + ___ = 75  →  ___ = 32.',
            'Zeile 1: 18 + 41 + ___ = 75  →  ___ = 16.',
            'Zeile 3: 9 + 32 + ___ = 75  →  ___ = 34.',
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

NEW_KNOWLEDGE = []
