from app import app,db
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

# db = SQLAlchemy(app)

class Skill(db.Model):
    __tablename__ = 'Skill'
    Skill_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String)

    def __init__(self, Skill_ID, Name):
        self.Skill_ID = Skill_ID
        self.Name = Name

    def json(self):
        return {
            "Skill_id": self.Skill_ID,
            "name": self.Name
        }

@app.route("/skill/test")
def testSkill():
    return "Skill route is working"

@app.route("/skills")
def getSkill():
    skillList = Skill.query.all()
    if len(skillList):
        return jsonify(
           {
               "code": 200,
               "data": [skill.json() for skill in skillList],
               "error" : False
           }
       )
    return jsonify(
        {
            "code": 200,
            "data": [],
            "message": "There are no skills.",
            "error" : False
        }
    ), 200

