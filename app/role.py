from crypt import methods
import json

from app.learning_journey import LearningJourney
from app.skill import Skill
from app import app,db
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, request

# Association Table
Role_has_Skill = db.Table('Role_has_Skill',
                    db.Column('Job_ID', db.Integer, db.ForeignKey('Job_Role.Job_ID')),
                    db.Column('Skill_ID', db.Integer, db.ForeignKey('Skill.Skill_ID'))
                    )


class Job_Role(db.Model):
    __tablename__ = 'Job_Role'
    Job_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Job_Role = db.Column(db.String)
    Job_Title = db.Column(db.String)
    Department = db.Column(db.String)
    Description = db.Column(db.String)
    Skills = db.relationship('Skill', secondary=Role_has_Skill)
    Learning_Journeys = db.relationship('LearningJourney', backref='Job_Role')

    def json(self):
        return {
            "Job_ID": self.Job_ID,
            "Job_Role": self.Job_Role,
            "Job_Title": self.Job_Title,
            "Department": self.Department,
            "Description": self.Description
        }
    def jsonWithSkills(self):
        return {
            "Job_ID": self.Job_ID,
            "Job_Role": self.Job_Role,
            "Job_Title":self.Job_Title,
            "Department":self.Department,
            "Description": self.Description,
            "Skills": [skill.json() for skill in self.Skills]
        }
    def jsonWithSkillsCourses(self):
        return {
            "Job_ID": self.Job_ID,
            "Job_Role": self.Job_Role,
            "Job_Title":self.Job_Title,
            "Department":self.Department,
            "Description": self.Description,
            "Skills": [skill.jsonWithCourse() for skill in self.Skills]
        }
        

@app.route("/role/test")
def testRole():
    return "role route is working"

@app.route("/roles")
def getRole():
    roleList = Job_Role.query.all()
    if len(roleList):
        return jsonify(
           {
               "code": 200,
               "error": False,
               "data": [role.jsonWithSkills() for role in roleList]
           }
       )
    return jsonify(
        {
            "code": 200,
            "error": False,
            "data": []
        }
    ), 200

@app.route("/roles/<int:id>")
def getRoleByID(id : int):
    
    roleList = Job_Role.query.filter_by(Job_ID = id).all()
    if len(roleList):
        return jsonify(
           {
               "code": 200,
               "error": False,
               "data": [role.jsonWithSkillsCourses() for role in roleList]
           }
       )
    return jsonify(
        {
            "code": 200,
            "error": False,
            "data": []
        }
    ), 200

@app.route("/roles", methods=["POST"])
def createRole():
    """
    Sample Request 
    {
        "Job_Role": "Sales Manager",
        "Job_Title": "Manager",
        "Department": "Sales",
        "Description": "Lorem ipsum",
        "Skills": ["S001", "S002"]
    }
    """
    data = request.get_json()
    try:
        roleExists = Job_Role.query.filter_by(Job_Role=data["Job_Role"]).first()
        if roleExists:
            return jsonify(
                {
                    "code": 409,
                    "error": "An error occurred while creating job role: Duplicate entry job role already exists.",
                    "data": roleExists.jsonWithSkillsCourses()
                }
            ), 409
        
        jobRoleData = {
            "Job_Role": data["Job_Role"],
            "Job_Title": data["Job_Title"],
            "Department": data["Department"],
            "Description": data["Description"]
        }
        jobRole = Job_Role(**jobRoleData)
        db.session.add(jobRole)
        db.session.commit()

        skills = db.session.query(Skill).filter(Skill.Skill_ID.in_(data["Skills"])).all()
        jobRole.Skills = [skill for skill in skills]
        db.session.commit()
        
        return jsonify(
            {
                "code": 200,
                "error": False,
                "data": jobRole.jsonWithSkillsCourses()
            }
        ), 200
    except Exception as e:
        db.session.rollback()
        return jsonify(
            {
                "code": 406,
                "error": f"An error occurred while creating job role: {e}",
                "data": data
            }
        ), 406

@app.route("/roles", methods=["PUT"])
def updateRole():
    """
    Sample Request 
    {
        "Job_ID": 4,
        "Job_Role": "HR Staff",
        "Job_Title": "Staff",
        "Department": "HR",
        "Description": "Lorem ipsum",
        "Skills": ["S003"]
    }
    """
    data = request.get_json()
    try:
        jobID = data["Job_ID"]
        jobRole = Job_Role.query.filter_by(Job_ID = jobID).first()
        if not jobRole:
            return jsonify(
                {
                    "code": 406,
                    "error": "An error occurred while updating job role: Job role not found.",
                    "data": data
                }
            ), 406
        
        roleExists = Job_Role.query.filter_by(Job_Role=data["Job_Role"]).first()
        if roleExists and roleExists.json()["Job_ID"] != jobID:
            return jsonify(
                {
                    "code": 409,
                    "error": "An error occurred while updating job role: Duplicate entry job role already exists.",
                    "data": roleExists.jsonWithSkillsCourses()
                }
            ), 409

        skills = db.session.query(Skill).filter(Skill.Skill_ID.in_(data["Skills"])).all()
        
        jobRole.Job_Role = data["Job_Role"]
        jobRole.Job_Title = data["Job_Title"]
        jobRole.Department = data["Department"]
        jobRole.Description = data["Description"]
        jobRole.Skills = [skill for skill in skills]
        db.session.commit()

        return jsonify(
            {
                "code": 200,
                "error": False,
                "data": jobRole.jsonWithSkillsCourses()
            }
        ), 200
    except Exception as e:
        db.session.rollback()
        return jsonify(
            {
                "code": 406,
                "error": f"An error occurred while updating job role: {e}",
                "data": data
            }
        ), 406

@app.route("/roles/<int:id>", methods=["DELETE"])
def deleteRole(id : int):
    try:
        jobRole = Job_Role.query.filter_by(Job_ID = id).first()
        if not jobRole:
            return jsonify(
                {
                    "code": 406,
                    "error": "An error occurred while deleting job role: Job role not found.",
                    "data": {"id": id}
                }
            ), 406

        # Check if associated learning joruneys, prevent deletion if associated LJs exists 
        learningJourneys = LearningJourney.query.filter_by(Job_Role_ID = id).all()
        if len(learningJourneys) > 0:
            return jsonify(
                {
                    "code": 406,
                    "error": f"An error occurred while deleting job role: Job role id {id} stll have learning journeys associated with it.",
                    "data": {
                        "id": id,
                        "associated_learning_journeys": [learningJourney.jsonWithCourseAndRole() for learningJourney in learningJourneys]
                    }
                }
            ), 406

        jobRole.Skills = []
        db.session.commit()

        db.session.delete(jobRole)
        db.session.commit()

        return jsonify(
            {
                "code": 200,
                "error": False,
                "data": jobRole.jsonWithSkillsCourses()
            }
        ), 200
    except Exception as e:
        db.session.rollback()
        return jsonify(
            {
                "code": 406,
                "error": f"An error occurred while deleting job role: {e}"
            }
        ), 406
