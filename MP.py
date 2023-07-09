import smtplib

# Údaje pre odosielanie e-mailu
od = 'tvoj_email@gmail.com'
heslo = 'tvoje_heslo'
komu = 'prijemca@gmail.com'
predmet = 'Toto je predmet správy'
obsah = 'Toto je obsah správy.'

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
