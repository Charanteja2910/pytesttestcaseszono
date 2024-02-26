from features.Home.principle_invite import principle_invites
from settings.conftest import checking_the_status_code_200

res = principle_invites()
data = res.json()
if (len(data["principalInvites"]) == 0):
    print("No invitations present in this account")
else:
    print(f"{len(data["principalInvites"])} invitations came to {data["principalInvites"][0]["customerDetails"]["name"]}")
def test_principal_invites():
    assert checking_the_status_code_200(res)

