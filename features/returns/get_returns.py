from settings.conftest import main_url
from settings.api_requests import postApi
from user.test_login import main_workspace

def payload():
    p = {
    "includeProduct": False,
    "includeSummary": True,
    "includeImportSources": True,
    "includeStatus": True,
    "includecfaIds": True,
    "pageNo": 1,
    "pageSize": 20,
    "searchKeyword": "",
    "sortBy": "date",
    "sortDirection": "DESC",
    "customerId": main_workspace[0]["cId"],
    "userType": "C",
    "filters": {},
    "startDate": "2024-01-13",
    "endDate": "2024-02-12"
}
    return p

def get_returns(a= payload()):
    payload = a
    url = f"{main_url}/claims/return-orders/list/{main_workspace[0]["pId"]}"
    res = postApi(url,payload)
    return res