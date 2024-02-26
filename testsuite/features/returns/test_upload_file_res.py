from features.returns.upload_returns.upload_file_res import upload_return_res
from settings.conftest import checking_the_status_code_201,checking_the_status_code_422
from features.returns.upload_returns.upload_file import header_division_id,cfa_id


def test_upload_return_file():
    if (checking_the_status_code_201(upload_return_res)):
        assert upload_return_res.json()["id"] != None
        assert upload_return_res.json()["cfaId"] == cfa_id
        assert upload_return_res.json()["headDivisionId"] == header_division_id
        assert upload_return_res.json()["importSource"] == "upload"
        for i in upload_return_res.json()["lines"]:
            if (i["batchId"] == ""):
                assert i["sku"] == None, "Sku should be null for Category mismatched batchcodes"
                assert i["productVariantId"] ==0 and i["linePrice"] == 0 and i["unitPrice"] ==0, "productId,unitPrice, linePrice should be 0"
                assert i["headDivisionId"] == header_division_id
            else:
                assert i["headDivisionId"] == header_division_id
                assert i["batchNumber"] != ""
                assert i["batchId"] != ""
                assert i["quantity"] != None
                assert i["expiryDate"] != ""
                assert i["productVariant"]["id"] != None
                assert i["productVariant"]["sku"] != ""
                assert i["productVariant"]["name"] != ""

    elif(checking_the_status_code_422(upload_return_res)):
        assert upload_return_res.json()["message"]
        print(upload_return_res.json()["message"]["error"])