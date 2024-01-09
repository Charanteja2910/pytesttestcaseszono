from settings.api_requests import postApi
from settings.conftest import postApi,main_url
from user.test_login import main_workspace
from orders.test_uploadfile import cart_data


def test_upload_checkout():
    payload = {
    "sellerWorkspaceId": main_workspace[0]["pId"],
    "customerId": main_workspace[0]["cId"],
    "poFileIds": [
        cart_data[0]["pofileId"]
    ]
}
    url = main_url + "/commerce-v2/orders/checkout/" + f"{main_workspace[0]["pId"]}"
    response = postApi(url,payload)
    print(response)