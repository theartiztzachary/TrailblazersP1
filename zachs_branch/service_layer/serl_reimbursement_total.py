from zachs_branch.entities.reimbursement_data import ReimbursementData
from zachs_branch.entities.reimbursement_totals_interfaces import ReimbursementTotalsServiceInterface
from zachs_branch.data_access_layer.dal_reimbursement_total import ReimbursementTotalsDataImplementation

from zachs_branch.utilities.custom_exceptions.total_is_zero import TotalIsZero
from zachs_branch.utilities.custom_exceptions.no_history import NoHistory

class ReimbursementTotalsServiceImplementation(ReimbursementTotalsServiceInterface):
    def __init__(self, data_implementation: ReimbursementTotalsDataImplementation):
        self.data_implementation = data_implementation

    def check_completed_reimbursement_total(self, employee_id: str) -> float or None:
        employee_id_int = int(employee_id)
        data_return = self.data_implementation.get_completed_reimbursement_total(employee_id_int)
        try:
            data = float(data_return[0])
            return data
        except TypeError:
            raise TotalIsZero("You have no completed reimbursements.")

    def check_pending_reimbursement_total(self, employee_id: str) -> float or None:
        employee_id_int = int(employee_id)
        data_return = self.data_implementation.get_pending_reimbursement_total(employee_id_int)
        try:
            data = float(data_return[0])
            return data
        except TypeError:
            raise TotalIsZero("You have no pending reimbursements.")

    def check_full_history(self, employee_id: str) -> [ReimbursementData]:
        return_list = []
        employee_id_int = int(employee_id)
        history_return = self.data_implementation.get_all_reimbursements(employee_id_int)
        if len(history_return) > 0:
            for i in range(len(history_return)):
                return_list.append(ReimbursementData(*history_return[i]))
            return return_list
        raise NoHistory("You have no reimbursement history.")