from tracemalloc import start
from turtle import back
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
import requests, json
import role
import learning_journey
import helper_function
import traceback
import os
import skill
backend_url = "http://localhost:5000/"
frontend_url = "http://localhost:8080/"

# Start selenium
def startDriver():

    # chrome_service = Service(ChromeDriverManager(
    #     chrome_type=ChromeType.CHROMIUM).install("./chromedriver"))
    # chrome_options = Options()
    # options = [
    #     "--headless",
    #     "--disable-gpu",
    #     "--window-size=1920,1200",
    #     "--ignore-certificate-errors",
    #     "--disable-extensions",
    #     "--no-sandbox",
    #     "--disable-dev-shm-usage"
    # ]
    # for option in options:
    #     chrome_options.add_argument(option)

    # driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    firefox_options = Options()
    # firefox_options.add_argument("--headless")
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=firefox_options)
    driver.fullscreen_window()
    driver.get(frontend_url)
    # print('running first function')
    # print(
    #     learning_journey.checkLearningJourney(
    #         driver,
    #         backend_url,
    #         frontend_url))
    # os.system("mysql -uroot < ../sql/test_spm.sql")
    # print(role.updateRoleTest(driver, backend_url, frontend_url))
    # os.system("mysql -uroot < ../sql/test_spm.sql")
    # print(role.createRoleTest(driver, backend_url, frontend_url))
    # os.system("mysql -uroot < ../sql/test_spm.sql")
    # print(role.deleteRoleTest(driver, backend_url, frontend_url))
    # os.system("mysql -uroot < ../sql/test_spm.sql")
    # print(role.searchRoleTest(driver, backend_url, frontend_url))
    # os.system("mysql -uroot < ../sql/test_spm.sql")
    # print(
    #     learning_journey.updateLearningJourneyTest(
    #         driver,
    #         backend_url,
    #         frontend_url))
    # os.system("mysql -uroot < ../sql/test_spm.sql")
    # print(
    #     learning_journey.createLearningJourneyTest(
    #         driver,
    #         backend_url,
    #         frontend_url))
    # os.system("mysql -uroot < ../sql/test_spm.sql")
    # print(
    #     learning_journey.deleteLearningJourneyTest(
    #         driver,
    #         backend_url,
    #         frontend_url))
    # os.system("mysql -uroot < ../sql/test_spm.sql")
    # print(skill.updateSkillTest(driver,backend_url,frontend_url))
    # os.system("mysql -uroot < ../sql/test_spm.sql")
    # print(skill.createSkillTest(driver,backend_url,frontend_url))
    # os.system("mysql -uroot < ../sql/test_spm.sql")
    # print(skill.deleteRoleTest(driver,backend_url,frontend_url))
    # os.system("mysql -uroot < ../sql/test_spm.sql")
    print(learning_journey.searchLearningJourneyTest(driver,backend_url,frontend_url))
    



startDriver()
