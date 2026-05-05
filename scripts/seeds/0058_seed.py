EXERCISE = {
    "id": "0058",
    "subject": "Mathe",
    "grade": 4,
    "title": "4. Lernzielkontrolle – Zahlenreihen, Verteilungsaufgaben, Zahlenrätsel",
    "topic": "Zahlenreihen, Verteilungsaufgaben, Zahlenrätsel",
    "publisher": "CATLUX",
    "source_pdf": "0058.pdf",
    "answer_pdf": "0058 (1).pdf",
    "total_points": 38.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Zahlenreihe fortsetzen",
        "text": (
            "Führe jede Zahlenreihe um zwei Glieder fort!\n"
            "a) 3; 5; 8; 12; 17; 23; 30; _________ _________\n"
            "b) 70; 68; 64; 62; 58; 56; 52; _________ _________\n"
            "c) 1; 2; 6; 12; 36; 72; 216; _________ _________"
        ),
        "answer": (
            "a) 38; 47\n"
            "b) 50; 46\n"
            "c) 432; 1296"
        ),
        "steps": [
            "a) Differenzen: +2, +3, +4, +5, +6, +7 → Muster: jeweils +1 mehr; 30+8=38, 38+9=47",
            "b) Muster: –2, –4 abwechselnd; 52–2=50, 50–4=46",
            "c) Muster: ×2, ×3 abwechselnd; 216×2=432, 432×3=1296",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.zahlen1000000.zahlenfolgen",
        ],
    },
    {
        "n": 2,
        "type": "Sachaufgabe Gewicht",
        "text": (
            "Florian ist um 8 kg leichter als Felix. Max und Sabine wiegen jeweils genauso viel\n"
            "wie Felix. Wie schwer ist jeder, wenn alle zusammen 152 kg wiegen?"
        ),
        "answer": (
            "Felix, Max und Sabine wiegen je 40 kg, Florian wiegt 32 kg."
        ),
        "steps": [
            "Florian = Felix – 8 kg; Max = Felix; Sabine = Felix",
            "Gesamt: Felix + Felix + Felix + (Felix – 8) = 152",
            "4 × Felix – 8 = 152 → 4 × Felix = 160 → Felix = 40 kg",
            "Florian = 40 – 8 = 32 kg",
            "Antwort: Felix, Max, Sabine je 40 kg; Florian 32 kg",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.sachaufgaben.zahlenraetsel",
        ],
    },
    {
        "n": 3,
        "type": "Rechenausdruck berechnen",
        "text": (
            "Zähle zu der Zahl 2736 den 8. Teil von 36728 und vervielfache das Ergebnis mit 18!"
        ),
        "answer": "131886",
        "steps": [
            "36728 ÷ 8 = 4591",
            "2736 + 4591 = 7327",
            "7327 × 18 = 131886",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.schriftlich.multiplikation",
            "mathe.klasse4.schriftlich.division",
        ],
    },
    {
        "n": 4,
        "type": "Verteilungsaufgabe",
        "text": (
            "In einer Packung sind 146 Bonbons. Sie werden auf die vier Kinder Richard, Marlon,\n"
            "Amadeus und Eleni verteilt. Dabei erhalten die Jungen jeweils gleich viele, während\n"
            "Eleni 10 Bonbons weniger als jeder Junge bekommt.\n"
            "Wie viele Bonbons bekommt jeder?"
        ),
        "answer": (
            "Jeder Junge erhält 39 Bonbons, Eleni erhält 29 Bonbons."
        ),
        "steps": [
            "Elenis Anteil angleichen: 146 + 10 = 156 (als ob alle gleich viel hätten)",
            "156 ÷ 4 = 39 Bonbons pro Junge",
            "Eleni: 39 – 10 = 29 Bonbons",
            "Probe: 3 × 39 + 29 = 117 + 29 = 146 ✓",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.schriftlich.division",
        ],
    },
    {
        "n": 5,
        "type": "Geldaufteilung",
        "text": (
            "Die beiden Freunde Sabrina und Florian haben zusammen 160 € gespart. Nun wollen\n"
            "sie ihr Sparbuch auflösen und das Geld aufteilen. Dabei erhält Sabrina dreimal so\n"
            "viel wie Florian. Wie viel Geld bekommt jeder?"
        ),
        "answer": (
            "Sabrina erhält 120 €, Florian erhält 40 €."
        ),
        "steps": [
            "Teile: Sabrina = 3 Teile, Florian = 1 Teil → gesamt 4 Teile",
            "1 Teil = 160 € ÷ 4 = 40 €",
            "Florian: 1 × 40 € = 40 €",
            "Sabrina: 3 × 40 € = 120 €",
            "Probe: 120 + 40 = 160 € ✓",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.sachaufgaben.zahlenraetsel",
        ],
    },
    {
        "n": 6,
        "type": "Division mit Rest",
        "text": (
            "Teilt man eine Zahl durch 13, so erhält man 7 und den Rest 9.\n"
            "Wie heißt die Zahl?"
        ),
        "answer": "Die Zahl ist 100.",
        "steps": [
            "13 × 7 = 91",
            "91 + 9 = 100",
            "Probe: 100 ÷ 13 = 7 Rest 9 ✓",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.schriftlich.division",
            "mathe.klasse4.sachaufgaben.umkehraufgaben",
        ],
    },
    {
        "n": 7,
        "type": "Zahlenrätsel drei Zahlen",
        "text": (
            "Drei Zahlen ergeben zusammen 100000. Eine Zahl heißt 27396. Sie ist genau\n"
            "dreimal so groß wie die kleinste Zahl. Wie heißen die drei Zahlen?"
        ),
        "answer": (
            "1. Zahl: 27396\n"
            "Kleinste Zahl: 9132\n"
            "3. Zahl: 63472"
        ),
        "steps": [
            "1. Zahl (gegeben): 27396",
            "Kleinste Zahl: 27396 ÷ 3 = 9132",
            "Zwischensumme: 27396 + 9132 = 36528",
            "3. Zahl: 100000 – 36528 = 63472",
            "Probe: 27396 + 9132 + 63472 = 100000 ✓",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.zahlenraetsel",
            "mathe.klasse4.schriftlich.division",
        ],
    },
    {
        "n": 8,
        "type": "Sachaufgabe Alter",
        "text": (
            "Familie Huber hat zwei Kinder, Luisa und Peter. Peter ist doppelt so alt wie Luisa,\n"
            "aber nur halb so alt wie Vater. Die Mutter ist fünf Jahre jünger als der Vater.\n"
            "Zusammen sind sie 105 Jahre alt. Peter feiert gerade seinen zwanzigsten Geburtstag.\n"
            "Wie alt sind die Familienmitglieder?"
        ),
        "answer": (
            "Peter: 20 Jahre\n"
            "Luisa: 10 Jahre\n"
            "Vater: 40 Jahre\n"
            "Mutter: 35 Jahre"
        ),
        "steps": [
            "Peter = 20 (gegeben)",
            "Luisa = Peter ÷ 2 = 20 ÷ 2 = 10",
            "Vater = Peter × 2 = 20 × 2 = 40",
            "Mutter = Vater – 5 = 40 – 5 = 35",
            "Probe: 20 + 10 + 40 + 35 = 105 ✓",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.sachaufgaben.zahlenraetsel",
        ],
    },
    {
        "n": 9,
        "type": "Schaubild erstellen",
        "text": (
            "Stelle als Schaubild dar: 850 g Brot, 500 g Müsli, 350 g Wurst, 250 g Butter,\n"
            "1000 g Zucker! Vergiss die Beschriftung nicht!"
        ),
        "answer": (
            "Balkendiagramm mit y-Achse (Gramm, bis mind. 1000 g) und x-Achse (Lebensmittel).\n"
            "Balken: Brot 850 g, Müsli 500 g, Wurst 350 g, Butter 250 g, Zucker 1000 g.\n"
            "Achsen beschriftet."
        ),
        "steps": [
            "Achsen einzeichnen: y-Achse = Gramm (Skalierung z.B. 0–1200 in 200er-Schritten), x-Achse = Lebensmittel",
            "Für jedes Lebensmittel einen Balken bis zur entsprechenden Grammzahl zeichnen",
            "Balken und Achsen beschriften",
        ],
        "points": 10.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.tabellen",
        ],
    },
]

NEW_KNOWLEDGE = []
