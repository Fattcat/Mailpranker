import smtplib

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

def send_email(subject, message, recipients, sender_email):

    # Údaje pre prihlásenie na Gmail účet

    email = 'tvojemail@gmail.com'

    password = 'tvojeheslo'

    # Vytvorenie MIME správy

    msg = MIMEMultipart()

    msg['From'] = sender_email

    msg['To'] = ', '.join(recipients)

    msg['Subject'] = subject

    # Vytvorenie textovej časti správy

    text = MIMEText(message, 'plain')

    msg.attach(text)

    # Pripojenie na Gmail SMTP server a odoslanie správy

    with smtplib.SMTP('smtp.gmail.com', 587) as server:

        server.starttls()

        server.login(email, password)

        server.send_message(msg)

# Hlavný program

if __name__ == "__main__":

    subject = "Testovacia správa"

    message = "Ahoj, ako sa máš?"

    # Zoznam prijímateľov, môžeš sem pridať ďalších používateľov

    recipients = ['prijemca1@gmail.com', 'prijemca2@gmail.com', 'prijemca3@gmail.com']

    # Počet iterácií odosielania správy

    iterations = 10

    # E-mail odosielateľa (tvoj druhý Gmail)

    sender_email = 'tvojemail2@gmail.com'

    for i in range(iterations):

        send_email(subject, message, recipients, sender_email)

        recipients.append(sender_email)
