from data_access_layer.employee_dao_imp import EmployeeDAOImp
from entities.reimbursement_data import ReimbursementData
from service_layer.employee_serl_interface import EmployeeServiceLayerInterface



class EmployeeServiceLayerImp(EmployeeServiceLayerInterface):

    def __init__(self, dao_imp: EmployeeDAOImp):
        self.dao_imp = dao_imp

    def serl_submit_reimbursement(self, reimbursements: ReimbursementData) -> ReimbursementData:
        reimbursements.reimbursement_id = int(reimbursements.reimbursement_id)
        reimbursements.employee_id = int(reimbursements.employee_id)
        reimbursements.amount = int(reimbursements.amount)
        if type(reimbursement_id) == int:
            return self.serl_submit_reimbursement()





