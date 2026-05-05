EXERCISE = {
    "id": "MQA04",
    "subject": "Mathe",
    "grade": 3,
    "title": "Magische Quadrate A 04",
    "topic": "Magisches Quadrat 3\u00d73: Zeilen, Spalten und Diagonalen haben dieselbe Summe",
    "publisher": "CATLUX",
    "source_pdf": "Magische Quadrate A 04.pdf",
    "answer_pdf": None,
    "total_points": 18.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Magisches Quadrat (3×3)",
        "text": (
            ' 13 | ___ | ___\n'
            '___ | ___ | ___\n'
            '  9 | ___ |   5\n'
            'Mag. Zahl: 27'
        ),
        "answer": (
            ' 13 |   5 |   9\n'
            '  5 |   9 |  13\n'
            '  9 |  13 |   5'
        ),
        "steps": [
            'Mag. Zahl S = 27.',
            'Mitte = S ÷ 3 = 27 ÷ 3 = 9.',
            'Zeile 3: 9 + 5 + ___ = 27  →  ___ = 13.',
            'Spalte 1: 13 + 9 + ___ = 27  →  ___ = 5.',
            'Spalte 2: 9 + 13 + ___ = 27  →  ___ = 5.',
            'Nebendiagonale: 9 + 9 + ___ = 27  →  ___ = 9.',
            'Zeile 2: 5 + 9 + ___ = 27  →  ___ = 13.',
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
            '___ | ___ |  10\n'
            '___ |  31 |  55\n'
            ' 52 | ___ | ___\n'
            'Mag. Zahl: 93'
        ),
        "answer": (
            ' 34 |  49 |  10\n'
            '  7 |  31 |  55\n'
            ' 52 |  13 |  28'
        ),
        "steps": [
            'Mag. Zahl S = 93.',
            'Mitte 31 bereits gegeben (S ÷ 3 = 31).',
            'Zeile 2: 31 + 55 + ___ = 93  →  ___ = 7.',
            'Spalte 1: 7 + 52 + ___ = 93  →  ___ = 34.',
            'Spalte 3: 10 + 55 + ___ = 93  →  ___ = 28.',
            'Zeile 1: 34 + 10 + ___ = 93  →  ___ = 49.',
            'Zeile 3: 52 + 28 + ___ = 93  →  ___ = 13.',
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
            ' 30 | ___ | ___\n'
            '  9 | ___ |  53\n'
            ' 54 | ___ | ___\n'
            'Mag. Zahl: 93'
        ),
        "answer": (
            ' 30 |  55 |   8\n'
            '  9 |  31 |  53\n'
            ' 54 |   7 |  32'
        ),
        "steps": [
            'Mag. Zahl S = 93.',
            'Mitte = S ÷ 3 = 93 ÷ 3 = 31.',
            'Hauptdiagonale: 30 + 31 + ___ = 93  →  ___ = 32.',
            'Nebendiagonale: 31 + 54 + ___ = 93  →  ___ = 8.',
            'Zeile 1: 30 + 8 + ___ = 93  →  ___ = 55.',
            'Zeile 3: 54 + 32 + ___ = 93  →  ___ = 7.',
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
            '___ | ___ |  27\n'
            '___ |  30 | ___\n'
            '___ | ___ |  19\n'
            'Mag. Zahl: 90'
        ),
        "answer": (
            ' 41 |  22 |  27\n'
            ' 16 |  30 |  44\n'
            ' 33 |  38 |  19'
        ),
        "steps": [
            'Mag. Zahl S = 90.',
            'Mitte 30 bereits gegeben (S ÷ 3 = 30).',
            'Spalte 3: 27 + 19 + ___ = 90  →  ___ = 44.',
            'Hauptdiagonale: 30 + 19 + ___ = 90  →  ___ = 41.',
            'Nebendiagonale: 27 + 30 + ___ = 90  →  ___ = 33.',
            'Zeile 1: 41 + 27 + ___ = 90  →  ___ = 22.',
            'Zeile 2: 30 + 44 + ___ = 90  →  ___ = 16.',
            'Zeile 3: 33 + 19 + ___ = 90  →  ___ = 38.',
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
            ' 22 | ___ | ___\n'
            '___ |  31 | ___\n'
            ' 18 | ___ |  40\n'
            'Mag. Zahl: 93'
        ),
        "answer": (
            ' 22 |  27 |  44\n'
            ' 53 |  31 |   9\n'
            ' 18 |  35 |  40'
        ),
        "steps": [
            'Mag. Zahl S = 93.',
            'Mitte 31 bereits gegeben (S ÷ 3 = 31).',
            'Zeile 3: 18 + 40 + ___ = 93  →  ___ = 35.',
            'Spalte 1: 22 + 18 + ___ = 93  →  ___ = 53.',
            'Spalte 2: 31 + 35 + ___ = 93  →  ___ = 27.',
            'Nebendiagonale: 31 + 18 + ___ = 93  →  ___ = 44.',
            'Zeile 2: 53 + 31 + ___ = 93  →  ___ = 9.',
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
            '___ | ___ | ___\n'
            '___ |  33 | ___\n'
            '___ |  15 |  41\n'
            'Mag. Zahl: 99'
        ),
        "answer": (
            ' 25 |  51 |  23\n'
            ' 31 |  33 |  35\n'
            ' 43 |  15 |  41'
        ),
        "steps": [
            'Mag. Zahl S = 99.',
            'Mitte 33 bereits gegeben (S ÷ 3 = 33).',
            'Zeile 3: 15 + 41 + ___ = 99  →  ___ = 43.',
            'Spalte 2: 33 + 15 + ___ = 99  →  ___ = 51.',
            'Hauptdiagonale: 33 + 41 + ___ = 99  →  ___ = 25.',
            'Nebendiagonale: 33 + 43 + ___ = 99  →  ___ = 23.',
            'Spalte 1: 25 + 43 + ___ = 99  →  ___ = 31.',
            'Spalte 3: 23 + 41 + ___ = 99  →  ___ = 35.',
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
            ' 18 | ___ | ___\n'
            ' 39 | ___ |  17\n'
            ' 27 | ___ | ___\n'
            'Mag. Zahl: 84'
        ),
        "answer": (
            ' 18 |  37 |  29\n'
            ' 39 |  28 |  17\n'
            ' 27 |  19 |  38'
        ),
        "steps": [
            'Mag. Zahl S = 84.',
            'Mitte = S ÷ 3 = 84 ÷ 3 = 28.',
            'Hauptdiagonale: 18 + 28 + ___ = 84  →  ___ = 38.',
            'Nebendiagonale: 28 + 27 + ___ = 84  →  ___ = 29.',
            'Zeile 1: 18 + 29 + ___ = 84  →  ___ = 37.',
            'Zeile 3: 27 + 38 + ___ = 84  →  ___ = 19.',
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
            ' 35 | ___ | ___\n'
            '___ |  31 | ___\n'
            ' 28 | ___ |  27\n'
            'Mag. Zahl: 93'
        ),
        "answer": (
            ' 35 |  24 |  34\n'
            ' 30 |  31 |  32\n'
            ' 28 |  38 |  27'
        ),
        "steps": [
            'Mag. Zahl S = 93.',
            'Mitte 31 bereits gegeben (S ÷ 3 = 31).',
            'Zeile 3: 28 + 27 + ___ = 93  →  ___ = 38.',
            'Spalte 1: 35 + 28 + ___ = 93  →  ___ = 30.',
            'Spalte 2: 31 + 38 + ___ = 93  →  ___ = 24.',
            'Nebendiagonale: 31 + 28 + ___ = 93  →  ___ = 34.',
            'Zeile 2: 30 + 31 + ___ = 93  →  ___ = 32.',
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
            '___ | ___ |  21\n'
            '___ |  16 |  12\n'
            ' 11 | ___ | ___\n'
            'Mag. Zahl: 48'
        ),
        "answer": (
            ' 17 |  10 |  21\n'
            ' 20 |  16 |  12\n'
            ' 11 |  22 |  15'
        ),
        "steps": [
            'Mag. Zahl S = 48.',
            'Mitte 16 bereits gegeben (S ÷ 3 = 16).',
            'Zeile 2: 16 + 12 + ___ = 48  →  ___ = 20.',
            'Spalte 1: 20 + 11 + ___ = 48  →  ___ = 17.',
            'Spalte 3: 21 + 12 + ___ = 48  →  ___ = 15.',
            'Zeile 1: 17 + 21 + ___ = 48  →  ___ = 10.',
            'Zeile 3: 11 + 15 + ___ = 48  →  ___ = 22.',
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
