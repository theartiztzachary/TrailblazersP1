from abc import ABC, abstractmethod

from entities.reimbursement_data import ReimbursementData


class ReimbursementServiceInterface(ABC):

    @abstractmethod
    def service_cancel_reimbursement_request(self, request_number: int,
                                             employee_reimbursement_request: ReimbursementData):
        pass
