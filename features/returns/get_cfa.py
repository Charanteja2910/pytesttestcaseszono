from settings.conftest import main_url
from settings.api_requests import getApi
from user.test_login import main_workspace


def get_cfa():
    url = f"{main_url}/users/me/v2?includeCFA=true&sellerWorkspaceId={main_workspace[1]["pId"]}"
    res = getApi(url)
    return res