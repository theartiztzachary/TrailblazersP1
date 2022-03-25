from unittest.mock import MagicMock

from data_access_layer.employee_dao_imp import EmployeeDAOImp
from entities.reimbursement_data import ReimbursementData
from service_layer.employee_serl_imp import EmployeeServiceLayerImp


employee_dao = EmployeeDAOImp()
employee_serl = EmployeeServiceLayerImp()




def test_serl_submit_reimbursement():
    employee_serl.employee_dao.submit_reimbursement = MagicMock(return_value=ReimbursementData(0, 1, 100.00, "Hotel", "stayed in HamptonInn", "pending"))
    employee_serl.serl_submit_reimbursement(ReimbursementData)
    employee_serl.serl_submit_reimbursement.assert_called_with(1)

def test_serl_catch_non_numeric_string_typecasted():
    pass

def test_serl_catch_non_numeric_string_not_typecasted():
    pass

def test_serl_reimbursement_amount_range():
    pass

def test_serl_reimbursement_amount_decimal_digits():
    pass

def test_serl_length_of_comments():
    pass


