from abc import ABC, abstractmethod

from data_access_layer.employee_dao_interface import EmployeeDAOInterface
from entities.reimbursement_data import ReimbursementData


class EmployeeServiceLayerInterface(ABC):

    def __init__(self, employee_dao: EmployeeDAOInterface):
        self.employee_dao = employee_dao

    @abstractmethod
    def serl_submit_reimbursement(self, reimbursements: ReimbursementData) -> ReimbursementData:
        pass


