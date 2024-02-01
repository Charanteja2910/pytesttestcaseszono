from features.orders.upload_files.delete_items_to_be_add_option import delete_items_to_be_added,pofile_id,po_file_line_ids
from features.orders.upload_files.pofile_details import pofile_data
from settings.conftest import checking_the_status_code_200


delete_items_to_be_added_res = delete_items_to_be_added()

po_file_details_res = pofile_data(pofile_id)
po_file_details_data = po_file_details_res.json()

def test_delete_items_to_be_added():
    assert checking_the_status_code_200(delete_items_to_be_added_res)
    if len(po_file_line_ids) ==0:
        print("UNMAPPED products not there in the pofile")
    else:
        for i in po_file_details_data["lines"]:
            assert "UNMAPPED" not in i["status"],"Assertion Failure product not deleted"


