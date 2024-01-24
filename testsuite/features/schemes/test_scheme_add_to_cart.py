from features.schemes.get_schemes import get_scheme
from settings.conftest import checking_the_status_code_201
from features.schemes.scheme_add_to_cart import scheme_to_cart
from features.schemes.scheme_cart_hover import scheme_hover_response

scheme_response  = scheme_to_cart()
schemes_response = scheme_to_cart()[0]
scheme_cart_data = scheme_response[0].json()
scheme_data = scheme_response[1]


scheme_hover_response = scheme_hover_response(scheme_data["id"])

scheme_hover_data = scheme_hover_response.json()



def test_scheme_add_cart():
    # print(scheme_cart_data)
    assert checking_the_status_code_201(schemes_response)

    assert scheme_cart_data["orders"][0]["id"]

def test_check_scheme_hover_response():
    assert scheme_data["id"] == scheme_hover_data["id"], "Invalid id, both id's should be equal"
    assert scheme_data["minimumQty"] == scheme_hover_data["minimumQty"], "invalid minimumQuantity"
    assert scheme_data["maximumQty"] == scheme_hover_data["maximumQty"], "invalid MaximumQuantity"
    assert scheme_data["discountPercentageUpto"] == scheme_hover_data["discountPercentageUpto"], "invalid DiscountPercentage"
    assert scheme_data["pts"] == scheme_hover_data["pts"], "invalid PriceToStockist"