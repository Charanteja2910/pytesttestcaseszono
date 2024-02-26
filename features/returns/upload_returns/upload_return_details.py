from settings.conftest import main_url
from settings.api_requests import postApi
from user.test_login import main_workspace
from features.returns.upload_returns.upload_file import upload_file

upload_id = upload_file().json()["id"]


def upload_return_details():
    payload ={
        "returnOrderId": str(upload_id),
        "includeProduct": True,
        "includeCreditInfo": True,
        "customerId": main_workspace[1]["cId"],
        "sortBy": "pts",
        "sortDirection": "DESC",
        "includeComments": True,
        "searchKeyword": ""
    }
    url = f"{main_url}/hub/claims/return-orders/details/{main_workspace[1]["pId"]}?sellerWorkspaceId={main_workspace[1]["pId"]}"
    res = postApi(url,payload)
    return res