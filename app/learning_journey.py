from app import app, db
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, request

# Learning Journey Association Table
Learning_Journey_has_Course = db.Table('Learning_Journey_has_Course',
                                db.Column('Course_ID', db.String, db.ForeignKey('Course.Course_ID')),
                                db.Column('Learning_Journey_ID', db.Integer, db.ForeignKey('Learning_Journey.Learning_Journey_ID'))
                                )
# 
# Learning Journey Class 
# 
class LearningJourney(db.Model):
    __tablename__ = 'Learning_Journey'
    Learning_Journey_ID = db.Column(db.Integer, primary_key=True)
    Learning_Journey_Name = db.Column(db.String)
    Staff_ID = db.Column(db.Integer)
    Description = db.Column(db.String)
    Courses = db.relationship('Course', secondary= Learning_Journey_has_Course)

    def __init__(self, Learning_Journey_Name, Staff_ID, Description):
        self.Learning_Journey_Name = Learning_Journey_Name
        self.Staff_ID = Staff_ID
        self.Description = Description

    def json(self):
        return {
            "Learning_Journey_ID": self.Learning_Journey_ID,
            "Learning_Journey_Name": self.Learning_Journey_Name,
            "Staff_ID": self.Staff_ID,
            "Description": self.Description,
            "Courses": [course.json() for course in self.Courses]
        }

@app.route("/learning_journey/test")
def testLearningJourney():
    return "Learning Journey route is working! congrats"

@app.route("/learning_journey")
def getLearning_Journeys():
    learningJourneyList = LearningJourney.query.all()
    if len(learningJourneyList):
        return jsonify(
           {
               "code": 200,
               "data": [lj.json() for lj in learningJourneyList],
               "error": False
           }
       )
    return jsonify(
        {
            "code": 200,
            "message": "There are no Learning Journeys.",
            "error": True
        }
    ), 200

@app.route("/learning_journey/<int:Learning_Journey_ID>")
def getCourses_by_LearningJourney(Learning_Journey_ID):
    Staff_ID = request.json['Staff_ID']
    print(Staff_ID)
    selectedLJ = LearningJourney.query.filter_by(Learning_Journey_ID = Learning_Journey_ID,Staff_ID = Staff_ID).all()
    if len(selectedLJ):
        return jsonify(
           {
               "code": 200,
               "data": [lj.json() for lj in selectedLJ],
               "error": False
           }
       )
    return jsonify(
        {
            "code": 200,
            "data": [],
            "message": "There are no Learning Journeys.",
            "error": False
        }
    ), 200
