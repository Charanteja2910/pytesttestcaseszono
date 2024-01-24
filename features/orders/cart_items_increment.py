from settings.api_requests import postApi
from settings.conftest import main_url
from features.orders.cart_del import order_line_id,pofile_id
from user.test_login import main_workspace

quantity_for_increment = 42
quantity_for_decrement = 40
# order_line_id[0]["qty"]+1
def item_increment():
    payload = {
    "customerId": main_workspace[0]["cId"],
    "sellerWorkspaceId": main_workspace[0]["pId"],
    "poFileId": pofile_id,
    "source": "manual",
    "lines": [
        {
            "productVariantId": order_line_id[0]["pVId"],
            "quantity": quantity,
            "operator": "add",
            "poFileLineId": order_line_id[0]["id"]
        }
    ]
    }
    url = main_url+"/commerce-v2/orders/additemtoactiveorder/"+f"{main_workspace[0]["pId"]}"
    response = postApi(url,payload)
    return response,order_line_id


def item_decrement():
    payload = {
        "customerId": main_workspace[0]["cId"],
        "sellerWorkspaceId": main_workspace[0]["pId"],
        "poFileId": pofile_id,
        "source": "manual",
        "lines": [
            {
                "productVariantId": order_line_id[0]["pVId"],
                "quantity": quantity_for_decrement,
                "operator": "minus",
                "poFileLineId": order_line_id[0]["id"]
            }
        ]
    }
    url = main_url + "/commerce-v2/orders/additemtoactiveorder/" + f"{main_workspace[0]["pId"]}"
    response = postApi(url, payload)
    return response,order_line_id
