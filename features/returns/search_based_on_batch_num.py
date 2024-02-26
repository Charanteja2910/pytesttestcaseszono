from settings.conftest import main_url
from settings.api_requests import postApi
from user.test_login import main_workspace
from features.returns.get_header_divisions import header_division


header_division_res = header_division()
header_division_id = header_division_res.json()[2]["id"]

batch_num = "GKD1392A"
def get_res_based_on_batch_num():
    payload = {
        "batchCodes": [
            batch_num
        ],
        "productVariantIds": [],
        "includeProduct": True,
        "includeInvoice": True,
        "customerId": main_workspace[0]["cId"],
        "doPartialSearch": False,
        "headDivisionId": header_division_id,
        "category": "NE"
    }

    url = f"{main_url}/hub/claims/batch/{main_workspace[0]["pId"]}/search?sellerWorkspaceId={main_workspace[0]["pId"]}"
    res = postApi(url,payload)
    return res

# get_res_based_on_batch_num()



