from settings.api_requests import getApi
from settings.conftest import main_url

def get_role_id():
    url = f"{main_url}/workspaces/roles/permissions?isSeller=false&isBuyer=true"
    res = getApi(url)
    return res