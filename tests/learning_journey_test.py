"""
Note:
    - Will need to install pytest to run test.
    - Run "pytest" in terminal to run all test cases in respective test files.
"""

"""
Unit tests for learning journeys 
"""

import os

from app import learning_journey

from app import app
from dotenv import load_dotenv
import pytest
from flask import json
from flask_sqlalchemy import SQLAlchemy

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
    return db


# Set up test data in database
# @pytest.fixture(autouse=True)
# def role(initialise_db):
#     print('role')
#     from app import role
#     test_role = role.Role(
#         name = "Analytics Manager",
#         skills = []
#     )
#     db.session.add(test_role)
#     db.session.commit()
#     return test_role

# @pytest.fixture(autouse=True)
# def skill(role):
#     from app import skill
#     role_id = role.id
#     test_skill = skill.Skill(
#         role_id = role_id,
#         name = "Business Application",
#     )
#     db.session.add(test_skill)
#     db.session.commit()
#     return test_skill

# @pytest.fixture(autouse=True)
# def course(skill):
#     from app import course
#     skill_id = skill.id
#     test_course = course.Course(
#         name = "Business Application",
#         duration = 4,
#         # prereq_course_id = 1,
#         # skills = [skill_id],
#     )
#     db.session.add(test_course)
#     db.session.commit()
#     return test_course

# def tearDown(): 
#     print('\n Tearing Down')
#     from app import role, skill, course
#     db.session.query(course.Course).delete()
#     db.session.query(skill.Skill).delete()
#     db.session.query(role.Role).delete()
#     print('\n Tearing Down Complete')


# Test cases
# def test_create_learning_journey(course):
#     with app.test_client() as test_client:
#         response = test_client.post('/learning_journey',
#                             data = json.dumps({
#                                 "learning_journey_name": "Journey 1",
#                                 # "username": 1,
#                                 "course_id": course.id,
#                             }),
#                             headers = {
#                                 "Content-Type": "application/json"
#                             }
#                         )
#         assert response.status_code == 200
#         global learning_journey
#         learning_journey = response.get_json()['data']
        

# def test_duplicate_create_learning_journey(course):
#     with app.test_client() as test_client:
#         response = test_client.post('/learning_journey',
#                             data = json.dumps({
#                                 "learning_journey_name": "Journey 1",
#                                 # "username": 1,
#                                 "course_id": course.id,
#                             }),
#                             headers = {
#                                 "Content-Type": "application/json"
#                             }
#                         )
#         assert response.status_code == 400


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
        response = test_client.put('/learning_journey/1',
                            data = json.dumps({
                                "Staff_ID": 1,
                                "Learning_Journey": {
                                    "Learning_Journey_ID": 1,
                                    "Courses": [
                                        {
                                            "Course_Category": "Course_Category_1",
                                            "Course_Desc": "Enterprise Business System Description",
                                            "Course_ID": "BAP101",
                                            "Course_Name": "Enterprise Business System",
                                            "Course_Status": "Open",
                                            "Course_Type": "Type_1"
                                        },
                                        {
                                            "Course_Category": "Course_Category_1",
                                            "Course_Desc": "Equip student with knowledge about agile approach regarding software project development ",
                                            "Course_ID": "IS212",
                                            "Course_Name": "Software Project Management",
                                            "Course_Status": "Open",
                                            "Course_Type": "Type_1"
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
        assert data["Description"] == "test"
        assert data["Learning_Journey_Name"] == "Learning Journey for Full Stack Developer"


def test_update_courses_in_learning_journey():
    with app.test_client() as test_client:
        response = test_client.put('/learning_journey/1',
                            data = json.dumps({
                                "Staff_ID": 1,
                                "Learning_Journey": {
                                    "Learning_Journey_ID": 1,
                                    "Courses": [
                                        {
                                            "Course_Category": "Course_Category_1",
                                            "Course_Desc": "Sales Management System Description",
                                            "Course_ID": "BAP102",
                                            "Course_Name": "Sales Management System",
                                            "Course_Status": "Open",
                                            "Course_Type": "Type_1"
                                        },
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
        assert data["Courses"][0]["Course_ID"] == "BAP102"


def test_update_courses_in_learning_journey_no_courses():
    with app.test_client() as test_client:
        response = test_client.put('/learning_journey/1',
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
        assert response.status_code == 200
        assert response.get_json()['code'] == 404
        assert response.get_json()['error'] == True 
        assert response.get_json()['message'] == "There should at least be 1 course in the Learning Journey"


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
        assert response.status_code == 200
        assert response.get_json()['error'] == False
        assert response.get_json()['message'] == "Learning Journey ID: 1 has been deleted"


def test_delete_learning_journey_not_found():
    with app.test_client() as test_client:
        response = test_client.delete(f"/learning_journey/0",
            data = json.dumps({
                "Staff_ID": 1
            }),
            headers = {
                "Content-Type": "application/json"
            }
        )
        assert response.status_code == 200
        assert response.get_json()['code'] == 400
        assert response.get_json()['error'] == True 
        assert response.get_json()['message'] == "There is no Learning Journeys with ID: 0"
