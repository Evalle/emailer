import sys
import os
from configparser import SafeConfigParser
from weather import get_weather_forecast
from sender import send_emails


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


def main():
    username, password = get_smtp_config()
    key = get_api_config()
    emails = get_emails()
    forecast = get_weather_forecast(key)
    send_emails(emails, forecast, username, password)

main()
