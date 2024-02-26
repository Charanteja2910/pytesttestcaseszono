from features.Teams.team_members_list import get_teams_list
from features.Teams.Edit_member_details import edit_member_details,member_id,employee_name
from settings.conftest import checking_the_status_code_200

edited_res = edit_member_details()

teams_list = get_teams_list().json()


def test_edit_member_details():
    assert checking_the_status_code_200(edited_res)
    assert edited_res.json()["teamMember"]["employeeName"] == employee_name
    for i in teams_list:
        if i["id"] == member_id:
            assert i["name"] == employee_name