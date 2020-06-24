#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.multipart import MIMEMultipart

i = 1
news = ""

r = requests.get("https://www.reuters.com/news/technology")
soup = BeautifulSoup(r.text, 'html.parser')
result = soup.find_all('h3', attrs = {'class' : 'story-title'})

for new in result:
    news += ("%s- "%i)
    news += new.text.strip()
    news += "\n"
    news += articleLink
    news += "\n"
    i += 1

#User Details
gmail_user = 'emails@luigi-marino.com'
gmail_password = '*7gMaH1aGf31'
sent_from = gmail_user
to = ['emails@luigi-marino.com']

#Email Title
msg = """Subject: Raspberry Pi News"""

#Add news to email message
msg += news

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, msg)
    server.close

    print ('Email Sent!')
except:
    print ('Something went wrong')

#print(news)