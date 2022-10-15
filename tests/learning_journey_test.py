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

# def test_get_courses_from_learning_journey():
#     with app.test_client() as test_client:
#         retrieve_courses = test_client.get(f"/learning_journey/{learning_journey['id']}")

#         assert retrieve_courses.get_json()["data"]["courses"] == []


# def test_update_learning_journey(course):
#     learning_journey_name = "Journey 2"
#     with app.test_client() as test_client:
#         response = test_client.put('/learning_journey',
#                             data = json.dumps({
#                                 "id": learning_journey['id'],
#                                 "learning_journey_name": learning_journey_name,
#                             }),
#                             headers = {
#                                 "Content-Type": "application/json"
#                             }
#                         )
#         assert response.status_code == 200

#         retrieve_learning_journey = test_client.get(f"/learning_journey/{learning_journey['id']}")
#         assert retrieve_learning_journey.get_json()['data']['name'] == learning_journey_name


# def test_duplicate_update_learning_journey(course):
#     learning_journey_name = "Journey 2"
#     with app.test_client() as test_client:
#         testDuplicateLearningJourney = test_client.post('/learning_journey',
#             data = json.dumps({
#                 "learning_journey_name": "Journey 3",
#                 # "username": 1,
#                 "course_id": course.id,
#             }),
#             headers = {
#                 "Content-Type": "application/json"
#             }
#         )
                        
#         response = test_client.put('/skill',
#                             data = json.dumps({
#                                 "id": testDuplicateLearningJourney['id'],
#                                 "name": learning_journey_name,
#                             }),
#                             headers = {
#                                 "Content-Type": "application/json"
#                             }
#                         )
#         assert response.status_code == 400
#         global learning_journey2
#         learning_journey2 = testDuplicateLearningJourney.get_json()['data']


# def test_delete_learning_journey():
#     with app.test_client() as test_client:
#         response = test_client.delete(f"/learning_journey/{learning_journey['id']}")
#         response2 = test_client.delete(f"/learning_journey/{learning_journey2['id']}")
#         assert response.status_code == 200
#         assert response2.status_code == 200
#         tearDown()

