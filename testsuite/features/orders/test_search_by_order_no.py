from features.orders.order_search_filter_by_cfa import search_filter_by_order_no,order_no
from settings.conftest import checking_the_status_code_201

orders_response = search_filter_by_order_no()
orders_data = orders_response.json()

def test_search_filter_by_order_no():
    assert checking_the_status_code_201(orders_response)
    assert orders_data["order"][0]["orderMetaData"]["refOrderNumber"] == order_no