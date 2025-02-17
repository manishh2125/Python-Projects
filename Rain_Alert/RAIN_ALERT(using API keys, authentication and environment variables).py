import requests
from twilio.rest import Client
import os

account_sid = "ACcd96972fbf706576b119242191bf4b"
auth_token = os.environ.get("MY_AUTH_KEY")

parameters={
    "lat":28.669081,
    "lon":77.430412,
    "appid":os.environ.get("MY_API_ID"),
    "cnt":4
}

response=requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
data=response.json()
#print(data["list"][0]['weather'][0]['id'])

will_rain=False
for hour_data in data['list']:
    condition_code_ID=hour_data['weather'][0]['id']
    if int(condition_code_ID)<700:
        will_rain = True
if will_rain:
    client=Client(account_sid,auth_token)
    message = client.messages.create(
        body="IT's going to rain today so bring an Umbrella...",
        from_='+18573419077',
        to='+917739259649'
    )

    print(message.status)