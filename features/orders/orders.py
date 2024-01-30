from settings.conftest import main_url
from user.test_login import main_workspace
from settings.api_requests import postApi

def payload():

    request_load = {
        "workspaceId": main_workspace[0]["pId"],
        "customerId": main_workspace[0]["cId"],
            "pageNo": 1, "skip": 1, "pageSize": 20, "sortBy": "orderDate", "sortDirection": "DESC", "includeCustomer": True,
            "includeSummary": True, "includeInvoice": True, "includeStatus": True, "startDate": "2023-12-05",
            "endDate": "2024-01-04", "searchKeyword": "",
            "filterModel": {"divisionIds": [], "headDivisionIds": [], "cfaIds": [], "status": [], "customerIds": []},
            "includeProductInfo": True, "includeCFA": True, "includeDivision": True
    }
    return request_load
def get_orders(a = payload()):
    payload = a
    url = main_url+"/commerce-v2/orders?customerWorkspaceId="+f"{main_workspace[0]["cwId"]}"+"&workspaceId="+f"{main_workspace[0]["pId"]}"
    res = postApi(url,payload)
    return res