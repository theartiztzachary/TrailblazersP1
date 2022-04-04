from data_access_layer.dal_login_interface import LogInDataAccessLayerInterface
from utilities.connection_manager import connection


class LogInDataAccessLayerImplementation(LogInDataAccessLayerInterface):

    def select_employee_information(self, username: str):
        sql = "select employee_password from employees where employee_username = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [username])
        employee_password = cursor.fetchone()
        result_list = [employee_password]
        return result_list

    def select_employee_id(self, username: str):
        sql = "select employee_id from employees where employee_username = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [username])
        employee_id = cursor.fetchone()
        result_list = [employee_id]
        return result_list

