from settings.api_requests import postApi
from settings.conftest import main_url
from features.orders.cart_del import order_line_id,pofile_id
from user.test_login import main_workspace

def test_item_increment():
    payload = {
    "customerId": main_workspace[0]["cId"],
    "sellerWorkspaceId": main_workspace[0]["pId"],
    "poFileId": pofile_id,
    "source": "manual",
    "lines": [
        {
            "productVariantId": order_line_id[2]["pVId"],
            "quantity": order_line_id[2]["qty"]*2,
            "operator": "add",
            "poFileLineId": order_line_id[2]["id"]
        }
    ]
    }
    url = main_url+"/commerce-v2/orders/additemtoactiveorder/"+f"{main_workspace[0]["pId"]}"
    response = postApi(url,payload)
    print(response)


def test_item_decrement():
    payload = {
        "customerId": main_workspace[0]["cId"],
        "sellerWorkspaceId": main_workspace[0]["pId"],
        "poFileId": pofile_id,
        "source": "manual",
        "lines": [
            {
                "productVariantId": order_line_id[2]["pVId"],
                "quantity": order_line_id[2]["qty"] / 2 ,
                "operator": "minus",
                "poFileLineId": order_line_id[2]["id"]
            }
        ]
    }
    url = main_url + "/commerce-v2/orders/additemtoactiveorder/" + f"{main_workspace[0]["pId"]}"
    response = postApi(url, payload)
    print(response)
