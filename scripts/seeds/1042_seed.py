EXERCISE = {
    "id": "1042",
    "subject": "HSU",
    "grade": 4,
    "title": "Lernzielkontrolle Wasser",
    "topic": "Wasser: Aggregatzustände, Kreislauf, Süß- und Salzwasser, Verdunstung, virtuelles Wasser",
    "publisher": "CATLUX",
    "source_pdf": "1042.pdf",
    "answer_pdf": "1042_Lösung.pdf",
    "total_points": 52.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Abbildung beschriften",
        "text": (
            "Wasser kommt in verschiedenen Zustandsformen vor. "
            "Beschrifte die Abbildung! (Aggregatzustände und Übergänge)"
        ),
        "answer": (
            "Die drei Aggregatzustände: fest (Eis), flüssig (Wasser), gasförmig (Wasserdampf).\n"
            "Übergänge: Schmelzen (fest → flüssig), Gefrieren (flüssig → fest), "
            "Verdampfen/Verdunsten (flüssig → gasförmig), Kondensieren (gasförmig → flüssig), "
            "Sublimieren (fest → gasförmig), Resublimieren (gasförmig → fest)."
        ),
        "steps": [
            "Drei Zustände benennen: Eis (fest), Wasser (flüssig), Wasserdampf (gasförmig).",
            "Übergänge zwischen den Zuständen mit Fachbegriffen beschriften.",
        ],
        "points": 7.0,
        "has_image": True,
        "image": "1042_q1_aggregatzustaende.png",
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 2,
        "type": "Lückentext mit Verben füllen",
        "text": (
            "Wie heißt der Vorgang? Fülle die Lücken mit Verben!\n"
            "a) In einem Raum befindet sich warme, feuchte Luft. An der kalten Fensterscheibe bilden sich kleine Wassertröpfchen.\n"
            "b) Der Boden wird gewischt. Nach einer Weile ist er wieder trocken.\n"
            "c) Auf dem Herd kocht Wasser in einem Topf ohne Deckel. Das Wasser wird weniger."
        ),
        "answer": (
            "a) kondensieren\n"
            "b) verdunsten\n"
            "c) verdampfen"
        ),
        "steps": [
            "a) Wasserdampf in warmer Luft trifft auf kalte Oberfläche → kondensiert.",
            "b) Nasser Boden trocknet bei Raumtemperatur → verdunstet.",
            "c) Kochendes Wasser bei 100 °C → verdampft.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 3,
        "type": "Erklären und Beispiele nennen",
        "text": (
            "a) Unter welchen Bedingungen verdunstet Wasser am schnellsten?\n"
            "b) Nenne zwei Beispiele aus dem täglichen Leben, wo Verdunstung beabsichtigt ist."
        ),
        "answer": (
            "a) Wasser verdunstet am schnellsten bei hoher Temperatur und bei Wind.\n"
            "b) Beispiele: Haare mit dem Fön trocknen, Wäsche bügeln mit einem Dampfbügeleisen."
        ),
        "steps": [
            "a) Hohe Temperatur → Teilchen bewegen sich schneller und lösen sich leichter.",
            "a) Wind → feuchte Luft wird weggetragen, trockene Luft nimmt mehr Feuchtigkeit auf.",
            "b) Fön: erzeugt warme Luft zur schnelleren Verdunstung.",
            "b) Bügeleisen: Dampf nimmt Feuchtigkeit auf.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 4,
        "type": "Unterschiede erläutern",
        "text": "Erläutere zwei Unterschiede zwischen verdunsten und verdampfen.",
        "answer": (
            "Beim Verdunsten ist das Wasser unsichtbar und hat eine Temperatur von unter 100 °C.\n"
            "Beim Verdampfen ist der Wasserdampf sichtbar und das Wasser hat eine Temperatur von genau oder über 100 °C."
        ),
        "steps": [
            "Unterschied 1: Verdunsten unsichtbar (< 100 °C), Verdampfen sichtbar (≥ 100 °C).",
            "Unterschied 2: Verdunsten an der Oberfläche bei beliebiger Temperatur, Verdampfen im gesamten Volumen beim Siedepunkt.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 5,
        "type": "Ankreuzen",
        "text": (
            "In welchen Räumen schweben besonders viele Wasserteilchen? Kreuze an!\n"
            "[ ] Hallenbad  [ ] Kinderzimmer\n"
            "[ ] Sauna  [ ] Dampfbad"
        ),
        "answer": "Richtig: Hallenbad und Dampfbad.",
        "steps": [
            "Hallenbad: große offene Wasserfläche → viel Verdunstung.",
            "Dampfbad: absichtlich erzeugte hohe Luftfeuchtigkeit durch Dampf.",
            "Sauna: trockene Hitze, weniger Wasserteilchen als Dampfbad.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 6,
        "type": "Möglichkeiten nennen",
        "text": (
            "Nach einem Regenguss ist ein Feldweg wieder trocken. "
            "Nenne zwei Möglichkeiten, was mit dem Wasser geschehen ist!"
        ),
        "answer": "Das Wasser ist verdunstet oder versickert.",
        "steps": [
            "Verdunstung: Sonne und Wind trocknen die Wasseroberfläche.",
            "Versickerung: Wasser dringt durch den Boden ins Grundwasser.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 7,
        "type": "Reihenfolge nummerieren",
        "text": (
            "Der Kreislauf des Wassers. Nummeriere die Sätze in der richtigen Reihenfolge!\n\n"
            "___ Es bilden sich Wolken, die der Wind über Land und Meer treibt.\n"
            "___ Wasser von Seen verdunstet und unsichtbare Wasserteilchen steigen in der warmen Luft nach oben.\n"
            "___ Nehmen sie noch mehr Wasser auf, werden die Tröpfchen immer schwerer und es beginnt zu regnen.\n"
            "___ Ein anderer Teil versickert im Boden.\n"
            "___ Es kann als Quelle wieder zu Tage treten.\n"
            "___ In tieferen Bodenschichten sammelt es sich als Grundwasser.\n"
            "___ Ein Teil des Regenwassers fließt in Bäche, Flüsse oder ins Meer.\n"
            "___ In den kalten Luftschichten kühlen sie ab und bilden kleine Wassertröpfchen."
        ),
        "answer": (
            "1 – Wasser von Seen verdunstet und unsichtbare Wasserteilchen steigen in der warmen Luft nach oben.\n"
            "2 – In den kalten Luftschichten kühlen sie ab und bilden kleine Wassertröpfchen.\n"
            "3 – Es bilden sich Wolken, die der Wind über Land und Meer treibt.\n"
            "4 – Nehmen sie noch mehr Wasser auf, werden die Tröpfchen immer schwerer und es beginnt zu regnen.\n"
            "5 – Ein Teil des Regenwassers fließt in Bäche, Flüsse oder ins Meer.\n"
            "6 – Ein anderer Teil versickert im Boden.\n"
            "7 – In tieferen Bodenschichten sammelt es sich als Grundwasser.\n"
            "8 – Es kann als Quelle wieder zu Tage treten."
        ),
        "steps": [
            "Verdunstung → Aufsteigen der Teilchen (1).",
            "Abkühlung in der Höhe → Tröpfchenbildung (2).",
            "Wolkenbildung und Transport durch Wind (3).",
            "Regen fällt (4).",
            "Abfluss in Gewässer (5) und Versickerung (6).",
            "Grundwasserbildung (7) → Quelle (8).",
        ],
        "points": 8.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 8,
        "type": "Richtig / Falsch",
        "text": (
            "Der „blaue Planet Erde”. Richtig (r) oder falsch (f)?\n"
            "___ Auf der Erde gibt es Unmengen von Trinkwasser.\n"
            "___ Meere bedecken fast drei Viertel der Erdoberfläche.\n"
            "___ Das Wasser der Meere ist ungenießbares Salzwasser.\n"
            "___ Ein großer Teil des Süßwassers kommt in Form von Eis vor."
        ),
        "answer": (
            "f – Auf der Erde gibt es Unmengen von Trinkwasser. (Falsch: Trinkwasser ist sehr knapp.)\n"
            "r – Meere bedecken fast drei Viertel der Erdoberfläche. (Richtig)\n"
            "r – Das Wasser der Meere ist ungenießbares Salzwasser. (Richtig)\n"
            "r – Ein großer Teil des Süßwassers kommt in Form von Eis vor. (Richtig)"
        ),
        "steps": [
            "Trinkwasser macht nur einen winzigen Anteil des Gesamtwassers aus → falsch.",
            "Drei Viertel der Erdoberfläche sind Meer → richtig.",
            "Meerwasser ist salzig und nicht trinkbar → richtig.",
            "Polkappen und Gletscher enthalten den größten Teil des Süßwassers → richtig.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.gewaesser"],
    },
    {
        "n": 9,
        "type": "Nennen und erklären",
        "text": (
            "a) Nenne zwei Dinge, für die jede Person täglich durchschnittlich am meisten Wasser verbraucht!\n"
            "b) Was könnte man hier jeweils tun, um Wasser einzusparen?"
        ),
        "answer": (
            "a) Baden und Toilettengang.\n"
            "b) Nicht baden, sondern duschen. Bei der Toilette eine Spartaste verwenden."
        ),
        "steps": [
            "a) Größte Wasserverbraucher im Haushalt: Bad/Dusche und Toilette.",
            "b) Duschen statt Baden spart ca. 100 Liter pro Mal.",
            "b) Spülkasten mit Spartaste reduziert Wasserverbrauch beim Spülen.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.gewaesser"],
    },
    {
        "n": 10,
        "type": "Begründen",
        "text": "Warum trocknen Meere nie aus? Nenne zwei Gründe!",
        "answer": (
            "1. Das Wasser verdunstet und regnet wieder ab (Wasserkreislauf).\n"
            "2. Die Flüsse fließen in die Meere und führen ständig Wasser zu."
        ),
        "steps": [
            "Kreislauf: Verdunstung → Wolken → Regen → Rücklauf ins Meer.",
            "Zufluss: alle Flüsse münden letztendlich ins Meer.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf", "hsu.klasse3.wasser.gewaesser"],
    },
    {
        "n": 11,
        "type": "Falsche Sätze streichen",
        "text": (
            "Streiche die falschen Sätze durch!\n"
            "• In der Luft ist immer Feuchtigkeit enthalten.\n"
            "• Warme Luft steigt in die Höhe.\n"
            "• Wolken bestehen aus Wassertröpfchen, die in der Luft schweben.\n"
            "• Kalte Luft kann mehr Wasserdampf schlucken als warme Luft.\n"
            "• Regenwasser kann im Sand nicht versickern.\n"
            "• Wasser kocht bei 90°.\n"
            "• Wasser gefriert bei 0°.\n"
            "• An einem sonnigen, windgeschützten Platz trocknet die Wäsche am schnellsten."
        ),
        "answer": (
            "Falsch (durchstreichen):\n"
            "– Kalte Luft kann mehr Wasserdampf schlucken als warme Luft. "
            "(Richtig ist: warme Luft nimmt mehr Feuchtigkeit auf.)\n"
            "– Regenwasser kann im Sand nicht versickern. "
            "(Richtig ist: Sand ist wasserdurchlässig.)\n"
            "– Wasser kocht bei 90°. (Richtig ist: 100 °C bei Normaldruck.)\n"
            "– An einem sonnigen, windgeschützten Platz trocknet die Wäsche am schnellsten. "
            "(Richtig ist: sonnig UND windig trocknet am schnellsten.)\n\n"
            "Richtig (stehen lassen):\n"
            "– In der Luft ist immer Feuchtigkeit enthalten.\n"
            "– Warme Luft steigt in die Höhe.\n"
            "– Wolken bestehen aus Wassertröpfchen, die in der Luft schweben.\n"
            "– Wasser gefriert bei 0°."
        ),
        "steps": [
            "Warme Luft kann mehr Wasserdampf aufnehmen als kalte → Aussage 4 falsch.",
            "Sand ist wasserdurchlässig → Aussage 5 falsch.",
            "Wasser kocht bei 100 °C (nicht 90 °C) → Aussage 6 falsch.",
            "Wind beschleunigt Verdunstung → windgeschützt ist nicht optimal → Aussage 8 falsch.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf", "hsu.klasse3.luft_wetter.phaenomene"],
    },
    {
        "n": 12,
        "type": "Erklären",
        "text": "Wo befindet sich der größte Teil des Süßwassers auf unserer Erde?",
        "answer": "An den beiden Erdpolen und in den Hochgebirgen (als Eis und Gletscher).",
        "steps": [
            "Polkappen (Arktis, Antarktis) enthalten den größten Teil des Süßwassers als Eis.",
            "Hochgebirgsgletscher sind eine weitere bedeutende Süßwasserreserve.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.gewaesser"],
    },
    {
        "n": 13,
        "type": "Erklären mit Stichpunkten",
        "text": (
            "Welches virtuelle Wasser steckt in einer Schinken-Pizza? "
            "Nenne 3 verschiedene Bereiche und erkläre in Stichpunkten!"
        ),
        "answer": (
            "1. Mehl / Teig: Getreidefelder müssen bewässert werden; Getreide muss mit Wasser gereinigt werden.\n"
            "2. Schinken / Schwein: Das Schwein braucht Wasser zum Trinken; Futterpflanzen für das Schwein brauchen Wasser.\n"
            "3. Tomatensoße: Tomaten müssen gegossen und gewaschen werden.\n"
            "4. Käse / Milch: Kühe brauchen Wasser zum Trinken; für die Milchproduktion und Käseherstellung wird Wasser benötigt."
        ),
        "steps": [
            "Virtuelles Wasser = das Wasser, das für die Herstellung eines Produkts benötigt wurde.",
            "Bereich 1: Mehlherstellung (Bewässerung der Felder).",
            "Bereich 2: Fleischproduktion (Wasser für Tier und Futter).",
            "Bereich 3: Tomaten/Gemüse (Bewässerung und Waschen).",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.gewaesser"],
    },
]

NEW_KNOWLEDGE = []
