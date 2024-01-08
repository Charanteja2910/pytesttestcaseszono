import pytest
import requests
from settings.conftest import main_url
from user.test_login import main_workspace
from settings.api_requests import postApi
from orders.test_orders_flow import test_check_out

order_id = test_check_out()

def test_orders():
    payload = {
    "workspaceId": main_workspace[0]["pId"],
    "customerId": main_workspace[0]["cId"],
        "pageNo": 1, "skip": 1, "pageSize": 20, "sortBy": "orderDate", "sortDirection": "DESC", "includeCustomer": True,
        "includeSummary": True, "includeInvoice": True, "includeStatus": True, "startDate": "2023-12-05",
        "endDate": "2024-01-04", "searchKeyword": "",
        "filterModel": {"divisionIds": [], "headDivisionIds": [], "cfaIds": [], "status": [], "customerIds": []},
        "includeProductInfo": True, "includeCFA": True, "includeDivision": True
}
    url = main_url+"/commerce-v2/orders?customerWorkspaceId="+f"{main_workspace[0]["cwId"]}"+"&workspaceId="+f"{main_workspace[0]["pId"]}"
    response = postApi(url,payload)
    print(response["totalRecords"])
    for i in response["order"]:
        print(i["id"])
    print(len(response))