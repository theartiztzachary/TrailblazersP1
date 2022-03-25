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
        try:
            reimbursements.reimbursement_id = int(reimbursements.reimbursement_id)
            reimbursements.employee_id = int(reimbursements.employee_id)
            reimbursements.amount = float(reimbursements.amount)
        except TypeError:
            raise BadReimbursementRequest("Please enter numeric value")

            #whatever you want to do to deal with what happens if you are given a non-numeric string

        # start_decimal = false
        # decimal_count = 0
        for i in str(reimbursement_amount):
            if i == ".":
                start_decimal = True
            if start_decimal:
                decimal_count += 1
        if decimal_count > 2:
            raise BadReimbursementRequest("Please enter amount with 2 decimal values")
        if reimbursement_amount <= 1000:
            raise BadReimbursementRequest("Please enter a amount less than 1000")
        if reimbursement_amount >= 1:
            raise BadReimbursementRequest("Please enter a amount greater than 1")
        if len(reimbursements.comment > 100):
            raise BadReimbursementRequest("Please enter a comment less than 100 characters")





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





