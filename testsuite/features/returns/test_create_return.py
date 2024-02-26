from features.returns.create_return_order import create_return_order,productId,batchId,batch_num,qty,category
from settings.conftest import checking_the_status_code_201

return_res = create_return_order()

def test_create_return():
    assert checking_the_status_code_201(return_res)
    assert return_res.json()["returnOrder"]["id"] != None, "OrderId should not be null"
    if (category == "NE"):
        assert return_res.json()["returnOrder"]["category"] == "Not Expired", "Category should be Not Expired"
    else:
        assert return_res.json()["returnOrder"]["category"] == "Expired", "Category should be Expired"
    assert return_res.json()["returnOrder"]["lines"][0]["batchNumber"] == batch_num
    assert return_res.json()["returnOrder"]["lines"][0]["batchId"] == batchId
    assert return_res.json()["returnOrder"]["lines"][0]["quantity"] == qty
    assert return_res.json()["returnOrder"]["lines"][0]["productVariantId"] == productId
    assert return_res.json()["returnOrder"]["importSource"] == "manual"


