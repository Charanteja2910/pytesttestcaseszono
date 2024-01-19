# import pytest
# from settings.conftest import main_url
# from settings.api_requests import postApi,getApi
# from user.test_login import main_workspace
# from schemes.test_schemes import get_scheme
# code = get_scheme()
# @pytest.fixture
# def test_onclick():
#     url = main_url+"/commerce-v2/scheme/"+f"{main_workspace[0]["pId"]}"+"/"+f"{code}"
#     response = getApi(url)
#     #print(response["sku"])
#     return response["sku"]
#
# def test_check_onclick(test_onclick):
#     payload = {
#         "skuCode": test_onclick[0]
#     }
#     url = main_url+"/commerce-v2/products/search/"+f"{main_workspace[0]["pId"]}"+"?pageNo=1&pageSize=10&customerId="+f"{main_workspace[0]["cId"]}"
#     response = postApi(url,payload)
#
#     print(response)
