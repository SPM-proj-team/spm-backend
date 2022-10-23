from app import app,db
# from app.skill import Skill
from flask import jsonify, request


class Course(db.Model):
    __tablename__ = 'Course'
    
    Course_ID = db.Column(db.String, primary_key=True)
    Course_Name = db.Column(db.String)
    Course_Desc = db.Column(db.String)
    Course_Type = db.Column(db.String)
    Course_Status = db.Column(db.String)
    Course_Category = db.Column(db.String)

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


@app.route("/courses", methods=["PUT"])
def updateSkillsMappedToCourse():
    """
    Sample Request 
    {
        "Course_ID": "COR001",
        "Skills": ["S003"]
    }
    """
    data = request.get_json()
    try:
        courseID = data["Course_ID"]
        course = Course.query.filter_by(Course_ID = courseID).first()
        if not course:
            return jsonify(
                {
                    "code": 406,
                    "error": True,
                    "message": f"An error occurred while mapping skills to course: Course ID {courseID} not found",
                    "data": data
                }
            ), 406
        
        skills = db.session.query(Skill).filter(Skill.Skill_ID.in_(data["Skills"])).all()
        course.Skills = [skill for skill in skills]
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "error": False,
                "data": course.jsonWithSkill()
            }
        ), 200
    except Exception as e:
        db.session.rollback()
        return jsonify(
            {
                "code": 406,
                "error": True,
                "message": f"An error occurred while mapping skills to course: {e}",
                "data": data
            }
        ), 406
