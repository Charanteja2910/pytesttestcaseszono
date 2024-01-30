from datetime import datetime
from settings.conftest import main_url
from user.test_login import main_workspace
from settings.api_requests import postApi

today_date = datetime.now()
formatted_date = today_date.strftime("%Y-%m-%d")

start_date = formatted_date
# end_dates = datetime(2024, 4,24)
# end_date = end_dates.strftime("%Y-%m-%d")
end_date = formatted_date

# # Get the current date
# current_date = datetime.now()
#
# # Add 20 days to the current date
# new_date = current_date + timedelta(days=20)
def filter_by_dates():
    payload = {}
    url = main_url+"/commerce-v2/scheme/"+f"{main_workspace[0]["pId"]}"+"?pageNo=1&pageSize=20&skuCode=&sortDirection=&sortBy=&includeCFA=true&startDate="+f"{start_date}"+"&endDate="+f"{end_date}"+"&dispatchFilters=false&status=&promotionType="
    res = postApi(url,payload)
    return res


