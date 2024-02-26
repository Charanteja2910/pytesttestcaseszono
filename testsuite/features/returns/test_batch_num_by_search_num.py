from features.returns.search_based_on_batch_num import get_res_based_on_batch_num,batch_num,header_division_id
from settings.conftest import checking_the_status_code_201

batch_num_res = get_res_based_on_batch_num()
def test_search_by_batch_num():
    assert checking_the_status_code_201(batch_num_res)
    if (len(batch_num_res.json()["response"]) != 0):
        assert batch_num_res.json()["response"][0]["batchCode"] == batch_num, "BatchCode should be equal to batch_num"
        assert batch_num_res.json()["response"][0]["headDivisionId"] == header_division_id, "Header_division_id is not equal to given header_division_id"
        assert batch_num_res.json()["response"][0]["productVariantId"] != None