import requests
import json


def login(username_f, password_f):
    """
    Login to the server
    """
    url = "https://samvidha.iare.ac.in/pages/login/checkUser.php"
    s = requests.Session()
    payload = {
        "username": username_f,
        "password": password_f
    }
    res = s.post(url, data=payload)
    res_d = json.loads(res.content)
    return s, res_d