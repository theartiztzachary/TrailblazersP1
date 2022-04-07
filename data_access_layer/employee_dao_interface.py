from abc import ABC, abstractmethod


class EmployeeDAOInterface(ABC):

    @abstractmethod
    def cancel_reimbursement_request(self):
        pass


