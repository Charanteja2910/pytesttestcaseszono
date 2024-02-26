from features.Teams.Member_login.login_process import main_workspace_of_member,main_token_of_member,id
from settings.conftest import main_url
import requests

def accept_invite():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + f"{main_token_of_member}"
    }
    url = f"{main_url}/teaminvite/accept/{id}"
    res = requests.put(url, headers = headers)
    print(res.json())

accept_invite()
