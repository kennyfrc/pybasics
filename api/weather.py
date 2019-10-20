import requests
import time
from datetime import datetime

# TODO: Loop over the entire list.

API_KEY = "3f02d0ee5b7adb95a078cc699c8a6663"

url = "https://api.openweathermap.org/data/2.5/forecast"
endpoint = "?q="
query = "Manila"
key = f"&appid={API_KEY}"

def status_check(status):
	if status == 'Rain':
		return "Oo."
	else:
		return "Hindi."

response = requests.get(url + endpoint + query + key)
json = response.json()

timestamp2hrs = json["list"][0]["dt"]
dt2hrs = datetime.fromtimestamp(timestamp2hrs)
status2hrs = json["list"][0]["weather"][0]["main"]

timestamp5hrs = json["list"][1]["dt"]
dt5hrs = datetime.fromtimestamp(timestamp5hrs)
status5hrs = json["list"][1]["weather"][0]["main"]

time.sleep(1)
print("Uulan ba? App: Manila Version")
print("--------")
time.sleep(2)
print(f"Uulan ba in 2 Hours? ({dt2hrs})")
time.sleep(2)
print(status_check(status2hrs))
print("--------")
time.sleep(1)
print(f"Uulan ba in 5 Hours? ({dt5hrs})")
time.sleep(2)
print(status_check(status5hrs))
time.sleep(2)
