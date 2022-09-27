from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Ilovespring!@localhost:3306/skills'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Skills(db.Model):
    __tablename__ = 'skills'
 
    skillID = db.Column(db.String(13), primary_key=True)
    skillName = db.Column(db.String(64), primary_key=True, nullable=False)
 
    def __init__(self, skillID, skillName):
        self.skillID = skillID
        self.skillName = skillName
 
    def json(self):
        return {"skillID": self.skillID, "skillName": self.skillName}

@app.route("/skills")
def get_all():
    allSkills = Skills.query.all()
    if len(allSkills):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "allSkills": [skill.json() for skill in allSkills] 
                    # a list of objects (avail) is returned
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no skills."
        }
    ), 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)