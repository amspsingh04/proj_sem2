from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
import random
import time
import requests

# Replace with the path to your geckodriver executable
geckodriver_path = "C:/Users/spsin/Desktop/geckodriver-v0.33.0-win64/geckodriver.exe"

# Replace with the URL of your Google Form
url = "https://docs.google.com/forms/d/e/1FAIpQLSfn0t0UHiuWxLfK_DtieJNboaiL77komaBohHJBa4a_ygJaNg/formResponse"

def fill_form():
        # Define the form data to be filled
        value = { 
            "entry.1744649345": random.randint(2,5),
            "entry.163424247": random.randint(2,5),
            "entry.2100612324": random.randint(2,5),
            "entry.879716223": random.choice(["Yes","No"]),
            "entry.499372462": random.choice(["Yes","No"]),
            "entry.2066777384": random.randint(2,5)
        }
        print(value, flush = True)
        return value

def submit(url, data):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        requests.post(url, data=data, headers=headers)
        print("Submitted successfully!")
    except:
        print("Error!")

for i in range(100):
    submit(url, fill_form())
    x=random.randint(60,600)
    time.sleep(x)
    print(x)
    

