from settings.conftest import main_url
from settings.api_requests import postApi
from user.test_login import main_workspace
from features.returns.get_header_divisions import header_division
from features.returns.search_based_on_batch_num import get_res_based_on_batch_num

res = get_res_based_on_batch_num()

if res.json()["response"] == []:
    print("This Batch Not Found")

productId = res.json()["response"][0]["productVariantId"]
header_division_res = header_division()


def get_num_of_batches_contains_same_product():
    payload = {
        "batchCodes": [
        ],
        "productVariantIds": [productId],
        "includeProduct": True,
        "includeInvoice": True,
        "customerId": main_workspace[0]["cId"],
        "doPartialSearch": False,
        "headDivisionId": header_division_res.json()[2]["id"],
        "category": "NE"
    }

    url = f"{main_url}/hub/claims/batch/{main_workspace[0]["pId"]}/search?sellerWorkspaceId={main_workspace[0]["pId"]}"
    res = postApi(url,payload)
    print(res.json())


get_num_of_batches_contains_same_product()