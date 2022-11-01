import requests

def staff():
    url = "http://localhost:5000/staff"
    response = requests.get(url)
    return response.elapsed.total_seconds()