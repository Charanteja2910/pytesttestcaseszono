from features.returns.return_submit_by_customer import return_submitted_by_customer,return_order_id
from settings.conftest import checking_the_status_code_201
from features.returns.create_return_order import productId,batchId,batch_num,qty,category
from features.returns.search_based_on_batch_num import header_division_id

return_submit_res = return_submitted_by_customer()
def test_submit_return():
    assert checking_the_status_code_201(return_submit_res)
    assert return_submit_res.json()["returnOrder"]["id"] == return_order_id
    assert return_submit_res.json()["returnOrder"]["headDivisionId"] == header_division_id
    assert return_submit_res.json()["returnOrder"]["status"] == "SUBMITTED"
    assert return_submit_res.json()["returnOrder"]["lines"][0]["batchNumber"] == batch_num
    assert return_submit_res.json()["returnOrder"]["lines"][0]["batchId"] == batchId
    assert return_submit_res.json()["returnOrder"]["lines"][0]["productVariantId"] == productId
    assert return_submit_res.json()["returnOrder"]["lines"][0]["quantity"] == qty
    assert return_submit_res.json()["returnOrder"]["lines"][0]["linePrice"] == return_submit_res.json()["returnOrder"]["lines"][0]["unitPrice"]*qty
