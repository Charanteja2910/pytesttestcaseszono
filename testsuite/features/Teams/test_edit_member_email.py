from features.Teams.edit_member_email import edit_member_email,member_id,email
from features.Teams.team_members_list import get_teams_list
from settings.conftest import checking_the_status_code_200,checking_the_status_code_422

edited_email_res = edit_member_email()

teams_list = get_teams_list().json()


def test_edit_member_email():
    if (checking_the_status_code_200(edited_email_res)):
        for i in teams_list:
            if i["id"] == member_id:
                assert i["email"] == email

    elif checking_the_status_code_422(edited_email_res):
        print(edited_email_res.json()["message"])