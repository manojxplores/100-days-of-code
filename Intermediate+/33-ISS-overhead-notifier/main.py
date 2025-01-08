import datetime
import requests
import smtplib

res = requests.get("http://api.open-notify.org/iss-now.json")
res.raise_for_status()
data = res.json()

lat = float(data["iss_position"]["latitude"])
lng = float(data["iss_position"]["longitude"])
iss_corr = (lat, lng)

MY_LAT = 22.339430
MY_LNG = 87.325340


def locate_iss(pos):
    if (MY_LAT - 5 <= pos[0] <= MY_LAT + 5) and (MY_LNG - 5 <= pos[0] <= MY_LNG + 5):
        return True
    return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}
res2 = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
res2.raise_for_status()
data2 = res2.json()

sunrise = int(data2["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data2["results"]["sunset"].split("T")[1].split(":")[0])

current_hour = datetime.datetime.utcnow().hour

if current_hour > sunset or current_hour < sunrise:
    if locate_iss(iss_corr):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            GMAIL = "your_email@gmail.com"
            PWD = "your_password"
            connection.starttls()
            connection.login(user=GMAIL, password=PWD)
            connection.sendmail(
                from_addr=GMAIL,
                to_addrs=GMAIL,
                msg="Subject:Look Up!\n\nThe ISS is currently above your location. Go outside and take a look!"
            )

