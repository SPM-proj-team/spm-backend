# from app.skill import Skill
# Skill = Skill
from app.skill import Skill
from app import app,db
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
# db = SQLAlchemy(app)


# Association Table
Role_has_Skill = db.Table('Role_has_Skill',
                    db.Column('Job_ID', db.Integer, db.ForeignKey('Job_Role.Job_ID')),
                    db.Column('Skill_ID', db.Integer, db.ForeignKey('Skill.Skill_ID'))
                    )



class Job_Role(db.Model):
    __tablename__ = 'Job_Role'
    Job_ID = db.Column(db.Integer, primary_key=True)
    Job_Role = db.Column(db.String)
    Job_Title = db.Column(db.String)
    Skills = db.relationship('Skill', secondary=Role_has_Skill)

    def __init__(self, name):
        self.name = name
   

    def json(self):
        print(type(self.Skills))
        return {
            "Job_ID": self.Job_ID,
            "Job_Role": self.Job_Role,
            "Job_Title":self.Job_Title,
            "Skills": [skill.json() for skill in self.Skills]
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
               "data": [role.json() for role in roleList]
           }
       )
    return jsonify(
        {
            "code": 200,
            "error": False,
            "data": "There are no roles."
        }
    ), 200

