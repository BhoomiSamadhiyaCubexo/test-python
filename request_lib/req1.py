import requests
from requests.exceptions import HTTPError


def response():
      """
      >>> response = requests.get(https://dummy.restapiexample.com/api/v1/employees)
      print(response)
      >>> response.status_code
      200

      """

if response:
      print("success")
else:
      print("error")




"-----------------------------------------------------------"


for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')  
    else:
        print('Success!')