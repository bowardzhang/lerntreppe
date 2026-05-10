EXERCISE = {
    "id": "0701",
    "subject": "Deutsch",
    "grade": 4,
    "title": "3. Lernzielkontrolle: Faelle, Satzergaenzungen, Konjunktionen",
    "topic": "Kasus, Satzglieder (Subjekt/Praedikat/Objekt), Zeitangabe, Ortsangabe, Konjunktionen",
    "publisher": "CATLUX",
    "source_pdf": "0701.pdf",
    "answer_pdf": "0701 (1).pdf",
    "total_points": 51.0,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Lateinische Fachbegriffe der Grammatik",
        "text": (
            "Wie heißen die lateinischen Fachbegriffe?\n"
            "2. Fall: ___    Satzgegenstand: ___\n"
            "1. Fall: ___    Satzergaenzung: ___\n"
            "Satzaussage: ___    3. Fall: ___"
        ),
        "answer": (
            "2. Fall = Genitiv ; Satzgegenstand = Subjekt ; "
            "1. Fall = Nominativ ; Satzergaenzung = Objekt ; "
            "Satzaussage = Praedikat ; 3. Fall = Dativ"
        ),
        "steps": [
            "1. Fall = Nominativ, 2. Fall = Genitiv, 3. Fall = Dativ, 4. Fall = Akkusativ.",
            "Satzgegenstand = Subjekt (wer/was?).",
            "Satzaussage = Praedikat (Verb).",
            "Satzergaenzung = Objekt (Akkusativ, Dativ oder Genitiv).",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.kasus",
            "deutsch.klasse4.grammatik.satzglieder",
        ],
    },
    {
        "n": 2,
        "type": "Fall und Frage bestimmen",
        "text": (
            "Schreibe auf, in welchem Fall das unterstrichene Nomen steht, "
            "und schreibe die passende Frage darunter.\n"
            "1. Ich brachte die Hausaufgaben meines Freundes von der Schule mit. (meines Freundes)\n"
            "2. Die Lehrerin schimpft dann oft meinen Freund. (meinen Freund)\n"
            "3. Mein Freund macht oft seine Hausaufgaben nicht. (Mein Freund)\n"
            "4. Ich helfe meinem Freund bei den Hausaufgaben. (meinem Freund)"
        ),
        "answer": (
            "1. 2. Fall; Wessen Hausaufgaben brachte ich mit? ; "
            "2. 4. Fall; Wen oder was schimpft die Lehrerin? ; "
            "3. 1. Fall; Wer oder was macht seine Hausaufgaben nicht? ; "
            "4. 3. Fall; Wem helfe ich bei den Hausaufgaben?"
        ),
        "steps": [
            "meines Freundes: Genitivattribut -> 2. Fall, Wessen?",
            "meinen Freund: Akkusativobjekt -> 4. Fall, Wen/was?",
            "Mein Freund: Subjekt -> 1. Fall, Wer/was?",
            "meinem Freund: Dativobjekt (helfen) -> 3. Fall, Wem?",
        ],
        "points": 8.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.kasus",
        ],
    },
    {
        "n": 3,
        "type": "Namen im richtigen Fall einsetzen",
        "text": (
            "Setze die Nomen in der richtigen Form ein und bestimme den Fall:\n"
            "Marius gibt ___ einen Knochen. (sein Hund)\n"
            "Das Halsband ___ ist rot. (das Tier)\n"
            "Der Junge liebt ___ sehr. (der Hund)\n"
            "Hasso ist ein Geschenk ___. (seine Oma)\n"
            "___ versorgt Marius gerne. (sein Haustier)"
        ),
        "answer": (
            "seinem Hund (3. Fall) ; "
            "des Tieres (2. Fall) ; "
            "den Hund (4. Fall) ; "
            "seiner Oma (2. Fall) ; "
            "Sein Haustier (1. Fall)"
        ),
        "steps": [
            "geben + Wem? -> Dativ: seinem Hund (3. Fall).",
            "Wessen Halsband? -> Genitiv: des Tieres (2. Fall).",
            "lieben + Wen? -> Akkusativ: den Hund (4. Fall).",
            "Geschenk wessen? -> Genitiv: seiner Oma (2. Fall).",
            "Subjekt des Satzes -> Nominativ: Sein Haustier (1. Fall).",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.kasus",
        ],
    },
    {
        "n": 4,
        "type": "Satzglieder zuordnen",
        "text": (
            "Ordne die Ausdruecke den richtigen Satzgliedfunktionen zu:\n"
            "ich ; suchen ; dem Bruder ; in der Schule ; der Freundin ; "
            "dem Verkehr ; Mitte des Monats ; auf dem Baum ; des Vaters ; mir\n"
            "Satzgegenstand / Satzaussage / Satzergaenzung 2.Fall / "
            "Satzergaenzung 3.Fall / Satzergaenzung 4.Fall / Zeitangabe / Ortsangabe"
        ),
        "answer": (
            "Satzgegenstand (1.Fall): ich. "
            "Satzaussage: suchen. "
            "Satzergaenzung 2.Fall: des Vaters. "
            "Satzergaenzung 3.Fall: dem Bruder, der Freundin, dem Verkehr, mir. "
            "Zeitangabe: Mitte des Monats. "
            "Ortsangabe: in der Schule, auf dem Baum."
        ),
        "steps": [
            "ich = Subjekt (Satzgegenstand).",
            "suchen = Verb (Satzaussage).",
            "des Vaters = Genitiv (2. Fall).",
            "dem Bruder, der Freundin, dem Verkehr, mir = Dativ (3. Fall).",
            "Mitte des Monats = Wann? -> Zeitangabe.",
            "in der Schule, auf dem Baum = Wo? -> Ortsangabe.",
        ],
        "points": 10.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.satzglieder",
            "deutsch.klasse4.grammatik.kasus",
        ],
    },
    {
        "n": 5,
        "type": "Satz erweitern",
        "text": (
            "Erweitere den Satz um eine Satzaussage, eine Zeitangabe, eine "
            "Ortsangabe und Ergaenzungen im 3. und 4. Fall:\n"
            "Der Postbote ___"
        ),
        "answer": "Beispiel: Der Postbote bringt mir heute ein Paeckchen ins Haus.",
        "steps": [
            "Satzaussage: bringt.",
            "3. Fall: mir (Wem?).",
            "4. Fall: ein Paeckchen (Was?).",
            "Zeitangabe: heute (Wann?).",
            "Ortsangabe: ins Haus (Wohin?).",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.satzglieder",
            "deutsch.klasse4.grammatik.kasus",
        ],
    },
    {
        "n": 6,
        "type": "Eigenen Satz bilden",
        "text": (
            "Bilde selbst einen Satz mit Satzgegenstand, Ortsangabe, Zeitangabe "
            "und zwei Faellen (3. Fall und 4. Fall)."
        ),
        "answer": (
            "Beispiel: Gestern kam zu uns in die Schule eine Gruppe des Opernhauses."
        ),
        "steps": [
            "Satzgegenstand + Zeitangabe + Ortsangabe + 3. Fall + 4. Fall kombinieren.",
            "Reihenfolge frei waehlbar.",
        ],
        "points": 5.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.satzglieder",
            "deutsch.klasse4.grammatik.kasus",
        ],
    },
    {
        "n": 7,
        "type": "Endungen ergaenzen",
        "text": (
            "Ergaenze die richtigen Endungen:\n"
            "Aufgeregt habe ich d___ Brief mein___ Freund vorgelesen. "
            "D___ Brief kam von mein___ Onkel aus Hamburg. "
            "Er schreibt, dass ich ___ am naechst___ Wochenende mit mein___ "
            "best___ Freund besuchen soll.\n"
            "Ich werde mein___ Onkel und mein___ Tante ein___ schoenen Brief "
            "schreiben und mich bei ___ bedanken. "
            "Ich werde ___ dann ein schoen___ Foto mein___ Familie mitbringen. "
            "Natürlich soll ich ___ auch von mein___ Eltern schoene Grüße ausrichten."
        ),
        "answer": (
            "den Brief meinem Freund ; Der Brief meinem Onkel ; "
            "ihn am naechsten Wochenende mit meinem besten Freund ; "
            "meinem Onkel und meiner Tante einen schoenen Brief ; bei ihnen ; "
            "ihnen ein schoenes Foto meiner Familie ; ihnen von meinen Eltern"
        ),
        "steps": [
            "den Brief (Akk., mask.) ; meinem Freund (Dativ).",
            "Der Brief (Nom.) ; meinem Onkel (Dativ, von).",
            "ihn (Akk.); naechsten (Dat.); meinem (Dat.); besten (Dat.).",
            "meinem Onkel (Dat.) ; meiner Tante (Dat.) ; einen schoenen (Akk.).",
            "bei ihnen (Dativ Pl.) ; ihnen (Dativ Pl.) ; schoenes (Akk.) ; meiner (Gen.).",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.kasus",
        ],
    },
    {
        "n": 8,
        "type": "Sätze mit Konjunktionen verbinden",
        "text": (
            "Verbinde die passenden Sätze mit sinnvollen Konjunktionen "
            "(jede nur einmal):\n"
            "1. Moni hat ihre Freundin verpasst. / Ich darf den Krimi nicht anschauen.\n"
            "2. Vater muss schnell zum Flughafen. / Sie schaut sich einen Spielfilm an.\n"
            "3. Wir haben das Spiel verloren. / Sie ist zu spaet gekommen.\n"
            "4. Mutter buegelt Vaters Hemden. / Wir hatten uns sehr angestrengt.\n"
            "5. Meine Oma musste sehr lachen. / Er hat seine Geschaefte erledigt.\n"
            "6. Vater hat mir streng verboten. / Ich erzaehlte ihr einen lustigen Witz."
        ),
        "answer": (
            "1. Moni hat ihre Freundin verpasst, weil sie zu spaet gekommen ist. ; "
            "2. Vater muss schnell zum Flughafen, nachdem er seine Geschaefte erledigt hat. ; "
            "3. Wir haben das Spiel verloren, obwohl wir uns sehr angestrengt hatten. ; "
            "4. Mutter buegelt Vaters Hemden, waehrend sie sich einen Spielfilm anschaut. ; "
            "5. Meine Oma musste sehr lachen, da ich ihr einen lustigen Witz erzaehlte. ; "
            "6. Vater hat mir streng verboten, dass ich den Krimi anschauen darf."
        ),
        "steps": [
            "1. Begruendung -> weil.",
            "2. Zeitlich danach -> nachdem.",
            "3. Gegensatz -> obwohl.",
            "4. Gleichzeitig -> waehrend.",
            "5. Begruendung (schwaechere) -> da.",
            "6. Inhalt des Verbots -> dass.",
        ],
        "points": 6.0,
        "has_image": False,
        "image": None,
        "knowledge": [
            "deutsch.klasse4.grammatik.wortarten",
        ],
    },
]

NEW_KNOWLEDGE = []
