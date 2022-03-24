from entities.reimbursement_totals_interfaces import ReimbursementTotalsServiceInterface
from data_access_layer.dal_reimbursement_total import ReimbursementTotalsDataImplementation
from utilities.custom_exceptions.total_is_zero import TotalIsZero

data_implementation = ReimbursementTotalsDataImplementation

def check_completed_reimbursement_total(employee_id: int) -> float or None:
    data_return = (None)
    try:
        data = float(data_return)
        return data
    except TypeError:
        print("You have no completed reimbursements.")

whut = check_completed_reimbursement_total(5)
print(whut)