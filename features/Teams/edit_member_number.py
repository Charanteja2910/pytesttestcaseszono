from features.Teams.team_members_list import get_teams_list
from settings.conftest import main_url
from user.test_login import main_workspace
from settings.api_requests import postApi

members_list = get_teams_list().json()
members_id = []
for i in members_list:
    if i["userType"] == "Member":
        members_id.append(i["id"])

if (len(members_id) ==0):
    print("none members are there in teams")

member_id = members_id[0]

mobile_number = "0910000099999"

def edit_mobile_number():
    payload = {
        "workspaceId": main_workspace[0]["cwId"],
        "inviteId": member_id,
        "newMobile": mobile_number
    }
    url = f"{main_url}/teams/update/mobile"
    res = postApi(url,payload)
    return res