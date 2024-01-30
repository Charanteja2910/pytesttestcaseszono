from features.orders.orders import get_orders,payload

order_no = get_orders().json()["order"][0]["orderMetaData"]["refOrderNumber"]




def search_filter_by_order_no():
    request_data = payload()
    request_data["searchKeyword"] = order_no
    filter_res = get_orders(request_data)

    return filter_res



