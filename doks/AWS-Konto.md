# AWS-Konto
Um an der Herausforderung zu arbeiten, muss jedes Team über **ein** AWS-Konto verfügen.

## AWS-Konto erstellen
Sie können sich für ein neues AWS-Konto anmelden
[hier](https://portal.aws.amazon.com/billing/signup).

Während der Kontoerstellung werden Sie aufgefordert, eine Support-Stufe auszuwählen. Bitte
wählen Sie den **Basic Support**.

## IAM-Benutzer anlegen
Mit der E-Mail-Adresse erhalten Sie Zugriff auf den Stammbenutzer des Kontos. Dieser
Benutzer hat die höchsten Privilegien im Konto und sollte nur für
Verwaltungsaufgaben verwendet werden. Für alle alltäglichen Aufgaben und insbesondere für diese Herausforderung
sollten IAM-Benutzer verwendet werden (sofern nicht anders angegeben).

Um IAM-Benutzer zu erstellen, besuchen Sie die Seite [Identity and Access Management
(IAM)](https://us-east-1.console.aws.amazon.com/iamv2) Dienst. Auf der Seite Benutzer
Seite können Sie neue IAM-Benutzer erstellen. Sie müssen einen Benutzer für jeden Ihrer
Teammitglieder und einen Benutzer für Sie selbst erstellen.

1. Wählen Sie den Menüpunkt **Benutzer** auf der linken Seite
1. Klicken Sie auf **Benutzer hinzufügen**.
1. Benutzerdetails festlegen
   * Geben Sie den **Benutzernamen** an.

     **HINWEIS:** Sie können alle Benutzer auf einmal erstellen, indem Sie auf **Weitere Benutzer hinzufügen** klicken.
   * Für **AWS-Berechtigungstyp auswählen** wählen Sie beide
     * ✅ Zugangsschlüssel - Programmatischer Zugang

       Wird für den Zugriff auf die AWS-APIs verwendet.
     * ✅ Passwort - Zugang zur AWS Management Console

       Wird für die Anmeldung bei der AWS Web UI, auch Management Console oder AWS Console genannt, verwendet.
     **Konsolenkennwort:** Automatisch generiertes Kennwort
     * **Passwortrücksetzung erforderlich:** ✅ Benutzer muss bei der nächsten Anmeldung ein neues Passwort erstellen
       Anmeldung
1. Berechtigungen festlegen
   * Wählen Sie **Vorhandene Richtlinien direkt anhängen**
   * ✅ **AdministratorZugang**. Damit haben Sie und Ihre Kollegen Zugang zu allen
     auf alle Dienste.

Für diese Herausforderung brauchen Sie keine Tags zu erstellen. Nachdem Sie überprüft haben
dass alle Informationen korrekt sind, können Sie mit der Erstellung der Benutzer fortfahren.

Nach der erfolgreichen Erstellung werden Sie zur letzten Seite des
Assistenten. Auf dieser Seite können Sie die csv-Datei mit den Anmeldedaten herunterladen.
Verteilen Sie diese Datei an Ihre Teammitglieder.

## Einlösen von Credits
Für den Wettbewerb hat AWS für jedes Team Credits gesponsert. Sie erhalten den
Code vom SAA-Team vor Ort.

**Hinweis:** Diese Aufgabe muss als Stammbenutzer des AWS-Kontos ausgeführt werden.

Nachdem Sie das Konto erstellt haben, können Sie die im [Billing Service ->
Credits](https://us-east-1.console.aws.amazon.com/billing/home?region=eu-west-1#/credits).

## Aktivieren Sie AWS Single Sign-on (SSO)
Um Kendra Experiences nutzen zu können, müssen Sie AWS SSO aktivieren und SSO
Benutzer erstellen. Wenn Sie die Funktion Kendra Experiences verwenden möchten, müssen Sie folgende Schritte ausführen
die folgenden Schritte.

### Aktivieren Sie AWS SSO
* Melden Sie sich als Root-Benutzer an.
* Aktivieren Sie SSO in der Region EU (Irland) | eu-west-1
  https://eu-west-1.console.aws.amazon.com/singlesignon/identity/home

### Gruppe und Benutzer erstellen
Sie können die SSO-Gruppe und die Benutzer mit jedem der zuvor erstellten Benutzer erstellen.
1. Wählen Sie **Gruppen** aus dem linken Menü
   * Erstellen Sie die *Gruppe* mit einem Namen Ihrer Wahl
1. Nachdem die Gruppe erstellt wurde, können Sie die Benutzer erstellen
1. Wählen Sie **Benutzer** aus dem linken Menü
   * Geben Sie dem Benutzer einen Namen
   * Wählen Sie *Senden Sie dem Benutzer eine E-Mail mit Anweisungen zur Einrichtung des Passworts.
   * Geben Sie eine gültige E-Mail-Adresse ein.
   * Geben Sie Vor- und Nachname an.
   * Fügen Sie den Benutzer zu der zuvor erstellten Gruppe hinzu
1. Gehen Sie zu Ihrem E-Mail-Client
1. *Akzeptieren Sie die Einladung** und geben Sie ein Passwort für den Benutzer an.

Danach kann der Benutzer bei der Konfiguration der Kendra Experiences
Funktion ausgewählt werden. 
