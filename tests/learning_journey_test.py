"""
Note:
    - Will need to install pytest to run test.
    - Run "pytest" in terminal to run all test cases in respective test files.
"""

"""
Unit tests for learning journeys 
"""

import os

from app import app
from dotenv import load_dotenv
import pytest
from flask import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

pytestmark = [pytest.mark.learning_journey]

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
def test_create_learning_journey():
    with app.test_client() as test_client:
        response = test_client.post('/learning_journey/create',
                            data = json.dumps({
                                "Learning_Journey": {
                                    "Courses": [
                                        {
                                            "Course_Category": "Core",
                                            "Course_Desc": "This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking,",
                                            "Course_ID": "COR001",
                                            "Course_Name": "Systems Thinking and Design",
                                            "Course_Status": "Active",
                                            "Course_Type": "Internal"
                                        }
                                    ],
                                    "Description": "test",
                                    "Learning_Journey_Name": "Learning Journey for Full Stack Developer",
                                    "Role": {
                                        "Department": "C-suite",
                                        "Description": "lorem ipsum",
                                        "Job_ID": 1,
                                        "Job_Role": "CEO",
                                        "Job_Title": "The big boss"
                                    },
                                    "Staff_ID": 1
                                }
                            }),
                            headers = {
                                "Content-Type": "application/json"
                            }
                        )
        assert response.status_code == 200
        assert response.get_json()['error'] == False
        lj = response.get_json()['data'][0]

        get_lj = test_client.post(f"/learning_journey/{lj['Learning_Journey_ID']}",
                    data = json.dumps(dict(Staff_ID=lj['Staff_ID'])),
                    content_type='application/json')
        data = get_lj.get_json()
        assert data['data'][0]['Learning_Journey_Name'] == "Learning Journey for Full Stack Developer"
        assert data["data"][0]["Description"] == "test"
        assert data["data"][0]["Role"]['Job_ID'] == 1
        assert len(data["data"][0]["Courses"]) == 1

# def test_duplicate_create_learning_journey():
#     with app.test_client() as test_client:
#         response = test_client.post('/learning_journey/create',
#                             data = json.dumps({
#                                 "Learning_Journey": {
#                                     "Courses": [
#                                         {
#                                             "Course_Category": "Core",
#                                             "Course_Desc": "This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking,",
#                                             "Course_ID": "COR001",
#                                             "Course_Name": "Systems Thinking and Design",
#                                             "Course_Status": "Active",
#                                             "Course_Type": "Internal"
#                                         }
#                                     ],
#                                     "Description": "test",
#                                     "Learning_Journey_Name": "Learning Journey for Full Stack Developer",
#                                     "Role": {
#                                         "Department": "C-suite",
#                                         "Description": "lorem ipsum",
#                                         "Job_ID": 1,
#                                         "Job_Role": "CEO",
#                                         "Job_Title": "The big boss"
#                                     },
#                                     "Staff_ID": 1
#                                 }
#                             }),
#                             headers = {
#                                 "Content-Type": "application/json"
#                             }
#                         )
#         assert response.status_code == 200
#         assert response.get_json()['code'] == 409
#         assert response.get_json()['error'] == True
#         assert response.get_json()['message'] == "An error occurred while creating learning journey: Duplicate learning journey name already exists for staff id 1" 


# def test_invalid_special_characters_create_learning_journey(course):
#     with app.test_client() as test_client:
#         response = test_client.post('/learning_journey',
#                             data = json.dumps({
#                                 "learning_journey_name": "Journey!!!#",
#                                 # "username": 1,
#                                 "course_id": course.id,
#                             }),
#                             headers = {
#                                 "Content-Type": "application/json"
#                             }
#                         )
#         assert response.status_code == 400


def test_get_learning_journeys_by_staff_id():
    with app.test_client() as test_client:
        response = test_client.post('/learning_journey',
                                   data = json.dumps(dict(Staff_ID=1)),
                                   content_type='application/json')
        assert response.status_code == 200
        all_learning_journeys = response.get_json()['data']
        assert len(all_learning_journeys) > 0


def test_get_courses_by_one_learning_journey():
    with app.test_client() as test_client:
        response = test_client.post(f"/learning_journey/1",
                                   data = json.dumps(dict(Staff_ID=1)),
                                   content_type='application/json')
        assert response.status_code == 200
        learning_journey = response.get_json()['data']
        assert len(learning_journey) > 0


