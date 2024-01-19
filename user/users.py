import pytest
import requests
from settings.conftest import checking_the_status_code_200
workspaces = []

def send_otp(main_url,mobile_number):
    payload = {
        "authChannel": "mobile",
        "mobile": "091" + f"{mobile_number}"
    }
    response = requests.post(main_url+"/sendotp", json = payload)
    #print(response.json(), '==============================>send_otp response')
    # send_otp_response = checking_the_status_code_200(response)
    # return send_otp_response
    return response
def verify_otp(test_send_otp,main_url,mobile_number):
    payload = {
        "authChannel": "mobile",
        "mobile": "091"+f"{mobile_number}",
        "otp": str(test_send_otp['mobile']['otp'])
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer "+f"{test_send_otp["temptoken"]}"
    }
    #print(test_send_otp["mobile"]["otp"], '==============================> otp value from send otp')
    response = requests.post(main_url+"/verifyotp",json = payload,headers = headers)
    #print(response.json(), '=========================================> verify otp response')
    # return response.json()["token"]
    return response


def get_workspace(test_verify_otp,main_url):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer "+f"{test_verify_otp}"
    }

    response = requests.get(main_url+"/workspaces",headers=headers)

    return response




