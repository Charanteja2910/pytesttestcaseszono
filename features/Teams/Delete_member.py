from features.Teams.team_members_list import get_teams_list
from user.test_login import main_workspace
from settings.conftest import main_url
from settings.api_requests import postApi

members_list = get_teams_list().json()

members_codes = []
for i in members_list:
    if i["employeeCode"] != "NA":
        members_codes.append(i["employeeCode"])

if len(members_codes) == 0:
    print("None members are there in this account")


employee_code = members_codes[0]

def Delete_member():
    payload = {
        "workspaceId": main_workspace[0]["cwId"],
        "teamMemberDetails": {
            "employeeCode": employee_code
        },
        "isArchive": True
    }
    url = f"{main_url}/teamMember/create"
    res = postApi(url, payload)
    return res

