from app import app,db
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify


class Course(db.Model):
    __tablename__ = 'Course'
    
    Course_ID = db.Column(db.String, primary_key=True)
    Course_Name = db.Column(db.String)
    Course_Desc = db.Column(db.String)
    Course_Type = db.Column(db.String)
    Course_Status = db.Column(db.String)
    Course_Category = db.Column(db.String)

    def __init__(self, Course_ID, Course_Name,Course_Desc,Course_Type,Course_Status,Course_Category):
        self. Course_ID = Course_ID
        self.Course_Name = Course_Name
        self.Course_Desc = Course_Desc
        self.Course_Type = Course_Type
        self.Course_Status = Course_Status
        self.Course_Category = Course_Category

    def json(self):
        return {
            "Course_ID": self.Course_ID,
            "Course_Name": self.Course_Name,
            "Course_Desc": self.Course_Desc,
            "Course_Type": self.Course_Type,
            "Course_Status": self.Course_Status,
            "Course_Category": self.Course_Category,
        }

@app.route("/course/test")
def testCourse():
    return "Course route is working"

@app.route("/courses")
def getCourse():
    courseList = Course.query.all()
    if len(courseList):
        return jsonify(
           {
               "code": 200,
               "data": [course.json() for course in courseList],
               "error" : False
           }
       )
    return jsonify(
        {
            "code": 200,
            "data": [],
            "message": "There are no course.",
            "error" : False
        }
    ), 200

