from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
import random
import requests

geckodriver_path = "Path to geckodriver.exe"

url = "Google Form URL"

def fill_form():
        value = { 
            "entry.ID": random.randint(2,5),
            "entry.ID": random.randint(2,5),
            "entry.ID": random.randint(2,5),
            "entry.ID": random.choice(["Yes","No"]),
            "entry.ID": random.choice(["Yes","No"]),
            "entry.ID": random.randint(2,5),
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

while(1):
    submit(url, fill_form())
    
    

