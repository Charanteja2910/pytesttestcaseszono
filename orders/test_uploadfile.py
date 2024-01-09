import requests
from user.test_login import main_workspace,main_token
from settings.conftest import main_url
from settings.api_requests import postApi

file_path = r"C:\Users\USER\Downloads\RAJASTHAN DRUG HOUSE.xlsx"

url = main_url+"/commerce-v2/poFile/upload/"+ f"{main_workspace[0]["pId"]}"
query_params = {
    'customerId': main_workspace[0]["cId"],
    'importSource': 'upload',
    'parserType': 'C2D_ORDER'
}
headers = {
    'Authorization': 'Bearer '+f"{main_token}"
}

# Prepare file for upload
files = {'file': open(file_path, 'rb')}

# Make the request with the file
response = requests.post(url, params=query_params, headers=headers, files=files)
data = []
for i in response.json():
    if i["status"] == "MAPPED":
        a = {"pvId": i["productVariantId"], "qty": i["unitQuantity"], "PF_line_id": i["id"],"pf_id":i["poFileId"]}
        data.append(a)

# print(data)



def add_cart():
    payload = {
    "customerId": main_workspace[0]["cId"],
    "sellerWorkspaceId": main_workspace[0]["pId"],
    "source": "upload",
    "poFileId": data[0]["pf_id"],
    "lines": [
        {
            "productVariantId": i["pvId"],
            "quantity": i["qty"],
            "poFileLineId": i["PF_line_id"]
        } for i in data
    ]
}
    url = main_url+"/commerce-v2/orders/additemtoactiveorder/"+f"{main_workspace[0]["pId"]}"
    response = postApi(url,payload)
    return response
