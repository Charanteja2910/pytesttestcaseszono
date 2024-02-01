from settings.conftest import main_url
from settings.api_requests import postApi
from user.test_login import main_workspace


a = "DULANE"
def search_by_manual():
    payload = {
        "searchKey": a
    }
    url = main_url+"/commerce-v2/products/search/"+f"{main_workspace[0]["pId"]}"+"?customerId="+f"{main_workspace[0]["cId"]}"+"&pageSize=20"
    res = postApi(url,payload)
    return res