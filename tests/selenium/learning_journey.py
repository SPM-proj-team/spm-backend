from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
import json
import time
import helper_function

def checkLearningJourney(driver,backend_url,frontend_url):
    # learning journeys test
    driver.get(frontend_url)
    time.sleep(2)
    # print("//div[contains(@class, 'card-body shadow-sm')]")
    learningJourneys = WebDriverWait(driver, 3).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'card-body shadow-sm')]"))
    )

    learningJoruneyRequest = requests.post(backend_url+"learning_journey", json = {"Staff_ID":1})
    # SST = single source of truth
    learningJourneySST = json.loads(learningJoruneyRequest.text)["data"]
    helper_function.testFormatCount("No. Of Learning Journey", len(learningJourneys), len(learningJourneySST))
    