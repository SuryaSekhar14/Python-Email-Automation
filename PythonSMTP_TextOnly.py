import smtplib

sender=input(str("Your Email:"))
receiver=input(str("Reciever's Email:"))
password=input(str("Your Password:"))

subject=input(str("Email's Subject:"))
data=input(str("Enter Email's Body:"))

smtpserver=smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(sender,password)
msg= f'Subject:{subject} \n\n {data}'

smtpserver.sendmail(sender,receiver,msg)
print('Sent')
smtpserver.close()