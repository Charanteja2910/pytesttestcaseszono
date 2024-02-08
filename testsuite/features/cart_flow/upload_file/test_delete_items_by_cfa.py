from features.orders.upload_files.delete_items_by_cfa import delete_items_by_cfa,pofile_id,po_file_line_ids
from features.orders.upload_files.pofile_details import pofile_data
from settings.conftest import checking_the_status_code_200

delete_cfa_res = delete_items_by_cfa()


pofile_details_res = pofile_data(pofile_id)
pofile_details_data = pofile_details_res.json()
print(pofile_details_data)

def test_delete_items_by_cfa():
    assert checking_the_status_code_200(delete_cfa_res)
    if (len(po_file_line_ids) == 0):
        print("CFA delete option not there in po_file and mapped products not there")
    else:
        for i in pofile_details_data["lines"]:
            assert "ORDER_CREATED" != i["status"]

