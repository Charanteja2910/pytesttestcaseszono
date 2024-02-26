from settings.conftest import main_url
from settings.api_requests import getApi
from user.test_login import main_workspace


def header_division():
    url = f"{main_url}/headDivision/{main_workspace[1]["pId"]}"
    res = getApi(url)
    return res