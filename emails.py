import sys
import os
import requests
from configparser import SafeConfigParser


def get_emails():   
    emails = dict()

    try:
        email_file = open('emails_with_names.txt', 'r')
        
        for line in email_file:
            (email, name) = line.split(',')
            emails[email] = name.strip()        
    
    except FileNotFoundError as err:
        print(err)
        sys.exit(1)

    return emails


def get_schedule():
    
    try:
        schedule_file = open('schedule.txt', 'r')
    except FileNotFoundError as err:
        print(err)
        sys.exit(1)

    schedule = schedule_file.read()
    
    return schedule


def get_weather_forecast(key):
    url = 'http://api.openweathermap.org/data/2.5/find?q=Prague&units=metric&appid=' + key
    weather_request = requests.get(url)
    weather_json = weather_request.json()
    print(weather_json)


def get_config():

    if os.path.isfile('./apikey.config'):
        parser = SafeConfigParser()
        parser.read('apikey.config')
        key = parser.get('apikey', 'key')

        if key == '':
            print('First you need to obtain api key for Open Weather Map')
            sys.exit(1)

        return key
    
    else: 
        print('Make sure that you have apikey.config file in your directory!')
        sys.exit(1)


def main():
    key = get_config()    
    emails = get_emails()
    print(emails)
    schedule = get_schedule()
    print(schedule)
    get_weather_forecast(key)

main()