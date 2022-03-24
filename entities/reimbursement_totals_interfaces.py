from abc import ABC, abstractmethod

# This is the interface for the data access layer's ability to grab the complete and pending reimbursement totals.
class ReimbursementTotalsDataInterface(ABC):

    # This method will get the sum of all the approved reimbursements.
    @abstractmethod
    def get_completed_reimbursement_total(self, employee_id: int) -> tuple:
        pass

    # This method will get the sum of all the pending reimbursements.
    @abstractmethod
    def get_pending_reimbursement_total(self, employee_id: int) -> tuple:
        pass

# This is the interface for the service layer's ability to check if the employee has reimbursement totals or not.
class ReimbursementTotalsServiceInterface(ABC):

    # This method will check if there is a sum of all the approved reimbursements.
    @abstractmethod
    def check_completed_reimbursement_total(self, employee_id: str) -> float or None:
        pass

    # This method will check if there is a sum of all the pending reimbursements.
    @abstractmethod
    def check_pending_reimbursement_total(self, employee_id: str) -> float or None:
        pass