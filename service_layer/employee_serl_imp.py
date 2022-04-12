from data_access_layer.employee_dao_imp import EmployeeDAOImp
from entities.reimbursement_data import ReimbursementData
from service_layer.employee_serl_interface import EmployeeServiceLayerInterface
from utilities.custom_exceptions.bad_reimbursement_request import BadReimbursementRequest


class EmployeeServiceLayerImp(EmployeeServiceLayerInterface):

    def __init__(self, dao_imp: EmployeeDAOImp):
        self.dao_imp = dao_imp

    def serl_submit_reimbursement(self, reimbursements: ReimbursementData) -> ReimbursementData:
        reimbursement_amount = reimbursements.amount
        start_decimal = False
        decimal_count = 0
        try:   # typecasting the input
            reimbursements.reimbursement_id = int(reimbursements.reimbursement_id)
            reimbursements.employee_id = int(reimbursements.employee_id)
            reimbursements.amount = float(reimbursements.amount)
        except ValueError:
            raise BadReimbursementRequest(
                "Please enter numeric value for reimbursement_id,employee_id and float value for amount")
        for i in str(reimbursement_amount):
            if i == ".":
                start_decimal = True
                continue
            if start_decimal:
                decimal_count += 1
        if decimal_count > 2:
            raise BadReimbursementRequest("Please enter amount with 2 decimal values")
        if reimbursements.amount >= 1000:
            raise BadReimbursementRequest("Please enter a amount less than 1000")
        if reimbursements.amount <= 1:
            raise BadReimbursementRequest("Please enter a amount greater than 1")
        if len(reimbursements.reimbursement_comment) > 100:
            raise BadReimbursementRequest("Please enter a comment less than 100 characters")

        returned_data = self.dao_imp.submit_reimbursement(reimbursements)
        return returned_data

        # for character in reimbursement_amount temporary holder is still a string version of the amount
        # if the character is '.'
        # started_decimal = true
        # if started_decimal
        # decimal_count += 1

        # if decimal_count > 2
        # raise error

        # if amount <= 1000 and amount >= 1
        # code here
        # raise error
