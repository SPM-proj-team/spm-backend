import requests

def skill():
    url = "http://localhost:5000/skills"
    response = requests.get(url)
    return response.elapsed.total_seconds()

def createSkill():
    url = "http://localhost:5000/skills"
    data = {
        "Skill_ID": "S099",
        "Name": "Solidity",
        "Courses": ["FIN001", "FIN002"]
    }
    response = requests.post(url, json=data)
    return response.elapsed.total_seconds()

def updateSkill():
    url = "http://localhost:5000/skills/S099"
    data = {
        "Skill_ID": "S099",
        "Name": "Solidit1",
        "Courses": ["FIN001"]
    }
    response = requests.put(url, json=data)
    return response.elapsed.total_seconds()


def deleteSkill():
    url = "http://localhost:5000/skills/S099"
    response = requests.delete(url)
    return response.elapsed.total_seconds()
