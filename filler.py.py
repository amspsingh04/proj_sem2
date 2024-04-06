from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

geckodriver_path = "C:/Users/spsin/Desktop/geckodriver-v0.33.0-win64/geckodriver.exe"

url = "https://docs.google.com/forms/d/e/1FAIpQLSdulvlzyZ_QB9KcCNTwL1sK-4DvoXibIJPtTUSJerDp1SfCDg/viewform"



def fill_form():
    age_selector = ['[data-value="18-25"]','[data-value="25-40"]','[data-value="40-60"]',]  # Adjust the value here as needed
    age_option = BROWSE.find_element(By.CSS_SELECTOR, random.choice(age_selector))
    age_option.click()

    education_selector = [
            '[data-value="High School"]',
            '[data-value="Undergraduate"]',
            '[data-value="Postgraduate"]'
        ]
    selected_education_selector = random.choice(education_selector)
    education_option = BROWSE.find_element(By.CSS_SELECTOR, selected_education_selector)
    education_option.click()
    
    location_selector = ['Rural', 'Suburban Town', 'Urban', 'Suburban Town', 'Urban', 'Suburban Town', 'Urban', 'Suburban Town', 'Urban', 'Suburban Town', 'Urban']
    selected_location_value = random.choice(location_selector)
    location_radio_button = WebDriverWait(BROWSE, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'[data-value="{selected_location_value}"]')))
    location_radio_button.click()

    tech_use_options = ['Yes', 'No', 'No', 'No', 'No', 'No']
    selected_option = random.choice(tech_use_options)
    WebDriverWait(BROWSE, 1).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, f'div[data-value="{selected_option}"]')
        )
    ).click()

    stigma_options = ['Yes', 'No']
    selected_option = random.choice(stigma_options)
    WebDriverWait(BROWSE, 1).until(
        EC.element_to_be_clickable(
        (By.CSS_SELECTOR, f'div[data-value="{selected_option}"]')
        )
    ).click()

    isolation_levels = ['1', '2', '3', '4', '5']
        
    selected_level = random.choice(isolation_levels)
        
    isolation_selector = f"div[data-value='{selected_level}']"
    WebDriverWait(BROWSE, 1).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, isolation_selector)
        )
    ).click()

    choice = random.choice(["Yes", "No"])
    choice_element = BROWSE.find_element(By.XPATH, f"//div[@aria-label='{choice}']")
    choice_element.click()

    difficulty_level = str(random.randint(1, 5))
    xpath_string = f"//div[contains(@class, 'eRqjfd')]//div[@data-value='{difficulty_level}']"
    difficulty_element = BROWSE.find_element(By.XPATH, xpath_string)
    difficulty_element.click()

    choices = ["Yes", "No"]
    selected_choice = random.choice(choices)
    xpath_string = f"//div[@class='Od2TWd hYsg7c' and @data-value='{selected_choice}']"
    informed_rights_element = BROWSE.find_element(By.XPATH, xpath_string)
    informed_rights_element.click()

    choices = ["Yes", "No"]
    selected_choice = random.choice(choices)
    xpath_string = f"//div[@class='Od2TWd hYsg7c' and @data-value='{selected_choice}']"
    case_details_difficulty_element = BROWSE.find_element(By.XPATH, xpath_string)
    case_details_difficulty_element.click()

    choices = ["Yes", "No"]
    selected_choice = random.choice(choices)
    xpath_string = f"//div[@class='Od2TWd hYsg7c' and @data-value='{selected_choice}']"
    lawyer_difficulty_element = BROWSE.find_element(By.XPATH, xpath_string)
    lawyer_difficulty_element.click()

    selected_value = random.choice(["Yes", "No"])
    xpath_string = f"//div[@class='Od2TWd hYsg7c'][@data-value='{selected_value}']"
    radio_button_element = WebDriverWait(BROWSE, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath_string))
    )
    radio_button_element.click()

    values = [str(i) for i in range(1, 6)]
    selected_value = random.choice(values)
    xpath_string = f"//div[@class='Od2TWd hYsg7c'][@data-value='{selected_value}']"
    radio_button_element = WebDriverWait(BROWSE, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath_string))
    )
    radio_button_element.click()

    values = ["Yes", "No"]
    selected_value = random.choice(values)
    xpath_string = f"//div[@class='Od2TWd hYsg7c'][@data-value='{selected_value}']"
    radio_button_element = WebDriverWait(BROWSE, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath_string))
    )
    radio_button_element.click()

    values = ["Yes", "No"]
    selected_value = random.choice(values)
    xpath_string = f"//div[@class='Od2TWd hYsg7c'][@data-value='{selected_value}']"
    radio_button_element = WebDriverWait(BROWSE, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath_string))
    )
    radio_button_element.click()

def submit(url, data):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        requests.post(url, data=data, headers=headers)
        print("Submitted successfully!")
    except:
        print("Error!")

submit(url, fill_form())
    
    

