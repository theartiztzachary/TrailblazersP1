from data_access_layer.dal_login_interface import LogInDataAccessLayerInterface


class LogInDataAccessLayerImplementation(LogInDataAccessLayerInterface):

    def select_employee_information(self, username: str, password: str):
        pass