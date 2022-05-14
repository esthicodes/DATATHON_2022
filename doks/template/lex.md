# Amazon Lex einrichten
[Amazon Lex](https://aws.amazon.com/lex/) ist ein KI-gestützter Chatbot-Dienst.
Sie verwenden ihn in diesem Einsatz, um die FAQs per Chat verfügbar zu machen.

Weitere Informationen über Amazon Lex finden Sie in der
[Dokumentation](https://docs.aws.amazon.com/lexv2/latest/dg/what-is.html).

Um sich mit den Kernkonzepten und der Terminologie von Amazon Lex vertraut zu machen, können Sie
lesen Sie den Abschnitt [Wie es
funktioniert](https://docs.aws.amazon.com/lexv2/latest/dg/how-it-works.html) in der
der Dokumentation lesen.

## Einrichtung
Der erste Schritt ist der Besuch der [Amazon Lex Console
Dienst](https://eu-west-1.console.aws.amazon.com/lexv2/home?region=eu-west-1#bots).
Dort können Sie einen Bot erstellen. Bitte stellen Sie sicher, dass Sie sich auf der **Lex V2
Konsole** befinden.

### Erstellen des Bots
1. Klicken Sie auf *Bot erstellen*.
1. *Bot-Einstellungen konfigurieren*.
   * Wählen Sie **Einen leeren Bot erstellen**.
   * Geben Sie ihm einen **Bot-Namen**.
   * Wählen Sie **Erstellen Sie eine Rolle mit grundlegenden Amazon Lex-Berechtigungen** im Abschnitt **IAM
     permissions** Abschnitt
   * Wählen Sie **Nein** im Abschnitt **Children's Online Privacy Protection Act (COPPA)**
     Abschnitt
1. * Sprachen hinzufügen*
   * Fügen Sie *Englisch (US)* als Sprache hinzu.
   *Deutsch (DE)* als Sprache hinzufügen

Nach der erfolgreichen Erstellung des Bots werden Sie zum Abschnitt *Intent* weitergeleitet
Bereich der Sprache *Englisch (US)* weitergeleitet. Hier können Sie einen neuen Intent hinzufügen. Wir müssen
zwei Intents erstellen, den Standard-Intent und einen für die Kendra-Integration.

### Standard-Intent erstellen
In Lex V2 müssen Sie mindestens einen Intent mit einer *Aussage* haben, den so genannten
Standard-Intent. Sie können die Benutzeroberfläche verwenden, zu der Sie weitergeleitet wurden, um diesen
Standard-Intent erstellen.
1. Intent-Details
   * Ändern Sie den **Intent-Namen**: DefaultIntent
1. Beispielhafte Äußerungen
   * **Aussage hinzufügen**: "Hallo Datentage 2022"
1. Abschließende Antworten
   * Nachricht: "Schön, dass Sie an der SAA Q&A Bot Challenge teilnehmen"
1. Klicken Sie auf **Absicht speichern** am unteren Rand
1. Klicken Sie auf **Build** am unteren Rand
1. *Optional:* Nachdem der Build erfolgreich war, können Sie den Bot mit dem **Test**
   Schaltfläche am unteren Rand

Sobald Sie den Bot mit Slack verbunden haben, können Sie *Hallo Data Days 2022"
als erste Nachricht an den Bot verwenden.

### Bot mit Kendra verknüpfen
Nachdem Sie den Standard-Intent erfolgreich erstellt haben, erstellen Sie einen neuen Intent, um ihn mit dem Kendra-Index zu verknüpfen.

**HINWEIS:** Der *eingebaute Intent* unterstützt nur *Englisch (US)* als Sprache. Also
stellen Sie bitte sicher, dass Sie die richtige Sprache ausgewählt haben. Und auch, dass die
FAQs in Kendra die richtige Sprache haben.

1. Rufen Sie die Übersichtsseite **Intents** auf
1. Klicken Sie auf **Intent hinzufügen** und wählen Sie *Eingebaute Intention verwenden*.
   * **Eingebaute Absicht**: Wählen Sie *AMAZON.KendraSearchIntent*.
   * Geben Sie ihm einen **Intent-Namen**.
   * Wählen Sie den zuvor erstellten Kendra-Index aus der Dropdown-Liste aus.
1. Sie werden zu dem neu erstellten Intent weitergeleitet
1. Abschließende Antworten
   * Fügen Sie den folgenden Text als **Nachricht** ein
     * Ich habe eine FAQ-Frage für Sie gefunden: ((x-amz-lex:kendra-search-response-question_answer-question-1)), und die Antwort lautet ((x-amz-lex:kendra-search-response-question_answer-answer-1))
   * Fügen Sie die folgenden zwei Zeilen als **Variationen** ein
     * Ich habe einen Auszug aus einem hilfreichen Dokument gefunden: ((x-amz-lex:kendra-search-response-document-1))
     * Ich denke, die Antwort auf Ihre Fragen lautet ((x-amz-lex:kendra-search-response-answer-1))
1. Klicken Sie auf **Absicht speichern** am unteren Rand
1. Klicken Sie unten auf **Build**.
1. *Optional:* Nachdem der Build erfolgreich war, können Sie den Bot mit dem **Test**
   Schaltfläche am unteren Rand
   * Senden Sie *Warum brauche ich Reiseschutz?* an den Bot

Nun haben Sie erfolgreich einen Amazon Lex-Bot erstellt und ihn mit dem
einem Kendra-Index verbunden.

## Nächster Schritt: Amazon mit Slack verbinden
Der letzte Schritt besteht darin, Amazon Lex mit Slack zu verbinden. Um dies einzurichten, gehen Sie auf die Seite
Abschnitt [Slack einrichten](./slack.md).
