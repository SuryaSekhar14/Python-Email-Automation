import smtplib
import csv

sender=input(str("Your Email: "))         #Enter your E-mail ID
password=input(str("Your Password: "))    #Enter your Password

subject=input(str("Email's Subject: "))     #Enter E-Mail's Subject
data=input(str("Enter Email's Body: "))     #Enter E-Mail's Body Text

smtpserver=smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(sender,password)
msg= f'Subject:{subject} \n\n {data}'

with open ('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        smtpserver.sendmail(sender,row[0],msg)
        print(f'Sent to {row[0]}')

smtpserver.close()
