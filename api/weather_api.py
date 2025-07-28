import requests
from config.settings import API_KEY, BASE_URL  # Make sure folder name is 'config', not 'configs'
#c3e1930e48364f76a4751249252407
def get_weather_data(city):
    url = f"{BASE_URL}?key={API_KEY}&q={city}&days=1&aqi=yes&alerts=yes"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("FAILED TO FETCH WEATHER DATA")
