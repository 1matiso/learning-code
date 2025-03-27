import datetime
import requests
from twilio.rest import Client

LATITUDE = -20.336840
LONGITUDE = -40.291931

API_KEY = "bbc710f2a41c86fa48eecf3edbdd7dde"
WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

TWILIO_SID = "ACf1d007cefd5d4d7002312e74930bbb48"
TWILIO_TOKEN = "30e858e63c95d8cc625ed4dd977dae31"
TWILIO_PHONE = "+12294944243"

weather_params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "units": "metric",
    "cnt": 4,


}


response = requests.get(url=WEATHER_ENDPOINT, params=weather_params)
weather_data = response.json()

will_rain = False

for items in weather_data["list"]:
    if weather_data["list"][0]["weather"][0]["id"] < 700:
        will_rain = True
if will_rain:
    account_sid = 'ACf1d007cefd5d4d7002312e74930bbb48'
    auth_token = '30e858e63c95d8cc625ed4dd977dae31'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body = 'Vai chover!',
        to='whatsapp:+5527992985138'
    )
