EXERCISE = {
    "id": "0015",
    "subject": "HSU",
    "grade": 4,
    "title": "Lernzielkontrolle: Wasser, Wassergewinnung",
    "topic": "Wassergewinnung, Kreislauf, Verdunsten/Verdampfen/Kondensieren, Grundwasser",
    "publisher": "CATLUX",
    "source_pdf": "0015.pdf",
    "answer_pdf": "0015 (1).pdf",
    "total_points": 48.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Beschriften (Wasserversorgungsanlage)",
        "text": (
            "Beschrifte die Zeichnung der Wasserversorgungsanlage! "
            "[Diagramm mit 7 Beschriftungsfeldern (a–g)]"
        ),
        "answer": (
            "a) Tiefbrunnen\n"
            "b) Wasserwerk\n"
            "c) Pumpe\n"
            "d) Hochbehälter\n"
            "e) Fallleitung\n"
            "f) Rohrnetz\n"
            "g) Steigleitung"
        ),
        "steps": [
            "Wasser wird aus dem Tiefbrunnen gepumpt.",
            "Im Wasserwerk wird das Wasser gereinigt.",
            "Die Pumpe befördert Wasser in den Hochbehälter.",
            "Vom Hochbehälter fließt Wasser über Fallleitung oder Steigleitung ins Rohrnetz.",
        ],
        "points": 7.0,
        "has_image": True,
        "image": "0015_q1_wasserversorgung.png",
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 2,
        "type": "Reihenfolge (Wasserversorgung)",
        "text": (
            "Bringe die Sätze in die richtige Reihenfolge!\n"
            "Dann können wir duschen, baden, waschen, …\n"
            "Das Wasser wird nun gereinigt.\n"
            "Das Leitungswasser kommt aus Seen, Quellen, Flüssen oder Tiefbrunnen.\n"
            "In den Häusern entnehmen wir das Wasser aus dem Wasserhahn.\n"
            "Bei Bedarf fließt das Wasser von den Hochbehältern in der Fallleitung oder "
            "Steigleitung zu den Häusern."
        ),
        "answer": (
            "1. Das Leitungswasser kommt aus Seen, Quellen, Flüssen oder Tiefbrunnen.\n"
            "2. Das Wasser wird nun gereinigt.\n"
            "3. Bei Bedarf fließt das Wasser von den Hochbehältern in der Fallleitung oder Steigleitung zu den Häusern.\n"
            "4. In den Häusern entnehmen wir das Wasser aus dem Wasserhahn.\n"
            "5. Dann können wir duschen, baden, waschen, …"
        ),
        "steps": [
            "Reihenfolge: Entnahme → Reinigung → Speicherung/Transport → Wasserhahn → Nutzung.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 3,
        "type": "Lückentext (Steigleitung/Pumpe)",
        "text": (
            "Fülle die Lücken!\n"
            "In einem Wasserhahn, der ____________ liegt als der Hochbehälter, steigt das Wasser "
            "nicht ohne Hilfe. In solch einen Hahn muss das Wasser ____________ werden."
        ),
        "answer": "höher; gepumpt",
        "steps": [
            "Wasser fließt durch Schwerkraft nach unten (Fallleitung).",
            "Liegt ein Hahn höher als der Hochbehälter, braucht es eine Pumpe (Steigleitung).",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 4,
        "type": "Freie Antwort (Wassersparen im Haushalt)",
        "text": "Nenne drei Möglichkeiten, wie du im Haushalt Wasserverschwendung vermeiden kannst!",
        "answer": (
            "1. Beim Zähneputzen einen Becher verwenden (Wasser abstellen).\n"
            "2. Bei der Toilettenspülung die Spartaste verwenden.\n"
            "3. Duschen statt Baden."
        ),
        "steps": [
            "Wasser bewusst einsparen durch einfache Alltagsgewohnheiten.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 5,
        "type": "Freie Antwort (Wasserdurchlässige Bodenschichten)",
        "text": "Nenne 3 wasserdurchlässige Bodenschichten!",
        "answer": "Sand, Kies, Humus (Erde)",
        "steps": [
            "Wasserdurchlässige Schichten lassen Wasser passieren: Humus, Sand, Kies.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 6,
        "type": "Fachbegriff (Synonym für verdichten)",
        "text": "Nenne ein anderes Wort für „verdichten”!",
        "answer": "kondensieren",
        "steps": [
            "Verdichten = kondensieren: Wasserteilchen rücken zusammen und werden wieder flüssig.",
        ],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 7,
        "type": "Erklärungsaufgabe (Wasser früher)",
        "text": (
            "Warum gingen die Menschen vor ein paar hundert Jahren im Haushalt viel sparsamer "
            "mit ihrem Wasser um, als wir heute?"
        ),
        "answer": (
            "Es gab noch keine Wasserleitungen. Das Wasser musste man selbst ins Haus holen. "
            "Das Wasser war sehr wertvoll."
        ),
        "steps": [
            "Keine Wasserleitung → Wasser musste mühsam vom Brunnen geholt werden.",
            "Ohne fließendes Wasser war jeder Tropfen kostbar.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 8,
        "type": "Erklärungsaufgabe (Putzmittel und Wasserverschmutzung)",
        "text": (
            "Warum verschmutzt man Wasser, wenn man zu viele Putz- und Reinigungsmittel verwendet?"
        ),
        "answer": (
            "Die Stoffe aus den Putzmitteln können oft in der Kläranlage nicht mehr herausgewaschen werden."
        ),
        "steps": [
            "Chemische Stoffe in Reinigungsmitteln sind schwer biologisch abbaubar.",
            "Die Kläranlage kann diese Schadstoffe nicht vollständig entfernen → Wasser bleibt verschmutzt.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 9,
        "type": "Zeichnen und Begründen (Quellenstehung)",
        "text": (
            "Zeichne ein, wo eine Quelle entstehen kann und begründe!"
        ),
        "answer": (
            "Eine Quelle entsteht dort, wo das Grundwasser von selbst an die Oberfläche tritt, "
            "weil es auf eine wasserundurchlässige Schicht trifft (z. B. eine Lehmschicht)."
        ),
        "steps": [
            "Wasser versickert durch wasserdurchlässige Schichten nach unten.",
            "Auf einer wasserundurchlässigen Schicht (Lehm/Ton) staut sich das Wasser.",
            "Dort, wo diese Schicht an der Erdoberfläche liegt, tritt Wasser aus → Quelle.",
        ],
        "points": 3.0,
        "has_image": True,
        "image": "0015_q9_quelle.png",
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 10,
        "type": "Freie Antwort (Grundwasser)",
        "text": "Wie entsteht Grundwasser und warum ist es so wichtig?",
        "answer": (
            "Grundwasser entsteht durch das Versickern von Regen im Erdboden, der sich dann auf "
            "wasserundurchlässigen Schichten sammelt. Während das Wasser langsam bis zu dieser Schicht "
            "abläuft, wird es gefiltert und gereinigt. Daher ist Grundwasser als Trinkwasser sehr gut geeignet."
        ),
        "steps": [
            "Regen versickert durch Humus, Sand, Kies → wird dabei gefiltert.",
            "Staut sich über wasserundurchlässiger Schicht (Ton/Lehm) → Grundwasser.",
            "Wichtig: sauberes, gefiltertes Trinkwasser.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 11,
        "type": "Ankreuzen (Verdunsten/Verdampfen/Verdichten)",
        "text": (
            "Wasser kann verdunsten, verdampfen oder verdichten. "
            "Was geschieht jeweils mit den Wasserteilchen? Kreuze an!\n"
            "1. Aufsteigende Wasserteilchen sind sichtbar.\n"
            "2. Die Temperatur des Wassers beträgt 30 °C.\n"
            "3. Winzige Wasserteilchen steigen langsam in die Luft.\n"
            "4. Mutter gießt die Blumen, am nächsten Tag sind sie trocken.\n"
            "5. Mutter kommt mit einer Schüssel kochend heißem Wasser.\n"
            "6. Beim Inhalieren wird dein Gesicht ganz nass.\n"
            "7. Du baust einen Schneemann und siehst den Hauch deines Atems.\n"
            "8. Auf dem Gehsteig ist eine Pfütze. Die Sonne scheint.\n"
            "9. Vater nimmt den Braten mit heißer Soße aus dem Ofen."
        ),
        "answer": (
            "1. verdichten (sichtbare Tröpfchen)\n"
            "2. verdunsten (unter 100 °C, langsam)\n"
            "3. verdunsten\n"
            "4. verdunsten\n"
            "5. verdampfen (kochend heißes Wasser, 100 °C)\n"
            "6. verdichten (Gesicht wird nass durch kondensierten Dampf)\n"
            "7. verdichten (Atemluft kondensiert in der Kälte)\n"
            "8. verdunsten (Pfütze trocknet durch Sonnenwärme)\n"
            "9. verdampfen (heiße Soße verdampft)"
        ),
        "steps": [
            "Verdunsten: bei Raumtemperatur, langsam, unsichtbar (Beispiele 2, 3, 4, 8).",
            "Verdampfen: bei Siedetemperatur (100 °C), schnell (Beispiele 5, 9).",
            "Verdichten/Kondensieren: Wasserdampf wird wieder sichtbar (Beispiele 1, 6, 7).",
        ],
        "points": 9.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 12,
        "type": "Korrekturaufgabe (Text korrigieren)",
        "text": (
            "Korrigiere folgenden Text. Streiche falsche Begriffe durch und "
            "schreibe ein passendes Wort darüber!\n\n"
            "Die Sonne erwärmt die Oberfläche der Erde, so dass große "
            "Wasserteilchen nach oben steigen. In kälteren Luftschichten "
            "verdampfen die Wasserteilchen. Je tiefer die Luftschichten sind, "
            "desto größer ist die Wahrscheinlichkeit, dass es schneit. "
            "Manchmal hagelt es auch, weil Wassertropfen in kalten "
            "Luftschichten gefrieren. Sie fallen langsam zur Erde herab, so "
            "dass sie nicht auftauen können. Je länger sie fallen, desto "
            "kleiner werden sie."
        ),
        "answer": (
            "Die Sonne erwärmt die Oberfläche der Erde, so dass "
            "(große → sehr kleine) Wasserteilchen nach oben steigen. "
            "In kälteren Luftschichten (verdampfen → verdichten) die "
            "Wasserteilchen. Je (tiefer → höher) die Luftschichten sind, "
            "desto größer ist die Wahrscheinlichkeit, dass es schneit. "
            "Manchmal hagelt es auch, weil Wassertropfen in kalten "
            "Luftschichten gefrieren. Sie fallen (langsam → schnell) zur "
            "Erde herab, so dass sie nicht auftauen können. Je länger sie "
            "fallen, desto (kleiner → größer) werden sie."
        ),
        "steps": [
            "Falsche Begriffe identifizieren und durch fachlich korrekte Wörter ersetzen.",
            "Kleine Wasserteilchen steigen auf (nicht große).",
            "Beim Aufsteigen kühlen sich die Teilchen ab → verdichten/kondensieren (nicht verdampfen).",
            "Schnee entsteht in höheren, kälteren Luftschichten — daher 'höher' statt 'tiefer'.",
            "Hagel ist schwer und fällt schnell; je länger es fällt, desto größer wird das Korn.",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 13,
        "type": "Erklärungsaufgabe (Weg des Regenwassers zur Quelle)",
        "text": (
            "Du stehst auf einer Wiese und es regnet. Was passiert nun für unsere Augen unsichtbar "
            "mit dem Wasser, bis wir es wieder aus einer Quelle hervortreten sehen? "
            "Erkläre genau und ausführlich!"
        ),
        "answer": (
            "Das Wasser versickert in die Erdschichten. Die erste Erdschicht ist Humus (Erde), "
            "die zweite Sand und die dritte Kies. Diese drei Erdschichten sind wasserdurchlässig. "
            "Die vierte Schicht besteht aus Lehm oder Ton. Sie ist wasserundurchlässig. "
            "Das Wasser kann also nicht mehr weiter und staut sich, bis eine Quelle entsteht. "
            "Wenn das Wasser durch die Schichten sickert, wird es gereinigt – darum ist Quellwasser so sauber."
        ),
        "steps": [
            "Regen trifft auf die Erde und versickert.",
            "Schicht 1: Humus (wasserdurchlässig)",
            "Schicht 2: Sand (wasserdurchlässig)",
            "Schicht 3: Kies (wasserdurchlässig) – Wasser wird dabei gefiltert.",
            "Schicht 4: Ton/Lehm (wasserundurchlässig) – Wasser staut sich auf.",
            "Wo die wasserundurchlässige Schicht an die Oberfläche tritt, entsteht eine Quelle.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 14,
        "type": "Erklärungsaufgabe (Verdunstung und Plastiktüte)",
        "text": (
            "Florian hat seine nassen Schwimmsachen fest in eine Plastiktüte eingewickelt. "
            "Nach der Schule legt er die Tüte zum Trocknen in die Sonne. "
            "Was sagst du dazu? Erkläre, warum Florian hier etwas richtig oder falsch macht!"
        ),
        "answer": (
            "Das ist falsch. Durch die Tüte ist die Hose luftdicht verpackt und kann nicht trocken, "
            "da das Wasser nicht verdunsten kann."
        ),
        "steps": [
            "Verdunstung braucht Luftzirkulation: Wasserdampf muss in die Umgebungsluft entweichen können.",
            "Eine geschlossene Plastiktüte verhindert die Luftzirkulation → kein Verdunsten möglich.",
            "Die Sonne wärmt die Tüte, aber ohne Luftaustausch bleibt die Hose nass.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
]

NEW_KNOWLEDGE = []
