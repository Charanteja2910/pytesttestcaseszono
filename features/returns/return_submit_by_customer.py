from settings.conftest import main_url
from settings.api_requests import postApi
from user.test_login import main_workspace
from features.returns.create_return_order import create_return_order


return_order_res = create_return_order()

return_order_id = return_order_res.json()["returnOrder"]["id"]
def return_submitted_by_customer():
    payload = {
        "returnOrderId": return_order_id,
        "status": "SUBMITTED",
        "customerId": main_workspace[0]["cId"]
    }

    url = f"{main_url}/hub/claims/return-orders/update/bycustomer/{main_workspace[0]["pId"]}?sellerWorkspaceId={main_workspace[0]["pId"]}"
    res = postApi(url,payload)
    return res

# return_submitted_by_customer()