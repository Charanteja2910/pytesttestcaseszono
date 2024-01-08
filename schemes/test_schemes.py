import requests
from settings.conftest import main_url
from user.test_login import main_workspace
from settings.api_requests import postApi

def get_scheme():
    payload = {}
    url = main_url+"/commerce-v2/scheme/"+f"{main_workspace[0]["pId"]}"
    response = postApi(url,payload,)
    for i in response["promotions"]:
        return i["id"]
