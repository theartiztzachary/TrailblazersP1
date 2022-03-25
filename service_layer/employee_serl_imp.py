from data_access_layer.employee_dao_imp import EmployeeDAOImp
from entities.reimbursement_data import ReimbursementData
from service_layer.employee_serl_interface import EmployeeServiceLayerInterface



class EmployeeServiceLayerImp(EmployeeServiceLayerInterface):

    def __init__(self, dao_imp: EmployeeDAOImp):
        self.dao_imp = dao_imp

    def serl_submit_reimbursement(self, reimbursements: ReimbursementData) -> ReimbursementData:
        # temporary_holder = reimbursements.amount
        try:
            reimbursements.reimbursement_id = int(reimbursements.reimbursement_id)
            reimbursements.employee_id = int(reimbursements.employee_id)
            reimbursements.amount = float(reimbursements.amount)
        except TypeError:
            pass
            #whatever you want to do to deal with what happens if you are given a non-numeric string

        # started_decimal = false
        # decimal_count = 0
        # for character in temporary_holder <- temporary holder is still a string version of the amount
            # if the character is '.'
                # started_decimal = true
            # if started_decimal
                # decimal_count += 1

        # if decimal_count > 2
            # raise error

        # if amount <= 1000 and amount >= 1
            # code here
        # raise error





