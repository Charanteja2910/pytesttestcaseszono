from user.users import send_otp,verify_otp,get_workspace
from user.mfa_login import verify_mobile_otp,verify_email_otp,get_workspacess
from settings.conftest import main_url
from features.Teams.team_members_list import get_teams_list

members_list = get_teams_list().json()
mobile_number =""
id = ""
for i in members_list:
    if i["userType"] == "Member" and i["inviteStatus"]=="P":
        mobile_number = i["mobile"][3:]
        id = i["id"]
        break
main_workspace_of_member = []
main_token_of_member = ""
send_otp_response = send_otp(main_url,mobile_number)

if send_otp_response.json()["mfaStatus"]:
    # print(otp_res)
    verify_mobile_res = verify_mobile_otp(send_otp_response.json(),mobile_number, main_url)
    # print(verify_mobile_res.json())
    # print(verify_mobile_res)
    verify_email_res = verify_email_otp(send_otp_response.json(), verify_mobile_res.json(), main_url)
    # print(verify_email_res.json())
    main_token_of_member = verify_email_res.json()["token"]
    get_workspaces = get_workspacess(verify_email_res.json(), main_url)
    # print(get_workspaces.json())
    for i in get_workspaces.json():
        for j in i["principal"]:
            each_principal = {"pId": j["principalWorkspaceId"], "cId": j["inviteId"],"cwId": j["clientWorkspaceId"]}
            main_workspace_of_member.append(each_principal)


else:
    token = verify_otp(send_otp_response.json(),main_url,mobile_number)
    main_token_of_member = token.json()["token"]
    workspace = get_workspace(token.json()["token"],main_url)
    # print(workspace.json())
    for i in workspace.json():
        for j in i["principal"]:
            each_principal = {"pId": j["principalWorkspaceId"], "cId": j["inviteId"],"cwId": j["clientWorkspaceId"]}
            main_workspace_of_member.append(each_principal)


print(main_token_of_member)
print(main_workspace_of_member)