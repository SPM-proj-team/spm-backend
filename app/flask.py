from app import db

# Association Tables
Learning_Journey_has_Course = db.Table('Learning_Journey_has_Course',
                                db.Column('Course_ID', db.String, db.ForeignKey('Course.Course_ID')),
                                db.Column('Learning_Journey_ID', db.Integer, db.ForeignKey('Learning_Journey.Learning_Journey_ID'))
                                )

Role_has_Skill = db.Table('Role_has_Skill',
                    db.Column('Job_ID', db.Integer, db.ForeignKey('Job_Role.Job_ID')),
                    db.Column('Skill_ID', db.Integer, db.ForeignKey('Skill.Skill_ID'))
                    )

Course_has_Skill = db.Table('Course_has_Skill',
                    db.Column('Course_ID', db.Integer, db.ForeignKey('Course.Course_ID')),
                    db.Column('Skill_id', db.Integer, db.ForeignKey('Skill.Skill_ID'))
                    )

User_has_Skill = db.Table('User_has_Skill',
                    db.Column('Skill_ID', db.Integer, db.ForeignKey('Skill.Skill_ID')),
                    db.Column('Staff_ID', db.Integer, db.ForeignKey('Staff.Staff_ID'))
                )

# Classes
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

class LearningJourney(db.Model):
    __tablename__ = 'Learning_Journey'
    Learning_Journey_ID = db.Column(db.Integer, primary_key=True)
    Learning_Journey_Name = db.Column(db.String)
    Staff_ID = db.Column(db.Integer)
    Description = db.Column(db.String)
    Courses = db.relationship('Course', secondary= Learning_Journey_has_Course)
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

class Job_Role(db.Model):
    __tablename__ = 'Job_Role'
    Job_ID = db.Column(db.Integer, primary_key=True)
    Job_Role = db.Column(db.String)
    Job_Title = db.Column(db.String)
    Department = db.Column(db.String)
    Description = db.Column(db.String)
    Skills = db.relationship('Skill', secondary=Role_has_Skill, backref='Roles')
    Learning_Journeys = db.relationship('LearningJourney', backref='Job_Role')

    def json(self):
        return {
            "Job_ID": self.Job_ID,
            "Job_Role": self.Job_Role,
            "Job_Title": self.Job_Title,
            "Department": self.Department,
            "Description": self.Description
        }
    def jsonWithSkills(self):
        return {
            "Job_ID": self.Job_ID,
            "Job_Role": self.Job_Role,
            "Job_Title":self.Job_Title,
            "Department":self.Department,
            "Description": self.Description,
            "Skills": [skill.json() for skill in self.Skills]
        }
    def jsonWithSkillsCourses(self):
        return {
            "Job_ID": self.Job_ID,
            "Job_Role": self.Job_Role,
            "Job_Title":self.Job_Title,
            "Department":self.Department,
            "Description": self.Description,
            "Skills": [skill.jsonWithCourse() for skill in self.Skills]
        }
   
class Skill(db.Model):
    __tablename__ = 'Skill'
    Skill_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String)
    Courses = db.relationship('Course', secondary=Course_has_Skill, backref='Skills')
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

class Staff(db.Model):
    __tablename__ = 'Staff'
    Staff_ID = db.Column(db.Integer, primary_key=True)
    Staff_FName = db.Column(db.String)
    Staff_LName = db.Column(db.String)
    Dept = db.Column(db.String)
    Email = db.Column(db.String)
    # Role_ID = db.Column(db.Integer, db.ForeignKey('Access_Role.Role_ID'))
