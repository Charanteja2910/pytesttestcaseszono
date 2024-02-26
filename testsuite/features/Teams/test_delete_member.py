from features.Teams.Delete_member import Delete_member,employee_code
from features.Teams.team_members_list import get_teams_list
from settings.conftest import checking_the_status_code_200

delete_res = Delete_member()
members_list = get_teams_list().json()

members_code = []
for i in members_list:
    if i["employeeCode"] != "NA":
        members_code.append(i["employeeCode"])


def test_delete_member():
    assert checking_the_status_code_200(delete_res)
    assert delete_res.json()["status"] == "deleted"
    assert len(delete_res.json()["teamMember"]) == 0
    assert employee_code not in members_code