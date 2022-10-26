from app import app, db
from flask import jsonify, request


Course_has_Skill = db.Table(
    'Course_has_Skill', db.Column(
        'Course_ID', db.Integer, db.ForeignKey('Course.Course_ID')), db.Column(
            'Skill_id', db.Integer, db.ForeignKey('Skill.Skill_ID')))

User_has_Skill = db.Table(
    'User_has_Skill', db.Column(
        'Skill_ID', db.Integer, db.ForeignKey('Skill.Skill_ID')), db.Column(
            'Staff_ID', db.Integer, db.ForeignKey('Staff.Staff_ID')))


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
    # primaryjoin="Course.Course_ID == Registration.Course_ID")

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


class Skill(db.Model):
    __tablename__ = 'Skill'
    Skill_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String)
    Courses = db.relationship(
        'Course',
        secondary=Course_has_Skill,
        backref='Skills')
    Users = db.relationship('Staff', secondary=User_has_Skill)

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


# Skills API
@app.route("/skill/test")
def testSkill():
    return "Skill route is working"


@app.route("/allskills")
def getAllSkills():
    skillList = Skill.query.all()
    if len(skillList):
        return jsonify(
            {
                "code": 200,
                "data": [skill.json() for skill in skillList],
                "error": False
            }
        ), 200
    return jsonify(
        {
            "code": 200,
            "data": [],
            "message": "There are no skills.",
            "error": False
        }
    ), 200


@app.route("/skills")
def getSkill():
    skillList = Skill.query.all()
    if len(skillList):
        return jsonify(
            {
                "code": 200,
                "data": [skill.jsonWithCourse() for skill in skillList],
                "error": False
            }
        ), 200
    return jsonify(
        {
            "code": 200,
            "data": [],
            "message": "There are no skills.",
            "error": False
        }
    ), 200


@app.route("/skills", methods=["POST"])
def createSkill():
    """
    Sample Request
    {
        "Skill_ID": "S099",
        "Name": "Solidity",
        "Courses": ["FIN001", "FIN002"]
    }
    """
    data = request.get_json()
    try:
        skillNameExists = Skill.query.filter_by(Name=data["Name"]).first()
        if skillNameExists:
            return jsonify(
                {
                    "code": 409,
                    "error": True,
                    "message": "An error occurred while creating skill: Duplicate entry skill name already exists",
                    "data": skillNameExists.jsonWithCourse()
                }
            ), 409
        skill = Skill()
        courses = Course.query.filter(Course.Course_ID.in_(data["Courses"]))
        skill.Skill_ID = data["Skill_ID"]
        skill.Name = data["Name"]
        skill.Courses = [course for course in courses]
        db.session.add(skill)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "error": False,
                "data": skill.jsonWithCourse()
            }
        ), 200
    except Exception as e:
        db.session.rollback()
        return jsonify(
            {
                "code": 406,
                "error": True,
                "message": f"An error occurred while creating skill: {e}",
                "data": data
            }
        ), 406


@app.route("/skills", methods=["PUT"])
def updateSkill():
    """
    Sample Request
    {
        "Skill_ID": "S099",
        "Name": "Ethereum",
        "Courses": ["FIN001"]
    }
    """
    data = request.get_json()
    skill_id = data["Skill_ID"]
    name = data["Name"]
    try:
        skill = Skill.query.filter_by(Skill_ID=skill_id).first()
        if not skill:
            return jsonify(
                {
                    "code": 406,
                    "error": True,
                    "message": f"An error occurred while updating skill: Skill ID {skill_id} does not exist",
                    "data": []
                }
            ), 406
        skillNameExists = Skill.query.filter_by(Name=name).first()
        if skillNameExists and skillNameExists.json()["Skill_ID"] != skill_id:
            return jsonify(
                {
                    "code": 409,
                    "error": True,
                    "message": "An error occurred while updating skill: Duplicate skill name already exists",
                    "data": skillNameExists.jsonWithCourse()
                }
            ), 409
        courses = Course.query.filter(Course.Course_ID.in_(data["Courses"]))
        skill.Name = name
        skill.Courses = [course for course in courses]
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "error": False,
                "data": skill.jsonWithCourse()
            }
        ), 200
    except Exception as e:
        db.session.rollback()
        return jsonify(
            {
                "code": 406,
                "error": True,
                "message": f"An error occurred while updating skill: {e}",
                "data": data
            }
        ), 406


@app.route("/skills", methods=["DELETE"])
def deleteSkill():
    try:
        Skill_ID = request.json['Skill_ID']
        skill = Skill.query.filter_by(Skill_ID=Skill_ID).first()
        if not skill:
            return jsonify(
                {
                    "code": 406,
                    "error": True,
                    "message": f"An error occurred while deleting skill: Skill ID {Skill_ID} not found",
                    "data": []
                }
            ), 406
        skill.Roles = []
        skill.Courses = []
        skill.Users = []
        db.session.commit()
        db.session.delete(skill)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "error": False,
                "message": f"Skill ID: {Skill_ID} has been deleted",
            }
        ), 200
    except Exception as e:
        db.session.rollback()
        return jsonify(
            {
                "code": 406,
                "error": True,
                "message": f"An error occurred while deleting skill: {e}",
                "data": {"Skill_ID": Skill_ID}
            }
        ), 406


# Course API
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
                "error": False
            }
        )
    return jsonify(
        {
            "code": 200,
            "data": [],
            "message": "There are no course.",
            "error": False
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
        course = Course.query.filter_by(Course_ID=courseID).first()
        if not course:
            return jsonify(
                {
                    "code": 406,
                    "error": True,
                    "message": f"An error occurred while mapping skills to course: Course ID {courseID} not found",
                    "data": data
                }
            ), 406

        skills = db.session.query(Skill).filter(
            Skill.Skill_ID.in_(data["Skills"])).all()
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
