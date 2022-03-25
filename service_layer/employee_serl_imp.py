from entities.reimbursement_data import ReimbursementData
from service_layer.employee_serl_interface import EmployeeServiceLayerInterface


class EmployeeServiceLayerImp(EmployeeServiceLayerInterface):
    def serl_submit_reimbursement(self, reimbursements: ReimbursementData) -> ReimbursementData:
        pass