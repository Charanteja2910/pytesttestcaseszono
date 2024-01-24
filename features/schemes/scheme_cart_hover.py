import requests
from settings.conftest import main_url
from user.test_login import main_workspace
from settings.api_requests import getApi
from features.schemes.get_schemes import get_scheme


def scheme_hover_response(id):
    url = main_url + "/commerce-v2/scheme/" + f"{main_workspace[0]["pId"]}/"+str(id)
    response = getApi(url)
    return response