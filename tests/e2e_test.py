"""
Note:
    - Will need to install pytest to run test.
    - Run "pytest" in terminal to run all test cases in respective test files.
"""

"""
End to end testing
"""

import os
from app import app
from dotenv import load_dotenv
import pytest
import chromedriver_autoinstaller
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium_tests import learning_journey, role
pytestmark = [pytest.mark.e2e]

#  Load function to read from .env


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


# Set up connection to DB
@pytest.fixture(autouse=True)
def initialise_db():
    db_host = os.environ.get("DB_HOSTNAME")
    db_port = os.environ.get("DB_PORT")
    db_username = os.environ.get("DB_USERNAME")
    db_password = os.environ.get("DB_PASSWORD")
    db_name = os.environ.get("DB_NAME")

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"mysql+mysqlconnector://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    global db
    db = SQLAlchemy(app)
    global sql_file
    sql_file = open('tests/sql/test_spm.sql', 'r')
    return db, sql_file


# Set up driver
@pytest.fixture(autouse=True)
def startDriver():
    chromedriver_autoinstaller.install()
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

    global driver
    global backend_url
    global frontend_url
    # driver = driver = webdriver.Firefox()
    # driver.maximize_window()
    driver = webdriver.Chrome(options=chrome_options)
    backend_url = "http://127.0.0.1:5000/"
    frontend_url = "http://127.0.0.1:8080/"

    return driver, backend_url, frontend_url


# Fixture to reset database before each test is run
@pytest.fixture(autouse=True)
def reset():
    # Before test commands
    print('\nResetting test database')
    sql_command = ''
    for line in sql_file:
        # Ignore commented lines
        if not line.startswith('--') and line.strip('\n'):
            # Append line to the command string
            sql_command += line.strip('\n')

            # If the command string ends with ';', it is a full statement
            if sql_command.endswith(';'):
                # Try to execute statement and commit it
                try:
                    db.session.execute(text(sql_command))
                    db.session.commit()
                # Assert in case of error
                except Exception as e:
                    print(e)

                # Finally, clear command string
                finally:
                    sql_command = ''
    # This is where the testing happens
    yield
    # Close driver after each test
    driver.close()


# Test cases
def test_run_home_page():
    driver.get(frontend_url)
    assert driver.title == "ljps"


def test_get_learning_journey():
    response = learning_journey.checkLearningJourney(
        driver, backend_url, frontend_url)
    assert response


def test_update_role():
    response = role.updateRoleTest(driver, backend_url, frontend_url)
    assert response


def test_create_role():
    response = role.createRoleTest(driver, backend_url, frontend_url)
    assert response


def test_delete_role():
    response = role.deleteRoleTest(driver, backend_url, frontend_url)
    assert response


def test_search_role():
    response = role.searchRoleTest(driver, backend_url, frontend_url)
    assert response

def test_update_learning_journey():
    response = learning_journey.updateLearningJourneyTest(driver,backend_url,frontend_url)
    assert response

def test_create_learning_journey():
    response = learning_journey.createLearningJourneyTest(driver, backend_url, frontend_url)
    assert response

def test_delete_learning_journey():
    response = learning_journey.deleteLearningJourneyTest(driver, backend_url, frontend_url)
    assert response
