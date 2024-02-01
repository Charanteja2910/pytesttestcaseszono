from features.orders.upload_files.delete_po_file import delete_po_file,pofile_id
from features.orders.get_pofile import get_pofile_data
from settings.conftest import checking_the_status_code_200

delete_po_file_res = delete_po_file()
delete_pofile_data = delete_po_file_res.json()

pofile_res = get_pofile_data().json()
po_data = []

for i in pofile_res["files"]:
    po_data.append(i["id"])

def test_delete_po_file():
    assert checking_the_status_code_200(delete_po_file_res)
    assert pofile_id not in po_data, "Assertion Failure Pofile not deleted"
