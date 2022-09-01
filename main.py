import requests
from twilio.rest import Client
import os

api_end_point = 'https://api.openweathermap.org/data/2.5/onecall'
api_id = '69f04e4613056b159c2761a9d9e664d2'
account_sid = "AC1d0964a6881e98c728dd63e0438c0ace"
auth_token = "e2bad5891d363ed1ed27d846a56ca1ad"
# twilio_ph_num = "+17755263191"

parameters = {
    'lat': 26.906010,
    'lon': 75.740730,
    'exclude':'current,daily,minutely,alerts',
    'appid': api_id
}

response = requests.get(url=api_end_point,params=parameters)
# print(response.status_code)
response.raise_for_status()
weather_data = response.json()

will_rain = True
weather_hour=weather_data['hourly'][:11]
for hour_data in weather_hour:
    condition_code = hour_data['weather'][0]['id']
    # print(condition_code)
    if condition_code >= 700:
        will_rain =True

if will_rain:

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Bring your umbrella,its going to rain today",
        from_="+17755263191",
        to= os.environ.get("PHONE NUMBER")
    )

    print(message.status)







