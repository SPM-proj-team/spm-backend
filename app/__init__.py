from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from os import environ
from dotenv import load_dotenv

load_dotenv()

user = environ.get('user') or "placeholderuser"
password = environ.get('password') or "placeholderpassword"

DB_HOSTNAME = environ.get('DB_HOSTNAME')
DB_USERNAME = environ.get('DB_USERNAME')
DB_PASSWORD = environ.get('DB_PASSWORD')
DB_NAME = environ.get('DB_NAME')

app = Flask(__name__)

CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://" + \
    DB_USERNAME + ":" + DB_PASSWORD + "@" + DB_HOSTNAME + ":3306/" + DB_NAME
# print
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}
db = SQLAlchemy(app)

from .staff import Staff
from .role import Job_Role
from .course_skill import Course, Skill
from .access_role import Access_Role
from .learning_journey import LearningJourney
from .registration import Registration
