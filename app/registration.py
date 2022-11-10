from app import app, db
from flask import jsonify, request


class Registration(db.Model):
    __tablename__ = 'Registration'
    Reg_ID = db.Column(db.String, primary_key=True)
    Course_ID = db.Column(db.String, db.ForeignKey('Course.Course_ID'))
    Staff_ID = db.Column(db.Integer, db.ForeignKey('Staff.Staff_ID'))
    Reg_Status = db.Column(db.String)
    Completion_Status = db.Column(db.String)
    

    def json(self):
        return {
            "Reg_ID": self.Reg_ID,
            # "Course_ID": self.Course_ID,
            "Staff": self.Staff.json(),
            "Reg_Status": self.Reg_Status,
            "Completion_Status": self.Completion_Status,
            "Course": self.Course.jsonWithSkill(),
        }


@app.route("/registration/test")
def testRegistration():
    return "Registration route is working"


@app.route("/registration")
def getRegistration():
    regList = Registration.query.all()
    if len(regList):
        return jsonify(
            {
                "code": 200,
                "data": [reg.json() for reg in regList],
                "error": False
            }
        )
    return jsonify(
        {
            "code": 200,
            "data": [],
            "message": "There are no Registrations",
            "error": False
        }
    ), 200


@app.route("/registration", methods=["POST"])
def getRegistrationbyStaffID():
    Staff_ID = int(request.json['Staff_ID'])
    regList = Registration.query.filter_by(Staff_ID=Staff_ID).all()
    if len(regList):
        return jsonify(
            {
                "code": 200,
                "data": [reg.json() for reg in regList],
                "error": False
            }
        ), 200
    return jsonify(
        {
            "code": 200,
            "message": "There are no Registrations",
            "error": False
        }
    ), 200