def test_get_courses_by_one_learning_journey_no_learning_journey():
    with app.test_client() as test_client:
        response = test_client.post(f"/learning_journey/1",
                                   data = json.dumps(dict(Staff_ID=2)),
                                   content_type='application/json')
        assert response.status_code == 200
        learning_journey = response.get_json()['data']
        assert len(learning_journey) == 0
        message = response.get_json()['message']
        assert message == "There are no Learning Journeys."


def test_update_learning_journey():
    with app.test_client() as test_client:
        response = test_client.put(f"/learning_journey/1",
                            data = json.dumps({
                                "Staff_ID": 1,
                                "Learning_Journey": {
                                    "Learning_Journey_ID": 1,
                                    "Courses": [
                                        {
                                            "Course_Category": "Core",
                                            "Course_Desc": "This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking",
                                            "Course_ID": "COR001",
                                            "Course_Name": "Systems Thinking and Design",
                                            "Course_Status": "Active",
                                            "Course_Type": "Internal"
                                        },
                                        {
                                            "Course_Category": "Core",
                                            "Course_Desc": "Apply Lean Six Sigma methodology and statistical tools such as Minitab to be used in process analytics",
                                            "Course_ID": "COR002",
                                            "Course_Name": "Lean Six Sigma Green Belt Certification",
                                            "Course_Status": "Active",
                                            "Course_Type": "Internal"
                                        }
                                    ],
                                    "Description": "test",
                                    "Learning_Journey_Name": "Learning Journey for Full Stack",
                                    "Role": {
                                        "Department": "C-suite",
                                        "Description": "lorem ipsum",
                                        "Job_ID": 1,
                                        "Job_Role": "CEO",
                                        "Job_Title": "The big boss"
                                    }
                                }
                            }),
                            headers = {
                                "Content-Type": "application/json"
                            }
                        )
        assert response.status_code == 200
        assert response.get_json()['error'] == False
        data = response.get_json()['data'][0]
        assert data["Description"] == "test"
        assert data["Role"]['Job_ID'] == 1
        assert data["Learning_Journey_Name"] == "Learning Journey for Full Stack"


def test_update_courses_in_learning_journey():
    with app.test_client() as test_client:
        response = test_client.put(f"/learning_journey/1",
                            data = json.dumps({
                                "Staff_ID": 1,
                                "Learning_Journey": {
                                    "Learning_Journey_ID": 1,
                                    "Courses": [
                                        {
                                            "Course_Category": "Core",
                                            "Course_Desc": "Apply Lean Six Sigma methodology and statistical tools such as Minitab to be used in process analytics",
                                            "Course_ID": "COR002",
                                            "Course_Name": "Lean Six Sigma Green Belt Certification",
                                            "Course_Status": "Active",
                                            "Course_Type": "Internal"
                                        }
                                    ],
                                    "Description": "test",
                                    "Learning_Journey_Name": "Learning Journey for Full Stack Developer",
                                    "Role": {
                                        "Department": "C-suite",
                                        "Description": "lorem ipsum",
                                        "Job_ID": 1,
                                        "Job_Role": "CEO",
                                        "Job_Title": "The big boss"
                                    }
                                }
                            }),
                            headers = {
                                "Content-Type": "application/json"
                            }
                        )
        assert response.status_code == 200
        assert response.get_json()['error'] == False
        data = response.get_json()['data'][0]
        assert len(data["Courses"]) == 1
        assert data["Courses"][0]["Course_ID"] == "COR002"


def test_update_courses_in_learning_journey_no_courses():
    with app.test_client() as test_client:
        response = test_client.put(f"/learning_journey/1",
                            data = json.dumps({
                                "Staff_ID": 1,
                                "Learning_Journey": {
                                    "Learning_Journey_ID": 1,
                                    "Courses": [],
                                    "Description": "test",
                                    "Learning_Journey_Name": "Learning Journey for Full Stack Developer",
                                    "Role": {
                                        "Department": "C-suite",
                                        "Description": "lorem ipsum",
                                        "Job_ID": 1,
                                        "Job_Role": "CEO",
                                        "Job_Title": "The big boss"
                                    }
                                }
                            }),
                            headers = {
                                "Content-Type": "application/json"
                            }
                        )
        assert response.status_code == 404
        assert response.get_json()['code'] == 404
        assert response.get_json()['error'] == True 
        assert response.get_json()['message'] == "There should at least be 1 course in the Learning Journey"


