from unittest.mock import MagicMock

from data_access_layer.employee_dao_imp import EmployeeDAOImp
from entities.reimbursement_data import ReimbursementData
from service_layer.employee_serl_imp import EmployeeServiceLayerImp
from utilities.custom_exceptions.bad_reimbursement_request import BadReimbursementRequest

employee_dao = EmployeeDAOImp()
employee_serl = EmployeeServiceLayerImp()




def test_serl_submit_reimbursement():
    employee_serl.employee_dao.submit_reimbursement = MagicMock(return_value=ReimbursementData(0, 1, 100.00, "Hotel", "stayed in HamptonInn", "pending"))
    employee_serl.serl_submit_reimbursement(ReimbursementData(int(0), int(1), float(100.00), "abc", "abc", "abc"))
    employee_serl.serl_submit_reimbursement.assert_called_with()

def test_serl_catch_non_numeric_string_typecasted():
    pass

def test_serl_catch_non_numeric_string_not_typecasted():
    pass

def test_serl_reimbursement_amount_range():
    reimbursementdata = ReimbursementData(0, 1, 10000.00, "Hotel", "stayed in HamptonInn", "pending")
    try:
        employee_serl.serl_submit_reimbursement(reimbursementdata)
        assert False
    except BadReimbursementRequest as e:
        assert str(e)

def test_serl_reimbursement_amount_decimal_digits():
    pass

def test_serl_length_of_comments():
    reimburesementdata = ReimbursementData(0, 1, 100.00, "Hotel", "I went to meet the customer on Monday March 21st. We went out for dinner. It was too late. While driving back I got struck in traffic and I was very tired too. It was already 11.00PM and looked like the traffic is still not cleared. So I stayed in HamptonInn Hotel that night ", "pending")
    try:
        employee_serl.serl_submit_reimbursement(reimburesementdata)
        assert False
    except BadReimbursementRequest as e:
        assert str(e)



