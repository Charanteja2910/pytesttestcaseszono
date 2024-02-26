from settings.conftest import main_url
from settings.api_requests import postApi
from user.test_login import main_workspace
from features.returns.get_header_divisions import header_division
from features.returns.get_cfa import get_cfa
from features.returns.upload_returns.upload_return_details import upload_return_details
from datetime import datetime,timedelta

today = datetime.today()

formatted_date = today.strftime("%Y/%m/%d")
yesterday = today - timedelta(days=1)

# Format yesterday's date to the desired format
formatted_yesterday = yesterday.strftime("%Y-%m-%d")
upload_return_res = upload_return_details()
header_division_id = header_division().json()[2]["id"]
cfa_id = get_cfa().json()["customerCFADivisions"][0]["id"]

res_date = today.strftime("%Y-%m-%dT00:00:00.000Z")

invoiceNumber = 1234
quantity = 150
lrNumber = 2548
lrDate = today.strftime("%Y-%m-%d")
goodsReceivedDate =formatted_yesterday
boxes = 10
vehicleDetails = "AP39 CP 2024"
def edit_upload_return_file():
    payload = {
        "customerId": main_workspace[1]["cId"],
        "importSource": "upload",
        "orderPlacedAt":formatted_date,
        "lines": [
            {
                "productVariantId": i["productVariantId"],
                "batchId": i["batchId"],
                "batchCode": i["batchNumber"],
                "quantity": quantity,
                "invoiceNumber":str(invoiceNumber),
                "category": "NE",
                "returnOrderLineId": i["id"]
            } for i in upload_return_res.json()["lines"]
        ],
        "headDivisionId": header_division_id,
        "lrNumber": str(lrNumber),
        "lrDate": lrDate,
        "noOfBoxes": boxes,
        "vehicleDetails": vehicleDetails,
        "goodsReceivedDate": formatted_yesterday,
        "category": "NE",
        "cfaId": cfa_id,
        "returnOrderId": upload_return_res.json()["id"]

    }
    url = f"{main_url}/hub/claims/return-orders/{main_workspace[1]["pId"]}?sellerWorkspaceId={main_workspace[1]["pId"]}"
    res = postApi(url,payload)
    return res



