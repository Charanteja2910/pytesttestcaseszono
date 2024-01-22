from settings.api_requests import postApi
from settings.conftest import main_url
from user.test_login import main_workspace
from features.orders import cart_response



order_line_id = []
order_id = cart_response[0]["orders"][0]["id"]
pofile_id = cart_response[0]["orders"][0]["pofileId"]
for i in cart_response[0]["orders"][0]["orderLine"]:
    order_line_id.append({"id":i["id"],"pVId":i["productVariantId"], "qty":i["quantity"]})
def test_del_cart_item():

    payload = {
    "sellerWorkspaceId": main_workspace[0]["pId"],
    "customerId": main_workspace[0]["cId"],
    "importSource": "manual",
    "poFileId": pofile_id,
    "lines": [
        {
            "orderId": order_id,
            "orderLineId": order_line_id[1]["id"]
        }
    ]
}
    url = main_url+"/commerce-v2/orders/deleteLines/"+f"{main_workspace[0]["pId"]}"
    response = postApi(url,payload)
    print(response)



