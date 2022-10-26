"""
Note:
    - Will need to install pytest to run test.
    - Run "pytest" in terminal to run all test cases in respective test files.
"""

"""
Integration tests for skills
"""


import os
from app import app
from dotenv import load_dotenv
import pytest
from flask import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
pytestmark = [pytest.mark.skill]

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
def test_create_skill():
    with app.test_client() as test_client:
        response = test_client.post('/skills',
                                    data=json.dumps({
                                        "Skill_ID": "S099",
                                        "Name": "Solidity",
                                        "Courses": ["FIN001", "FIN002"]
                                    }),
                                    headers={
                                        "Content-Type": "application/json"
                                    }
                                    )
        assert response.status_code == 200
        assert response.get_json()["error"] == False


def test_duplicate_create_skill():
    with app.test_client() as test_client:
        response = test_client.post('/skills',
                                    data=json.dumps({
                                        "Skill_ID": "S100",
                                        "Name": "Critical Thinking",
                                        "Courses": ["FIN001", "FIN002"]
                                    }),
                                    headers={
                                        "Content-Type": "application/json"
                                    }
                                    )
        assert response.status_code == 409
        assert response.get_json()["error"]
        assert response.get_json()[
            "message"] == "An error occurred while creating skill: Duplicate entry skill name already exists"


def test_get_all_skills():
    with app.test_client() as test_client:
        response = test_client.get('/allskills')
        assert response.status_code == 200
        assert response.get_json()["error"] == False
        all_skills = response.get_json()['data']
        assert len(all_skills) > 0


def test_get_all_skills_with_courses():
    with app.test_client() as test_client:
        response = test_client.get('/skills')
        assert response.status_code == 200
        assert response.get_json()["error"] == False
        all_skills_with_courses = response.get_json()['data']
        assert len(all_skills_with_courses) > 0


def test_update_skill():
    with app.test_client() as test_client:
        response = test_client.put('/skills',
                                   data=json.dumps({
                                       "Skill_ID": "S001",
                                       "Name": "Ethereum",
                                       "Courses": ["FIN001"]
                                   }),
                                   headers={
                                       "Content-Type": "application/json"
                                   }
                                   )
        assert response.status_code == 200
        assert response.get_json()["error"] == False
        data = response.get_json()["data"]
        assert data["Name"] == "Ethereum"
        assert len(data["Courses"]) == 1


def test_duplicate_update_role():
    with app.test_client() as test_client:
        response = test_client.put('/skills',
                                   data=json.dumps({
                                       "Skill_ID": "S001",
                                       "Name": "People Management",
                                       "Courses": ["FIN001"]
                                   }),
                                   headers={
                                       "Content-Type": "application/json"
                                   }
                                   )
        assert response.status_code == 409
        assert response.get_json()['code'] == 409
        assert response.get_json()['error']
        assert response.get_json()[
            'message'] == "An error occurred while updating skill: Duplicate skill name already exists"


def test_update_skill_not_found():
    with app.test_client() as test_client:
        response = test_client.put('/skills',
                                   data=json.dumps({
                                       "Skill_ID": "S999",
                                       "Name": "Blockchain",
                                       "Courses": ["FIN001", "FIN002"]
                                   }),
                                   headers={
                                       "Content-Type": "application/json"
                                   }
                                   )
        assert response.status_code == 406
        assert response.get_json()['code'] == 406
        assert response.get_json()['error']
        assert response.get_json()[
            'message'] == "An error occurred while updating skill: Skill ID S999 does not exist"


def test_delete_skill():
    with app.test_client() as test_client:
        response = test_client.delete("/skills",
                                      data=json.dumps({
                                          "Skill_ID": "S001"
                                      }),
                                      headers={
                                          "Content-Type": "application/json"
                                      }
                                      )

        assert response.status_code == 200
        assert response.get_json()['error'] == False


def test_delete_skill_not_found():
    with app.test_client() as test_client:
        response = test_client.delete("/skills",
                                      data=json.dumps({
                                          "Skill_ID": "S999"
                                      }),
                                      headers={
                                          "Content-Type": "application/json"
                                      }
                                      )
        assert response.status_code == 406
        assert response.get_json()['code'] == 406
        assert response.get_json()['error']
        assert response.get_json()[
            'message'] == "An error occurred while deleting skill: Skill ID S999 not found"
