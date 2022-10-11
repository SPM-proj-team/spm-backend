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
def test_create_role():
    with app.test_client() as test_client:
        response = test_client.post('/roles',
                            data = json.dumps({
                                "Job_ID": 4,
                                "Job_Role": "Sales Manager",
                                "Job_Title": "Manager",
                                "Department": "Sales",
                                "Skills": ["S001", "S002"]
                            }),
                            headers = {
                                "Content-Type": "application/json"
                            }
                        )

        assert response.status_code == 200
        assert response.get_json()['error'] == False

        get_role = test_client.get(f"/roles/4")
        data = get_role.get_json()
        assert data['data'][0]['Job_Role'] == "Sales Manager"
        assert data["data"][0]["Job_Title"] == "Manager"
        assert data["data"][0]["Department"] == "Sales"
        assert len(data["data"][0]["Skills"]) == 2

# @pytest.mark.run(order=2)
def test_duplicate_create_role():
    with app.test_client() as test_client:
        response = test_client.post('/roles',
                            data = json.dumps({
                                "Job_ID": 4,
                                "Job_Role": "Sales Manager",
                                "Job_Title": "Manager",
                                "Department": "Sales",
                                "Skills": ["S001", "S002"]
                            }),
                            headers = {
                                "Content-Type": "application/json"
                            }
                        )
        assert response.status_code == 409
        assert response.get_json()['error'] == "An error occurred while creating job role: Duplicate entry job role already exists."


def test_get_all_roles():
    with app.test_client() as test_client:
        response = test_client.get('/roles')
        assert response.status_code == 200
        all_roles = response.get_json()['data']
        assert len(all_roles) > 0


def test_get_single_role():
    with app.test_client() as test_client:
        response = test_client.get(f"/roles/1")
        assert response.status_code == 200
        assert len(response.get_json()['data']) > 0

def test_get_single_role_not_found():
    with app.test_client() as test_client:
        response = test_client.get(f"/roles/99")
        assert response.status_code == 200
        assert len(response.get_json()['data']) == 0

def test_update_role():
    with app.test_client() as test_client:
        response = test_client.put('/roles',
                            data = json.dumps({
                                "Job_ID": 4,
                                "Job_Role": "HR Staff",
                                "Job_Title": "Staff",
                                "Department": "HR",
                                "Skills": ["S003"]
                            }),
                            headers = {
                                "Content-Type": "application/json"
                            }
                        )
        assert response.status_code == 200
        assert response.get_json()['error'] == False

        get_role = test_client.get(f"/roles/4")
        data = get_role.get_json()
        assert data["data"][0]["Job_Role"] == "HR Staff"
        assert data["data"][0]["Job_Title"] == "Staff"
        assert data["data"][0]["Department"] == "HR"
        assert len(data["data"][0]["Skills"]) == 1

def test_update_role_not_found():
    with app.test_client() as test_client:
        response = test_client.put('/roles',
                            data = json.dumps({
                                "Job_ID": 99,
                                "Job_Role": "Sales Manager",
                                "Job_Title": "Manager",
                                "Department": "Sales",
                                "Skills": ["S001", "S002"]
                            }),
                            headers = {
                                "Content-Type": "application/json"
                            }
                        )
        assert response.status_code == 406
        assert response.get_json()['error'] == "Job role not found."
        
def test_duplicate_update_role():
    with app.test_client() as test_client:
        testDuplicateRole = test_client.post('/roles',
            data = json.dumps({
                "Job_ID": 5,
                "Job_Role": "Sales Manager",
                "Job_Title": "Manager",
                "Department": "Sales",
                "Skills": ["S001", "S002"]
            }),
            headers = {
                "Content-Type": "application/json"
            }
        )

        assert testDuplicateRole.status_code == 200
        assert testDuplicateRole.get_json()['error'] == False
                        
        response = test_client.put('/roles',
            data = json.dumps({
                "Job_ID": 5,
                "Job_Role": "HR Staff",
                "Job_Title": "Staff",
                "Department": "HR",
                "Skills": ["S003"]
            }),
            headers = {
                "Content-Type": "application/json"
            }
        )
        assert response.status_code == 409
        assert response.get_json()['error'] == "An error occurred while updating job role: Duplicate entry job role already exists."

def test_delete_role():
    with app.test_client() as test_client:
        response = test_client.delete(f"/roles/4")
        response2 = test_client.delete(f"/roles/5")
        assert response.status_code == 200
        assert response.get_json()['error'] == False
        assert response2.status_code == 200
        assert response2.get_json()['error'] == False
