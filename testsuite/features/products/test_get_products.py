from features.products.get_products import get_products
from settings.conftest import checking_the_status_code_201


products_data_response = get_products()


def test_get_products():
    # Check if the status code is 201
    assert checking_the_status_code_201(products_data_response)

    # Check if 'total' is greater than 'endRecord' and 'products' is present
    response_json = products_data_response.json()
    assert response_json["total"] > response_json["endRecord"] and response_json[
        "products"], "Invalid total, endRecord, or products"

    # Check the length of 'products' is equal to 'endRecord'
    assert response_json["endRecord"] == len(response_json["products"]), "Length of products does not match endRecord"

    # Check properties of the first product
    first_product = response_json["products"][0]
    assert first_product["id"], "Product id is missing"
    assert len(str(first_product["id"])) == 5, "Invalid product id length"

    # Check properties of the first product variant
    first_variant = first_product["productVariants"][0]
    assert first_variant["productVariantId"], "Product variant id is missing"
    assert len(str(first_variant["productVariantId"])) == 5, "Invalid product variant id length"
    assert first_variant["minOrderQty"], "Minimum order quantity is missing"
    assert first_variant["name"], "Product variant name is missing"
    assert first_variant["price"], "Product variant price is missing"
    assert first_variant["productId"] == first_product[
        "id"], "Product variant's productId does not match the product id"
