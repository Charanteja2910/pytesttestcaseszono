from features.Home.cumulative_returns import cumulative_returns
from settings.conftest import checking_the_status_code_201
from features.returns.returns_count_of_multiple_priniciples import total_returns


cumulative_res = cumulative_returns()


# print(cumulative_res)

print(cumulative_res.json()["totalReturns"])
print(cumulative_res.json()["totalReturnAmount"])

def test_cumulative_returns():
    assert checking_the_status_code_201(cumulative_res)
    assert cumulative_res.json()["totalReturns"] != None, "TotalReturns should not be empty in cumulative orders"
    assert total_returns == int(cumulative_res.json()["totalReturns"])
    assert cumulative_res.json()["totalReturnAmount"] != None