from features.returns.upload_returns.edit_upload_return_file import edit_upload_return_file,quantity,lrNumber,lrDate,boxes,invoiceNumber,vehicleDetails,res_date
from settings.conftest import checking_the_status_code_201

edited_upload_return_res = edit_upload_return_file()


def test_edit_upload_return_file():
    assert checking_the_status_code_201(edited_upload_return_res)
    assert edited_upload_return_res.json()["returnOrder"]["lrNumber"] ==str(lrNumber)
    assert edited_upload_return_res.json()["returnOrder"]["lrDate"] == res_date
    assert edited_upload_return_res.json()["returnOrder"]["noOfBoxes"] == boxes
    assert edited_upload_return_res.json()["returnOrder"]["vehicleDetails"] == vehicleDetails
    for i in edited_upload_return_res.json()["returnOrder"]["lines"]:
        if i["batchId"] != "":
            assert i["quantity"] == quantity, "Quantity should be equal to updated quantity"
            assert i["invoiceNumber"] == str(invoiceNumber)


