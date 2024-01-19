
from settings.api_requests import postApi
from settings.conftest import main_url
from user.test_login import main_workspace
from orders.orders_flow import cart_response



def test_check_out():
    payload = {
        "sellerWorkspaceId": main_workspace[0]["pId"],
        "customerId": main_workspace[0]["cId"],
        "poFileIds": [i["pofileId"] for i in cart_response[0]["orders"]]
    }
    url = main_url + "/commerce-v2/orders/checkout/" + f"{main_workspace[0]["pId"]}"
    responses = postApi(url, payload)
    print(responses)