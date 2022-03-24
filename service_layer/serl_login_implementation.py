from data_access_layer.dal_login_implementation import LogInDataAccessLayerImplementation
from data_access_layer.dal_login_interface import LogInDataAccessLayerInterface
from service_layer.serl_login_interface import LogInServiceLayerInterface
from utilities.custom_exceptions.incorrect_password import IncorrectPassword


class LogInServiceLayerImplementation(LogInServiceLayerInterface):

    def __init__(self, login_data_access_object: LogInDataAccessLayerImplementation):

        self.login_data_access_object = login_data_access_object

    def service_select_employee_information(self, username: str, password: str):
        result = self.login_data_access_object.select_employee_information(username)
        try:
            unpacked_result = result[0][0]
        except TypeError as e:
            assert str(e) == "The employee username could not be found within the database. Please try again. "
        if unpacked_result == password:
            return True
        else:
            raise IncorrectPassword("The password you have given is incorrect. Please try again.")
