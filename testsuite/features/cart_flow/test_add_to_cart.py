from features.products.get_products import get_products
from features.orders.orders_flow import add_to_cart

# for i in products_data.json()["products"]:
#     for j in i["productVariants"]:
#         data_list.append({"productVId": j["productVariantId"], "minQty": j["minOrderQty"]})
# print(products_data.json())
c = add_to_cart()
cart_response = c[0]
products_data = c[1]
# print(cart_response.json())
# print(products_data.json())

# for i in cart_response.json()["orders"][0]["orderLine"]:
#     print(i["productVariantId"])
# for j in products_data.json()["products"][0]["productVariants"]:
#     print(j["productVariantId"])


def test_add_to_cart():
    # Assuming cart_response is the response object and products_data is another response object

    # Asserting status code
    assert cart_response.status_code == 201, f"Expected status code 201, but got {cart_response.status_code}"

    # Asserting product variant ID
    expected_variant_id = products_data.json()["products"][0]["productVariants"][0]["productVariantId"]
    assert cart_response.json()["orders"][0]["orderLine"][0][
               "productVariantId"] == expected_variant_id, f"Expected variant ID {expected_variant_id}, but got {cart_response.json()['orders'][0]['orderLine'][0]['productVariantId']}"

    # Asserting quantity
    expected_quantity = products_data.json()["products"][0]["productVariants"][0]["minOrderQty"]
    assert cart_response.json()["orders"][0]["orderLine"][0][
               "quantity"] == expected_quantity, f"Expected quantity {expected_quantity}, but got {cart_response.json()['orders'][0]['orderLine'][0]['quantity']}"

    # Asserting import source
    assert cart_response.json()["orders"][0]["importSource"] == "manual", "Expected import source to be 'manual'"

    # Asserting SKU
    expected_sku = products_data.json()["products"][0]["productVariants"][0]["sku"]
    assert cart_response.json()["orders"][0]["orderLine"][0][
               "sku"] == expected_sku, f"Expected SKU {expected_sku}, but got {cart_response.json()['orders'][0]['orderLine'][0]['sku']}"

    # Asserting SKU name
    expected_sku_name = products_data.json()["products"][0]["productVariants"][0]["name"]
    assert cart_response.json()["orders"][0]["orderLine"][0][
               "skuName"] == expected_sku_name, f"Expected SKU name {expected_sku_name}, but got {cart_response.json()['orders'][0]['orderLine'][0]['skuName']}"
