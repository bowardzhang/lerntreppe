EXERCISE = {
    "id": "MQA05",
    "subject": "Mathe",
    "grade": 3,
    "title": "Magische Quadrate A 05",
    "topic": "Magisches Quadrat 3\u00d73: Zeilen, Spalten und Diagonalen haben dieselbe Summe",
    "publisher": "CATLUX",
    "source_pdf": "Magische Quadrate A 05.pdf",
    "answer_pdf": None,
    "total_points": 18.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Magisches Quadrat (3×3)",
        "text": (
            ' 33 | ___ | ___\n'
            '___ |  23 | ___\n'
            ' 29 | ___ |  13\n'
            'Mag. Zahl: 69'
        ),
        "answer": (
            ' 33 |  19 |  17\n'
            '  7 |  23 |  39\n'
            ' 29 |  27 |  13'
        ),
        "steps": [
            'Mag. Zahl S = 69.',
            'Mitte 23 bereits gegeben (S ÷ 3 = 23).',
            'Zeile 3: 29 + 13 + ___ = 69  →  ___ = 27.',
            'Spalte 1: 33 + 29 + ___ = 69  →  ___ = 7.',
            'Spalte 2: 23 + 27 + ___ = 69  →  ___ = 19.',
            'Nebendiagonale: 23 + 29 + ___ = 69  →  ___ = 17.',
            'Zeile 2: 7 + 23 + ___ = 69  →  ___ = 39.',
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
            '___ | ___ |   5\n'
            '___ |  23 | ___\n'
            '___ | ___ |  22\n'
            'Mag. Zahl: 69'
        ),
        "answer": (
            ' 24 |  40 |   5\n'
            '  4 |  23 |  42\n'
            ' 41 |   6 |  22'
        ),
        "steps": [
            'Mag. Zahl S = 69.',
            'Mitte 23 bereits gegeben (S ÷ 3 = 23).',
            'Spalte 3: 5 + 22 + ___ = 69  →  ___ = 42.',
            'Hauptdiagonale: 23 + 22 + ___ = 69  →  ___ = 24.',
            'Nebendiagonale: 5 + 23 + ___ = 69  →  ___ = 41.',
            'Zeile 1: 24 + 5 + ___ = 69  →  ___ = 40.',
            'Zeile 2: 23 + 42 + ___ = 69  →  ___ = 4.',
            'Zeile 3: 41 + 22 + ___ = 69  →  ___ = 6.',
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
            ' 28 | ___ | ___\n'
            '___ | ___ | ___\n'
            ' 59 | ___ |  36\n'
            'Mag. Zahl: 96'
        ),
        "answer": (
            ' 28 |  63 |   5\n'
            '  9 |  32 |  55\n'
            ' 59 |   1 |  36'
        ),
        "steps": [
            'Mag. Zahl S = 96.',
            'Mitte = S ÷ 3 = 96 ÷ 3 = 32.',
            'Zeile 3: 59 + 36 + ___ = 96  →  ___ = 1.',
            'Spalte 1: 28 + 59 + ___ = 96  →  ___ = 9.',
            'Spalte 2: 32 + 1 + ___ = 96  →  ___ = 63.',
            'Nebendiagonale: 32 + 59 + ___ = 96  →  ___ = 5.',
            'Zeile 2: 9 + 32 + ___ = 96  →  ___ = 55.',
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
            '___ | ___ |   8\n'
            '___ |  31 |  52\n'
            ' 54 | ___ | ___\n'
            'Mag. Zahl: 93'
        ),
        "answer": (
            ' 29 |  56 |   8\n'
            ' 10 |  31 |  52\n'
            ' 54 |   6 |  33'
        ),
        "steps": [
            'Mag. Zahl S = 93.',
            'Mitte 31 bereits gegeben (S ÷ 3 = 31).',
            'Zeile 2: 31 + 52 + ___ = 93  →  ___ = 10.',
            'Spalte 1: 10 + 54 + ___ = 93  →  ___ = 29.',
            'Spalte 3: 8 + 52 + ___ = 93  →  ___ = 33.',
            'Zeile 1: 29 + 8 + ___ = 93  →  ___ = 56.',
            'Zeile 3: 54 + 33 + ___ = 93  →  ___ = 6.',
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
            '___ | ___ | ___\n'
            '___ |  21 | ___\n'
            '___ |  22 |  20\n'
            'Mag. Zahl: 63'
        ),
        "answer": (
            ' 22 |  20 |  21\n'
            ' 20 |  21 |  22\n'
            ' 21 |  22 |  20'
        ),
        "steps": [
            'Mag. Zahl S = 63.',
            'Mitte 21 bereits gegeben (S ÷ 3 = 21).',
            'Zeile 3: 22 + 20 + ___ = 63  →  ___ = 21.',
            'Spalte 2: 21 + 22 + ___ = 63  →  ___ = 20.',
            'Hauptdiagonale: 21 + 20 + ___ = 63  →  ___ = 22.',
            'Nebendiagonale: 21 + 21 + ___ = 63  →  ___ = 21.',
            'Spalte 1: 22 + 21 + ___ = 63  →  ___ = 20.',
            'Spalte 3: 21 + 20 + ___ = 63  →  ___ = 22.',
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
            ' 25 | ___ | ___\n'
            ' 51 | ___ |  15\n'
            ' 23 | ___ | ___\n'
            'Mag. Zahl: 99'
        ),
        "answer": (
            ' 25 |  31 |  43\n'
            ' 51 |  33 |  15\n'
            ' 23 |  35 |  41'
        ),
        "steps": [
            'Mag. Zahl S = 99.',
            'Mitte = S ÷ 3 = 99 ÷ 3 = 33.',
            'Hauptdiagonale: 25 + 33 + ___ = 99  →  ___ = 41.',
            'Nebendiagonale: 33 + 23 + ___ = 99  →  ___ = 43.',
            'Zeile 1: 25 + 43 + ___ = 99  →  ___ = 31.',
            'Zeile 3: 23 + 41 + ___ = 99  →  ___ = 35.',
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
            '___ | ___ | ___\n'
            '___ |  26 | ___\n'
            '___ |  23 |  15\n'
            'Mag. Zahl: 78'
        ),
        "answer": (
            ' 37 |  29 |  12\n'
            '  1 |  26 |  51\n'
            ' 40 |  23 |  15'
        ),
        "steps": [
            'Mag. Zahl S = 78.',
            'Mitte 26 bereits gegeben (S ÷ 3 = 26).',
            'Zeile 3: 23 + 15 + ___ = 78  →  ___ = 40.',
            'Spalte 2: 26 + 23 + ___ = 78  →  ___ = 29.',
            'Hauptdiagonale: 26 + 15 + ___ = 78  →  ___ = 37.',
            'Nebendiagonale: 26 + 40 + ___ = 78  →  ___ = 12.',
            'Spalte 1: 37 + 40 + ___ = 78  →  ___ = 1.',
            'Spalte 3: 12 + 15 + ___ = 78  →  ___ = 51.',
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
            ' 28 | ___ | ___\n'
            ' 11 | ___ |  33\n'
            ' 27 | ___ | ___\n'
            'Mag. Zahl: 66'
        ),
        "answer": (
            ' 28 |  21 |  17\n'
            ' 11 |  22 |  33\n'
            ' 27 |  23 |  16'
        ),
        "steps": [
            'Mag. Zahl S = 66.',
            'Mitte = S ÷ 3 = 66 ÷ 3 = 22.',
            'Hauptdiagonale: 28 + 22 + ___ = 66  →  ___ = 16.',
            'Nebendiagonale: 22 + 27 + ___ = 66  →  ___ = 17.',
            'Zeile 1: 28 + 17 + ___ = 66  →  ___ = 21.',
            'Zeile 3: 27 + 16 + ___ = 66  →  ___ = 23.',
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
            '___ | ___ |  31\n'
            '___ |  26 | ___\n'
            '___ | ___ |  29\n'
            'Mag. Zahl: 78'
        ),
        "answer": (
            ' 23 |  24 |  31\n'
            ' 34 |  26 |  18\n'
            ' 21 |  28 |  29'
        ),
        "steps": [
            'Mag. Zahl S = 78.',
            'Mitte 26 bereits gegeben (S ÷ 3 = 26).',
            'Spalte 3: 31 + 29 + ___ = 78  →  ___ = 18.',
            'Hauptdiagonale: 26 + 29 + ___ = 78  →  ___ = 23.',
            'Nebendiagonale: 31 + 26 + ___ = 78  →  ___ = 21.',
            'Zeile 1: 23 + 31 + ___ = 78  →  ___ = 24.',
            'Zeile 2: 26 + 18 + ___ = 78  →  ___ = 34.',
            'Zeile 3: 21 + 29 + ___ = 78  →  ___ = 28.',
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
