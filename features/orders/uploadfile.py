import requests
from user.test_login import main_workspace,main_token
from settings.conftest import main_url
from settings.api_requests import postApi

file_path = r"C:\Users\USER\Downloads\UAT PO.xlsx"
# file_path = r"C:\Users\USER\Downloads\RAJASTHAN DRUG HOUSE.xlsx"
# file_path = r"C:/Users/USER/Downloads/Book%20(6)_RAJ.pdf"



url =main_url+"/commerce-v2/poFile/upload/"+f"{main_workspace[0]["pId"]}"+"?customerId="+f"{main_workspace[0]["cId"]}"+"&importSource=upload&parserType=C2D_ORDER"

payload = {
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
response = requests.post(url, payload, headers=headers, files=files)
mapped_data = []
unmapped_data = []
for i in response.json():
    if i["status"] == "MAPPED":
        a = {"pvId": i["productVariantId"], "qty": i["unitQuantity"], "PF_line_id": i["id"],"pf_id":i["poFileId"]}
        mapped_data.append(a)
    else:
        a = {"product_name": i["distributorProductName"], "data": {"pvId": i["productVariantId"], "qty": i["unitQuantity"], "PF_line_id": i["id"], "pf_id":i["poFileId"]}}
        unmapped_data.append(a)

# print(mapped_data)

empty_data = []
for i in unmapped_data:
    payload = {
        "searchKey": i["product_name"]
    }
    url = f"{main_url}/commerce-v2/products/search/{main_workspace[0]["pId"]}?customerId={main_workspace[0]["cId"]}"
    response = postApi(url,payload)
    if response["total"] != 0:
        if i["data"]["qty"] == 0:
            a = {"pvId": response["products"][0]["productVariants"][0]["productVariantId"],"qty":response["products"][0]["productVariants"][0]["minOrderQty"],"PF_line_id":i["data"]["PF_line_id"],"pf_id":i["data"]["pf_id"]}
            mapped_data.append(a)
        else:
            a = {"pvId": response["products"][0]["productVariants"][0]["productVariantId"],
                 "qty": i["data"]["qty"],
                 "PF_line_id": i["data"]["PF_line_id"], "pf_id": i["data"]["pf_id"]}
            mapped_data.append(a)
    else:
        a = f"{i["product_name"]} not there in products"
        empty_data.append(a)


print(len(mapped_data))

# for i in mapped_data:
#     print(i)

def add_cart():
    payload = {
    "customerId": main_workspace[0]["cId"],
    "sellerWorkspaceId": main_workspace[0]["pId"],
    "source": "upload",
    "poFileId": mapped_data[0]["pf_id"],
    "lines": [
        {
            "productVariantId": i["pvId"],
            "quantity": i["qty"],
            "poFileLineId": i["PF_line_id"]
        } for i in mapped_data
    ]
}
    url = main_url+"/commerce-v2/orders/additemtoactiveorder/"+f"{main_workspace[0]["pId"]}"
    response = postApi(url,payload)
    return response
    # print(response)
