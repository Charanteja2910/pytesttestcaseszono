from features.schemes import get_scheme
from settings.conftest import checking_the_status_code_201

scheme_response_data = get_scheme()

def test_get_schemes():
    # Check if the status code is 201
    assert checking_the_status_code_201(scheme_response_data), "Invalid status code"

    response_json = scheme_response_data.json()

    # Check if 'totalRecords' is greater than 'endRecord'
    assert response_json["totalRecords"] > response_json["endRecord"], "Invalid totalRecords or endRecord"

    # Check if 'endRecord' matches the length of 'promotions'
    assert response_json["endRecord"] == len(response_json["promotions"]), "Length of promotions does not match endRecord"

    # Check properties of the first promotion
    first_promotion = response_json["promotions"][0]
    assert first_promotion["id"], "Promotion id is missing"
    assert len(str(first_promotion["id"])) == 4, "Invalid promotion id length"
    assert first_promotion["productVariantIds"], "Product variant ids are missing"
    assert first_promotion["minimumQty"], "Minimum quantity is missing"
