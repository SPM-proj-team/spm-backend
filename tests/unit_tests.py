import unittest

from app import Job_Role, Course, Skill, LearningJourney, Registration, Staff, Access_Role


class TestJobRole(unittest.TestCase):
    def test_json(self):
        j1 = Job_Role(
            Job_Role='Operation staff', 
            Job_Title='Staff',
            Department='Operations',
            Description='A staff of operations'
        )
        self.assertEqual(j1.json(), {
            'Job_ID': None,
            'Job_Role': 'Operation staff',
            'Job_Title': 'Staff',
            'Department': 'Operations',
            'Description': 'A staff of operations'
        })

class TestCourse(unittest.TestCase):
    def test_json(self):
        c1 = Course(
            Course_ID='IS212',
            Course_Name='Software Project Management',
            Course_Desc='Equip student with knowledge about agile approach regarding software project development',
            Course_Type='Type_1',
            Course_Status='Open',
            Course_Category='Course_Category_1'
        )
        self.assertEqual(c1.json(), {
            'Course_ID': 'IS212',
            'Course_Name': 'Software Project Management',
            'Course_Desc': 'Equip student with knowledge about agile approach regarding software project development',
            'Course_Type': 'Type_1',
            'Course_Status': 'Open',
            'Course_Category': 'Course_Category_1'
        })

class TestSkill(unittest.TestCase):
    def test_json(self):
        s1 = Skill(
            Name='Jira',
        )
        self.assertEqual(s1.json(), {
            'Skill_ID': None,
            'Name': 'Jira'
        })

class TestLearningJourney(unittest.TestCase):
    def test_json(self):
        l1 = LearningJourney(
            Learning_Journey_Name='FirstLJ',
            Staff_ID=1,
            Description='My first journey'
        )
        self.assertEqual(l1.json(), {
            'Learning_Journey_ID': None,
            'Learning_Journey_Name': 'FirstLJ',
            'Staff_ID': 1,
            'Description': 'My first journey'
        })
 

class TestAccessRole(unittest.TestCase):
    def test_json(self):
        ar1 = Access_Role(
            Role_Name="testRole"
        )
        self.assertEqual(ar1.json(), {
            'Role_ID': None,
            'Role_Name': 'testRole'
        })


class TestStaff(unittest.TestCase):
    def test_json(self):
        s1 = Staff(
            Staff_FName = "FirstName",
            Staff_LName = "LastName",
            Dept = "Department",
            Email = "Email"
        )
        self.assertEqual(s1.json(), {
            'Staff_ID': None,
            'Staff_FName': 'FirstName',
            'Staff_LName': 'LastName',
            'Dept': 'Department',
            'Email': 'Email'
        })

if __name__ == "__main__":
    unittest.main()
