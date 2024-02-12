from user.test_login import main_workspace
from settings.conftest import main_url
from settings.api_requests import postApi
from datetime import date
from features.orders.orders import get_orders,payload

today_date = date.today()
formatted_date = today_date.strftime("%Y-%m-%d")

month = today_date.month
year = today_date.year
day = 1

start_date = f"{year:04d}-{month:02d}-{day:02d}"

req_payload = payload()
req_payload["startDate"] =start_date
req_payload["endDate"] = formatted_date

orders_res = get_orders(req_payload)

def cumulative_orders():
    payload = {
        "endDate": f"{formatted_date}",
        "startDate": f"{start_date}"
    }
    url = f"{main_url}/commerce-v2/orders/cumulative/{main_workspace[0]["pId"]}?customerWorkspaceId={main_workspace[0]["cwId"]}"
    res = postApi(url,payload)
    return res