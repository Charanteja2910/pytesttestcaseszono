from user.test_login import main_workspace
from features.Home.cumulative_orders import formatted_date,start_date
from features.orders.orders import payload
from settings.conftest import main_url
from settings.api_requests import postApi

req_payload = payload()
req_payload["startDate"] =start_date
req_payload["endDate"] = formatted_date
total_orders = 0

def get_data(i,a):
    payload = a
    url = main_url + "/commerce-v2/orders?customerWorkspaceId=" + f"{i["cwId"]}" + "&workspaceId=" + f"{i["pId"]}"
    res = postApi(url, payload)
    return res.json()["totalRecords"]


for i in main_workspace:
    req_payload["workspaceId"] = i["pId"]
    req_payload["customerId"] = i["cId"]
    a = get_data(i,req_payload)
    total_orders+=a

# print(total_orders)



