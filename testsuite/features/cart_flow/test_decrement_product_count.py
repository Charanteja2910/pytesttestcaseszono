from features.orders.cart_items_increment import item_decrement,quantity_for_decrement
from settings.conftest import checking_the_status_code_201

cart_decrement_response = item_decrement()
decrement_data = cart_decrement_response[0].json()
product_variant_id = cart_decrement_response[1][0]["pVId"]
item_quantity = cart_decrement_response[1][0]["qty"]

def test_decrement_count():
    assert checking_the_status_code_201(cart_decrement_response), "Invalid Response"
    assert decrement_data["orders"][0]["orderLine"][0]["productVariantId"] == product_variant_id
    assert decrement_data["orders"][0]["orderLine"][0]["quantity"] == (quantity_for_decrement//item_quantity -1) * item_quantity






