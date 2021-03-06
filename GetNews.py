from bs4 import BeautifulSoup
import re
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from datetime import date

#Get Todays date and store as a variable
today = date.today()

#Empty News String
news = ""
i = 1
#Request Reuters Website
r = requests.get("https://uk.reuters.com/")
page = BeautifulSoup(r.text, 'html.parser')

items = page.find_all('a', attrs={'href': re.compile("/article/")})

#Find all <a> tags with href containing "/article"
for link in items[1:16]:
    title = (("Title: {}".format(link.text.strip()))+"\n")
    link = (("https://uk.reuters.com/{}".format(link.get("href")))+"\n")

    news += ("%s-%s%s\n"%(i,title,link))
    i += 1
    
#Print for testing purposes
#print(news)

#User Details
gmail_user = 'emails@luigi-marino.com'
gmail_password = ''
sent_from = gmail_user
to = ['me@onenote.com']

#Email Title
msg = str(today) + "\n"

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