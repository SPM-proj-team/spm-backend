from app import app
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = 'Role'
    Role_ID = db.Column(db.Integer, primary_key=True)
    Role_Name = db.Column(db.String)
    def __init__(self, name):
        self.name = name
   

    def json(self):
        return {
            "role_id": self.role_id,
            "name": self.name
        }


@app.route("/role/test")
def testRole():
    return "role route is working"

@app.route("/role")
def getRole():
    roleList = Role.query.all()
    if len(roleList):
        return jsonify(
           {
               "code": 200,
               "data": [role.json() for role in roleList]
           }
       )
    return jsonify(
        {
            "code": 200,
            "message": "There are no roles."
        }
    ), 200

