from settings.conftest import mobile_number,main_url
from user.users import send_otp
from user.test_login import verify_mobile_otp,verify_email_otp,get_workspacess

send_otp_response = send_otp(main_url,mobile_number)
verify_mobile_res = verify_mobile_otp(send_otp_response.json(),mobile_number, main_url)
verify_email_res = verify_email_otp(send_otp_response.json(), verify_mobile_res.json(), main_url)
get_workspaces = get_workspacess(verify_email_res.json(), main_url)
# print(send_otp_response.json())
# print(verify_mobile_res.json())
# print(verify_email_res.json())
# print(get_workspaces.json())
def test_send_otp():
    assert send_otp_response.status_code == 200
    assert "mobile" in send_otp_response.json()
    assert len(str(send_otp_response.json()["mobile"]["otp"])) == 4
    assert "temptoken" in send_otp_response.json()
    assert send_otp_response.json()["authChannel"] == "mobile"
    if (send_otp_response.json()["mfaStatus"]):
        assert "email" in send_otp_response.json()
        assert len(str(send_otp_response.json()["email"]["otp"])) == 4
        assert "otp" in send_otp_response.json()["email"]
        assert "sendOtp" in send_otp_response.json()["email"]
        assert "temptoken" in send_otp_response.json()

def test_verify_mobile_otp():
    assert verify_mobile_res.status_code == 200
    assert "temptoken" in verify_mobile_res.json()
    assert len(str(verify_mobile_res.json()["mobile"])) == 13
    assert "inviteId" in verify_mobile_res.json()

def test_verify_email_otp():
    assert verify_email_res.status_code == 200
    assert "token" in verify_email_res.json()
    assert verify_email_res.json()["isOtpValid"]


def test_get_workspace():
    if len(get_workspaces.json()) >0:
        assert get_workspaces.json()[0]["workspaceMembers"] and get_workspaces.json()[0]["channels"] and get_workspaces.json()[0]["principal"]
