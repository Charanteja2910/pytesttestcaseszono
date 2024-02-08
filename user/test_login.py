
from settings.conftest import main_url,mobile_number
from user.users import send_otp,verify_otp,get_workspace
from user.mfa_login import verify_mobile_otp,verify_email_otp, get_workspacess
main_workspace = []
main_token = ""
send_otp_response = send_otp(main_url, mobile_number)

# print(send_otp_response.json())
# print(send_otp_response)
# print(1)


if send_otp_response.json()["mfaStatus"]:
    # print(otp_res)
    verify_mobile_res = verify_mobile_otp(send_otp_response.json(),mobile_number, main_url)
    # print(verify_mobile_res.json())
    # print(verify_mobile_res)
    verify_email_res = verify_email_otp(send_otp_response.json(), verify_mobile_res.json(), main_url)
    # print(verify_email_res.json())
    main_token = verify_email_res.json()["token"]
    get_workspaces = get_workspacess(verify_email_res.json(), main_url)
    for i in get_workspaces.json():
        for j in i["principal"]:
            each_principal = {"pId": j["principalWorkspaceId"], "cId": j["inviteId"],"cwId": j["clientWorkspaceId"]}
            main_workspace.append(each_principal)


else:
    token = verify_otp(send_otp_response.json(),main_url,mobile_number)
    main_token = token.json()["token"]
    workspace = get_workspace(token.json()["token"],main_url)
    for i in workspace.json():
        for j in i["principal"]:
            each_principal = {"pId": j["principalWorkspaceId"], "cId": j["inviteId"],"cwId": j["clientWorkspaceId"]}
            main_workspace.append(each_principal)


# print(main_workspace)
# print(len(main_workspace))
# print(main_token)


