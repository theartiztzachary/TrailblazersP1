from abc import ABC, abstractmethod

from entities.reimbursement_data import ReimbursementData


class ReimbursementDAOInterface(ABC):

    @abstractmethod
    def cancel_reimbursement_request(self, reimbursement_id: int):
        pass

# delete if it does not work
    @abstractmethod
    def get_status_code_update(self, reimbursement_id: int):
        pass

    @abstractmethod
    def get_reimbursement_id_number(self, reimbursement_id: int):
        pass


