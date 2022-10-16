from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

import role
import learning_journey
import helper_function
import traceback

backend_url = "http://localhost:5000/"
frontend_url = "http://localhost:8080/"
# Start selenium
def startDriver():
    chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    chrome_options = Options()
    options = [
        "--headless",
        "--disable-gpu",
        "--window-size=1920,1200",
        "--ignore-certificate-errors",
        "--disable-extensions",
        "--no-sandbox",
        "--disable-dev-shm-usage"
    ]
    for option in options:
        chrome_options.add_argument(option)

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    #  go in url
    try:
        driver.get(frontend_url)
        helper_function.testFormatSingle("Running of home page", True)
    except Exception as e:
        helper_function.testFormatSingle("Running of home page", False)
        print(e)
        traceback.print_exc()
        return False
    
    ## Test get learning journeys for staff
    try:
        learning_journey.checkLearningJourney(driver,backend_url,frontend_url)
    except Exception as e:
        print(e)
        traceback.print_exc()
        return False
   
    # Test update and deletion of job roles
    try:
        role.updateRoleTest(driver,backend_url,frontend_url)
    except Exception as e:
        print(e)
        traceback.print_exc()
        return False
    try:
        role.createRoleTest(driver,backend_url,frontend_url)
    except Exception as e:
        print(e)
        traceback.print_exc()
        return False

    try:
        role.deleteRoleTest(driver,backend_url,frontend_url)
    except Exception as e:
        print(e)
        traceback.print_exc()
        return False
    driver.quit()
    return True
    

startDriver()

