from app.course import Course
from app import app,db
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

# db = SQLAlchemy(app)
Course_has_Skill = db.Table('Course_has_Skill',
                    db.Column('Course_ID', db.Integer, db.ForeignKey('Course.Course_ID')),
                    db.Column('Skill_id', db.Integer, db.ForeignKey('Skill.Skill_ID'))
                    )

class Skill(db.Model):
    __tablename__ = 'Skill'
    Skill_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String)
    Courses = db.relationship('Course', secondary=Course_has_Skill)

    def __init__(self, Skill_ID, Name):
        self.Skill_ID = Skill_ID
        self.Name = Name

    def json(self):
        return {
            "Skill_ID": self.Skill_ID,
            "Name": self.Name
        }
    def jsonWithCourse(self):
        return {
            "Skill_ID": self.Skill_ID,
            "Name": self.Name,
            "Courses": [course.json() for course in self.Courses]
        }
    

@app.route("/skill/test")
def testSkill():
    return "Skill route is working"


# Consider removing this

# @app.route("/skills")
# def getSkill():
#     skillList = Skill.query.all()
#     if len(skillList):
#         return jsonify(
#            {
#                "code": 200,
#                "data": [skill.json() for skill in skillList],
#                "error" : False
#            }
#        )
#     return jsonify(
#         {
#             "code": 200,
#             "data": [],
#             "message": "There are no skills.",
#             "error" : False
#         }
#     ), 200

@app.route("/skills")
def getSkill():
    skillList = Skill.query.all()
    if len(skillList):
        return jsonify(
           {
               "code": 200,
               "data": [skill.jsonWithCourse() for skill in skillList],
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
