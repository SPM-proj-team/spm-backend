from app import app, db
from flask import jsonify, request
from app.course_skill import Course

Learning_Journey_has_Course = db.Table(
    'Learning_Journey_has_Course',
    db.Column(
        'Course_ID',
        db.String,
        db.ForeignKey('Course.Course_ID')),
    db.Column(
        'Learning_Journey_ID',
        db.Integer,
        db.ForeignKey('Learning_Journey.Learning_Journey_ID')))


class LearningJourney(db.Model):
    __tablename__ = 'Learning_Journey'
    Learning_Journey_ID = db.Column(db.Integer, primary_key=True)
    Learning_Journey_Name = db.Column(db.String)
    Staff_ID = db.Column(db.Integer)
    Description = db.Column(db.String)
    Courses = db.relationship('Course', secondary=Learning_Journey_has_Course)
    Job_Role_ID = db.Column(db.Integer, db.ForeignKey('Job_Role.Job_ID'))

    def json(self):
        return {
            "Learning_Journey_ID": self.Learning_Journey_ID,
            "Learning_Journey_Name": self.Learning_Journey_Name,
            "Staff_ID": self.Staff_ID,
            "Description": self.Description
        }

    def jsonWithCourseAndRole(self):
        return {
            "Learning_Journey_ID": self.Learning_Journey_ID,
            "Learning_Journey_Name": self.Learning_Journey_Name,
            "Staff_ID": self.Staff_ID,
            "Description": self.Description,
            "Courses": [course.json() for course in self.Courses],
            "Role": self.Job_Role.json()
        }


@app.route("/learning_journey/test")
def testLearningJourney():
    return "Learning Journey route is working! congrats"


@app.route("/learning_journey", methods=["POST"])
def getLearning_Journeys_byStaffID():
    Staff_ID = request.json['Staff_ID']
    learningJourneyList = LearningJourney.query.filter_by(
        Staff_ID=Staff_ID).all()
    if len(learningJourneyList):
        return jsonify({"code": 200, "data": [lj.jsonWithCourseAndRole(
        ) for lj in learningJourneyList], "error": False}), 200
    return jsonify(
        {
            "code": 200,
            "message": "There are no Learning Journeys.",
            "error": True
        }
    ), 200


@app.route("/learning_journey/<int:Learning_Journey_ID>", methods=["POST"])
def getCourses_by_one_LearningJourney(Learning_Journey_ID):
    Staff_ID = request.json['Staff_ID']
    selectedLJ = LearningJourney.query.filter_by(
        Learning_Journey_ID=Learning_Journey_ID,
        Staff_ID=Staff_ID).all()
    if len(selectedLJ):
        return jsonify(
            {
                "code": 200,
                "data": [lj.jsonWithCourseAndRole() for lj in selectedLJ],
                "error": False
            }
        ), 200
    return jsonify(
        {
            "code": 200,
            "data": [],
            "message": "There are no Learning Journeys.",
            "error": False
        }
    ), 200


@app.route("/learning_journey/create", methods=["POST"])
def createLearningJourney():
    try:
        courseID = []
        learningJourney = LearningJourney()
        data = request.json['Learning_Journey']
        learningJourneyExists = LearningJourney.query.filter_by(
            Learning_Journey_Name=data['Learning_Journey_Name'],
            Staff_ID=data['Staff_ID']).first()
        if learningJourneyExists:
            return jsonify(
                {
                    "code": 409,
                    "error": True,
                    "message": f"An error occurred while creating learning journey: Duplicate learning journey name already exists for staff id {data['Staff_ID']}",
                    "data": learningJourneyExists.jsonWithCourseAndRole()
                }
            ), 200
        for course in data['Courses']:
            courseID.append(course['Course_ID'])
        if len(courseID) == 0:
            return jsonify(
                {
                    "code": 404,
                    "data": [],
                    "error": True,
                    "message": "There should at least be 1 course in the Learning Journey"
                }
            ), 200
        courses = Course.query.filter(Course.Course_ID.in_(courseID))
        learningJourney.Learning_Journey_Name = data['Learning_Journey_Name']
        learningJourney.Staff_ID = data['Staff_ID']
        learningJourney.Description = data['Description']
        learningJourney.Courses = [course for course in courses]
        learningJourney.Job_Role_ID = data['Role']['Job_ID']
        db.session.add(learningJourney)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": [learningJourney.jsonWithCourseAndRole()],
                "error": False
            }
        ), 200
    except Exception as e:
        db.session.rollback()
        return jsonify(
            {
                "code": 406,
                "error": True,
                "message": f"An error occurred while creating learning journey: {e}",
                "data": data
            }
        ), 200


@app.route("/learning_journey/<int:Learning_Journey_ID>", methods=["PUT"])
def updateLearningJourney(Learning_Journey_ID):
    Staff_ID = request.json['Staff_ID']
    LJ = request.json['Learning_Journey']
    Learning_Journey_ID = LJ["Learning_Journey_ID"]
    selectedLJ = LearningJourney.query.filter_by(
        Learning_Journey_ID=Learning_Journey_ID,
        Staff_ID=Staff_ID).all()
    if len(selectedLJ):
        selectedLJ = selectedLJ[0]
        updatedCoursesID = []
        for course in LJ["Courses"]:
            updatedCoursesID.append(course["Course_ID"])
        if len(updatedCoursesID) == 0:
            return jsonify(
                {
                    "code": 404,
                    "data": [],
                    "error": True,
                    "message": "There should at least be 1 course in the Learning Journey"
                }
            ), 404
        courses = Course.query.filter(Course.Course_ID.in_(updatedCoursesID))
        selectedLJ.Description = LJ["Description"]
        selectedLJ.Learning_Journey_Name = LJ["Learning_Journey_Name"]
        selectedLJ.Role = LJ["Role"]
        selectedLJ.Courses = [course for course in courses]
        print(courses)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": [selectedLJ.jsonWithCourseAndRole()],
                "error": False
            }
        ), 200
    return jsonify(
        {
            "code": 200,
            "data": [],
            "message": "There are no Learning Journeys with the ID " + str(Learning_Journey_ID),
            "error": False
        }
    ), 200


@app.route("/learning_journey/<int:Learning_Journey_ID>", methods=["DELETE"])
def deleteLearningJourney(Learning_Journey_ID):
    try:
        Staff_ID = request.json['Staff_ID']
        LJ = LearningJourney.query.filter_by(
            Learning_Journey_ID=Learning_Journey_ID,
            Staff_ID=Staff_ID).first()
        if not LJ:
            return jsonify(
                {
                    "code": 406,
                    "data": [],
                    "message": "There is no Learning Journeys with ID: " + str(Learning_Journey_ID),
                    "error": True
                }
            ), 406

        LJ.Courses = []
        db.session.commit()
        db.session.delete(LJ)
        db.session.commit()
        return jsonify({"code": 200, "message": "Learning Journey ID: " + str(Learning_Journey_ID) + " has been deleted", "error": False}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify(
            {
                "code": 406,
                "error": True,
                "message": f"An error occurred while deleting learning journey: {e}",
                "data": {"id": id}
            }
        ), 406
