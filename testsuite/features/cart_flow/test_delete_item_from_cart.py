from features.orders.cart_del import del_cart_item
from settings.conftest import checking_the_status_code_201
from features.orders.orders_flow import cart_response



cart = del_cart_item()
cart_delete_response = cart[0].json()
item_id = cart[1]

items_ids = []
for i in cart_response[0]["orders"][0]["orderLine"]:
    items_ids.append(i["id"])

def test_item_delete():
    assert checking_the_status_code_201(cart[0]), "Invalid Response"
    assert item_id in items_ids, "Product not deleted"

