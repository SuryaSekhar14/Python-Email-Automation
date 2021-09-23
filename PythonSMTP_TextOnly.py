import smtplib


sender=input(str("Your Email:"))         #Enter your E-mail ID
receiver=input(str("Reciever's Email:"))    #Enter Reciever's Email ID   
password=input(str("Your Password:"))    #Enter your Password

subject=input(str("Email's Subject:"))     #Enter E-Mail's Subject
data=input(str("Enter Email's Body:"))     #Enter E-Mail's Body Text

smtpserver=smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(sender,password)
msg= f'Subject:{subject} \n\n {data}'

smtpserver.sendmail(sender,receiver,msg)
print('Sent')
smtpserver.close() 
