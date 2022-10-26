from app import app, db
from flask import jsonify


class Access_Role(db.Model):
    __tablename__ = 'Access_Role'
    Role_ID = db.Column(db.Integer, primary_key=True)
    Role_Name = db.Column(db.String)
    Staff = db.relationship('Staff', backref='Access_Role')

    def json(self):
        return {
            "Role_ID": self.Role_ID,
            "Role_Name": self.Role_Name
        }


@app.route("/accessrole/test")
def testAccess_Role():
    return "accessrole route is working"


@app.route("/accessrole")
def getAccess_Role():
    acList = Access_Role.query.all()
    if len(acList):
        return jsonify(
            {
                "code": 200,
                "data": [ac.json() for ac in acList],
                "error": False
            }
        )
    return jsonify(
        {
            "code": 200,
            "data": [],
            "message": "There are no Access Role.",
            "error": False
        }
    ), 200
