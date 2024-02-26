from settings.conftest import main_url
from settings.api_requests import deleteApi
from user.test_login import main_workspace
from features.returns.create_return_order import create_return_order
from features.returns.get_cfa import get_cfa

return_order_res = create_return_order()
cfa_id = get_cfa()


def returns_deletion():
    payload = {
        "customerId": main_workspace[0]["pId"],
        "cfaId":  cfa_id.json()["customerCFADivisions"][0]["id"],
        "returnOrderId": return_order_res.json()["returnOrder"]["id"]
    }
    url = f"{main_url}/hub/claims/return-orders/{main_workspace[0]["pId"]}?sellerWorkspaceId={main_workspace[0]["Pid"]}"
    res = deleteApi(url,payload)
    print(res.json())