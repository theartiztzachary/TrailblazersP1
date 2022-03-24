from unittest.mock import MagicMock

from data_access_layer.dal_login_implementation import LogInDataAccessLayerImplementation
#from entities.employee_data import EmployeeData
from service_layer.serl_login_implementation import LogInServiceLayerImplementation
from utilities.custom_exceptions.employee_not_found import EmployeeNotFound
from utilities.custom_exceptions.incorrect_password import IncorrectPassword

login_data_access_object = LogInDataAccessLayerImplementation()
login_service_object = LogInServiceLayerImplementation(login_data_access_object)

# test_a_gator = EmployeeData(1, "Albert", "Gator", "AGator", "Password")

def test_select_employee_information_success(): #MOCKED
    login_service_object.login_data_access_object.select_employee_information = MagicMock(return_value=[('Password',)])
    result = login_service_object.service_select_employee_information("AGator", "Password")
    assert result == "Password"


def test_select_employee_information_incorrect_username(): #MOCKED
    try:
        login_service_object.login_data_access_object.select_employee_information = MagicMock(
        return_value=[None])
        login_service_object.service_select_employee_information("WGator", "Password")
        assert False
    except EmployeeNotFound as e:
        assert str(e) == "The employee username could not be found within the database. Please try again."
        #assert result is None


def test_select_employee_information_incorrect_password(): #MOCKED
    try:
        login_service_object.login_data_access_object.select_employee_information = MagicMock(return_value=[('Password',)])
        login_service_object.service_select_employee_information("AGator", "WrongPassword")
        assert False
    except IncorrectPassword as e:
        assert str(e) == "The password you have given is incorrect. Please try again."


