import requests
from datetime import datetime
import smtplib
import time

my_email="wishlist1357@gmail.com"
my_password="abcd123"

my_lat=28.669081
my_long=77.430412


def is_iss_overhead():
    response=requests.get(url="http://api.open-notify.org/iss-now.json")
    data=response.json()
    lat=float(data["iss_position"]["latitude"])
    long=float(data["iss_position"]["longitude"])
    if my_lat-5<=lat<=my_lat+5 and my_long-5<=long<=my_long+5:
        return True

def is_night():
    parameters= {
        "lat":my_lat,
        "lng":my_long,
        "formatted":0

    }

    setrise=requests.get(url="https://api.sunrisesunset.io/json",params=parameters)
    setrise.raise_for_status()
    sunrise=setrise.json()["results"]["sunrise"]
    sunset=setrise.json()["results"]["sunset"]
    sunrise=int(sunrise.split(":")[0])
    sunset=int(sunset.split(":")[0])

    time_now=datetime.now().hour

    if time_now>=sunset or time_now<=sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection=smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_email,my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="subject: look up\n\n The ISS is above you in the sky."
        )