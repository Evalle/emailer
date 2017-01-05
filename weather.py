import requests


def get_weather_forecast(key):
    # connecting to weather API
    url = 'http://api.openweathermap.org/data/2.5/weather?id=3067696&units=metric&appid=' + key
    weather_request = requests.get(url)
    weather_json = weather_request.json()

    # get weather description and temperatures from JSON
    description = weather_json['weather'][0]['description']
    temp_min = str(weather_json['main']['temp_min'])
    temp_max = str(weather_json['main']['temp_max'])

    # creating our forecast string
    forecast = 'The forecast for today is ' + description + ' with a high of ' + \
        temp_max + ' and a low of ' + temp_min + ' degrees'

    return forecast
