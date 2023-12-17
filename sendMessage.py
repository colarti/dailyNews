import smtplib, ssl
import os

def send_message(msg):
    host = 'smtp.gmail.com'
    port = 465

    username = 'learnpython407@gmail.com'
    password = os.getenv('APP_PW')

    receiver = 'learnpython407@gmail.com'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, msg)
        

if __name__ == '__main__':
    content = '''\
Subject: Bar Joke of the Day

A guy was in a bar drinking beer. He would finish his beer, 
pull out his wallet and look at a picture of his wife, order 
another beer take out his wallet and looks at a picture of 
his wife. He did this several times, finally, the bartender 
asks, why after you finish a beer you take out your wallet and 
look at a picture of your wife. The guy says as soon as she 
starts looking better to me, I go home.
'''

    send_message(content)