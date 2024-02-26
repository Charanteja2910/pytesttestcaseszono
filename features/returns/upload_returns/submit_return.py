from settings.conftest import main_url
from settings.api_requests import postApi
from user.test_login import main_workspace
from features.returns.upload_returns.upload_file_res import upload_id

def return_submitted_by_customer():
    payload = {
        "returnOrderId": upload_id,
        "status": "SUBMITTED",
        "customerId": main_workspace[1]["cId"]
    }

    url = f"{main_url}/hub/claims/return-orders/update/bycustomer/{main_workspace[1]["pId"]}?sellerWorkspaceId={main_workspace[1]["pId"]}"
    res = postApi(url,payload)
    return res

submit_return_res = return_submitted_by_customer()