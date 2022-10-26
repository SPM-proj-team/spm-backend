from app import app,db
from flask import jsonify


class Course(db.Model):
    __tablename__ = 'Course'
    Course_ID = db.Column(db.String, primary_key=True)
    Course_Name = db.Column(db.String)
    Course_Desc = db.Column(db.String)
    Course_Type = db.Column(db.String)
    Course_Status = db.Column(db.String)
    Course_Category = db.Column(db.String)
    Registrations = db.relationship('Registration', backref='Course')
    # Registrations = db.relationship('Registration', backref='Course', lazy='dynamic',
    #                     primaryjoin="Course.Course_ID == Registration.Course_ID")

    def json(self):
        return {
            "Course_ID": self.Course_ID,
            "Course_Name": self.Course_Name,
            "Course_Desc": self.Course_Desc,
            "Course_Type": self.Course_Type,
            "Course_Status": self.Course_Status,
            "Course_Category": self.Course_Category,
        }
    def jsonWithSkill(self):
        return {
            "Course_ID": self.Course_ID,
            "Course_Name": self.Course_Name,
            "Course_Desc": self.Course_Desc,
            "Course_Type": self.Course_Type,
            "Course_Status": self.Course_Status,
            "Course_Category": self.Course_Category,
            "Skills": [skill.json() for skill in self.Skills]
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
               "data": [course.jsonWithSkill() for course in courseList],
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

