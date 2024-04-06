import random
from time import sleep
import requests
from selenium import webdriver
geckodriver_path = "C:/Users/spsin/Desktop/geckodriver-v0.34.0-win64/geckodriver.exe"
import random
##web=webdriver.Chrome()

url = "https://docs.google.com/forms/d/e/1FAIpQLSfGLMU06ONEbRZishBqLBQ1JnwYX-EUrEs7llHPRPOipZlv-A/formResponse"

def fill_form():
    value = {
        "entry.807024958": random.choice(["18-25","25-40","40-60","60+"]),
        "entry.1248644046": random.choice(["High School","Undergraduate","High School"]),
        "entry.1834313967": random.choice(["Urban","Urban","Urban","Suburban Town","Urban","Suburban Town"]),
        "entry.452441886": random.choice(["No","No"]),
        "entry.1438833650": random.choice(["Yes","Yes","Yes"]),
        "entry.1236244612": random.randint(3,5),
        "entry.1351653536": random.choice(["Yes","Yes","Yes","Yes"]),
        "entry.898755193": random.randint(3,5),
        "entry.1230739075": random.choice(["No","No","No","No","No","No","No","No","No","No","No","No","Yes"]),
        "entry.318386453": random.choice(["Yes","Yes","Yes","Yes","No","No"]),
        "entry.1540566283":random.choice(["Yes"]),
        "entry.1781788144": random.choice(["No"]),
        "entry.348153171": random.randint(4,5),
        "entry.359965727": random.choice(["Yes","Yes","Yes","Yes","Yes","No"]),
        "entry.2042783684": random.choice(["Yes"]),
    }
    print(value, flush=True) 
    return value

def submit(url, data):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Referer": url  
        }
        response = requests.post(url, data=data, headers=headers)
        if response.status_code == 200:
            print("Submitted successfully!")
        else:
            print(f"Error submitting form, status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred during submission: {e}")
for _ in range(150):
    submit(url, fill_form())    
    
