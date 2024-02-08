from features.orders.get_pofile import get_pofile_data
from features.orders.upload_files.pofile_details import pofile_data
from user.test_login import main_workspace
from settings.conftest import main_url
from settings.api_requests import deleteApi

po_file_data = get_pofile_data().json()
data = []
for i in po_file_data["files"]:
    data.append(i["id"])

pofile_id = data[0]

po_details_res = pofile_data(pofile_id)
po_file_line_ids = []
if po_details_res.json() == []:
    print(f"products not there in the {pofile_id}")
else:
    for i in po_details_res.json()["lines"]:
        if i["status"] == "UNMAPPED":
            po_file_line_ids.append(i["poFileLineId"])

# items_deleted = len(po_file_line_ids)
# data_length = len(po_details_res.json()["lines"])

def delete_items_to_be_added():
    payload = {
      "poFileLineIds": [
        i for i in po_file_line_ids
      ],
      "poFileId": pofile_id,
      "customerId": main_workspace[0]["cId"]
    }
    url = f"{main_url}/commerce-v2/poFile/{main_workspace[0]["pId"]}"
    res = deleteApi(url,payload)
    return res
