from features.Home.cumulative_orders import cumulative_orders
from settings.conftest import checking_the_status_code_201
from features.orders.orders_count_of_multiple_principals import total_orders

cumulative_res = cumulative_orders()


# print(cumulative_res)
print(total_orders)
print(cumulative_res.json()["totalOrders"])
print(cumulative_res.json()["totalOrderedAmount"])

def test_cumulative_orders():
    assert checking_the_status_code_201(cumulative_res)
    assert cumulative_res.json()["totalOrders"] != None, "TotalOrders should not be empty in cumulative orders"
    assert total_orders == int(cumulative_res.json()["totalOrders"])
    assert cumulative_res.json()["totalOrderedAmount"] != None