from data_access_layer.employee_dao_interface import EmployeeDAOInterface


class EmployeeDAOImp(EmployeeDAOInterface):

    #  check to make sure request_number is in database; if true, return true, else return false
    def cancel_reimbursement_request(self, request_number: int) -> bool:
        pass
