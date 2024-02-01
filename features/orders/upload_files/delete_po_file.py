from settings.conftest import main_url
from settings.api_requests import deleteApi
from user.test_login import main_workspace
from features.orders.get_pofile import get_pofile_data

pofile_data = get_pofile_data().json()
data = []
for i in pofile_data["files"]:
    data.append(i["id"])

pofile_id = data[0]
def delete_po_file():
    payload = {
        "poFileId": pofile_id,
        "customerId": main_workspace[0]["cId"]
    }
    url = f"{main_url}/commerce-v2/poFile/{main_workspace[0]["pId"]}"
    res = deleteApi(url,payload)
    return res