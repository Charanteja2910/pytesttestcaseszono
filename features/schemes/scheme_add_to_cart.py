import requests
from settings.conftest import main_url
from user.test_login import main_workspace
from settings.api_requests import postApi
from features.schemes.get_schemes import get_scheme

# scheme_response = get_scheme()
#
# schemes_data = scheme_response.json()["promotions"][0]
def scheme_to_cart():
    scheme_response = get_scheme()

    schemes_data = scheme_response.json()["promotions"][0]
    payload = {
        "customerId": main_workspace[0]["cId"],
        "sellerWorkspaceId": main_workspace[0]["pId"],
        "source": "manual",
        "lines": [
            {"productVariantId": int(schemes_data["productVariantIds"][2:7]), "quantity": schemes_data["minimumQty"], "operator": "add"}

        ]

    }
    url = main_url+"/commerce-v2/orders/additemtoactiveorder/"+f"{main_workspace[0]["pId"]}"
    response = postApi(url,payload)
    return response,schemes_data
