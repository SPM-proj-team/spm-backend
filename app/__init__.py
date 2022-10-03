from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from os import environ
from dotenv import load_dotenv

load_dotenv()

user = environ.get('user') or "placeholderuser" 
password = environ.get('password') or "placeholderpassword" 

app=Flask(__name__)

CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://"+user+":"+password+"@localhost:3306/spm_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}
db = SQLAlchemy(app)

from .role import Job_Role
from .skill import Skill
from .course import Course
from .learning_journey import LearningJourney
