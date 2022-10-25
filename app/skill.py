from app.course import Course
from app.flask import Skill, Staff
from app import app,db
from flask import jsonify, request

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

@app.route("/allskills")
def getAllSkills():
    skillList = Skill.query.all()
    if len(skillList):
        return jsonify(
           {
               "code": 200,
               "data": [skill.json() for skill in skillList],
               "error" : False
           }
       ), 200
    return jsonify(
        {
            "code": 200,
            "data": [],
            "message": "There are no skills.",
            "error" : False
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
               "error" : False
           }
       ), 200
    return jsonify(
        {
            "code": 200,
            "data": [],
            "message": "There are no skills.",
            "error" : False
        }
    ), 200

# Consider removing this

# @app.route("/skills", methods=["POST"])
# def getSkillByID():
    data = request.get_json()
    skillList = Skill.query.filter_by(Skill_ID=data["Skill_ID"]).all()
    if len(skillList):
        return jsonify(
           {
               "code": 200,
               "data": [skill.jsonWithCourse() for skill in skillList],
               "error" : False
           }
       ), 200
    return jsonify(
        {
            "code": 200,
            "data": [],
            "message": "There are no skills.",
            "error" : False
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