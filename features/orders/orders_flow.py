
from settings.conftest import main_url
from user.test_login import main_workspace
from features.products.get_products import get_products
from settings.api_requests import postApi

cart_response = []

def add_to_cart():
    data = get_products()
    payload = {
        "customerId": main_workspace[0]["cId"],
        "sellerWorkspaceId": main_workspace[0]["pId"],
        "source": "manual",
        "lines": [
            {"productVariantId": variant["productVariantId"], "quantity": variant["minOrderQty"], "operator": "add"}
            for product in data.json()["products"]
            for variant in product["productVariants"]
        ]

    }
    url = main_url+"/commerce-v2/orders/additemtoactiveorder/"+f"{main_workspace[0]["pId"]}"
    res = postApi(url,payload)
    cart_response.append(res.json())
    return [res,data]
    # print(cart_response)
    # print(res.json())
    # print(len(data_list))


add_to_cart()


