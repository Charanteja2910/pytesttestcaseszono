import pytest
import requests
workspaces = []

def verify_mobile_otp(otp_res,mfa_no,main_url):
    payload = {
        "authChannel": "mobile",
        "mobile": "091"+f"{mfa_no}",
        "otp": str(otp_res["mobile"]["otp"]),
        "mfa_status": True
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer "+f"{otp_res["temptoken"]}"
    }
    response = requests.post(main_url+"/verifyotp", json = payload,headers = headers)
    return response.json()

def verify_email_otp(otp_res,verify_mobile_res,main_url):
    payload = {
        "authChannel": "email",
        "email": verify_mobile_res["email"],
        "otp": str(otp_res["email"]["otp"]),
        "mfa_status": True
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer "+f"{verify_mobile_res["temptoken"]}"
    }
    response = requests.post(main_url+"/verifyotp", json = payload,headers = headers)
    return response.json()

def get_workspacess(verify_email_res,main_url):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + f"{verify_email_res["token"]}"
    }
    response = requests.get(main_url+"/workspaces",headers = headers)
    for i in response.json():
        for j in i["principal"]:
            each_principal = {"pId": j["principalWorkspaceId"], "cId": j["inviteId"],"cwId": j["clientWorkspaceId"]}
            workspaces.append(each_principal)
    return workspaces
