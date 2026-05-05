EXERCISE = {
    "id": "0906",
    "subject": "Mathe",
    "grade": 4,
    "title": "3. Probe – Sachaufgaben",
    "topic": "Sachaufgaben",
    "publisher": "CATLUX",
    "source_pdf": "0906.pdf",
    "answer_pdf": "0906 (1).pdf",
    "total_points": 26.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Kreuze an",
        "text": (
            "Welche Fragen kannst du durch Rechnen beantworten? Kreuze an!\n\n"
            "Gegeben ist eine Werbeanzeige des Radl-Markts mit folgenden Preisen:\n"
            "  Puky 300 (3-Gang-Schaltung): 195,50€\n"
            "  Speedy 50 (Alufelgen + 5-Gang): 229,–€\n"
            "  Fahrradhelm: 42€\n"
            "  Beleuchtungsset: 25,50€\n"
            "  Fahrradmantel: 10€/Stück\n"
            "  Werkzeugset: 12,75€\n"
            "  Flasche: 3,25€\n\n"
            "Fragen:\n"
            "a) Wie viel muss Florian für das Rad Puky und eine Fahrradflasche bezahlen?\n"
            "b) Florian hat 300€. Reicht sein Geld für das Rad Puky und einen Fahrradkorb?\n"
            "c) Kosten das Fahrrad Puky und ein Fahrradhelm mehr als das Rad Speedy?\n"
            "d) Wie lange hat der Radl-Markt geöffnet, wenn Florian das Speedy 50 kaufen möchte?"
        ),
        "answer": (
            "Durch Rechnen beantwortbar: a) und c).\n"
            "Nicht beantwortbar: b) (kein Fahrradkorb-Preis angegeben), d) (Öffnungszeiten nicht angegeben)."
        ),
        "steps": [
            "a) Ja – Puky 195,50€ + Flasche 3,25€ = 198,75€ → durch Rechnen beantwortbar",
            "b) Nein – kein Preis für Fahrradkorb in der Anzeige angegeben",
            "c) Ja – Puky 195,50€ + Helm 42€ = 237,50€ > Speedy 229€ → durch Rechnen beantwortbar",
            "d) Nein – Öffnungszeiten des Radl-Markts sind nicht angegeben",
        ],
        "points": 2.0,
        "has_image": True,
        "image": "0906_q1_radlmarkt.png",
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.groessen.geld",
        ],
    },
    {
        "n": 2,
        "type": "Tabelle ausfüllen",
        "text": (
            "Diese Tabellen kannst du ausfüllen!\n\n"
            "Tabelle 1 (Geschwindigkeit 120km/h):\n"
            "  1h → 120km\n"
            "  30min → ?\n"
            "  10min → ?\n"
            "  1min → ?\n"
            "  11min → ?\n\n"
            "Tabelle 2 (Geschwindigkeit 140km/h):\n"
            "  1h → 140km\n"
            "  ? → 280km\n"
            "  ? → 70km\n"
            "  ? → 35km\n"
            "  ? → 245km"
        ),
        "answer": (
            "Tabelle 1: 30min→60km, 10min→20km, 1min→2km, 11min→22km\n"
            "Tabelle 2: 2h→280km, 30min→70km, 15min→35km, 1h45min→245km"
        ),
        "steps": [
            "Tabelle 1: 120km/h → 120 : 2 = 60km (30min); 120 : 6 = 20km (10min); 120 : 60 = 2km (1min); 2 × 11 = 22km (11min)",
            "Tabelle 2: 140 × 2 = 280km → 2h; 140 : 2 = 70km → 30min; 70 : 2 = 35km → 15min; 245 : 140 × 60 = 105min = 1h45min → 245km",
        ],
        "points": 8.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.tabellen",
            "mathe.klasse4.groessen.zeit",
        ],
    },
    {
        "n": 3,
        "type": "Textaufgabe",
        "text": (
            "Löse die Textaufgabe mit Skizze, Rechnungen und Antworten!\n\n"
            "Familie Meier macht einen Ausflug. Mit ihren Rädern fahren sie um 8.15 Uhr von zu Hause weg. "
            "Nach 1 Stunde 25 Minuten machen sie 35 Minuten am Fischteich eine Pause. Danach fahren sie "
            "noch 40 Minuten zu einer Burg. Die Burgbesichtigung dauert 1 Stunde 30 Minuten. Für den "
            "Rückweg brauchen sie 2 Stunden 30 Minuten.\n\n"
            "a) Zeichne eine Skizze mit allen Angaben aus der Geschichte!\n"
            "b) Was musst du ausrechnen? Kreuze an! (Abfahrt / Dauer des Ausflugs / Länge der Strecke / Ankunft)\n"
            "c) Rechne nun aus!\n"
            "F: Wie viele Stunden und Minuten dauert der Ausflug?\n"
            "F: Um wie viel Uhr sind sie wieder zu Hause?"
        ),
        "answer": (
            "b) Dauer des Ausflugs und Ankunft.\n"
            "c) Der Ausflug dauert 6 Stunden und 40 Minuten. Die Familie ist um 14.55 Uhr wieder zu Hause."
        ),
        "steps": [
            "Abschnitte: 1h 25min + 35min + 40min + 1h 30min + 2h 30min",
            "Summe: 1h 25min + 35min = 2h; + 40min = 2h 40min; + 1h 30min = 4h 10min; + 2h 30min = 6h 40min",
            "Ankunft: 8.15 Uhr + 6h 40min = 14.55 Uhr",
            "A: Der Ausflug dauert 6 Stunden und 40 Minuten.",
            "A: Die Familie ist um 14.55 Uhr wieder zu Hause.",
        ],
        "points": 9.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.groessen.zeit",
        ],
    },
    {
        "n": 4,
        "type": "Textaufgabe",
        "text": (
            "Die Freunde Florian und Tim wollen zu einem Fußballspiel nach München fahren, das um 14.00 Uhr beginnt.\n\n"
            "Florian fährt mit dem Rad. Bis nach München sind es 35km. Er schafft 14km in der Stunde. "
            "Für eine Pause plant er 20 Minuten ein. Tim fährt die gleiche Strecke mit dem Auto. "
            "Dafür braucht er 30 Minuten. Beim Tanken braucht er zusätzlich 10 Minuten.\n\n"
            "a) Trage wichtige Angaben ein:\n"
            "   Abfahrt von Florian | Abfahrt von Tim\n"
            "   Geschwindigkeit von Florian | Fahrzeit von Tim\n"
            "   Pause von Florian | Tanken\n"
            "   Gesamtstrecke\n\n"
            "b) Wie lange ist Florian insgesamt unterwegs?\n"
            "c) Wie lange ist Tim unterwegs?\n"
            "d) Wann muss Florian losradeln, wenn er 30 Minuten vor dem Spiel in München sein möchte?\n"
            "d) Wie lange stand Tim im Stau, wenn er um 13.00 Uhr losfuhr, aber erst um 14.10 Uhr in München ankam?"
        ),
        "answer": (
            "a) Florian: Abfahrt 11.10 Uhr, 14km/h, Pause 20min, Strecke 35km; Tim: Abfahrt 13.20 Uhr, Fahrzeit 30min, Tanken 10min\n"
            "b) Florian ist 2h 50min unterwegs.\n"
            "c) Tim ist 40min unterwegs.\n"
            "d1) Florian muss um 10.40 Uhr losradeln.\n"
            "d2) Tim stand 30 Minuten im Stau."
        ),
        "steps": [
            "a) Florian: 14km/h, Pause 20min, Strecke 35km; Tim: Fahrzeit 30min, Tanken 10min",
            "b) 1h→14km, 2h→28km, 30min→7km → 2h 30min für 35km; + 20min Pause = 2h 50min",
            "   Abfahrt Florian: 14.00 Uhr – 30min (vor Spiel) – 2h 50min = 11.10 Uhr (für d1)",
            "c) Tim: 30min Fahrt + 10min Tanken = 40min; Abfahrt Tim: 14.00 – 40min = 13.20 Uhr",
            "d1) Florian möchte 30min vor 14.00 = 13.30 Uhr ankommen; 13.30 Uhr – 2h 50min = 10.40 Uhr",
            "d2) Tim losfuhr 13.00 Uhr, ankam 14.10 Uhr → Gesamtzeit 1h 10min; normal 40min → Stau: 1h 10min – 40min = 30min",
        ],
        "points": 0.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.groessen.zeit",
        ],
    },
    {
        "n": 5,
        "type": "Sachaufgabe",
        "text": (
            "Anna und Leon sollen für das Sportfest 3 Reihen Hütchen am Sportplatz aufstellen. "
            "Die Hütchen in jeder Reihe müssen 3m Abstand voneinander haben. Jede Reihe ist 27m lang.\n\n"
            "F: Wie viele Hütchen brauchen die Kinder, wenn auch am Anfang von jeder Reihe ein Hütchen stehen muss."
        ),
        "answer": "Anna und Leon sollen 30 Hütchen für das Sportfest aufstellen. In jede Reihe kommen 10 Hütchen.",
        "steps": [
            "Hütchen pro Reihe: 27m : 3m = 9 Abstände → 9 + 1 = 10 Hütchen pro Reihe",
            "3 Reihen: 10 × 3 = 30 Hütchen gesamt",
            "A: Anna und Leon sollen 30 Hütchen für das Sportfest aufstellen.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.schriftlich.division",
        ],
    },
    {
        "n": 6,
        "type": "Sachaufgabe",
        "text": (
            "Florian ist 1,41m groß. Uli ist 15cm größer als Florian. Florian ist 7cm kleiner als Sarah, "
            "aber 24cm größer als Sabine.\n"
            "Wie groß sind die Kinder?\n"
            "Florian: _______ Uli: _______ Sarah: _______ Sabine: _______"
        ),
        "answer": "Florian: 1,41m  Uli: 1,56m  Sarah: 1,48m  Sabine: 1,17m",
        "steps": [
            "Florian: 1,41m (gegeben)",
            "Uli: 1,41m + 15cm = 1,41m + 0,15m = 1,56m",
            "Sarah: 1,41m + 7cm = 1,41m + 0,07m = 1,48m",
            "Sabine: 1,41m – 24cm = 1,41m – 0,24m = 1,17m",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.groessen.laenge",
        ],
    },
]

NEW_KNOWLEDGE = []
