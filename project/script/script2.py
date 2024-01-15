import requests
from requests.exceptions import Timeout


def employees_json():
        response = requests.get("https://dummy.restapiexample.com/api/v1/employees")
        json_response = response.json()
        return json_response

       
def employees_successful_get():
        response = requests.get("https://dummy.restapiexample.com/api/v1/employees")
        return (f"{response} error in get")


def employees_unsuccessful_get():
        response = requests.get("https://dummy.restapiexample.com/api/v1/employees")
        return (f"{response} error in get")

      
def employees_get_with_timeout():
        response = requests.get("https://dummy.restapiexample.com/api/v1/employees", Timeout = 0.001)
        return response


def employees_malperformed_url():
        response = requests.get("http://www.thiswebsitedoesnotexist.com")
        return response


def get_employees(employee_id):
    response = requests.get(f"https://dummy.restapiexample.com/api/v1/employees{employee_id}")
    if response.status_code == 200:
        return response.json()
    else:
        return None


'''var = employees_successful_get()
print(var)
var2 = employees_unsuccessful_get()
print(var2)
var1 = employees_json()
print(var1)
var3 = get_employee(12)
print(var3)'''