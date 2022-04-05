from abc import ABC, abstractmethod

from entities.reimbursement_data import ReimbursementData


class EmployeeDAOInterface(ABC):

    @abstractmethod
    def submit_reimbursement(self, reimbursements: ReimbursementData) -> ReimbursementData:
        pass

    @abstractmethod
    def get_reimbursement_info_by_id(self, reimbursement_id: int) -> ReimbursementData:
        pass
