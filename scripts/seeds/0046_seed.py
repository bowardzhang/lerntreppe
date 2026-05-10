EXERCISE = {
    "id": "0046",
    "subject": "Mathe",
    "grade": 4,
    "title": "Probeunterricht: Text- und Verteilungsaufgaben",
    "topic": "Sachaufgaben, mehrstufiges Rechnen, Größen, Geld, Längen, Zeit",
    "publisher": "CATLUX",
    "source_pdf": "0046.pdf",
    "answer_pdf": "0046 (1).pdf",
    "total_points": 22.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Verteilungsaufgabe (Gummibaerchen)",
        "text": (
            "Tom, Ralf und Sabine teilen 216 Gummibaerchen gerecht unter sich auf.\n"
            "a) Wie viele Gummibaerchen erhaelt jedes Kind?\n"
            "b) Sabine bekommt 15 Gummibaerchen mehr als Tom und Ralf. "
            "Wie viele bekommt jedes Kind nun?"
        ),
        "answer": (
            "a) 216 : 3 = 72 Gummibaerchen pro Kind. "
            "b) (216 - 15) : 3 = 201 : 3 = 67 ; Tom 67, Ralf 67, Sabine 67 + 15 = 82."
        ),
        "steps": [
            "a) Gleichmaessige Verteilung: 216 : 3 = 72.",
            "b) Sabines Bonus abziehen: 216 - 15 = 201.",
            "201 : 3 = 67 (Tom und Ralf).",
            "Sabine: 67 + 15 = 82.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
        ],
    },
    {
        "n": 2,
        "type": "Klassenverteilung",
        "text": (
            "In der Klasse 4a sind 27 Kinder. Es sind 3 Jungen mehr als Maedchen. "
            "Wie viele Maedchen und wie viele Jungen sind in der Klasse?"
        ),
        "answer": "12 Maedchen und 15 Jungen.",
        "steps": [
            "27 - 3 = 24.",
            "24 : 2 = 12 Maedchen.",
            "12 + 3 = 15 Jungen.",
            "Probe: 12 + 15 = 27.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
        ],
    },
    {
        "n": 3,
        "type": "Gewichtsaufgabe",
        "text": (
            "Tim, Tom, Mark und Florian wiegen zusammen 170 kg. "
            "Tom, Mark und Florian wiegen alle gleich viel. Tim wiegt 10 kg mehr "
            "als jeder der anderen drei. Wie viel wiegt jeder?"
        ),
        "answer": "Tom, Mark, Florian je 40 kg ; Tim 50 kg.",
        "steps": [
            "170 - 10 = 160 kg (4 gleiche Anteile).",
            "160 : 4 = 40 kg (Tom, Mark, Florian).",
            "Tim: 40 + 10 = 50 kg.",
            "Probe: 40 + 40 + 40 + 50 = 170 kg.",
        ],
        "points": 1.5,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.groessen.gewicht",
        ],
    },
    {
        "n": 4,
        "type": "Rohrleitung",
        "text": (
            "Eine Rohrleitung hat zwei gleich lange Teile von je 50 m und 37 m. "
            "Insgesamt sollen 12 m abgezogen und der Rest in 6 gleich lange "
            "Stuecke geteilt werden. Wie lang ist jedes Stueck?"
        ),
        "answer": "27 m pro Stueck.",
        "steps": [
            "Gesamtlaenge: (50 + 37) · 2 = 174 m.",
            "Abzug: 174 - 12 = 162 m.",
            "162 : 6 = 27 m pro Stueck.",
        ],
        "points": 1.5,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.groessen.laenge",
        ],
    },
    {
        "n": 5,
        "type": "Kilometergeld",
        "text": (
            "Vater fährt 480 km zu seiner Schwester. Bei der Rueckfahrt fehlen "
            "noch 240 km. Pro 80 km bekommt er 14 Euro Kilometergeld. "
            "Wie viel Euro erhaelt er insgesamt?"
        ),
        "answer": "126 Euro.",
        "steps": [
            "Gesamtstrecke: 480 + 240 = 720 km.",
            "720 : 80 = 9 (Achtzig-Kilometer-Abschnitte).",
            "9 · 14 = 126 Euro.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.groessen.geld",
            "mathe.klasse4.groessen.laenge",
        ],
    },
    {
        "n": 6,
        "type": "Theaterbestuhlung",
        "text": (
            "In der ersten Reihe sind 27 Plaetze, jede weitere Reihe hat 6 Plaetze "
            "mehr als die vorherige.\n"
            "a) Wie viele Plaetze sind in der 7. Reihe?\n"
            "b) Im Theater sind insgesamt 2499 Plaetze. Wie viele Plaetze sind "
            "in der letzten Reihe, wenn 9 Reihen weniger waeren?"
        ),
        "answer": (
            "a) 27 + 6·6 = 63 Plaetze. "
            "b) 27 · 9 = 243 ; 2499 - 243 = 2256 ; 2256 : 6 = 376 ; "
            "letzte Reihe = 27 + 6·k mit Gesamtsumme 2499."
        ),
        "steps": [
            "a) Differenzfolge: Reihe n hat 27 + (n-1)·6 Plaetze.",
            "Reihe 7: 27 + 6·6 = 63.",
            "b) Aufgabe als Naeherung: 27 · 9 = 243 ; 2499 - 243 = 2256.",
            "Bei stetigem Zuwachs: Anzahl Reihen ergibt sich aus Mittelwertberechnung.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
        ],
    },
    {
        "n": 7,
        "type": "Schulfest-Gewinn",
        "text": (
            "Die Klasse hat für das Schulfest eingekauft: 35 Becher Limonade zu "
            "je 80 Cent (= 28,00 Euro), 50 Brezen zu je 60 Cent (= 30,00 Euro), "
            "20 Wuerstchen zu je 1,40 Euro (= 28,00 Euro), Sonstiges 0,80 Euro. "
            "Verkauft wurden alle Speisen mit 25 Euro Gewinn auf Limonade, 20 Euro "
            "Gewinn auf Brezen, 18 Euro auf Wuerstchen, abzueglich Reste. "
            "Wie hoch ist der Gewinn (Beispielrechnung)?"
        ),
        "answer": (
            "Ausgaben: 28,00 + 30,00 + 28,00 + 0,80 = 86,80 Euro. "
            "Einnahmen (Beispiel): 175,00 Euro. "
            "Gewinn = 175,00 - 86,80 = 88,20 Euro."
        ),
        "steps": [
            "Ausgaben aufsummieren: 86,80 Euro.",
            "Einnahmen aufsummieren (Beispielwert).",
            "Gewinn = Einnahmen - Ausgaben.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.groessen.geld",
        ],
    },
    {
        "n": 8,
        "type": "Familienalter",
        "text": (
            "Familie Huber: Peter ist doppelt so alt wie Luisa. Vater ist doppelt "
            "so alt wie Peter, Mutter ist 5 Jahre juenger als Vater. Zusammen sind "
            "sie 105 Jahre alt. Wie alt ist jeder?"
        ),
        "answer": "Luisa 10, Peter 20, Vater 40, Mutter 35.",
        "steps": [
            "Sei Luisa = x. Dann Peter = 2x, Vater = 4x, Mutter = 4x - 5.",
            "Summe: x + 2x + 4x + 4x - 5 = 11x - 5 = 105.",
            "11x = 110 ; x = 10.",
            "Luisa 10, Peter 20, Vater 40, Mutter 35.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
        ],
    },
    {
        "n": 9,
        "type": "Sticker-Paeckchen",
        "text": (
            "Jan kauft 145 Sticker-Paeckchen zu je 30 Cent. Zwei Paeckchen "
            "spendiert ihm der Verkaeufer dazu (also 145 zahlbar). "
            "Berechne die Gesamtkosten und die Anzahl der Paeckchen."
        ),
        "answer": "145 Paeckchen, Gesamtkosten: 145 · 0,30 = 43,50 Euro plus 2 gratis = 147 Paeckchen.",
        "steps": [
            "Gesamtkosten: 145 · 30 Cent = 4350 Cent = 43,50 Euro.",
            "Anzahl Paeckchen: 145 + 2 = 147.",
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
        "n": 10,
        "type": "Bootsfahrt",
        "text": (
            "Ein Ausflugsboot hat Platz für 27 Personen. Bei voller Belegung "
            "fährt das Boot 4 Mal. Wie viele Personen wurden insgesamt befoerdert?"
        ),
        "answer": "27 · 4 = 108 Personen.",
        "steps": [
            "27 Personen pro Fahrt.",
            "27 · 4 = 108 Personen.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
        ],
    },
    {
        "n": 11,
        "type": "Leitposten an Strecke",
        "text": (
            "Eine Strecke ist 2000 m lang. Alle 200 m steht auf jeder Seite ein "
            "Leitposten (auch am Anfang und am Ende). Wie viele Leitposten sind "
            "es insgesamt?"
        ),
        "answer": "(2000 : 200 + 1) · 2 = 11 · 2 = 22 Leitposten.",
        "steps": [
            "Anzahl pro Seite: 2000 : 200 = 10 Abschnitte ; 10 + 1 = 11 Posten.",
            "Beide Seiten: 11 · 2 = 22 Leitposten.",
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
        "n": 12,
        "type": "Plaetzchenteig",
        "text": (
            "Mama backt aus 1 kg Mehl, 500 g Butter und 250 g Zucker Plaetzchen. "
            "Wie viel Gramm Teig hat sie ungefaehr (ohne Wasserverlust)?"
        ),
        "answer": "1000 + 500 + 250 = 1750 g = 1 kg 750 g.",
        "steps": [
            "1 kg = 1000 g.",
            "1000 + 500 + 250 = 1750 g.",
            "Umrechnung: 1750 g = 1 kg 750 g.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.groessen.gewicht",
        ],
    },
    {
        "n": 13,
        "type": "Schulweg",
        "text": (
            "Ben braucht zur Schule 12 Minuten. Er geht von Montag bis Freitag "
            "morgens hin und mittags zurück. Wie viele Minuten ist er pro Woche "
            "unterwegs? Rechne in Stunden und Minuten um."
        ),
        "answer": "12 · 2 · 5 = 120 Minuten = 2 Stunden.",
        "steps": [
            "Pro Tag: 12 + 12 = 24 Minuten.",
            "Pro Woche: 24 · 5 = 120 Minuten.",
            "120 Minuten = 2 Stunden.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.groessen.zeit",
            "mathe.klasse4.sachaufgaben.mehrstufig",
        ],
    },
    {
        "n": 14,
        "type": "Park-Baeume",
        "text": (
            "In einem Park werden entlang eines 400 m langen Weges alle 8 m "
            "Baeume gepflanzt (am Anfang und am Ende ein Baum). "
            "Wie viele Baeume werden gepflanzt?"
        ),
        "answer": "400 : 8 + 1 = 51 Baeume.",
        "steps": [
            "400 : 8 = 50 Abschnitte.",
            "Anzahl Baeume = Abschnitte + 1 = 51.",
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
        "n": 15,
        "type": "Hamburg-Fahrt",
        "text": (
            "Familie Schmitt fährt 720 km nach Hamburg. Sie machen nach 2/3 "
            "der Strecke eine Pause. Wie viele Kilometer sind sie schon gefahren "
            "und wie viele bleiben?"
        ),
        "answer": "720 · 2 : 3 = 480 km gefahren ; 720 - 480 = 240 km bleiben.",
        "steps": [
            "2/3 von 720 = 720 : 3 · 2 = 240 · 2 = 480 km.",
            "Restliche Strecke: 720 - 480 = 240 km.",
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
        "n": 16,
        "type": "Sparschweine",
        "text": (
            "Anna hat 18 Euro mehr im Sparschwein als Ben. Zusammen haben beide "
            "84 Euro. Wie viel hat jedes Kind?"
        ),
        "answer": "Ben 33 Euro, Anna 51 Euro.",
        "steps": [
            "84 - 18 = 66 (gleiche Anteile).",
            "66 : 2 = 33 Euro (Ben).",
            "33 + 18 = 51 Euro (Anna).",
            "Probe: 33 + 51 = 84.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.groessen.geld",
        ],
    },
]

NEW_KNOWLEDGE = []
