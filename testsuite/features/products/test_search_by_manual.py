from features.products.search_by_manual import a,search_by_manual
from features.products.get_products import get_products
from settings.conftest import checking_the_status_code_201

res = search_by_manual()
res_data = res.json()
input_data = a

products_data = get_products().json()
count = 0
for i in products_data["products"]:
    if (input_data in i["productVariants"][0]["sku"] or input_data in i["productVariants"][0]["name"]):
        count+=1
def test_search_by_manual():
    assert checking_the_status_code_201(search_by_manual())
    if (res_data["total"] == 0):
        print("Products Not Found with input_data")
    for i in res_data["products"]:
        assert (input_data in i["productVariants"][0]["sku"] or input_data in i["productVariants"][0]["name"]), "Assertion Failure Products Not Found"
    assert count == res_data["total"]
    print(res_data["products"])
    print(res_data["total"])

