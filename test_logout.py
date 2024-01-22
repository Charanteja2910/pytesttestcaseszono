# import requests
#
#
# def test_log_out(main_url):
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiMDkzZWZmNmEtMTM0Yy00ZDFmLWIyNjQtMTVlYTllOTU0YTBmIiwid29ya3NwYWNlSWQiOiJlY2RjYTMxOS1mMDZjLTQzZWYtYjYxMi05YTkwYjU0Njg0MWYiLCJ3b3Jrc3BhY2VSb2xlcyI6WyJhZG0iXX0sImlhdCI6MTcwMzI0Nzg3MywiZXhwIjoxNzAzMjUzODczfQ.MGwVECBQb3pXLVhr5y8tEhxnzdL4TMj1dg3cfTtlA9g"
#     }
#     response = requests.put(main_url+"/logout",headers = headers)
#     assert response.status_code == 200