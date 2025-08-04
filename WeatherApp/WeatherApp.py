import requests
import json
from win32com.client import Dispatch

city = input("Enter City: ")

url = f"http://api.weatherapi.com/v1/current.json?key=ca8a23e5e22248a8bbd105228250408&q={city}"

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
print(wdic['current']["temp_c"])
speaker = Dispatch("SAPI.SpVoice")
speaker.Speak(f"The temperature of {city} is {wdic['current']["temp_c"]} Degree Celcius")
