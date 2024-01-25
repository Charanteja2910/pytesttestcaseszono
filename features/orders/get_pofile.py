from settings.api_requests import getApi
from user.test_login import main_workspace
from settings.conftest import main_url


def get_pofile_data():
    url = main_url+"/commerce-v2/poFiles/"+f"{main_workspace[0]["pId"]}"+"?customerId="+f"{main_workspace[0]["cId"]}"+"&includeActiveOrders=true&includeSummary=true"
    res = getApi(url)
    return res