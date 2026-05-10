EXERCISE = {
    "id": "0318",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: Wissenswertes über Portugal",
    "topic": "Leseverstehen, Sachtext, Geografie, Portugal",
    "publisher": "CATLUX",
    "source_pdf": "0318.pdf",
    "answer_pdf": "0318 (1).pdf",
    "total_points": 26.0,
}

LESETEXT = (
    "Wissenswertes über Portugal (Auszug)\n\n"
    "Die portugiesische Flagge ist gruen-rot. Die Farbe Gruen steht für die "
    "Hoffnung, Rot für das Blut jener, die für das Land ihr Leben gaben.\n\n"
    "Portugal liegt im Suedwesten Europas auf der Iberischen Halbinsel und "
    "hat eine Flaeche von 92 100 km². Es grenzt nur an Spanien und an den "
    "Atlantischen Ozean. Zu Portugal gehoeren auch die Inseln Madeira und die "
    "Azoren. Der laengste Fluss ist der Tejo. Der Norden ist gruen, bergig "
    "und mit Weinstoecken bedeckt. Der Sueden (Algarve) ist trockener, "
    "flacher und karg. Der Name Algarve stammt aus dem Arabischen 'Al-Gharb' "
    "und bedeutet 'der Westen'.\n\n"
    "Bekannte Seefahrer aus Portugal sind Heinrich der Seefahrer (ab 1419) "
    "und Vasco da Gama. Der Turm von Belem (1516) erinnert an die Zeit der "
    "großen Entdeckungen.\n\n"
    "Bis 1974 herrschte Salazar als Diktator. Seit dem 25. April 1974 ist "
    "Portugal eine Demokratie. 1993 trat das Land der Europaeischen Union "
    "bei. Vier wichtige Nationalfeiertage sind: Tag der Republik (5. Oktober), "
    "Tag der Freiheit (25. April), Nationalfeiertag (10. Juni) und Tag der "
    "Unabhaengigkeit (1. Dezember). Am 10. Juni 1980 starb der Dichter "
    "Luis de Camoes.\n\n"
    "Hauptstadt ist Lissabon. Über den Tejo führt eine 2278 m lange Bruecke "
    "(seit 1966). Im Norden liegt die Stadt Porto, von der der Portwein "
    "stammt. Vom Wein und der Stadt 'Porto' kommt auch der Landesname. "
    "Seit 2002 ist der Euro die Waehrung. Die Küche ist gepraegt von "
    "Stockfisch (Bacalhau), der auf viele Arten zubereitet wird, sowie "
    "Sardinen und Makrelen. Aus Portugal stammt auch viel Kork.\n\n"
    "In Portugal leben etwa 10 Millionen Menschen."
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Fragen zum Text in ganzen Sätzen",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Beantworte in ganzen Sätzen:\n"
            "(a) Was bedeuten die Farben der portugiesischen Flagge?\n"
            "(b) Woher stammt der Name 'Algarve' und was bedeutet er?\n"
            "(c) Nenne zwei wichtige Feiertage Portugals und wann sie gefeiert "
            "werden.\n"
            "(d) Was feiern die Portugiesen mit dem 'Tag der Unabhaengigkeit'?\n"
            "(e) Wer war Luis de Camoes?\n"
            "(f) Woher kommt der Name Portugal?"
        ),
        "answer": (
            "(a) Gruen steht für Hoffnung, Rot für das Blut jener, die für "
            "das Land ihr Leben gaben. ; "
            "(b) Der Name stammt aus dem Arabischen ('Al-Gharb') und bedeutet "
            "'Westen'. ; "
            "(c) Z. B. Tag der Republik (5. Oktober) und Tag der Freiheit "
            "(25. April). ; "
            "(d) Die Portugiesen feiern das Ende der spanischen Herrschaft am "
            "1. Dezember (vor mehr als 300 Jahren), einen wichtigen Schritt "
            "zur Unabhaengigkeit. ; "
            "(e) Ein portugiesischer Dichter, der am 10. Juni 1980 erwaehnt "
            "wird (sein Todestag wird gefeiert). ; "
            "(f) Vom Wein und der Stadt 'Porto' im Norden des Landes."
        ),
        "steps": [
            "Antworten in ganzen Sätzen formulieren.",
            "Auf Textstellen Bezug nehmen.",
        ],
        "points": 15.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
            "hsu.klasse4.europa.nachbarlaender",
        ],
    },
    {
        "n": 2,
        "type": "Aussage im Text identifizieren",
        "text": (
            "Welcher Satz steht so im Text? Kreuze an:\n"
            "(a) In Portugal gibt es immer wieder Stierkaempfe.\n"
            "(b) Die Portugiesen verwenden den Stockfisch immer wieder, "
            "wobei jeder seine eigenen Rezepte hat.\n"
            "(c) Die Portugiesen verwenden den Stockfisch sehr häufig, "
            "wobei viele eigene Rezepte beruehmt sind."
        ),
        "answer": "Richtig: (b).",
        "steps": [
            "Originalformulierung im Text suchen ('immer wieder', 'eigenen').",
        ],
        "points": 1.5,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 3,
        "type": "Richtige Aussagen ankreuzen",
        "text": (
            "Welche Aussagen sind richtig? Kreuze an:\n"
            "(1) Portugal grenzt an ein Meer.\n"
            "(2) In Portugal wachsen Reis, Orangen und Oliven.\n"
            "(3) Etwa 10 Millionen Menschen leben in Portugal.\n"
            "(4) Seit 1974 ist Portugal ein demokratischer Staat.\n"
            "(5) Portugal grenzt an Italien.\n"
            "(6) Salazar regiert Portugal heute noch.\n"
            "(7) Der Norden Portugals ist trocken und karg.\n"
            "(8) Vasco da Gama war ein Maler."
        ),
        "answer": "Richtig: (1), (2), (3), (4).",
        "steps": [
            "(5) falsch: Portugal grenzt an Spanien.",
            "(6) falsch: Salazar regierte bis 1974.",
            "(7) falsch: Der Sueden (Algarve) ist trocken/karg.",
            "(8) falsch: Vasco da Gama war ein Seefahrer.",
        ],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
    {
        "n": 4,
        "type": "Norden und Süden zuordnen",
        "text": (
            "Ordne die Eigenschaften zu (Norden / Sueden Portugals):\n"
            "flach, gruen, Weinstoecke, trocken, Gemueseplantagen, bergig, karg"
        ),
        "answer": (
            "Norden: gruen, Weinstoecke, Gemueseplantagen, bergig. ; "
            "Sueden: flach, trocken, karg."
        ),
        "steps": [
            "Aus dem Text die Beschreibungen entnehmen.",
        ],
        "points": 3.5,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
            "hsu.klasse4.europa.nachbarlaender",
        ],
    },
    {
        "n": 5,
        "type": "Im Text unterstreichen",
        "text": (
            "Unterstreiche im Text in den richtigen Farben:\n"
            "(rot) zwei Seefahrer ; (blau) die Waehrung ; (gruen) wofuer der "
            "Turm von Belem steht ; (gelb) Zubereitungsarten von Stockfisch."
        ),
        "answer": (
            "Seefahrer: Heinrich der Seefahrer, Vasco da Gama. ; "
            "Waehrung: Euro (seit 2002). ; "
            "Turm von Belem: erinnert an die Zeit der großen Entdeckungen "
            "(1516). ; "
            "Stockfisch: Bacalhau, auf viele Arten zubereitet (z. B. mit "
            "eigenen Rezepten)."
        ),
        "steps": [
            "Stellen im Text farblich markieren und auflisten.",
        ],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.texte.leseverstehen",
        ],
    },
]

NEW_KNOWLEDGE = []
