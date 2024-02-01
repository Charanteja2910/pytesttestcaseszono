from settings.conftest import main_url
from user.test_login import main_workspace
from settings.api_requests import postApi

def pofile_data(a):
    payload = {
        "pofileId": a
    }
    url = main_url+"/commerce-v2/pofiles/details/"+f"{main_workspace[0]["pId"]}"
    res = postApi(url,payload)
    return res



