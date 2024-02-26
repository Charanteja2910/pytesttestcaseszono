from user.test_login import main_workspace
from settings.conftest import main_url
from settings.api_requests import postApi
from datetime import date

today_date = date.today()
formatted_date = today_date.strftime("%Y-%m-%d")

month = today_date.month
year = today_date.year
day = 1

start_date = f"{year:04d}-{month:02d}-{day:02d}"



def cumulative_returns():
    payload = {
        "endDate": f"{formatted_date}",
        "startDate": f"{start_date}"
    }
    url = f"{main_url}/hub/claims/return-orders/cumulative/{main_workspace[0]["pId"]}?customerWorkspaceId={main_workspace[0]["cwId"]}&sellerWorkspaceId={main_workspace[0]["pId"]}"
    res = postApi(url,payload)
    return res
    # print(res.json())