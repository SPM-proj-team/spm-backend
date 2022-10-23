from app import db

class Staff(db.Model):
    __tablename__ = 'Staff'
    Staff_ID = db.Column(db.Integer, primary_key=True)
    Staff_FName = db.Column(db.String)
    Staff_LName = db.Column(db.String)
    Dept = db.Column(db.String)
    Email = db.Column(db.String)
    # Role_ID = db.Column(db.Integer, db.ForeignKey('Access_Role.Role_ID'))