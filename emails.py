import sys
import os
import smtplib
from configparser import SafeConfigParser
from weather import get_weather_forecast

def get_emails():   
    emails = dict()

    try:
        email_file = open('emails_with_names.txt', 'r')
        
        for line in email_file:
            (email, name) = line.split(',')
            emails[email] = name.strip()        
    
    except FileNotFoundError as err:
        print('You need to create emailes_with_names.txt file')
        print(err)
        sys.exit(1)

    return emails 


def get_api_config():

    if os.path.isfile('./apikey.config'):
        parser = SafeConfigParser()
        parser.read('apikey.config')
        key = parser.get('apikey', 'key')

        if key == '':
            print('First you need to obtain api key for Open Weather Map')
            sys.exit(1)

        return key
    
    else: 
        print('Make sure you have apikey.config file in working directory!')
        sys.exit(1)


def get_smtp_config():

    if os.path.isfile('./smtp.config'):
        parser = SafeConfigParser()
        parser.read('smtp.config')
        username = parser.get('credentials', 'username')
        password = parser.get('credentials', 'password')

        if username == '':
            print('You need to obtain username for email account')
            sys.exit(1)
        elif password == '':
            print('You need obtain password for email account')
            sys.exit(1)

        return username, password
    
    else: 
        print('Make sure you have smtp.config file in working directory!')
        sys.exit(1)


def send_emails(emails, forecast, username, password):
    # Connect to smtp server 
    server = smtplib.SMTP('smtp.gmail.com', '587')
    # Start encryption
    server.starttls()
    # Login
    server.login(username, password)

    # Send to whole mail list
    for to_email, name in emails.items():
        message = 'Subject: Weather forecast for today\n'
        message += 'Hi ' + name + '!\n\n'
        message += forecast + '\n\n'
        message += 'Cheers, your email forecast app'
        server.sendmail('emailer.app11@gmail.com', to_email, message)
    server.quit()

 
def main():
    username, password = get_smtp_config()
    key = get_api_config()    
    emails = get_emails()
    forecast = get_weather_forecast(key)
    send_emails(emails, forecast, username, password)

main()