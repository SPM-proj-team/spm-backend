from app import app
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

db = SQLAlchemy(app)
# 
# Courses Class 
# 
class Courses(db.Model):
    __tablename__ = 'Courses'
    Course_ID = db.Column(db.String, primary_key=True)
    Course_Name = db.Column(db.String)
    Course_Desc = db.Column(db.String)
    Course_Status = db.Column(db.String)
    Course_Type = db.Column(db.String)
    Course_Category = db.Column(db.String)


    def __init__(self, Course_ID, Course_Name, Course_Desc, Course_Status, Course_Type, Course_Category):
        self.Course_ID = Course_ID
        self.Course_Name = Course_Name
        self.Course_Desc = Course_Desc
        self.Course_Status = Course_Status
        self.Course_Type = Course_Type
        self.Course_Category = Course_Category

    def json(self):
        return {
            "Course_ID": self.Course_ID,
            "Course_Name": self.Course_Name,
            "Course_Desc": self.Course_Desc,
            "Course_Status": self.Course_Status,
            "Course_Type": self.Course_Type,
            "Course_Category": self.Course_Category
        }

@app.route("/courses")
def getAllCourses():
    CoursesList = Courses.query.all()
    if len(CoursesList):
        return jsonify(
           {
               "code": 200,
               "data": [course.json() for course in CoursesList],
               "error": False
           }
       )
    return jsonify(
        {
            "code": 200,
            "message": "There are no Courses.",
            "error": True
        }
    ), 200