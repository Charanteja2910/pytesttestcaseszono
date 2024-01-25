from features.orders.cart_del import del_cart_item
from settings.conftest import checking_the_status_code_201
from features.orders.orders_flow import cart_response
from features.orders.get_pofile import get_pofile_data


cart = del_cart_item()
cart_delete_response = cart[0].json()
item_id = cart[1]



pofile_response =get_pofile_data().json()

ids_in_pofile = []
for i in pofile_response["files"]:
    if i["importSource"] == "manual":
        ids_in_pofile.append(i["lines"][0]["productVariantId"])


def test_item_delete():
    assert checking_the_status_code_201(cart[0]), "Invalid Response"
    assert item_id not in ids_in_pofile, "Product not deleted"

