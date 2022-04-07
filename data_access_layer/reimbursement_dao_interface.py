from abc import ABC, abstractmethod

from entities.reimbursement_data import ReimbursementData


class ReimbursementDAOInterface(ABC):

    @abstractmethod
    def cancel_reimbursement_request(self, reimbursement_id: int):
        pass



