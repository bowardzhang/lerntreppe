EXERCISE = {
    "id": "0209",
    "subject": "HSU",
    "grade": 4,
    "title": "Lernzielkontrolle Wasser (2)",
    "topic": "Wasser: Aggregatzustände, Kreislauf, Süß- und Salzwasser, Quellen, Verdunstung",
    "publisher": "CATLUX",
    "source_pdf": "0209.pdf",
    "answer_pdf": "0209_Lösung.pdf",
    "total_points": 56.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Begründen und benennen",
        "text": (
            "Wieso ist der Name „Erde” eigentlich gar nicht so passend für unseren Planeten? "
            "Begründe und finde einen besseren Namen!"
        ),
        "answer": (
            "Ein besserer Name wäre „Wasser”, weil die Erde überwiegend aus Wasser besteht. "
            "¾ der Erde ist Wasser und nur ¼ ist „Erde”."
        ),
        "steps": [
            "Wasseranteil der Erde nennen: ¾ Wasser, ¼ Erde.",
            "Begründung: Name „Erde” passt nicht, weil Wasser überwiegt.",
            "Besseren Namen vorschlagen, z. B. „Wasser”.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.gewaesser"],
    },
    {
        "n": 2,
        "type": "Beispiele nennen",
        "text": "Süßwasser brauchen wir täglich zum Leben. Nenne drei unterschiedliche Beispiele!",
        "answer": (
            "Wir brauchen Süßwasser zum Trinken, zum Waschen, zum Heilen (Thermalwasser) usw."
        ),
        "steps": [
            "Drei verschiedene Verwendungen von Süßwasser nennen, z. B.: Trinken, Waschen, Kochen, Thermalwasser.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.gewaesser"],
    },
    {
        "n": 3,
        "type": "Erklären",
        "text": (
            "Wenn Wasser auch aus den Ozeanen verdunstet, wieso gibt es dann kein salziges Regenwasser?"
        ),
        "answer": "Wenn das Wasser verdunstet, bleibt das Salz im Meer zurück.",
        "steps": [
            "Beim Verdunsten lösen sich nur Wassermoleküle, nicht das Salz.",
            "Das Salz bleibt im Meer zurück.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 4,
        "type": "Erklären",
        "text": "Wie kommt das Salz ins Meer?",
        "answer": (
            "Immer wenn es regnet, versickert Wasser in der Erde. Auf seinem Weg in die Tiefe löst es "
            "Salze und Kalk aus den Bodenschichten. Kommt das Wasser wieder an die Oberfläche, führt es "
            "die gelösten Salze auf seinem Weg zum Meer mit und löst weitere Minerale aus dem Flussbett. "
            "Eine weitere Quelle sind Unterwasser-Vulkane, die Lava auf den Meeresboden schleudern, "
            "die mit dem Wasser reagiert und Salze freisetzt. Verdunstet das Meerwasser, bleibt das Salz zurück."
        ),
        "steps": [
            "Regenwasser versickert und löst Salze aus Bodenschichten.",
            "Wasser transportiert Salze über Flüsse ins Meer.",
            "Unterwasser-Vulkane setzen zusätzliche Salze frei.",
            "Meerwasser verdunstet, Salz bleibt zurück.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.gewaesser"],
    },
    {
        "n": 5,
        "type": "Schaubild auswählen",
        "text": (
            "Das Wasser auf der Erde ist zum Teil Süßwasser und zum Teil Salzwasser. "
            "Welches Schaubild zeigt am besten das Verhältnis von Salz- und Süßwasser? "
            "Kreuze das richtige Glas an! (drei Gläser zur Auswahl)"
        ),
        "answer": "Das dritte Glas (fast volles Glas = Salzwasser, sehr wenig Süßwasser).",
        "steps": [
            "Meer: über 97 % Salzwasser, nur knapp 3 % Süßwasser.",
            "Das dritte Glas zeigt das richtige Verhältnis.",
        ],
        "points": 1.0,
        "has_image": True,
        "image": "0209_q5_glasdiagramm.png",
        "knowledge": ["hsu.klasse3.wasser.gewaesser"],
    },
    {
        "n": 6,
        "type": "Beschriften und erklären",
        "text": (
            "a) Wie entsteht eine Quelle? Beschrifte die Erdschichten und zeichne mit einem blauen Stift ein, "
            "an welcher Stelle das Wasser austritt!\n"
            "b) Wie bezeichnet man die Schichten,\n"
            "   – durch die das Wasser versickert?\n"
            "   – durch die das Wasser nicht versickert?"
        ),
        "answer": (
            "a) Erdschichten von oben nach unten: Humus, Sand, Kies, Lehm/Ton. "
            "Das Wasser versickert durch Humus, Sand und Kies, staut sich auf der Lehm/Ton-Schicht "
            "und tritt an der Oberfläche als Quelle aus.\n"
            "b) Schichten, durch die das Wasser versickert: wasserdurchlässig. "
            "Schichten, durch die das Wasser nicht versickert: wasserundurchlässig."
        ),
        "steps": [
            "Erdschichten benennen: Humus, Sand, Kies, Lehm/Ton.",
            "Wasser staut sich auf undurchlässiger Schicht (Lehm/Ton).",
            "Wasseraustritt an der Erdoberfläche = Quelle einzeichnen.",
            "Wasserdurchlässige Schichten: Humus, Sand, Kies.",
            "Wasserundurchlässige Schicht: Lehm/Ton.",
        ],
        "points": 7.0,
        "has_image": True,
        "image": "0209_q6_erdschichten.png",
        "knowledge": ["hsu.klasse3.wasser.gewaesser"],
    },
    {
        "n": 7,
        "type": "Lückentext / Fachbegriffe einsetzen",
        "text": (
            "Wasser kann in verschiedenen Zustandsformen vorkommen. Erkläre die Zeichnung "
            "durch das Einsetzen passender Worte (Fachbegriffe).\n"
            "100 °C Wasser: Die Wasserteilchen ___, ___. Wasser ist ___.\n"
            "Das Wasser wird abgekühlt: Die Wasserteilchen ___, Wasser ist ___.\n"
            "0 °C Wasser: Aus Wasser wird ___, ___. Wasser ist ___."
        ),
        "answer": (
            "100 °C: Die Wasserteilchen verdampfen, Wasser siedet. Wasser ist gasförmig.\n"
            "Abkühlung: Die Wasserteilchen kondensieren, Wasser ist flüssig.\n"
            "0 °C: Aus Wasser wird Eis, Wasser gefriert. Wasser ist fest."
        ),
        "steps": [
            "Bei 100 °C: Wasser siedet → Wasserteilchen verdampfen → gasförmig.",
            "Beim Abkühlen: Wasserdampf kondensiert → flüssig.",
            "Bei 0 °C: Wasser gefriert → Eis entsteht → fest.",
        ],
        "points": 8.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 8,
        "type": "Erklären",
        "text": "Warum regnet es? Erkläre genau!",
        "answer": (
            "Bei Sonnenwärme verdunstet Wasser und wird zu unsichtbarem Wasserdampf. "
            "In kalten Luftschichten kondensiert der Wasserdampf zu Tröpfchen. Millionen Tropfen bilden eine Wolke. "
            "Aus vielen Tröpfchen in der Wolke bilden sich größere Tropfen, die als Regen oder Schnee fallen, "
            "wenn sie groß und schwer genug sind."
        ),
        "steps": [
            "Sonnenwärme → Wasser verdunstet → unsichtbarer Wasserdampf steigt auf.",
            "In Kälte kondensiert Dampf → Tröpfchen → Wolkenbildung.",
            "Tröpfchen werden größer und schwerer → Regen oder Schnee fällt.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 9,
        "type": "Richtig / Falsch",
        "text": (
            "Richtig oder falsch? Kreuze nur die richtigen Aussagen an!\n"
            "1. Quellwasser ist so sauber, dass man es trinken kann.\n"
            "2. Wasser kann für immer komplett verschwinden.\n"
            "3. Beim Tafelputzen verdunstet Wasser.\n"
            "4. Wasser verdampft unsichtbar.\n"
            "5. Wasser erstarrt beim Siedepunkt.\n"
            "6. Wasser kondensiert bei hoher Temperatur.\n"
            "7. Mit Wasser kann man sogar Strom erzeugen.\n"
            "8. Der Meeresspiegel steigt immer weiter an, weil alle Flüsse ins Meer münden.\n"
            "9. Die Brille beschlägt, wenn ich vom warmen Zimmer in die Kälte gehe.\n"
            "10. Das Volumen von Eis ist größer als das Volumen von Wasser.\n"
            "11. Der Aggregatzustand bleibt gleich, wenn Wasserdampf abkühlt.\n"
            "12. Wasser hat vier Aggregatzustände."
        ),
        "answer": (
            "Richtig: 1 (Quellwasser ist trinkbar), 3 (Tafelputzen → Verdunstung), "
            "7 (Wasser zur Stromerzeugung), 10 (Eis hat größeres Volumen als Wasser).\n"
            "Falsch: 2, 4, 5, 6, 8, 9, 11, 12."
        ),
        "steps": [
            "Aussage 1: richtig – Quellwasser gilt als trinkbar.",
            "Aussage 3: richtig – nasse Tafel trocknet durch Verdunstung.",
            "Aussage 7: richtig – Wasserkraft erzeugt Strom.",
            "Aussage 10: richtig – Wasser dehnt sich beim Gefrieren aus.",
            "Alle anderen Aussagen sind falsch.",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 10,
        "type": "Erklären",
        "text": (
            "Als Sabine im Frühling durch den Garten geht, sieht sie, dass einige Dinge kaputt gegangen sind. "
            "Das Rohr an der Wassertonne ist geplatzt und auch eine Gießkanne voll Wasser hat Risse bekommen. "
            "Erkläre, warum das passiert ist!"
        ),
        "answer": (
            "In dem Rohr und der Gießkanne war Wasser. Dieses ist im Winter gefroren. "
            "Wenn Wasser gefriert, dehnt es sich aus. Das Volumen nimmt um ca. ein Zehntel zu. "
            "Diese Ausdehnung kann eine große Kraft ausüben und zum Platzen der Rohre und der Gießkanne führen."
        ),
        "steps": [
            "Wasser in Rohr/Gießkanne ist im Winter gefroren.",
            "Wasser dehnt sich beim Gefrieren aus (Volumen nimmt um ca. 1/10 zu).",
            "Ausdehnung erzeugt Druck → Rohr und Gießkanne platzen.",
        ],
        "points": 3.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 11,
        "type": "Begründen mit Zahlenangaben",
        "text": (
            "Obwohl es auf der Erde sehr viel Wasser gibt, müssen wir mit unserem Trinkwasser sparsam umgehen. "
            "Stimmt das? Beweise deine Begründung mit Zahlenangaben!"
        ),
        "answer": (
            "Ja, das stimmt. Das meiste Wasser ist Salzwasser, mehr als 97 %. Menschen und Tiere können "
            "Salzwasser nicht trinken, weil Salz dem Körper Wasser entzieht. Süßwasser macht nur knapp "
            "3 % des Wasservorrates aus. Dieses Süßwasser ist ungleichmäßig verteilt und oft verschmutzt, "
            "sodass es erst gereinigt werden muss."
        ),
        "steps": [
            "Über 97 % des Wassers auf der Erde ist Salzwasser → nicht trinkbar.",
            "Nur knapp 3 % ist Süßwasser.",
            "Süßwasser ist ungleichmäßig verteilt und häufig verschmutzt.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.gewaesser"],
    },
    {
        "n": 12,
        "type": "Lückentext",
        "text": (
            "Ergänze den Lückentext sinnvoll:\n"
            "Wenn das Wasser langsam und unsichtbar verschwindet, sagt man es ___. "
            "Die Wasserteilchen an der Wasseroberfläche bewegen sich auseinander und werden von der ___ aufgenommen. "
            "Je ___ die Luft ist, umso ___ läuft dieser Vorgang ab. "
            "Das Wasser befindet sich nun in einem ___ Zustand. "
            "Wird die Luft ___, kann sie nicht mehr so viele Wasserteilchen aufnehmen. "
            "Die Teilchen rücken wieder zusammen und bilden winzige ___. "
            "Diese halten sich an kleinsten Staubteilchen in der Luft oder an kühlen Gegenständen fest. "
            "So können wir sie wieder sehen. Man sagt, das Wasser ___. Es ist wieder in einem ___ Zustand."
        ),
        "answer": (
            "verdunstet; Luft; wärmer; schneller; gasförmigen; kalt; Tröpfchen; kondensiert; flüssigen."
        ),
        "steps": [
            "Langsames, unsichtbares Verdunsten → Verdunstung.",
            "Wasserteilchen gehen in die Luft über.",
            "Wärmere Luft → schnellere Verdunstung → gasförmiger Zustand.",
            "Kälter werdende Luft → Sättigung erreicht → Tröpfchenbildung.",
            "Wasser kondensiert → wird wieder flüssig.",
        ],
        "points": 9.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
    {
        "n": 13,
        "type": "Unterschiede nennen mit Beispiel",
        "text": (
            "Wir haben zweimal im Klassenzimmer Wasser „verschwinden” lassen.\n"
            "Versuch 1: Die nasse Tafel wird wieder trocken.\n"
            "Versuch 2: Etwas Wasser in einem Topf kochen lassen.\n"
            "Einmal ist es verdunstet und einmal ist es verdampft.\n"
            "Nenne 2 Unterschiede zwischen der Verdunstung und dem Verdampfen und gib jeweils ein weiteres Beispiel an!"
        ),
        "answer": (
            "Verdunstung: Unsichtbare Wasserteilchen steigen permanent in die Luft. "
            "Das Wasser muss nicht erhitzt werden. "
            "Beispiele: Haare mit dem Fön trocknen, Wasserpfützen trocknen aus, Blumen im Garten gießen.\n"
            "Verdampfen: Sichtbarer Wasserdampf steigt auf. "
            "Das Wasser muss erhitzt werden (auf 100 °C). "
            "Beispiel: Wasserdampf bei Flugzeugen am Himmel sichtbar."
        ),
        "steps": [
            "Unterschied 1: Verdunstung unsichtbar, Verdampfen sichtbar.",
            "Unterschied 2: Verdunstung braucht keine Erhitzung, Verdampfen erfordert 100 °C.",
            "Beispiel Verdunstung: Pfützen trocknen aus, nasse Wäsche trocknet.",
            "Beispiel Verdampfen: Kochtopf ohne Deckel, Dampf über heißem Tee.",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": ["hsu.klasse3.wasser.kreislauf"],
    },
]

NEW_KNOWLEDGE = []
