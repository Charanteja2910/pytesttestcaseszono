from features.orders.cart_items_increment import item_decrement,quantity_for_decrement
from settings.conftest import checking_the_status_code_201
from features.orders.get_pofile import get_pofile_data

cart_decrement_response = item_decrement()
decrement_data = cart_decrement_response[0].json()
product_variant_id = cart_decrement_response[1][0]["pVId"]
item_quantity = cart_decrement_response[1][0]["qty"]

pofile_response =get_pofile_data().json()

ids_in_pofile = []
for i in pofile_response["files"]:
    if i["importSource"] == "manual":
        ids_in_pofile.append(i["lines"][0]["productVariantId"])


def test_decrement_count():
    if (quantity_for_decrement < item_quantity):
        assert decrement_data["message"]["message"] == "Quantity cannot be below the Minimum Order Quantity (MOQ)"
    else:
        assert checking_the_status_code_201(cart_decrement_response[0]), "Invalid Response"
        assert decrement_data["orders"][0]["orderLine"][0]["productVariantId"] in ids_in_pofile
        assert decrement_data["orders"][0]["orderLine"][0]["quantity"] == (quantity_for_decrement//item_quantity) * item_quantity






