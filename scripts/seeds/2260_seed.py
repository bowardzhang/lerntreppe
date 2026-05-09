EXERCISE = {
    "id": "2260",
    "subject": "Deutsch",
    "grade": 4,
    "title": "Leseprobe: CATLUXApp – Nutzungsbedingungen und Datenschutz",
    "topic": "Leseverstehen, Sachtext, App, Internet, Datenschutz, Nutzungsbedingungen",
    "publisher": "CATLUX",
    "source_pdf": "2260.pdf",
    "answer_pdf": "2260 (1).pdf",
    "total_points": 28.0,
}

LESETEXT = (
    "CATLUXApp – Nutzungsbedingungen und Datenschutz\n\n"
    "CATLUXApp ist eine App für Smartphones und größere Computer. Damit "
    "können sich zwei oder mehr Menschen Nachrichten schicken. Diese "
    "Nachrichten können Texte enthalten, Tonaufnahmen, Fotos oder Videos. "
    "Da der aktuelle Datenschutz sehr mangelhaft ist, ist die Gefahr groß, "
    "dass Kinder in Kontakt mit Unbekannten kommen oder mit unerwünschten "
    "Videos, Nachrichten oder Kettenbriefen überschwemmt werden. Die Webseite "
    "von CATLUXApp wird jetzt auch auf Deutsch angeboten und richtet sich an "
    "ein deutschsprachiges Publikum. Trotzdem wird nur eine englische Version "
    "der Nutzungsbedingungen – auf der Seite auch unter AGB zu finden – zur "
    "Verfügung gestellt. Auch wenn man davon ausgehen kann, dass ca. 60 % der "
    "Deutschen in der Lage sind, eine Konversation in Englisch zu führen, "
    "bedeutet das noch nicht, dass sie auch Rechtsenglisch verstehen. Wie das "
    "Landgericht Berlin mit Urteil vom 09.05.2023 entschied, sind daher die "
    "derzeitigen AGB von CATLUXApp als ungültig anzusehen.\n\n"
    "Auszug aus den Nutzungsbedingungen:\n"
    "1. CATLUXApp sucht selbstständig in den auf dem Telefon gespeicherten "
    "Kontakten nach anderen registrierten Nutzern.\n"
    "2. Hat ein Unbefugter Zugriff auf ein Kundenkonto, übernimmt CATLUXApp "
    "keinerlei Haftung; der Kunde haftet für eventuell entstehende Schäden.\n"
    "3. Der Status-Text kann von allen Nutzern gesehen werden. CATLUXApp "
    "garantiert keinerlei Vertraulichkeit. Status-Angaben dürfen zu "
    "geschäftlichen Zwecken verwendet werden.\n"
    "4. CATLUXApp behält sich das Recht vor, jeden Nutzer aus beliebigem "
    "Grund von dem Dienst auszuschließen.\n"
    "5. CATLUXApp schließt jegliche Haftung aus.\n"
    "6. Nur Personen über 16 Jahre dürfen CATLUXApp nutzen.\n"
    "7. Im Falle eines Rechtsstreits ist der Gerichtsstand Santa Monica Bay, "
    "Kalifornien.\n"
    "8. Alle Ansprüche müssen innerhalb eines Jahres nach ihrem Entstehen "
    "geltend gemacht werden.\n\n"
    "Auszug aus der Datenschutzerklärung:\n"
    "1. Status oder andere Inhalte werden nicht als personenbezogene Daten "
    "betrachtet.\n"
    "2. CATLUXApp überprüft regelmäßig das Adressbuch im Telefon.\n"
    "3. Bei der Nutzung werden Datum, Zeit und Telefonnummern gespeichert.\n"
    "4. Nur Telefonnummern werden gespeichert, Namen erscheinen nur lokal.\n"
    "5. Eine Nachricht, die nicht gesendet werden kann, wird auf Servern "
    "längstens für 30 Tage zwischengespeichert.\n"
    "6. Telefonnummern können ohne weitere Einwilligung für Nicht-Marketing- "
    "oder Verwaltungszwecke verwendet werden.\n"
    "7. Nutzerdaten werden für Vorlieben/Trends-Analyse verwendet (IP-Adresse, "
    "Browsertyp).\n"
    "8. Cookies werden eingesetzt.\n"
    "9. Personenbezogene Daten werden für gewerbliche Zwecke an Dritte "
    "übermittelt.\n"
    "10. Personenbezogene Daten werden bei gesetzlicher Pflicht offenbart.\n"
    "11. CATLUXApp erhebt wissentlich keine personenbezogenen Daten von "
    "Personen unter 16 Jahren.\n"
    "12. Außerhalb der USA übermitteln Nutzer ihre Daten in die USA und "
    "akzeptieren kalifornisches Recht.\n"
    "13. Bei Verkauf von CATLUXApp gehen Nutzerdaten an das andere Unternehmen "
    "über.\n\n"
    "Fußnoten:\n"
    "App = Computer-Programm ; Smartphone = Telefon mit Internet ; "
    "AGB = Allgemeine Geschäftsbedingungen ; offline = nicht mit Internet "
    "verbunden ; Server = Computer ohne Bildschirm zum Speichern ; "
    "Marketing = Werbung ; IP-Adresse = Adresse für Geräte im Netz ; "
    "Browser = Programm zum Anschauen von Internetseiten ; Cookies = kleine "
    "Datenmengen, die der Server speichert."
)

