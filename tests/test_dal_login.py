from data_access_layer.dal_login_implementation import LogInDataAccessLayerImplementation
from utilities.custom_exceptions.employee_not_found import EmployeeNotFound

LogIn_data_access_object = LogInDataAccessLayerImplementation()


def test_select_employee_information_success():
    result = LogIn_data_access_object.select_employee_information("AGator")
    assert result == [('Password',)]


def test_select_employee_information_incorrect_username_return_empty():

    result = LogIn_data_access_object.select_employee_information("WGator")
    assert result == [None]


