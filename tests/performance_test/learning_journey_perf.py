import requests


def learning_journey():
    url = "http://localhost:5000/learningjourney"
    data = {
        "Staff_ID": "STF001"
    }
    response = requests.post(url)
    return response.elapsed.total_seconds()


def createLearningJourney():
    url = "http://localhost:5000/learningjourney"
    data = {
        "Staff_ID": 1,
        "Learning_Journey": {
            "Courses": [
                {
                    "Course_ID": "COR001"
                }
            ],
            "Description": "create",
            "Learning_Journey_Name": "Learning Journey for Full Stack Developer",
            "Role": {
                "Department": "Operations",
                "Description": "Slavery is no go. Please promote me",
                "Job_ID": 1,
                "Job_Role": "Operation Slave",
                "Job_Title": "Staff"
            },
            "Staff_ID": 1
        }
    }
    response = requests.post(url, json=data)
    return response.elapsed.total_seconds()

def updateLearningJourney():
    url = "http://localhost:5000/learningjourney/1"
    data = {
        "Staff_ID": 1,
        "Learning_Journey": {
            "Courses": [
                {
                    "Course_ID": "COR001"
                }
            ],
            "Description": "create",
            "Learning_Journey_Name": "Learning Journey for Full Stack Developer",
            "Role": {
                "Department": "Operations",
                "Description": "Slavery is no go. Please promote me",
                "Job_ID": 1,
                "Job_Role": "Operation Slave",
                "Job_Title": "Staff"
            },
            "Staff_ID": 1
        }
    }
    response = requests.put(url, json=data)
    return response.elapsed.total_seconds()

def deleteLearningJourney():
    url = "http://localhost:5000/learningjourney/1"
    data = {
        "Staff_ID": 1,
    }
    response = requests.delete(url)
    return response.elapsed.total_seconds()