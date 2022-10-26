"""
Note:
    - Will need to install pytest to run test.
    - Run "pytest" in terminal to run all test cases in respective test files.
"""

"""
Integration tests for registration
"""


import os
from app import app
from dotenv import load_dotenv
import pytest
from flask import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
pytestmark = [pytest.mark.registration]

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


# Test cases
def test_get_all_registrations():
    with app.test_client() as test_client:
        response = test_client.get('/registration')
        assert response.status_code == 200
        assert response.get_json()["error"] == False
        all_registrations = response.get_json()['data']
        assert len(all_registrations) > 0


def test_get_registration_by_staff_id():
    with app.test_client() as test_client:
        response = test_client.post('/registration',
                                    data=json.dumps({
                                        "Staff_ID": 130001
                                    }),
                                    headers={
                                        "Content-Type": "application/json"
                                    }
                                    )
        assert response.status_code == 200
        assert response.get_json()["error"] == False
        assert len(response.get_json()["data"]) == 2


def test_get_registration_by_staff_id_no_registrations():
    with app.test_client() as test_client:
        response = test_client.post('/registration',
                                    data=json.dumps({
                                        "Staff_ID": 1
                                    }),
                                    headers={
                                        "Content-Type": "application/json"
                                    }
                                    )
        assert response.status_code == 200
        assert response.get_json()["error"] == False
        assert response.get_json()["message"] == "There are no Registrations"
