from features.Teams.edit_member_number import edit_mobile_number,mobile_number,member_id
from features.Teams.team_members_list import get_teams_list
from settings.conftest import checking_the_status_code_200,checking_the_status_code_422

edited_mobile_res = edit_mobile_number()

teams_list = get_teams_list().json()

def test_edit_mobile_number():
    if checking_the_status_code_200(edited_mobile_res):
        assert edited_mobile_res.json()["phone"] == mobile_number
        for i in teams_list:
            if i["id"] == member_id:
                assert i["mobile"] == mobile_number

    elif checking_the_status_code_422(edited_mobile_res):
        print(edited_mobile_res.json()["message"])