# Die Q&A-Bot-Vorlage
Die Herausforderung besteht darin, einen Q&A-Bot zu erstellen, der Reisenden beim Abrufen hilft
Angaben zu ihrer Versicherung. Der Schwerpunkt liegt auf der Arbeit in der Data Science
Seite und weniger auf der Infrastrukturseite. Daher finden Sie die
Anweisungen zum Einrichten einer grundlegenden End-to-End-Implementierung eines Q&A-Bots unten.
Wenn Sie diese Schritte abgeschlossen haben, können Sie mit einem Bot chatten und fragen
es einige grundlegende Fragen.

Die Q&A-Bot-Vorlage, die Sie bereitstellen, besteht aus den folgenden Komponenten:
* Ein Slack-Arbeitsbereich - um mit dem Bot zu interagieren
* Amazon Lex – der AWS-Service zum Erstellen von Konversationsschnittstellen
* Amazon Kendra - ein intelligenter Suchdienst
* Amazon S3 - zum Speichern der FAQ-Datensätze

![Vorlagenarchitektur](./images/template-architecture.png)

**Hinweis:** Der Amazon Kendra-Service wird nicht in allen AWS-Regionen unterstützt.
Daher sollten Sie eine der unterstützten Regionen auswählen. Wir empfehlen die Verwendung
die **EU (Irland) | Region eu-west-1**. Für alle Service-Kreationen und Arbeiten
dass Sie tun werden, müssen Sie sicherstellen, dass die richtige Region verwendet wird. Das
kann wie folgt erfolgen:
* **Programmgesteuerter Zugriff:** `export AWS_DEFAULT_REGION=eu-west-1` auf der CLI
* **Zugriff auf die AWS Management Console:** Wählen Sie die Region in der oberen rechten Ecke aus

Wir haben die Bereitstellung und Konfiguration der einzelnen Dienste aufgeteilt in
getrennte Abschnitte. In jedem von ihnen finden Sie eine Schritt-für-Schritt-Anleitung. Die Reihenfolge von
die Bereitstellung erfolgt in umgekehrter Reihenfolge als oben aufgeführt.

1. [Amazon Kendra einrichten](./bot-template/amazon-kendra.md)
1. [Amazon Lex einrichten](./bot-template/amazon-lex.md)
1. [Slack einrichten](./bot-template/slack.md)
