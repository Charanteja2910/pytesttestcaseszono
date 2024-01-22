import pytest
import requests
from user import token,workspace
from settings.conftest import main_url

@pytest.fixture
def test_update():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + f"{token}"
    }
    payload = {
    "email": "pankajg@pharmarack.com",
    "firstName": "ABHIMANYU Krishna"
}
    response = requests.put(main_url+"/users",json = payload ,headers = headers)
    return response.json()



def test_get_user(test_update):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + f"{token}"
    }
    url = main_url+"/users/me/v2?includeCFA=true&sellerWorkspaceId="+f"{workspace[0]["pId"]}"
    response = requests.get(url, headers = headers)
    print(response.json())
    assert response.json()["firstName"] == test_update["data"]["firstName"]



