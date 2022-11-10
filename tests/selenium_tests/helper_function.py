from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def testFormatCount(name, count, correctCount):
    print("=" * 8)
    print(name + " Counts")
    print(f"Actual Count: {count} \nCorrectCount :{correctCount}")
    print("Test status: " + str(count == correctCount))
    print("=" * 8)
    if (count != correctCount):
        return False
    else:
        return True


def testFormatSingle(name, status):
    print("=" * 8)
    print("Test: " + name)
    print("Test status: " + str(status))
    print("=" * 8)
    if (status == False):
        return False
    else:
        return True


def quitFormaT(str):
    print(str + ": Fail")


def Login(driver, frontend_url):
    try:
        driver.get(frontend_url)
        email = WebDriverWait(
            driver, 3).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[@type='email']")))
        email[0].send_keys("john.doe@test.com.sg")
        id = WebDriverWait(
            driver, 3).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[@type='number']")))
        id[0].send_keys("1")

        loginBtn = WebDriverWait(
            driver, 3).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//button[text()='Login']")))
        loginBtn[0].click()
    except Exception:
        pass
