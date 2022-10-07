import requests
import os


def import_weather():

    key = os.getenv('API_KEY')

    url1 = 'http://api.openweathermap.org/data/2.5/weather?id=4180439&appid=' + key

    payload = ""
    headers = {}

    response = requests.request(
        "GET", url1, headers=headers, data=payload)

    out = response.json()

    result = {}
    result['lon'] = out['coord']['lon']
    result['lat'] = out['coord']['lat']
    result['desc_short'] = out['weather'][0]['main']
    result['desc_long'] = out['weather'][0]['description']
    result['temp'] = out['main']['temp']
    result['feels_like'] = out['main']['feels_like']
    result['temp_min'] = out['main']['temp_min']
    result['temp_max'] = out['main']['temp_max']
    result['pressure'] = out['main']['pressure']
    result['humidity'] = out['main']['humidity']
    result['visibility'] = out['visibility']
    result['wind_speed'] = out['wind']['speed']
    result['wind_deg'] = out['wind']['deg']
    result['clouds'] = out['clouds']['all']
    result['dt'] = out['dt']
    result['sunrise'] = out['sys']['sunrise']
    result['sunset'] = out['sys']['sunset']
    result['timezone'] = out['timezone']
    result['city'] = out['name']

    return result
