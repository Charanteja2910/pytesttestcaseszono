
from settings.conftest import main_url
from user.test_login import main_workspace
from products.get_products import get_products
from settings.api_requests import postApi

cart_response = []
data = get_products()
data_list = []
for i in data["products"]:
    for j in i["productVariants"]:
        data_list.append({"productVId": j["productVariantId"], "minQty": j["minOrderQty"]})

def add_to_cart():
    payload = {
        "customerId": main_workspace[0]["cId"],
        "sellerWorkspaceId": main_workspace[0]["pId"],
        "source": "manual",
        "lines": [{"productVariantId": i["productVId"],"quantity": i["minQty"],"operator": "add"} for i in data_list ]
    }
    url = main_url+"/commerce-v2/orders/additemtoactiveorder/"+f"{main_workspace[0]["pId"]}"
    res = postApi(url,payload)
    cart_response.append(res)
    # print(cart_response)
    # print(response)
    # print(len(data_list))


add_to_cart()


