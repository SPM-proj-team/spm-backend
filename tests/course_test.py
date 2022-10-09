"""
Note:
    - Will need to install pytest to run test.
    - Run "pytest" in terminal to run all test cases in respective test files.
"""

"""
Unit tests for courses 
"""

import os

from app import app
from dotenv import load_dotenv
from datetime import datetime, timedelta
import pytest
from flask import json
from flask_sqlalchemy import SQLAlchemy

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
#         skills = [skill_id],
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
#     db.session.commit()
#     print('\n Tearing Down Complete')


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


# def test_get_courses_from_skill(skill):
#     with app.test_client() as test_client:
#         retrieve_courses = test_client.get(f"/skill/{skill['id']}")

#         assert retrieve_courses.get_json()["data"]["courses"] == []

# def test_create_course(skill):
#     with app.test_client() as test_client:
#         response = test_client.post('/course',
#                             data = json.dumps({
#                                 "name": "BAP101",
#                                 "duration": 5,
#                                 "skills": [skill.id]
#                             }),
#                             headers = {
#                                 "Content-Type": "application/json"
#                             }
#                         )
#         assert response.status_code == 200
#         global course
#         course = response.get_json()['data']


# def test_update_course():
#     course_name = "BAP102"
#     with app.test_client() as test_client:
#         response = test_client.put('/course',
#                             data = json.dumps({
#                                 "id": course['id'],
#                                 "name": course_name,
#                             }),
#                             headers = {
#                                 "Content-Type": "application/json"
#                             }
#                         )
#         assert response.status_code == 200

#         retrieve_course = test_client.get(f"/course/{course['id']}")
#         assert retrieve_course.get_json()['data']['name'] == course_name


# def test_delete_course():
#     with app.test_client() as test_client:
#         response = test_client.delete(f"/course/{course['id']}")
#         assert response.status_code == 200
#         tearDown()

