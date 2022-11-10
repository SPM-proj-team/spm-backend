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
from sqlalchemy.sql import text

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
def test_create_role():
    with app.test_client() as test_client:
        response = test_client.post('/roles',
                                    data=json.dumps({
                                        "Job_Role": "DevOps Engineer",
                                        "Job_Title": "Staff",
                                        "Department": "Technology",
                                        "Description": "Lorem",
                                        "Skills": [1, 2]
                                    }),
                                    headers={
                                        "Content-Type": "application/json"
                                    }
                                    )

        assert response.status_code == 200
        assert response.get_json()['error'] == False
        jobRole = response.get_json()['data']

        getRole = test_client.get(f"/roles/{jobRole['Job_ID']}")
        data = getRole.get_json()
        assert data['data'][0]['Job_Role'] == "DevOps Engineer"
        assert data["data"][0]["Job_Title"] == "Staff"
        assert data["data"][0]["Department"] == "Technology"
        assert data["data"][0]["Description"] == "Lorem"
        assert len(data["data"][0]["Skills"]) == 2
        

def test_duplicate_create_role():
    with app.test_client() as test_client:
        response = test_client.post('/roles',
                                    data=json.dumps({
                                        "Job_Role": "Sales Manager",
                                        "Job_Title": "Manager",
                                        "Department": "Sales",
                                        "Description": "Lorem",
                                        "Skills": [1, 2]
                                    }),
                                    headers={
                                        "Content-Type": "application/json"
                                    }
                                    )
        assert response.status_code == 409
        assert response.get_json()['code'] == 409
        assert response.get_json()['error'] == True
        assert response.get_json()['message'] == "An error occurred while creating job role: Duplicate entry job role already exists"


def test_get_all_roles():
    with app.test_client() as test_client:
        response = test_client.get('/roles')
        assert response.status_code == 200
        assert response.get_json()["error"] == False
        all_roles = response.get_json()['data']
        assert len(all_roles) > 0


def test_get_single_role():
    with app.test_client() as test_client:
        response = test_client.get(f"/roles/1")
        assert response.status_code == 200
        assert response.get_json()["error"] == False
        assert len(response.get_json()['data']) > 0


def test_get_single_role_not_found():
    with app.test_client() as test_client:
        response = test_client.get(f"/roles/9999")
        assert response.status_code == 200
        assert response.get_json()["error"] == False
        assert len(response.get_json()['data']) == 0


def test_update_role():
    with app.test_client() as test_client:
        response = test_client.put('/roles',
                                   data=json.dumps({
                                       "Job_ID": 1,
                                       "Job_Role": "HR Staff",
                                       "Job_Title": "Staff",
                                       "Department": "HR",
                                       "Description": "Ipsum",
                                       "Skills": [3]
                                   }),
                                   headers={
                                       "Content-Type": "application/json"
                                   }
                                   )
        assert response.status_code == 200
        assert response.get_json()['error'] == False

        getRole = test_client.get(f"/roles/1")
        data = getRole.get_json()
        assert data["data"][0]["Job_Role"] == "HR Staff"
        assert data["data"][0]["Job_Title"] == "Staff"
        assert data["data"][0]["Department"] == "HR"
        assert data["data"][0]["Description"] == "Ipsum"
        assert len(data["data"][0]["Skills"]) == 1


def test_duplicate_update_role():
    with app.test_client() as test_client:
        testDuplicateRole = test_client.post('/roles',
                                             data=json.dumps({
                                                 "Job_Role": "DevOps Engineer",
                                                 "Job_Title": "Staff",
                                                 "Department": "Technology",
                                                 "Description": "Lorem",
                                                 "Skills": [1, 2]
                                             }),
                                             headers={
                                                 "Content-Type": "application/json"
                                             }
                                             )

        assert testDuplicateRole.status_code == 200
        assert testDuplicateRole.get_json()['error'] == False
        jobRole = testDuplicateRole.get_json()['data']
                        
        response = test_client.put('/roles',
                                   data=json.dumps({
                                       "Job_ID": jobRole['Job_ID'],
                                       "Job_Role": "Sales Manager",
                                       "Job_Title": "Manager",
                                       "Department": "Sales",
                                       "Description": "Ipsum",
                                       "Skills": [3]
                                   }),
                                   headers={
                                       "Content-Type": "application/json"
                                   }
                                   )
        assert response.status_code == 409
        assert response.get_json()['code'] == 409
        assert response.get_json()['error'] == True
        assert response.get_json()['message'] == "An error occurred while updating job role: Duplicate entry job role already exists"


def test_update_role_not_found():
    with app.test_client() as test_client:
        response = test_client.put('/roles',
                                   data=json.dumps({
                                       "Job_ID": 99,
                                       "Job_Role": "DevOps Engineer",
                                       "Job_Title": "Staff",
                                       "Department": "Technology",
                                       "Description": "Ipsum",
                                       "Skills": [1, 2]
                                   }),
                                   headers={
                                       "Content-Type": "application/json"
                                   }
                                   )
        assert response.status_code == 406
        assert response.get_json()['code'] == 406
        assert response.get_json()['error'] == True
        assert response.get_json()['message'] == "An error occurred while updating job role: Job ID not found"


def test_delete_role_associated_learning_journey():
    with app.test_client() as test_client:
        response = test_client.delete(f"/roles/1")
        assert response.get_json()['code'] == 406
        assert response.get_json()['error'] == True
        assert response.get_json()['message'] == "An error occurred while deleting job role: Job role id 1 stll have learning journeys associated with it"
        assert len(response.get_json()['data']['associated_learning_journeys']) > 0


def test_delete_role():
    with app.test_client() as test_client:
        testDuplicateRole = test_client.post('/roles',
                                             data=json.dumps({
                                                 "Job_Role": "DevOps Engineer",
                                                 "Job_Title": "Staff",
                                                 "Department": "Technology",
                                                 "Description": "Lorem",
                                                 "Skills": [1, 2]
                                             }),
                                             headers={
                                                 "Content-Type": "application/json"
                                             }
                                             )

        assert testDuplicateRole.status_code == 200
        assert testDuplicateRole.get_json()['error'] == False
        jobRole = testDuplicateRole.get_json()['data']
        response = test_client.delete(f"/roles/{jobRole['Job_ID']}")
        assert response.status_code == 200
        assert response.get_json()['error'] == False


def test_delete_role_not_found():
    with app.test_client() as test_client:
        response = test_client.delete(f"/roles/99")
        assert response.status_code == 406
        assert response.get_json()['code'] == 406
        assert response.get_json()['error'] == True
        assert response.get_json()['message'] == f"An error occurred while deleting job role: Job role id 99 not found"