QUESTIONS = [
    {
        "n": 1,
        "type": "Textart",
        "text": (
            f"Lesetext:\n{LESETEXT}\n\n"
            "Um was für eine Art Text handelt es sich?\n"
            "(a) Gebrauchsanweisung (b) Personenbeschreibung (c) Fachbeitrag (d) Erzählung"
        ),
        "answer": "Richtig: (c) Fachbeitrag.",
        "steps": ["Sachtext mit fachlichen Informationen."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 2,
        "type": "Synonyme",
        "text": (
            "Finde Synonyme:\n"
            "Publikum ___\n"
            "Konversation ___\n"
            "Unbefugter ___\n"
            "lokal ___"
        ),
        "answer": (
            "Publikum → Gesellschaft, Volk, Leute ; "
            "Konversation → Gespräch ; "
            "Unbefugter → unrechtmäßige Person ; "
            "lokal → örtlich, gebietsweise."
        ),
        "steps": ["Synonyme finden."],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 3,
        "type": "Autor unbekannt",
        "text": "Wer hat den Text wann geschrieben?",
        "answer": "Das weiß man nicht (Angaben fehlen).",
        "steps": ["Keine Autorenangabe im Text."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 4,
        "type": "Funktion CATLUXApp",
        "text": "Was kann man mit CATLUXApp machen?",
        "answer": "Man kann sich Nachrichten senden mit Text, Tonaufnahmen, Fotos oder Videos.",
        "steps": ["Aus dem 1. Absatz."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 5,
        "type": "Nicht für Kinder",
        "text": "Wieso ist CATLUXApp nicht für Kinder geeignet?",
        "answer": (
            "Kinder können in Kontakt mit Unbekannten kommen oder mit "
            "unerwünschten Videos, Nachrichten oder Kettenbriefen "
            "überschwemmt werden."
        ),
        "steps": ["Aus dem 1. Absatz."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 6,
        "type": "Urteil Landgericht",
        "text": "Was hat das Landgericht Berlin 2023 entschieden?",
        "answer": "Es hat entschieden, dass die AGB von CATLUXApp ungültig sind.",
        "steps": ["Aus dem 1. Absatz."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 7,
        "type": "Begründung Urteil",
        "text": "Warum hat das Landgericht so entschieden?",
        "answer": "Viele Menschen können kein Englisch oder kein Rechtsenglisch verstehen.",
        "steps": ["Aus dem 1. Absatz."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 8,
        "type": "Nutzungsbedingungen",
        "text": (
            "Welche Aussagen treffen auf die Nutzungsbedingungen zu?\n"
            "(a) Sie garantieren, den Status-Text vertraulich zu behandeln.\n"
            "(b) Status nur für eigene Kontakte einstellbar.\n"
            "(c) Nutzung ab 12 Jahren.\n"
            "(d) Sie können jederzeit das Nutzen der App verbieten.\n"
            "(e) Verlangt Zugriff auf die Kontakte."
        ),
        "answer": "Richtig: (d) und (e).",
        "steps": ["Nutzungsbedingungen lesen."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 9,
        "type": "Auszug Datenschutz",
        "text": (
            "Bei der Datenschutzerklärung handelt es sich nur um einen Auszug. "
            "Unterstreiche die entsprechende Stelle grün!"
        ),
        "answer": "'Nachfolgend finden Sie eine kurze Übersicht über ausgewählte Punkte der Datenschutzerklärung.'",
        "steps": ["Stelle markieren."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 10,
        "type": "Punkt 1 erklären",
        "text": "Lies den ersten Punkt der Datenschutzerklärung. Erkläre mit eigenen Worten.",
        "answer": "Alles was man schreibt, gilt nicht als personenbezogene Daten – ein eigentümlicher Schutz fehlt.",
        "steps": ["Eigene Worte verwenden."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 11,
        "type": "Speicherdauer",
        "text": (
            "Wie lange bleibt eine Nachricht, die nicht zugestellt werden kann, "
            "auf den Servern?\n"
            "(a) So lange wie CATLUXApp es will\n"
            "(b) Für immer\n"
            "(c) Für 30 Tage\n"
            "(d) Für einen Tag"
        ),
        "answer": "Richtig: (c) Für 30 Tage.",
        "steps": ["Aus Datenschutz Punkt 5."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 12,
        "type": "Werbezwecke",
        "text": (
            "Deine Telefonnummer kann ohne deine Einwilligung zu Werbezwecken "
            "verwendet werden.\n"
            "(a) Das stimmt (b) Das stimmt nicht\n"
            "Begründe und unterstreiche blau!"
        ),
        "answer": (
            "Das stimmt nicht. Punkt 6 sagt 'für Nicht-Marketing- oder "
            "Verwaltungszwecke', nicht für Werbung."
        ),
        "steps": ["Datenschutz Punkt 6 prüfen."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 13,
        "type": "Punkt 11 überflüssig",
        "text": (
            "Lies den 11. Punkt der Datenschutzerklärung. Erkläre, warum er "
            "eigentlich überflüssig ist."
        ),
        "answer": (
            "Punkt 11 sagt, dass keine Daten von unter 16-Jährigen erhoben werden. "
            "Das ist überflüssig, da laut Nutzungsbedingung Punkt 6 die App nur "
            "ab 16 Jahren nutzbar ist."
        ),
        "steps": ["Verbindung zwischen den Bestimmungen herstellen."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 14,
        "type": "Recht Klage",
        "text": (
            "Wenn man CATLUXApp verklagt, wird deutsches Recht angewendet.\n"
            "(a) Stimmt nur in Deutschland.\n"
            "(b) Stimmt nicht. Egal wo man lebt, es wird kalifornisches Recht angewendet."
        ),
        "answer": "(b) Stimmt nicht — kalifornisches Recht wird angewendet (Datenschutz Punkt 12).",
        "steps": ["Datenschutz Punkt 12 prüfen."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 15,
        "type": "Verkauf Daten",
        "text": (
            "Wenn CATLUXApp verkauft wird, werden alle gespeicherten Daten gelöscht.\n"
            "(a) Stimmt (b) Stimmt nicht"
        ),
        "answer": "(b) Stimmt nicht. Daten gehen an das andere Unternehmen über (Punkt 13).",
        "steps": ["Datenschutz Punkt 13 prüfen."],
        "points": 1.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 16,
        "type": "Bedenklichster Punkt",
        "text": "Welchen Punkt findest du am bedenklichsten? Begründe deine Meinung!",
        "answer": "Individuelle Lösungen.",
        "steps": ["Eigene Meinung."],
        "points": 2.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
    {
        "n": 17,
        "type": "Vor- und Nachteile",
        "text": "Nenne 2 Vorteile und 2 Nachteile von Nachrichtendiensten!",
        "answer": (
            "Vorteile: schnelle, direkte Kommunikation; sofortige Antworten. ; "
            "Nachteile: Datenschutz (Telefonnummer nötig); unerwünschte "
            "Kontaktaufnahme/Spam; Cybermobbing; Kettenbriefe; problematische Inhalte."
        ),
        "steps": ["2 Vorteile und 2 Nachteile."],
        "points": 4.0,
        "has_image": False,
        "image": None,
        "knowledge": ["deutsch.klasse4.texte.leseverstehen"],
    },
]

NEW_KNOWLEDGE = []
