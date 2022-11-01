import pandas as pd
import time 
import requests
import access_role_perf
import staff_perf
import skill_perf
import course_perf
import learning_journey_perf

df = pd.DataFrame()
skills = []
staff = []
courses = []
learning_journey = []
access_role = []

# skills
skills.append(skill_perf.skill())
skills.append(skill_perf.createSkill())
skills.append(skill_perf.updateSkill())
skills.append(skill_perf.deleteSkill())

# staff
staff.append(staff_perf.staff())

# course
courses.append(course_perf.course())
courses.append(course_perf.updateCourse())


# access role
access_role.append(access_role_perf.access_role())

# learning journey
learning_journey.append(learning_journey_perf.learning_journey())
learning_journey.append(learning_journey_perf.createLearningJourney())
learning_journey.append(learning_journey_perf.updateLearningJourney())
learning_journey.append(learning_journey_perf.deleteLearningJourney())

df["Api Tasks"] = ["Get Skills", "Create Skill", "Update Skill", "Delete Skill", "Get Staff", "Get Courses", "Update Course", "Get Access Role", "Get Learning Journey", "Create Learning Journey", "Update Learning Journey", "Delete Learning Journey"]
df["Time Taken"] = skills + staff + courses + access_role + learning_journey

df.to_csv("performance_test.csv", index=False)

