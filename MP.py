import smtplib

# Údaje pre odosielanie e-mailu
od = input'Odosielatel je : ')
heslo = input('tvoje_heslo : ')
komu = input('nazov prijemcu : ')
predmet = input('Napiste predmet správy : ')
obsah = input('Napiste obsah spravy : ')

# Pripojenie k SMTP serveru Gmailu
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# Prihlásenie do účtu
server.login(od, heslo)

# Vytvorenie e-mailu
sprava = f'Subject: {predmet}\n\n{obsah}'

# Odoslanie e-mailu
server.sendmail(od, komu, sprava)

# Odpojenie sa
server.quit()
