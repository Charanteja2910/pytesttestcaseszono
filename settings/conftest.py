import pytest


main_url = "https://api-qa.beta.pharmconnect.com"
mobile_number= 9898989833

# 9898989833
# 9647297912
#9898989833
#8008472669
#9448066818
#8008472669
#9810424353
#9647297912
#6661166666
#9172266773

def checking_the_status_code_201(response):
    if response.status_code == 201:
        return True

def checking_the_status_code_200(response):
    if response.status_code == 200:
        return True
def checking_the_status_code_422(response):
    if response.status_code == 422:
        return True