# def test_duplicate_update_courses_in_learning_journey():
#     with app.test_client() as test_client:
#         testDuplicateLJ = test_client.post('/learning_journey/create',
#                             data = json.dumps({
#                                 "Learning_Journey": {
#                                     "Courses": [
#                                         {
#                                             "Course_Category": "Core",
#                                             "Course_Desc": "This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking,",
#                                             "Course_ID": "COR001",
#                                             "Course_Name": "Systems Thinking and Design",
#                                             "Course_Status": "Active",
#                                             "Course_Type": "Internal"
#                                         }
#                                     ],
#                                     "Description": "test",
#                                     "Learning_Journey_Name": "Learning Journey for DevOps Engineer",
#                                     "Role": {
#                                         "Department": "C-suite",
#                                         "Description": "lorem ipsum",
#                                         "Job_ID": 1,
#                                         "Job_Role": "CEO",
#                                         "Job_Title": "The big boss"
#                                     },
#                                     "Staff_ID": 1
#                                 }
#                             }),
#                             headers = {
#                                 "Content-Type": "application/json"
#                             }
#                         )
#         assert testDuplicateLJ.status_code == 200
#         assert testDuplicateLJ.get_json()['error'] == False
#         global lj2
#         lj2 = testDuplicateLJ.get_json()['data'][0]

#         response = test_client.put(f"/learning_journey/{lj2['Learning_Journey_ID']}",
#                             data = json.dumps({
#                                 "Staff_ID": lj2['Staff_ID'],
#                                 "Learning_Journey": {
#                                     "Learning_Journey_ID": lj2['Learning_Journey_ID'],
#                                     "Courses": [
#                                         {
#                                             "Course_Category": "Core",
#                                             "Course_Desc": "This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking,",
#                                             "Course_ID": "COR001",
#                                             "Course_Name": "Systems Thinking and Design",
#                                             "Course_Status": "Active",
#                                             "Course_Type": "Internal"
#                                         }
#                                     ],
#                                     "Description": "test",
#                                     "Learning_Journey_Name": lj['Learning_Journey_Name'],
#                                     "Role": {
#                                         "Department": "C-suite",
#                                         "Description": "lorem ipsum",
#                                         "Job_ID": 1,
#                                         "Job_Role": "CEO",
#                                         "Job_Title": "The big boss"
#                                     }
#                                 }
#                             }),
#                             headers = {
#                                 "Content-Type": "application/json"
#                             }
#                         )
#         assert response.status_code == 200
#         assert response.get_json()['code'] == 409
#         assert response.get_json()['error'] == True 
#         assert response.get_json()['message'] == "An error occurred while updating learning journey: Duplicate learning journey name already exists for staff id 1." 


def test_delete_learning_journey():
    with app.test_client() as test_client:
        response = test_client.delete(f"/learning_journey/1",
            data = json.dumps({
                "Staff_ID": 1
            }),
            headers = {
                "Content-Type": "application/json"
            }
        )
        # response2 = test_client.delete(f"/learning_journey/{lj2['Learning_Journey_ID']}",
        #     data = json.dumps({
        #         "Staff_ID": lj2['Staff_ID']
        #     }),
        #     headers = {
        #         "Content-Type": "application/json"
        #     }
        # )
        assert response.status_code == 200
        assert response.get_json()['error'] == False
        assert response.get_json()['message'] == f"Learning Journey ID: 1 has been deleted"
        # assert response2.status_code == 200
        # assert response2.get_json()['error'] == False
        # assert response2.get_json()['message'] == f"Learning Journey ID: {lj2['Learning_Journey_ID']} has been deleted"


def test_delete_learning_journey_not_found():
    with app.test_client() as test_client:
        response = test_client.delete(f"/learning_journey/99",
            data = json.dumps({
                "Staff_ID": 1
            }),
            headers = {
                "Content-Type": "application/json"
            }
        )
        assert response.status_code == 406
        assert response.get_json()['message'] == f"There is no Learning Journeys with ID: 99"
        assert response.get_json()['error'] == True 
        assert response.get_json()['code'] == 406
