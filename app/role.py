from app import app
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

db = SQLAlchemy(app)

class Job_Role(db.Model):
    __tablename__ = 'Job_Role'
    Job_ID = db.Column(db.Integer, primary_key=True)
    Job_Role = db.Column(db.String)
    Job_Title = db.Column(db.String)

    def __init__(self, name):
        self.name = name
   

    def json(self):
        return {
            "Job_ID": self.Job_ID,
            "Job_Role": self.Job_Role,
            "Job_Title":self.Job_Title,

        }
        
# Association Table


@app.route("/role/test")
def testRole():
    return "role route is working"

@app.route("/roles")
def getRole():
    roleList = Job_Role.query.all()
    if len(roleList):
        return jsonify(
           {
               "code": 200,
               "error": False,
               "data": [role.json() for role in roleList]
           }
       )
    return jsonify(
        {
            "code": 200,
            "error": False,
            "data": "There are no roles."
        }
    ), 200

