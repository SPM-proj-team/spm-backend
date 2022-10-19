"""
Note:
    - Will need to install pytest to run test.
    - Run "pytest" in terminal to run all test cases in respective test files.
"""

"""
Unit tests for skills 
"""

import os
from app import app
from dotenv import load_dotenv
import pytest
from flask_sqlalchemy import SQLAlchemy

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
    return db


@pytest.fixture(autouse=True)
def setUp():
    db.create_all()

def tearDown(): 
    db.session.remove()
    db.drop_all()


# Test cases
# def test_create_skill(role):
#     with app.test_client() as test_client:
#         response = test_client.post('/skills',
#                             data = json.dumps({
#                                 # "role_id": role.id,
#                                 "name": "Business Application",
#                             }),
#                             headers = {
#                                 "Content-Type": "application/json"
#                             }
#                         )
#         assert response.status_code == 200
#         global skill
#         skill = response.get_json()['data']
        

# def test_duplicate_create_skill(role):
#     with app.test_client() as test_client:
#         response = test_client.post('/skills',
#                             data = json.dumps({
#                                 # "role_id": role.id,
#                                 "name": "Business Application",
#                             }),
#                             headers = {
#                                 "Content-Type": "application/json"
#                             }
#                         )
#         assert response.status_code == 400


# def test_invalid_special_characters_create_skill(role):
#     with app.test_client() as test_client:
#         response = test_client.post('/skills',
#                             data = json.dumps({
#                                 # "role_id": role.id,
#                                 "name": "Invalid Skill!!!@@",
#                             }),
#                             headers = {
#                                 "Content-Type": "application/json"
#                             }
#                         )
#         assert response.status_code == 400


def test_get_all_skills():
    with app.test_client() as test_client:
        response = test_client.get('/skills')
        assert response.status_code == 200
        all_skills = response.get_json()['data']
        assert len(all_skills) > 0


# def test_get_single_skill():
#     with app.test_client() as test_client:
#         response = test_client.get(f"/skills/{skill['id']}")
#         assert response.status_code == 200


# def test_get_skills_from_role(role):
#     with app.test_client() as test_client:
#         retrieve_skills = test_client.get(f"/role/{role['id']}")

#         assert retrieve_skills.get_json()["data"]["Skills"] == []


# def test_update_skill():
#     skill_name = "Statistical Evaluation"
#     with app.test_client() as test_client:
#         response = test_client.put('/skills',
#                             data = json.dumps({
#                                 "id": skill['id'],
#                                 "name": skill_name,
#                             }),
#                             headers = {
#                                 "Content-Type": "application/json"
#                             }
#                         )
#         assert response.status_code == 200

#         retrieve_skill = test_client.get(f"/skills/{skill['id']}")
#         assert retrieve_skill.get_json()['data']['name'] == skill_name


# def test_duplicate_update_role(role):
#     skill_name = "Statistical Evaluation"
#     with app.test_client() as test_client:
#         testDuplicateSkill = test_client.post('/skills',
#             data = json.dumps({
#                 # "role_id": role.id,
#                 "name": "Analytical Methods",
#             }),
#             headers = {
#                 "Content-Type": "application/json"
#             }
#         )
                        
#         response = test_client.put('/skills',
#                             data = json.dumps({
#                                 "id": testDuplicateSkill['id'],
#                                 "name": skill_name,
#                             }),
#                             headers = {
#                                 "Content-Type": "application/json"
#                             }
#                         )
#         assert response.status_code == 400
#         global skill2
#         skill2 = testDuplicateSkill.get_json()['data']


# def test_delete_skill():
#     with app.test_client() as test_client:
#         response = test_client.delete(f"/skills/{skill['id']}")
#         response2 = test_client.delete(f"/skills/{skill2['id']}")
#         assert response.status_code == 200
#         assert response2.status_code == 200
#         tearDown()

