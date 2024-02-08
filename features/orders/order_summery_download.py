from features.orders.orders import get_orders
from settings.conftest import main_url
from settings.api_requests import getApi
from user.test_login import main_workspace


orders_data = []
order_res = get_orders().json()
for i in order_res["order"]:
    orders_data.append((i["id"],i["orderMetaData"]["refOrderNumber"]))


def order_summary_download():
    url = f"{main_url}/order/download/{main_workspace[0]["pId"]}?orderId={orders_data[0][0]}&downloadContentType=CSV&customerId={main_workspace[0]["cId"]}"
    res = getApi(url)
    return res,orders_data