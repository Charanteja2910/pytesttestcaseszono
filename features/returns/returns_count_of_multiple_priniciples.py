from user.test_login import main_workspace
from features.Home.cumulative_returns import formatted_date,start_date
from features.returns.get_returns import payload
from features.returns.get_returns import get_returns
from settings.conftest import main_url
from settings.api_requests import postApi

req_payload = payload()
req_payload["startDate"] =start_date
req_payload["endDate"] = formatted_date
total_returns = 0

def returns(load,i):
    payload = load
    url = f"{main_url}/hub/claims/return-orders/list/{i["pId"]}?sellerWorkspaceId={i["pId"]}"
    res = postApi(url,payload)
    # print(res.json())
    return res.json()["totalRecords"]



for i in main_workspace:
    req_payload["customerId"] = i["cId"]
    a = returns(req_payload,i)
    total_returns+=a