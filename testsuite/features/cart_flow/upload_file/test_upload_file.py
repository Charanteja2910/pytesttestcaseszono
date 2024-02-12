from features.orders.uploadfile import upload_response,add_to_cart_response,mapped_data
from settings.conftest import checking_the_status_code_201,checking_the_status_code_422
from features.orders.upload_files.pofile_details import pofile_data
from features.orders.get_pofile import get_pofile_data
upload_file_response = upload_response

def test_upload_file():
    if(checking_the_status_code_201(upload_file_response)):
        product_skus = []
        for i in add_to_cart_response["orders"][0]["orderLine"]:
            product_skus.append(i["sku"])

        pofile_id = add_to_cart_response["orders"][0]["pofileId"]

        pofile_res = pofile_data(pofile_id)
        order_created = []
        for i in pofile_res.json()["lines"]:
            if i["status"] == "ORDER_CREATED":
                order_created.append(i["productVariant"]["sku"])

        pofile_ids = []
        pofile_res = get_pofile_data()
        for i in pofile_res.json()["files"]:
            pofile_ids.append(i["id"])

        for i in upload_file_response.json():
            assert i["uploadedProductName"] != None, "Dt_Product_name should not be empty"
            assert isinstance(i["sequence"],int), "Sequence value should be integer"
            assert i["sequence"] <= len(upload_file_response.json()), "Sequence value should not be greater that size of uploaded_response"
            if (i["status"] == "UNMAPPED"):
                assert(i["principalErpSku"] == None and i["pts"] == None and i["principalProductName"] ==None)
                assert i["errorMessage"], "Error message not there for unmapped product"
                assert i["errorMessage"] == "Product is not mapped.", "Error message was not correct"
            elif (i["status"] == "MAPPED"):
                assert (i["principalErpSku"] != None and i["pts"] != None), "Mapped products sku and pts should not be empty"
                assert i["errorMessage"] == None, "Error message was not correct"
        assert len(mapped_data) == len(add_to_cart_response["orders"][0]["orderLine"]), "added products to cart not correct"
        assert add_to_cart_response["orders"][0]["importSource"] == "upload","importSource should be upload"
        assert pofile_id in pofile_ids, "given pofile_id is not in pofilesData"
        assert len(product_skus) == len(order_created), "Both lengths should be equal"
        for i in product_skus:
            assert i in order_created, "item not added to the cfa cart in pofile details"

    elif(checking_the_status_code_422(upload_file_response)):
        if ("response" in upload_file_response.json()):
            assert upload_file_response.json()["response"]["message"] == "Product mapping failed"
            print("Something went wrong")
        else:
            assert upload_file_response.json()["variables"]["message"] == "File not mapped - Template not found during parsing", "Error message was not correct while ticket created"
            print("ticket created")

    elif(upload_file_response.status_code == 400):
        print(upload_file_response.json()["message"]["message"])