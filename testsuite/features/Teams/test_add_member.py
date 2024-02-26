from features.Teams.add_member import add_member,member_data
from features.Teams.team_members_list import get_teams_list
from settings.conftest import checking_the_status_code_200,checking_the_status_code_422


add_member_res = add_member()
teams_list_res = get_teams_list().json()

print(add_member_res)
def test_add_member():
    if (checking_the_status_code_200(add_member_res)):
        assert checking_the_status_code_200(add_member_res)
        assert add_member_res.json()["teamMember"]["mobile"] == member_data["mobileNumber"]
        assert add_member_res.json()["teamMember"]["email"] == member_data["email"]
        assert add_member_res.json()["teamMember"]["employeeCode"] == member_data["employeeCode"]
        assert add_member_res.json()["teamMember"]["name"] == member_data["employeeName"]
        for i in teams_list_res:
            if member_data["employeeCode"] == i["employeeCode"]:
                assert i["mobile"] == member_data["mobileNumber"]
                assert i["name"] == member_data["employeeName"]
                assert i["email"] == member_data["email"]
                assert i["userType"] == "Member"
                assert i["inviteStatus"] == "P"
                print("added")
    elif(checking_the_status_code_422(add_member_res)):
        print(add_member_res.json())
        print("already exists")