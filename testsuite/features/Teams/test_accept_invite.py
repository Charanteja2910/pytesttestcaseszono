from features.Teams.Member_login.member_accept_invite import accept_invite,id
from features.Teams.team_members_list import get_teams_list
from settings.conftest import checking_the_status_code_200
invite_res = accept_invite()
team_list = get_teams_list()

def test_accept_invite():
    if (checking_the_status_code_200(invite_res)):
        for i in team_list:
            if i["id"] == id:
                assert i["inviteStatus"] == "A"
