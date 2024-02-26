from settings.conftest import main_url
from settings.api_requests import postApi
from user.test_login import main_workspace
from features.returns.get_header_divisions import header_division
from features.returns.search_based_on_batch_num import get_res_based_on_batch_num
from features.returns.get_cfa import get_cfa
from datetime import datetime

today = datetime.today()

formatted_date = today.strftime("%Y/%m/%d")

header_division_res = header_division()
cfa_id = get_cfa()
batch_num_res = get_res_based_on_batch_num()

if batch_num_res.json()["response"] == []:
    print("This Batch Not Found")

productId = batch_num_res.json()["response"][0]["productVariantId"]
batchId = batch_num_res.json()["response"][0]["id"]
batch_num = batch_num_res.json()["response"][0]["batchCode"]
qty = 100
category = "NE"
def create_return_order():
    payload = {
        "customerId": main_workspace[0]["cId"],
        "importSource": "manual",
        "orderPlacedAt": formatted_date,
        "lines": [
            {
                "productVariantId": productId,
                "batchId": batchId,
                "batchCode": batch_num,
                "quantity": qty,
                "category": category
            }
        ],
        "headDivisionId": header_division_res.json()[2]["id"],
        "category": "NE",
        "cfaId": cfa_id.json()["customerCFADivisions"][0]["id"]
    }

    url = f"{main_url}/hub/claims/return-orders/{main_workspace[0]["pId"]}?sellerWorkspaceId={main_workspace[0]["pId"]}"
    res = postApi(url,payload)
    return res

