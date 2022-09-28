"""
Note:
    - Will need to install pytest to run test.
    - Run "pytest" in terminal to run all test cases in respective test files.
"""

"""
Unit tests for roles 
"""

import os
from app import app
from dotenv import load_dotenv
import pytest
from flask import json
from flask_sqlalchemy import SQLAlchemy

pytestmark = [pytest.mark.role]

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

# Test cases
# def test_create_role():
#     with app.test_client() as test_client:
#         response = test_client.post('/roles',
#                             data = json.dumps({
#                                 "Job_Role": "Manager",
#                                 "Job_Title": "Analytics Manager",
#                                 "Skills": [],
#                             }),
#                             headers = {
#                                 "Content-Type": "application/json"
#                             }
#                         )
#         assert response.status_code == 200
#         global role
#         role = response.get_json()['data']


# def test_duplicate_create_role():
#     with app.test_client() as test_client:
#         response = test_client.post('/roles',
#                             data = json.dumps({
#                                 "Job_Role": "Manager",
#                                 "Job_Title": "Analytics Manager",
#                                 "Skills": [],
#                             }),
#                             headers = {
#                                 "Content-Type": "application/json"
#                             }
#                         )
#         assert response.status_code == 400


def test_get_all_roles():
    with app.test_client() as test_client:
        response = test_client.get('/roles')
        assert response.status_code == 200
        all_roles = response.get_json()['data']
        assert len(all_roles) > 0


# def test_get_single_role():
#     with app.test_client() as test_client:
#         response = test_client.get(f"/roles/{role['id']}")
#         assert response.status_code == 200


# def test_update_role():
#     role_name = "Analytics Executive"
#     with app.test_client() as test_client:
#         response = test_client.put('/roles',
#                             data = json.dumps({
#                                 "id": role['id'],
#                                 "name": role_name,
#                                 "skills": []
#                             }),
#                             headers = {
#                                 "Content-Type": "application/json"
#                             }
#                         )
#         assert response.status_code == 200

#         retrieve_role = test_client.get(f"/roles/{role['id']}")
#         assert retrieve_role.get_json()['data']['name'] == role_name 


# def test_duplicate_update_role():
#     role_name = "Analytics Executive"
#     with app.test_client() as test_client:
#         testDuplicateRole = test_client.post('/roles',
#             data = json.dumps({
#                 "name": "Finance Executive",
#                 "skills": []
#             }),
#             headers = {
#                 "Content-Type": "application/json"
#             }
#         )
                        
#         response = test_client.put('/roles',
#                             data = json.dumps({
#                                 "id": role['id'],
#                                 "name": role_name,
#                                 "skills": []
#                             }),
#                             headers = {
#                                 "Content-Type": "application/json"
#                             }
#                         )
#         assert response.status_code == 400
#         global role2
#         role2 = testDuplicateRole.get_json()['data']

        

# def test_delete_role():
#     with app.test_client() as test_client:
#         response = test_client.delete(f"/roles/{role['id']}")
#         response2 = test_client.delete(f"/roles/{role2['id']}")
#         assert response.status_code == 200
#         assert response2.status_code == 200
