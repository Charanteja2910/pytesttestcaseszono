from settings.conftest import main_url
from settings.api_requests import postApi
from user.test_login import main_workspace
from features.returns.create_return_order import create_return_order

return_order_res = create_return_order()


def return_details():
    payload = {
        "returnOrderId": return_order_res.json()["returnOrder"]["id"],
        "includeProduct": True,
        "includeCreditInfo": True,
        "customerId": main_workspace[0]["cId"],
        "sortBy": "pts",
        "sortDirection": "DESC",
        "includeComments": True,
        "searchKeyword": ""
    }
    url = f"{main_url}/hub/claims/return-orders/details/{main_workspace[0]["pId"]}?sellerWorkspaceId={main_workspace[0]["pId"]}"
    res = postApi(url,payload)
    print(res.json())

return_details()