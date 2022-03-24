from data_access_layer.dal_login_interface import LogInDataAccessLayerInterface

from utilities.connection_manager import connection


class LogInDataAccessLayerImplementation(LogInDataAccessLayerInterface):

    def select_employee_information(self, username: str):
        sql = "select employee_password from employees where employee_username = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [username])
        employee_password = cursor.fetchone()#[0]
        result_list = [employee_password]
        #print(type(result_list))
        return result_list





            # if employee_password is None:
            #     return None
            # else:
            #     return employee_password

