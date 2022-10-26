from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
import json
import time
from selenium_tests import helper_function


def checkLearningJourney(driver, backend_url, frontend_url):
    # learning journeys test
    driver.get(frontend_url)
    time.sleep(2)
    # print("//div[contains(@class, 'card-body shadow-sm')]")
    learningJourneys = WebDriverWait(
        driver, 3).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//div[contains(@class, 'card-body shadow-sm')]")))

    learningJoruneyRequest = requests.post(
        backend_url + "learning_journey", json={"Staff_ID": 1})
    # SST = single source of truth
    learningJourneySST = json.loads(learningJoruneyRequest.text)["data"]
    return helper_function.testFormatCount(
        "No. Of Learning Journey",
        len(learningJourneys),
        len(learningJourneySST))


def updateLearningJourneyTest(driver, backend_url, frontend_url):
    # learningJoruneyRequest = requests.post(
    #     backend_url + "learning_journey/1", json={"Staff_ID": 1})
    # print(learningJoruneyRequest.text)
    # fixData = json.loads(learningJoruneyRequest.text)["data"][0]
    # fixData = json.dumps(fixData)
    driver.get(frontend_url)
    time.sleep(2)
    learningJourneys = WebDriverWait(
        driver, 3).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//div[contains(@class, 'card-body shadow-sm')]")))
    learningJourneys[0].click()
    time.sleep(2)

    name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='name']"))
    )
    name.send_keys("test update learning journey name")
    desc = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@id='desc']"))
    )
    desc.send_keys("test update learning journey desc")
    # //button[@class="btn btn-primary btn-lg shadow w-100 fw-semibold"]
    updateBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//button[@class='btn btn-primary btn-lg shadow w-100 fw-semibold']")))
    updateBtn.click()
    time.sleep(3)
    try:
        desc = WebDriverWait(
            driver, 3).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@id='desc']")))

        # fixRequest = requests.put(
        #     backend_url +
        #     "learning_journey/1",
        #     json={
        #         "Staff_ID": 1,
        #         "Learning_Journey": fixData})
        # print(json.dumps(fixData))
        # print(fixRequest.text)
        return helper_function.testFormatSingle(
            "Updating Learning Journey test", True)
    except Exception as e:
        print(e)
        return helper_function.testFormatSingle(
            "Updating Learning Journey test", False)

# create


def createLearningJourneyTest(driver, backend_url, frontend_url):
    # learningJoruneyRequest = requests.post(backend_url+"learning_journey", json = {"Staff_ID":1})
    # print(learningJoruneyRequest.text)
    # dataCount = len(json.loads(learningJoruneyRequest.text)["data"])
    # fixData = json.dumps(fixData)
    driver.get(frontend_url)
    time.sleep(2)
    learningJourneys = WebDriverWait(
        driver, 3).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//a[@href='/CreateLearningJourney']")))
    learningJourneys[0].click()
    time.sleep(2)
    name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='name']"))
    )
    name.send_keys("test create learning journey name")
    desc = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@id='desc']"))
    )
    desc.send_keys("test create learning journey desc")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    nextBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//button[@class='btn btn-primary btn-lg shadow w-100 fw-semibold']")))
    nextBtn.click()
    time.sleep(2)
    roles = WebDriverWait(
        driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@class='ico-card']")))
    roles[0].click()
    courseAccordions = WebDriverWait(
        driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//button[@class='accordion-button fw-bold collapsed']")))
    courseAccordions[0].click()

    course1 = WebDriverWait(
        driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//li[@class='list-group-item']")))
    time.sleep(1)
    course1[0].click()
    createBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//button[@class='btn btn-lg btn-primary w-100 shadow fw-semibold']")))
    createBtn.click()
    driver.get(frontend_url)

    try:
        # checkname = WebDriverWait(driver, 2).until(EC.presence_of_element_located(
        #     (By.XPATH, "//*[text()[contains(., 'test create learning journey name')]]")))
        # checkdesc = WebDriverWait(driver, 2).until(EC.presence_of_element_located(
        #     (By.XPATH, "//*[text()[contains(., 'test create learning journey desc')]]")))
        return helper_function.testFormatSingle(
            "Create Learning Journey test", True)
    except BaseException:
        return helper_function.testFormatSingle(
            "Create Learning Journey test", False)

# delete


def deleteLearningJourneyTest(driver, backend_url, frontend_url):
    driver.get(frontend_url)
    time.sleep(2)
    learningJourneys = WebDriverWait(
        driver, 3).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//div[contains(@class, 'card-body shadow-sm')]")))
    learningJourneys[0].click()
    time.sleep(2)

    deleteBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//button[@class='btn btn-danger btn-lg shadow w-100 fw-semibold']")))
    deleteBtn.click()

    confirmBtn = WebDriverWait(
        driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@id='delete-modal-btn']")))
    time.sleep(3)
    confirmBtn.click()
    driver.get(frontend_url)
    learningJourneys = WebDriverWait(
        driver, 3).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//div[contains(@class, 'card-body shadow-sm')]")))
    if len(learningJourneys) == 1:
        return helper_function.testFormatSingle(
            "Delete Learning Journey test", True)
    else:
        return helper_function.testFormatSingle(
            "Delete Learning Journey test", False)
