from settings.conftest import main_url
from user.test_login import main_workspace,main_token
from features.returns.get_header_divisions import header_division
from features.returns.get_cfa import get_cfa
import requests

header_division_id = header_division().json()[2]["id"]
cfa_id = get_cfa().json()["customerCFADivisions"][0]["id"]


file_path = r"C:\Users\USER\Downloads\Return upload.csv"



def upload_file():
    url = f"{main_url}/hub/claims/return-orders/upload/{main_workspace[1]["pId"]}?customerId={main_workspace[1]["cId"]}&sellerWorkspaceId={main_workspace[1]["pId"]}&importSource=upload&parserType=C2D_RETURNS&cfaId={cfa_id}&headDivisionId={header_division_id}&category=NE"
    headers = {
        'Authorization': 'Bearer ' + f"{main_token}"
    }
    files = {'file': open(file_path, 'rb')}
    # Make the request with the file
    response = requests.post(url,headers=headers, files=files)
    return response
