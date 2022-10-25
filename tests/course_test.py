"""
Note:
    - Will need to install pytest to run test.
    - Run "pytest" in terminal to run all test cases in respective test files.
"""

"""
Integration tests for courses 
"""

import os

from app import app
from dotenv import load_dotenv
import pytest
from flask import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

pytestmark = [pytest.mark.course]

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
    sql_file = open('tests/sql/test_spm.sql','r')
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
def test_get_all_courses():
    with app.test_client() as test_client:
        response = test_client.get('/courses')
        assert response.status_code == 200
        all_courses = response.get_json()['data']
        assert len(all_courses) > 0


# def test_get_single_course(course):
#     with app.test_client() as test_client:
#         response = test_client.get(f"/course/{course['id']}")
#         assert response.status_code == 200


def test_update_skills_mapped_to_course():
    with app.test_client() as test_client:
        response = test_client.put('/courses',
                            data = json.dumps({
                                "Course_ID": "COR001",
                                "Skills": ["S003"]
                            }),
                            headers = {
                                "Content-Type": "application/json"
                            }
                        )
        assert response.status_code == 200
        assert response.get_json()["error"] == False
        data = response.get_json()["data"]
        assert len(data["Skills"]) == 1
        assert data["Skills"][0]["Skill_ID"] == "S003"

def test_update_skills_mapped_to_course_not_found():
    testCourseID = "MGMT999"
    with app.test_client() as test_client:
        response = test_client.put('/courses',
                            data = json.dumps({
                                "Course_ID": testCourseID,
                                "Skills": ["S003"]
                            }),
                            headers = {
                                "Content-Type": "application/json"
                            }
                        )
        assert response.status_code == 406
        assert response.get_json()["error"] == True
        assert response.get_json()["message"] == f"An error occurred while mapping skills to course: Course ID {testCourseID} not found"
