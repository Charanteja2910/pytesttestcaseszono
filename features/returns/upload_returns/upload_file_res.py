from features.returns.upload_returns.upload_file import upload_file
from settings.conftest import checking_the_status_code_201,checking_the_status_code_422

upload_return_res = upload_file()

if (checking_the_status_code_422(upload_return_res)):
    print(upload_return_res["message"]["error"])
elif (checking_the_status_code_201(upload_return_res)):
    upload_id = upload_return_res.json()["id"]



