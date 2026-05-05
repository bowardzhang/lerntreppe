EXERCISE = {
    "id": "MQA03",
    "subject": "Mathe",
    "grade": 3,
    "title": "Magische Quadrate A 03",
    "topic": "Magisches Quadrat 3\u00d73: Zeilen, Spalten und Diagonalen haben dieselbe Summe",
    "publisher": "CATLUX",
    "source_pdf": "Magische Quadrate A 03.pdf",
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
            '___ |  33 |  15\n'
            'Mag. Zahl: 90'
        ),
        "answer": (
            ' 45 |  27 |  18\n'
            '  3 |  30 |  57\n'
            ' 42 |  33 |  15'
        ),
        "steps": [
            'Mag. Zahl S = 90.',
            'Mitte 30 bereits gegeben (S ÷ 3 = 30).',
            'Zeile 3: 33 + 15 + ___ = 90  →  ___ = 42.',
            'Spalte 2: 30 + 33 + ___ = 90  →  ___ = 27.',
            'Hauptdiagonale: 30 + 15 + ___ = 90  →  ___ = 45.',
            'Nebendiagonale: 30 + 42 + ___ = 90  →  ___ = 18.',
            'Spalte 1: 45 + 42 + ___ = 90  →  ___ = 3.',
            'Spalte 3: 18 + 15 + ___ = 90  →  ___ = 57.',
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse3.schriftlich.addition",
            "mathe.klasse3.schriftlich.subtraktion",
            "mathe.klasse3.zahlenraetsel.magische_quadrate",
        ],
    },
    {
        "n": 2,
        "type": "Magisches Quadrat (3×3)",
        "text": (
            '  3 | ___ | ___\n'
            '___ |  18 | ___\n'
            ' 16 | ___ |  33\n'
            'Mag. Zahl: 54'
        ),
        "answer": (
            '  3 |  31 |  20\n'
            ' 35 |  18 |   1\n'
            ' 16 |   5 |  33'
        ),
        "steps": [
            'Mag. Zahl S = 54.',
            'Mitte 18 bereits gegeben (S ÷ 3 = 18).',
            'Zeile 3: 16 + 33 + ___ = 54  →  ___ = 5.',
            'Spalte 1: 3 + 16 + ___ = 54  →  ___ = 35.',
            'Spalte 2: 18 + 5 + ___ = 54  →  ___ = 31.',
            'Nebendiagonale: 18 + 16 + ___ = 54  →  ___ = 20.',
            'Zeile 2: 35 + 18 + ___ = 54  →  ___ = 1.',
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse3.schriftlich.addition",
            "mathe.klasse3.schriftlich.subtraktion",
            "mathe.klasse3.zahlenraetsel.magische_quadrate",
        ],
    },
    {
        "n": 3,
        "type": "Magisches Quadrat (3×3)",
        "text": (
            '___ | ___ |   9\n'
            '___ |  29 |  43\n'
            ' 49 | ___ | ___\n'
            'Mag. Zahl: 87'
        ),
        "answer": (
            ' 23 |  55 |   9\n'
            ' 15 |  29 |  43\n'
            ' 49 |   3 |  35'
        ),
        "steps": [
            'Mag. Zahl S = 87.',
            'Mitte 29 bereits gegeben (S ÷ 3 = 29).',
            'Zeile 2: 29 + 43 + ___ = 87  →  ___ = 15.',
            'Spalte 1: 15 + 49 + ___ = 87  →  ___ = 23.',
            'Spalte 3: 9 + 43 + ___ = 87  →  ___ = 35.',
            'Zeile 1: 23 + 9 + ___ = 87  →  ___ = 55.',
            'Zeile 3: 49 + 35 + ___ = 87  →  ___ = 3.',
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse3.schriftlich.addition",
            "mathe.klasse3.schriftlich.subtraktion",
            "mathe.klasse3.zahlenraetsel.magische_quadrate",
        ],
    },
    {
        "n": 4,
        "type": "Magisches Quadrat (3×3)",
        "text": (
            '___ | ___ |  15\n'
            '___ |  23 | ___\n'
            '___ | ___ |  24\n'
            'Mag. Zahl: 69'
        ),
        "answer": (
            ' 22 |  32 |  15\n'
            ' 16 |  23 |  30\n'
            ' 31 |  14 |  24'
        ),
        "steps": [
            'Mag. Zahl S = 69.',
            'Mitte 23 bereits gegeben (S ÷ 3 = 23).',
            'Spalte 3: 15 + 24 + ___ = 69  →  ___ = 30.',
            'Hauptdiagonale: 23 + 24 + ___ = 69  →  ___ = 22.',
            'Nebendiagonale: 15 + 23 + ___ = 69  →  ___ = 31.',
            'Zeile 1: 22 + 15 + ___ = 69  →  ___ = 32.',
            'Zeile 2: 23 + 30 + ___ = 69  →  ___ = 16.',
            'Zeile 3: 31 + 24 + ___ = 69  →  ___ = 14.',
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse3.schriftlich.addition",
            "mathe.klasse3.schriftlich.subtraktion",
            "mathe.klasse3.zahlenraetsel.magische_quadrate",
        ],
    },
    {
        "n": 5,
        "type": "Magisches Quadrat (3×3)",
        "text": (
            '  7 | ___ | ___\n'
            '___ | ___ | ___\n'
            ' 31 | ___ |  49\n'
            'Mag. Zahl: 84'
        ),
        "answer": (
            '  7 |  52 |  25\n'
            ' 46 |  28 |  10\n'
            ' 31 |   4 |  49'
        ),
        "steps": [
            'Mag. Zahl S = 84.',
            'Mitte = S ÷ 3 = 84 ÷ 3 = 28.',
            'Zeile 3: 31 + 49 + ___ = 84  →  ___ = 4.',
            'Spalte 1: 7 + 31 + ___ = 84  →  ___ = 46.',
            'Spalte 2: 28 + 4 + ___ = 84  →  ___ = 52.',
            'Nebendiagonale: 28 + 31 + ___ = 84  →  ___ = 25.',
            'Zeile 2: 46 + 28 + ___ = 84  →  ___ = 10.',
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse3.schriftlich.addition",
            "mathe.klasse3.schriftlich.subtraktion",
            "mathe.klasse3.zahlenraetsel.magische_quadrate",
        ],
    },
    {
        "n": 6,
        "type": "Magisches Quadrat (3×3)",
        "text": (
            ' 15 | ___ | ___\n'
            ' 16 | ___ |  18\n'
            ' 20 | ___ | ___\n'
            'Mag. Zahl: 51'
        ),
        "answer": (
            ' 15 |  22 |  14\n'
            ' 16 |  17 |  18\n'
            ' 20 |  12 |  19'
        ),
        "steps": [
            'Mag. Zahl S = 51.',
            'Mitte = S ÷ 3 = 51 ÷ 3 = 17.',
            'Hauptdiagonale: 15 + 17 + ___ = 51  →  ___ = 19.',
            'Nebendiagonale: 17 + 20 + ___ = 51  →  ___ = 14.',
            'Zeile 1: 15 + 14 + ___ = 51  →  ___ = 22.',
            'Zeile 3: 20 + 19 + ___ = 51  →  ___ = 12.',
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse3.schriftlich.addition",
            "mathe.klasse3.schriftlich.subtraktion",
            "mathe.klasse3.zahlenraetsel.magische_quadrate",
        ],
    },
    {
        "n": 7,
        "type": "Magisches Quadrat (3×3)",
        "text": (
            ' 21 | ___ | ___\n'
            '___ |  16 | ___\n'
            ' 16 | ___ |  11\n'
            'Mag. Zahl: 48'
        ),
        "answer": (
            ' 21 |  11 |  16\n'
            ' 11 |  16 |  21\n'
            ' 16 |  21 |  11'
        ),
        "steps": [
            'Mag. Zahl S = 48.',
            'Mitte 16 bereits gegeben (S ÷ 3 = 16).',
            'Zeile 3: 16 + 11 + ___ = 48  →  ___ = 21.',
            'Spalte 1: 21 + 16 + ___ = 48  →  ___ = 11.',
            'Spalte 2: 16 + 21 + ___ = 48  →  ___ = 11.',
            'Nebendiagonale: 16 + 16 + ___ = 48  →  ___ = 16.',
            'Zeile 2: 11 + 16 + ___ = 48  →  ___ = 21.',
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse3.schriftlich.addition",
            "mathe.klasse3.schriftlich.subtraktion",
            "mathe.klasse3.zahlenraetsel.magische_quadrate",
        ],
    },
    {
        "n": 8,
        "type": "Magisches Quadrat (3×3)",
        "text": (
            '___ | ___ |   7\n'
            '___ |  10 | ___\n'
            '___ | ___ |  10\n'
            'Mag. Zahl: 30'
        ),
        "answer": (
            ' 10 |  13 |   7\n'
            '  7 |  10 |  13\n'
            ' 13 |   7 |  10'
        ),
        "steps": [
            'Mag. Zahl S = 30.',
            'Mitte 10 bereits gegeben (S ÷ 3 = 10).',
            'Spalte 3: 7 + 10 + ___ = 30  →  ___ = 13.',
            'Hauptdiagonale: 10 + 10 + ___ = 30  →  ___ = 10.',
            'Nebendiagonale: 7 + 10 + ___ = 30  →  ___ = 13.',
            'Zeile 1: 10 + 7 + ___ = 30  →  ___ = 13.',
            'Zeile 2: 10 + 13 + ___ = 30  →  ___ = 7.',
            'Zeile 3: 13 + 10 + ___ = 30  →  ___ = 7.',
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse3.schriftlich.addition",
            "mathe.klasse3.schriftlich.subtraktion",
            "mathe.klasse3.zahlenraetsel.magische_quadrate",
        ],
    },
    {
        "n": 9,
        "type": "Magisches Quadrat (3×3)",
        "text": (
            ' 22 | ___ | ___\n'
            '  8 | ___ |  40\n'
            ' 42 | ___ | ___\n'
            'Mag. Zahl: 72'
        ),
        "answer": (
            ' 22 |  44 |   6\n'
            '  8 |  24 |  40\n'
            ' 42 |   4 |  26'
        ),
        "steps": [
            'Mag. Zahl S = 72.',
            'Mitte = S ÷ 3 = 72 ÷ 3 = 24.',
            'Hauptdiagonale: 22 + 24 + ___ = 72  →  ___ = 26.',
            'Nebendiagonale: 24 + 42 + ___ = 72  →  ___ = 6.',
            'Zeile 1: 22 + 6 + ___ = 72  →  ___ = 44.',
            'Zeile 3: 42 + 26 + ___ = 72  →  ___ = 4.',
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse3.schriftlich.addition",
            "mathe.klasse3.schriftlich.subtraktion",
            "mathe.klasse3.zahlenraetsel.magische_quadrate",
        ],
    },
]

NEW_KNOWLEDGE = []
