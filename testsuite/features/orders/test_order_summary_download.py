from features.orders.order_summery_download import order_summary_download
from settings.conftest import checking_the_status_code_200

import io
import pandas as pd
import json

download_res = order_summary_download()[0]
order_id_data = order_summary_download()[1][0]
data = download_res.text

# Assuming data is in CSV format, adjust this line accordingly if it's in a different format
df = pd.read_csv(io.StringIO(data))

# Specify the Excel file path where you want to save the data
excel_file_path = "output.xlsx"

# Save the DataFrame to Excel
df.to_excel(excel_file_path, index=False)

# Optionally, print a message to confirm that the Excel file has been saved
print(f"Data saved to {excel_file_path}")



df = pd.read_excel(r"C:\Users\USER\Desktop\pytestproject\testsuite\features\orders\output.xlsx")

# Convert the DataFrame to JSON
json_data = df.to_json(orient="records")

data = json.loads(json_data)

def test_order_summery_download():
    assert checking_the_status_code_200(download_res)
    for i in data:
        assert i["Order Number"] == order_id_data[1]
