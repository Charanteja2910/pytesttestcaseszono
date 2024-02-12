from features.Home.cumulative_orders import cumulative_orders,orders_res
from settings.conftest import checking_the_status_code_201

cumulative_res = cumulative_orders()


# print(cumulative_res)
print(orders_res.json()["totalRecords"])
print(cumulative_res.json()["totalOrders"])
print(cumulative_res.json()["totalOrderedAmount"])

def test_cumulative_orders():
    assert checking_the_status_code_201(cumulative_res)
    assert cumulative_res.json()["totalOrders"] != None, "TotalOrders should not be empty in cumulative orders"
    assert orders_res.json()["totalRecords"] == int(cumulative_res.json()["totalOrders"])
    assert cumulative_res.json()["totalOrderedAmount"] != None