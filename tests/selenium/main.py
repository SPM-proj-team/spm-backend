from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
# Start selenium
def startDriver():
    # intiatise driver (take note that different os require different drivers to be downloaded)
    driver = webdriver.Chrome('./chrome_driver/chromedriver')

    # demo for login 

    #  go in url
    driver.get("https://www.browserstack.com/users/sign_in")
    # enter email and password, take note that sometimes depending on client render or server render elements might not load as 
    # fast then will cause error, that's why you can WebDriverWait and EC 
    emailuser = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user_email_login"))
    )
    emailuser.send_keys("test@test.com")

    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user_password"))
    )
    password.send_keys("password")
    # this is the standard find element with out EC and WebDriverWait
    login = driver.find_element(By.ID,"user_submit")
    login.click()


    #  for you to take a look before the driver closes
    time.sleep(5)
    driver.quit()



# this is for sample 
startDriver()
