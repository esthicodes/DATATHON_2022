# Amazon Kendra einrichten
[Amazon Kendra](https://aws.amazon.com/kendra/) ist ein intelligenter Suchdienst
angetrieben durch maschinelles Lernen (ML). In dieser Template-Implementierung werden Sie
die Kendra FAQ-Funktion verwenden. Dies erlaubt Ihnen, einfache Suchen auf dem
bereitgestellten FAQ-Datensatz durchzuführen.

Weitere Informationen über Amazon Kendra finden Sie in der
[Dokumentation](https://docs.aws.amazon.com/kendra/latest/dg/what-is-kendra.html).

## Einrichten

### S3 Bucket erstellen
Um die FAQs zu Kendra hinzuzufügen, müssen Sie sie in einen S3-Bucket hochladen. Dies
kann mit den folgenden Schritten durchgeführt werden:
1. Gehen Sie zur [Amazon S3 Service Console](https://s3.console.aws.amazon.com/s3/buckets?region=eu-west-1)
1. Erstellen Sie ein neues Bucket
   * Geben Sie ihm einen **Bucket-Namen**. Der Name muss global eindeutig sein.
   * Wählen Sie **EU (Irland) eu-west-1** als AWS-Region.
   * Der Rest der Einstellungen kann auf den Standardwerten belassen werden
1. Hochladen der FAQ-Datensätze
   * Gehen Sie zu dem neu erstellten Bucket.
   * Klicken Sie auf die Schaltfläche **Upload**.
   * Laden Sie die `.json` Dateien aus dem Ordner [dataset](./../../dataset/) hoch

### Erstellen des Kendra-Index
Nachdem Sie die FAQ-Datensätze hochgeladen haben, müssen Sie den Amazon Kendra Service erstellen.
1. Rufen Sie die [Amazon Kendra Service
   Konsole](https://eu-west-1.console.aws.amazon.com/kendra/home?region=eu-west-1#indexes)
1. Erstellen Sie einen neuen Index
   * Geben Sie ihm einen **Indexnamen**.
   * Erstellen Sie eine neue **IAM-Rolle**.
2. Es muss keine spezielle **Benutzerzugriffskontrolle** konfiguriert werden
3. Wählen Sie die **Developer Edition** für die **Provisioning Editions** im
letzten Schritt

Nach der erfolgreichen Erstellung des Indexes werden Sie zur Index-Homepage weitergeleitet.
Seite weitergeleitet.

Der letzte Schritt bei der Kendra-Konfiguration ist dann das Hinzufügen der FAQs. Sie
Sie müssen diesen Schritt für beide Datensätze wiederholen:
* `COVID-19 FAQs | Allianz Global Assistance.json`
* `Reiseversicherung FAQs | Allianz Global Assistance.json`

**Hinweis:** FAQs werden in Kendra nicht als *Datenquellen* behandelt. Es gibt einen separaten
Menüpunkt auf der linken Seite, wo Sie die FAQs hochladen und verwalten können.

Beim Hinzufügen der FAQ stellen Sie bitte sicher, dass Sie die richtige Sprache für die
Datei, die Sie ausgewählt haben.
1. Klicken Sie auf den Menüpunkt **FAQs** auf der linken Seite
1. Wählen Sie **FAQ hinzufügen**.
   * Geben Sie ihr einen **FAQ-Namen**.

     Stellen Sie *-de* (oder etwas Ähnliches) voran, da Sie auch eine weitere Sprache hinzufügen müssen
     eine weitere Sprache
   * Wählen Sie die **Standardsprache** (z.B. *Englisch (en)*), um die Datei anzupassen.
   * Das **FAQ-Dateiformat** ist *JSON-Datei*.
   * **S3 durchsuchen** und den Datensatz auswählen, der der von Ihnen gewählten Sprache entspricht
    oben
   * Erstellen Sie eine neue **IAM-Rolle**.
1. Klicken Sie auf **Hinzufügen** und warten Sie, bis Sie auf die FAQ-Seite weitergeleitet werden

Die Erstellung und Indizierung der FAQs kann einige Zeit in Anspruch nehmen. Sie müssen nicht warten, bis
Sie müssen nicht warten, bis sie *Aktiv* sind und können mit dem nächsten Schritt fortfahren.

## Nächster Schritt: Amazon Lex Bot erstellen
Nachdem Sie nun die FAQs zu Amazon Kendra hinzugefügt haben, ist Ihr nächster Schritt die Erstellung des
den Amazon Lex Bot zu erstellen und ihn mit den FAQs zu verbinden. Sie finden die Anweisungen
hierzu finden Sie im [Amazon Lex Abschnitt](./amazon-lex.md).
