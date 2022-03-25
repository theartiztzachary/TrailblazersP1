from abc import ABC, abstractmethod

from data_access_layer.employee_dao_interface import EmployeeDAOInterface
from entities.reimbursement_data import ReimbursementData


class EmployeeServiceLayerInterface(ABC):


    @abstractmethod
    def serl_submit_reimbursement(self, reimbursements: ReimbursementData) -> ReimbursementData:
        pass


