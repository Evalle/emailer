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
    url = 'http://api.openweathermap.org/data/2.5/weather?id= 3067696&units=metric&appid=' + key
    weather_request = requests.get(url)
    weather_json = weather_request.json()
    print(weather_json)

    description = weather_json['weather'][0]['description']
    temp_min = str(weather_json['main']['temp_min'])
    temp_max = str(weather_json['main']['temp_max'])

    forecast = 'The forecast for today is ' + description + ' with a high of ' + \
    temp_max + ' and a low of ' + temp_min + ' degrees'

    print(forecast)


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
        print('Make sure you have apikey.config file in working directory!')
        sys.exit(1)


def main():
    key = get_config()    
    emails = get_emails()
    print(emails)
    schedule = get_schedule()
    print(schedule)
    get_weather_forecast(key)

main()