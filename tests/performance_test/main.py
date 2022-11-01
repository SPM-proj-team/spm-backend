import pandas as pd
import time 
import requests
import access_role_test
import staff_test
import skill_test
import course_test
import learning_journey_test

df = pd.DataFrame()
skills = []
staff = []
courses = []
learning_journey = []
access_role = []

# skills
skills.append(skill_test.skill())
skills.append(skill_test.createSkill())
skills.append(skill_test.updateSkill())
skills.append(skill_test.deleteSkill())

# staff
staff.append(staff_test.staff())

# course
courses.append(course_test.course())
courses.append(course_test.updateCourse())


# access role
access_role.append(access_role_test.access_role())

# learning journey
learning_journey.append(learning_journey_test.learning_journey())
learning_journey.append(learning_journey_test.createLearningJourney())
learning_journey.append(learning_journey_test.updateLearningJourney())
learning_journey.append(learning_journey_test.deleteLearningJourney())

df["Api Tasks"] = ["Get Skills", "Create Skill", "Update Skill", "Delete Skill", "Get Staff", "Get Courses", "Update Course", "Get Access Role", "Get Learning Journey", "Create Learning Journey", "Update Learning Journey", "Delete Learning Journey"]
df["Time Taken"] = skills + staff + courses + access_role + learning_journey

df.to_csv("performance_test.csv", index=False)

