import requests

def course():
    url = "http://localhost:5000/courses"
    response = requests.get(url)
    return response.elapsed.total_seconds()

def updateCourse():
    url = "http://localhost:5000/courses/FIN001"
    data = {
        "Course_ID": "COR001",
        "Skills": [3]
    }
    response = requests.put(url, json=data)
    return response.elapsed.total_seconds()

