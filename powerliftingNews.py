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
r = requests.get("https://www.powerliftingwatch.com/")
page = BeautifulSoup(r.text, 'html.parser')

#Get all <a> tags in the page with href beginning with /node/
items = page.find_all('a', attrs={'href': re.compile("/node/")})

#Find all <a> tags with href containing "/article"
for item in items[0:11:2]:
    title = (("{}".format(item.text.strip()))+"\n")
    link = (("https://www.powerliftingwatch.com/{}".format(item.get("href")))+"\n")
    news += ("%s-%s%s\n"%(i,title,link))
    i += 1
    
#Print for testing purposes
#print(news)

#User Details
gmail_user = 'emails@luigi-marino.com'
gmail_password = '*7gMaH1aGf31'
sent_from = gmail_user
to = ['me@onenote.com']

#Email Subject
msg = 'Subject: @Powerlifting News' + "\n"

#Email Title
msg += str(today) + "\n"

#Add news to email message
msg += news

#Try block for sending email
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, msg)
    server.close

    print ('Email Sent!')
except:
    print ('Something went wrong')