from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
import json
import time
# from selenium_tests import helper_function
import helper_function


def updateSkillTest(driver, backend_url, frontend_url):

    driver.get(frontend_url)
    helper_function.Login(driver, frontend_url)
    time.sleep(2)

    adminBtn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='/Admin']"))
    )
    adminBtn.click()

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)/2;")
    time.sleep(2)
    # test update and delete role
    createUpdateSkillBtn = WebDriverWait(
        driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//h5[text()='Update & Delete Skills']")))
    createUpdateSkillBtn.click()

    prevRequest = requests.get(backend_url + "skills")
    prevSST = json.loads(prevRequest.text)["data"][0]
    prevCount = len(prevSST["Courses"])

    SkillSearchBar = WebDriverWait(
        driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='skillInputText']")))
    SkillSearchBar.send_keys("Critical")
    skill = WebDriverWait(
        driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//td[text()='Critical Thinking']")))
    skill.click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    addSkillBtn = WebDriverWait(
        driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[text()=' + Add Courses ']")))
    time.sleep(2)
    addSkillBtn.click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    courseSearch = WebDriverWait(
        driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//input[@id='skillInputText']")))

    courseSearch[1].send_keys("leading")

    addCourseBtn = WebDriverWait(
        driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[text()=' + Add ']")))
    addCourseBtn.click()

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    save = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()=' Update ']"))
    )
    save.click()
    time.sleep(5)
    currentRequest = requests.get(backend_url + "skills")
    currentSST = json.loads(currentRequest.text)["data"][0]
    currentCount = len(currentSST["Courses"])
    
    return helper_function.testFormatCount(
        "Updated No. Of Skills",
        currentCount,
        prevCount + 1)



def createSkillTest(driver, backend_url, frontend_url):
    prevRequest = requests.get(backend_url + "skills")
    prevCount = len(json.loads(prevRequest.text)["data"])

    driver.get(frontend_url)
    helper_function.Login(driver, frontend_url)
    #  go to admin page
    adminBtn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='/Admin']"))
    )
    adminBtn.click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    createCreateRoleBtn = WebDriverWait(
        driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//h5[text()='Create New Skills']")))
    createCreateRoleBtn.click()
    skillNameInput = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='skill_Name']"))
    )
    skillNameInput.send_keys("skill name test")

    # //select[@id='department']

    addCourseBtn = WebDriverWait(
        driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[text()=' + Add Courses ']")))
    addCourseBtn.click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    skillSearch = WebDriverWait(
        driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//input[@id='skillInputText']")))
    # print(len(skillSearch))
    skillSearch[0].send_keys("lean")

    addSkill = WebDriverWait(
        driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[text()=' + Add ']")))
    addSkill.click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    create = WebDriverWait(
        driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@id='create-btn']")))
    create.click()
    time.sleep(2)
    currentRequest = requests.get(backend_url + "skills")
    currentCount = len(json.loads(currentRequest.text)["data"])
    return helper_function.testFormatCount(
        "Updated No. Of Roles", currentCount, prevCount + 1)


def deleteRoleTest(driver, backend_url, frontend_url):
    driver.get(frontend_url)
    helper_function.Login(driver, frontend_url)
    adminBtn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='/Admin']"))
    )
    adminBtn.click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    # test update and delete role
    createUpdateRoleBtn = WebDriverWait(
        driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//h5[text()='Update & Delete Skills']")))
    createUpdateRoleBtn.click()

    prevRequest = requests.get(backend_url + "skills")
    prevCount = len(json.loads(prevRequest.text)["data"])

    RoleSearchBar = WebDriverWait(
        driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='skillInputText']")))
    RoleSearchBar.send_keys("critical")
    skill = WebDriverWait(
        driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//td[text()='Critical Thinking']")))
    skill.click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    delete = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='delete-btn']"))
    )
    delete.click()
    time.sleep(2)
    # delConfrim = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//button[text()=' Delete ']"))
    # )
    # delConfrim.click()
    time.sleep(2)
    currentRequest = requests.get(backend_url + "skills")
    currentCount = len(json.loads(currentRequest.text)["data"]) -1

    return helper_function.testFormatCount(
        "Delete No. Of Roles", currentCount, prevCount - 1)

