from features.schemes.filter_by_calender import filter_by_dates,start_date,end_date
from settings.conftest import checking_the_status_code_201
from datetime import datetime

filter_data = filter_by_dates().json()
def test_filter_by_date():
    assert checking_the_status_code_201(filter_by_dates())
    for i in filter_data["promotions"]:
        res_start_date = i["startsAt"]
        given_date_object1 = datetime.strptime(res_start_date, "%Y-%m-%dT%H:%M:%S.%fZ")
        res_end_date = i["endsAt"]
        given_date_object2 = datetime.strptime(res_end_date, "%Y-%m-%dT%H:%M:%S.%fZ")
        response_start_date = given_date_object1.strftime("%Y-%m-%d")
        response_end_date = given_date_object2.strftime("%Y-%m-%d")
        assert response_start_date <= start_date <= response_end_date and res_start_date <= end_date <= response_end_date


