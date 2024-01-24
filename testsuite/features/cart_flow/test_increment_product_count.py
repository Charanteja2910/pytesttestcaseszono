from features.orders.cart_items_increment import item_increment,quantity_for_increment
from settings.conftest import checking_the_status_code_201

increment_response = item_increment()

increment_data = increment_response[0].json()
item_quantity = increment_response[1][0]["qty"]
productVariantId = increment_response[1][0]["pVId"]


def test_items_increment():
    assert checking_the_status_code_201(increment_response[0]), "Invalid Response"
    assert productVariantId == increment_data["orders"][0]["orderLine"][0]["productVariantId"], "qty added to other product"
    if (quantity_for_increment % item_quantity ==0):
        assert increment_data["orders"][0]["orderLine"][0]["quantity"] == ((quantity_for_increment // item_quantity)* item_quantity), "Invalid Qty Added"
    else:
        assert increment_data["orders"][0]["orderLine"][0]["quantity"] == (((quantity_for_increment // item_quantity)+1) * item_quantity), "Invalid Qty Added"
