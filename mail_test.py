import smtplib
content = 'Attaaaaack'
mail=smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('adityashukla2799@gmail.com', '')
mail.sendmail('adityashukla2799@gmail.com', 'f20170185@hyderabad.bits-pilani.ac.in', content)
mail.close()