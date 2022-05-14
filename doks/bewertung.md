# Bewertung
Am Ende des Datathons wird eine Jury alle eingereichten Beiträge bewerten. Die
Einreichungen werden auf quantitativer und qualitativer Ebene bewertet. Sie werden
Weitere Informationen zur quantitativen Bewertung finden Sie weiter unten.

Für diesen Wettbewerb gelten die folgenden Bewertungskriterien:
* Quantitative Bewertung der Antworten des Q&A Bots

  Vorgegebene Fragen müssen vom Bot beantwortet werden. Die Antworten werden dann
  Die Antworten werden dann mit Hilfe bekannter Techniken mit den Beispielantworten verglichen.
* Qualitative Bewertung der Q&A Bot-Antworten

  Die Jury stellt dem Bot 5 vordefinierte Fragen und bewertet diese im Hinblick auf
  hinsichtlich ihrer Nützlichkeit aus Kundensicht
* Qualität des Pitches

  Bewertung des Pitches in Bezug auf Storytelling, Förderung der
  Lösung/Ansatzes, Attraktivität der Präsentation
* Kreativität sowie Umfang und Tiefe der Lösung

  Wie kreativ sind die Features und wie gut passen sie zum Gesamtkonzept?
  Sowie Umfang und Tiefe der Features

## Details zur qualitativen Bewertung
Um der Bewertung auch einen qualitativen Aspekt zu geben, wird die Jury dem Bot
vordefinierte Fragen stellen. Die Antworten werden auf der Grundlage bewährter
Metriken bewertet. Das Skript, das verwendet wird, finden Sie
[hier](./../scripts/quantitative-evaluation.py).

### Wie werden wir die qualitative Bewertung durchführen?
Während des Datathons werden wir jedes Team besuchen und eine Slack-Anwendung mit ihrem Bot verbinden.
ihrem Bot. Nach Ablauf der Einreichungsfrist werden wir dann diese Anwendung nutzen, um die
vordefinierten Fragen stellen. Die gegebenen Antworten werden dann zur Berechnung der
quantitative und qualitative Bewertung.

### Datensatz
Die quantitative Bewertung basiert auf den Informationen, die in den folgenden Datensätzen enthalten sind:
* [FAQs zur Reiseversicherung | Allianz Global Assistance](https://www.allianztravelinsurance.com/faq.htm)
* [COVID-19 FAQs | Allianz Global Assistance](https://www.allianztravelinsurance.com/covid-19-faq.htm)
* [Allgemeine Geschäftsbedingungen (AGB) - Allianz Travel Switzerland](https://www.allianz-travel.ch/en_CH/services/download-center.html)

Sie finden alle diese Datensätze im Ordner [dataset](./../dataset/) des
Stammverzeichnis dieses Repositorys.

Die Fragen, die gestellt werden, sind eine Kombination aus verschiedenen Schwierigkeits
Stufen. Sie enthalten einfache Fragen mit Antworten, die in einzelnen Daten
Quelle. Nicht-triviale Fragen mit den Informationen aus einer Datenquelle.
Fragen, die nur durch Kombination der Informationen aus mehreren Datenquellen beantwortet werden können.
Datenquellen beantwortet werden können.

### Q&A Beispiele
* Was ist in den nicht erstattungsfähigen Reisekosten enthalten?

  Zu den nicht erstattungsfähigen Kosten gehören im Voraus gezahlte Reisekautionen/Zahlungen, die
  verloren gehen, wenn Sie die Reise aus einem bestimmten Grund vor der Abreise stornieren müssen. Einige
  Beispiele sind Mietkosten für den Urlaub, Campingplatzgebühren, Gebühren für einen Mietwagen;
  Eintrittskarten für Touren oder Veranstaltungen sowie Hotel- und Flugticketkosten. Erkundigen Sie sich
  Welche Kosten für Ihre Reise nicht erstattungsfähig sind, erfahren Sie bei Ihrem Reiseanbieter.
  nicht erstattungsfähig sind, da die Stornierungsrichtlinien unterschiedlich sind.

* Was muss ich tun, bevor ich eine Reise buche?

  Bevor Sie eine Reise buchen, können Sie sich auf unserer interaktiven Karte über aktuelle
  Informationen über Reiseanforderungen und Einreisebeschränkungen für internationale
  Reiseziele, einschließlich COVID-19-Tests, Impfvorschriften, erforderliche
  Reisedokumente und Quarantänezeiten. (Der Inhalt wird von Sherpa, einem
  angeschlossenen Drittanbieter).

* Mein Partner ist krank. Wir sind nicht verheiratet. Sind wir versichert?

  Nein, unverheiratete Partner sind nicht versichert.
 Übersetzt mit www.DeepL.com/Translator (kostenlose Version)
