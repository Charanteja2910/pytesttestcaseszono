from features.returns.upload_returns.upload_file_res import upload_return_res
from features.returns.upload_returns.submit_return import submit_return_res
from settings.conftest import checking_the_status_code_201


def test_upload_return_submit():
    if(checking_the_status_code_201(submit_return_res)):
        assert upload_return_res.json()["id"] == submit_return_res.json()["returnOrder"]["id"]
        assert submit_return_res.json()["returnOrder"]["importSource"] == "upload"
        assert len(upload_return_res.json()["lines"]) == len(submit_return_res.json()["returnOrder"]["lines"])
        for i in upload_return_res.json()["lines"]:
            for j in submit_return_res.json()["returnOrder"]["lines"]:
                if(j["batchId"] != ""):
                    if i["batchNumber"] == j["batchNumber"]:
                        assert i["batchId"] == j["batchId"]
                        assert i["quantity"] == j["quantity"]
                        assert i["productVariant"]["id"] == j["productVariant"]["id"]
                        assert i["productVariant"]["sku"] == j["productVariant"]["sku"]
                        assert i["productVariant"]["name"] == j["productVariant"]["name"]