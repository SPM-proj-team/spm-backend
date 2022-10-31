import requests

def access_role():
    url = "http://localhost:5000/accessrole"
    response = requests.get(url)
    return response.elapsed.total_seconds()