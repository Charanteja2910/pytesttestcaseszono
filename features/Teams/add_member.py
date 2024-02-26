from settings.api_requests import postApi
from settings.conftest import main_url
from user.test_login import main_workspace
from features.Teams.get_role_ids import get_role_id

role_ids = get_role_id().json()
member_role_id = ""
for i in role_ids["roles"]:
    if i["title"] == "Member":
        member_role_id = i["id"]
member_data = {
    "mobileNumber": "0919393939395",
    "email": "pank@pharmarack.com",
    "employeeName": "undefined",
    "employeeCode": "1223"
}

def add_member():
    payload = {
        "workspaceId": main_workspace[0]["cwId"],
        "email": member_data["email"],
        "phone": member_data["mobileNumber"],
        "userType": "Member",
        "roleIds": [
            member_role_id
        ],
        "divisionIds": [],
        "CFAIds": [],
        "teamMemberDetails": {
            "employeeName": member_data["employeeName"],
            "employeeCode": member_data["employeeCode"]
        }
    }
    url = f"{main_url}/teamMember/create"
    res = postApi(url,payload)
    return res