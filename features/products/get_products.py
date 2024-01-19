import requests
from settings.conftest import main_url
from settings.api_requests import postApi
from user.test_login import main_workspace

def get_products():
    payload = {}
    url = main_url+"/commerce-v2/products/search/"+f"{main_workspace[0]["pId"]}"+"?pageNo=1&pageSize=5&customerId="+f"{main_workspace[0]["cId"]}"
    response_data = postApi(url,payload)
    # print(response_data)

    return response_data
    # for i in response_data['products']:
    #     print(i["productVariants"]["sku"])




