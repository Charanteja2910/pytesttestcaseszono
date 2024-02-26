
from settings.conftest import main_url
from settings.api_requests import getApi


def principle_invites():
    url = f"{main_url}/principalinvite"
    res = getApi(url)
    return res

