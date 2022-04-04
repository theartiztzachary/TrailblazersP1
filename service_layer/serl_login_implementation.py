from data_access_layer.dal_login_implementation import LogInDataAccessLayerImplementation
from service_layer.serl_login_interface import LogInServiceLayerInterface
from utilities.custom_exceptions.employee_not_found import EmployeeNotFound
from utilities.custom_exceptions.incorrect_password import IncorrectPassword


class LogInServiceLayerImplementation(LogInServiceLayerInterface):

    def __init__(self, login_data_access_object: LogInDataAccessLayerImplementation):
        self.login_data_access_object = login_data_access_object

    def service_select_employee_information(self, username: str, password: str):
        result = self.login_data_access_object.select_employee_information(username)
        unpacked_result_level_one = result[0]  #Unpacking either list(None) or List(tuple(password))
        if unpacked_result_level_one is None:
            raise EmployeeNotFound("The employee username could not be found within the database. Please try again.")
        else:
            unpacked_result_level_two = unpacked_result_level_one[0]  #Unpacking tuple(password)
            if unpacked_result_level_two == password:
                result2 = self.login_data_access_object.select_employee_id(username)
                unpacked_result_level_one = result2[0]
                unpacked_employee_id_number = unpacked_result_level_one[0]  # Unpacking tuple(password)
                return unpacked_employee_id_number
            else:
                raise IncorrectPassword("The password you have given is incorrect. Please try again.")


