from app import app
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

db = SQLAlchemy(app)

class Skill(db.Model):
    __tablename__ = 'Skill'
    Skill_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String)

    def __init__(self, Skill_ID, Name):
        self.Skill_ID = Skill_ID
        self.Name = Name

    def json(self):
        return {
            "skill_id": self.skill_id,
            "name": self.name
        }

@app.route("/skill/test")
def testSkill():
    return "Skill route is working"

@app.route("/skill")
def getSkill():
    skillList = Skill.query.all()
    if len(skillList):
        return jsonify(
           {
               "code": 200,
               "data": [skill.json() for skill in skillList]
           }
       )
    return jsonify(
        {
            "code": 200,
            "message": "There are no skills."
        }
    ), 200

