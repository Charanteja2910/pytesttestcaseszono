from settings.api_requests import postApi
from settings.conftest import main_url
from user.test_login import main_workspace
from features.orders.orders_flow import add_to_cart


cart_response = add_to_cart()[0]
cart_data = cart_response.json()

carts_id = []
order_id = cart_data["orders"][0]["id"]
pofile_id = cart_data["orders"][0]["pofileId"]
for i in cart_data["orders"][0]["orderLine"]:
    carts_id.append({"id":i["id"]})

def delete_items_by_cfa():
    payload = {
        "sellerWorkspaceId": main_workspace[0]["pId"],
        "customerId": main_workspace[0]["cId"],
        "importSource": "manual",
        "poFileId": pofile_id,
        "lines": [
            {
                "orderId": order_id,
                "orderLineId": i["id"]
            } for i in carts_id
        ]
    }
    url = main_url+"/commerce-v2/orders/deleteLines/"+f"{main_workspace[0]["pId"]}"
    res = postApi(url,payload)
    return res


