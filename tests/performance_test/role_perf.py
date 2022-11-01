import requests

def role():
    url = "http://localhost:5000/roles"
    response = requests.get(url)
    return response.elapsed.total_seconds()

def createRole():
    url = "http://localhost:5000/roles"
    data = {
        "Job_Role": "testing",
        "Job_Title": "Manager",
        "Department": "Sales",
        "Description": "Lorem ipsum",
        "Skills": [1, 2]
    }
    response = requests.post(url, json=data)
    return response.elapsed.total_seconds()

# def updateRole():
#     url = "http://localhost:5000/roles/1"
#     data = {
#         "Job_Role": "testing",
#         "Job_Title": "Manager",
#         "Department": "Sales",
#         "Description": "Lorem ipsum",
#         "Skills": ["S001"]
#     }
#     response = requests.put(url, json=data)
#     return response.elapsed.total_seconds()

def deleteRole():
    url = "http://localhost:5000/roles/1"
    response = requests.delete(url)
    return response.elapsed.total_seconds()
    