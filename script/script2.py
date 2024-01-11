import requests
from requests.exceptions import HTTPError


def employees_json():
        response = requests.get("https://dummy.restapiexample.com/api/v1/employees")
        json_response = response.json()
        return json_response
        
def employees_successful_get():
      response = requests.get("https://dummy.restapiexample.com/api/v1/employees")
      return "successful get"


def employees_unsuccessful_get():
      response = requests.get("https://dummy.restapiexample.com/api/v1/employees__1")
      return "error in get"
      
def employees_get_with_timeout():
        response = requests.get("https://dummy.restapiexample.com/api/v1/employees", timeout=0.001)
        return "time out"

def employees_malperformed_url():
        response = requests.get("https://dummy.restapiexample.com/api/v1/employees")
        return "NOT a malperforming api"

def employees_get_with_customheaders():
        p        


var = employees_successful_get()
print(var)
var2 = employees_unsuccessful_get()
print(var2)
var1 = employees_json()
print(var1)
