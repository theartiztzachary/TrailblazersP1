from unittest.mock import MagicMock

from data_access_layer.employee_dao_imp import EmployeeDAOImp
from entities.reimbursement_data import ReimbursementData
from service_layer.employee_serl_imp import EmployeeServiceLayerImp
from utilities.custom_exceptions.bad_reimbursement_request import BadReimbursementRequest

employee_dao = EmployeeDAOImp()
employee_serl = EmployeeServiceLayerImp(employee_dao)

mocking_object = ReimbursementData("0", "1", "100.00", "Hotel", "stayed in HamptonInn", "pending")


def test_serl_submit_reimbursement():
    employee_serl.dao_imp.submit_reimbursement = MagicMock(return_value=mocking_object)
    result_data = employee_serl.serl_submit_reimbursement(mocking_object)
    assert result_data.reimbursement_id == 0
    # employee_serl.dao_imp.submit_reimbursement.assert_called_with(mocking_object) # <-add the number you are looking for :)

# def test_serl_catch_numeric_string_typecasted():
#     employee_serl.dao_imp.submit_reimbursement = MagicMock(return_value=ReimbursementData(2, 1, 75.00, "hotel", "stayed at Hilton", "approved"))
#
#
# def test_serl_catch_non_numeric_string_not_typecasted():
#     employee_serl.dao_imp.submit_reimbursement = MagicMock(return_value=int)
#     try:
#         employee_serl.serl_submit_reimbursement("one")
#         assert False
#     except BadReimbursementRequest as e:
#         assert str(e) == "Please enter numeric value"


def test_serl_reimbursement_amount_above_the_limit():
    reimbursementdata = ReimbursementData("0", "1", "10000.00", "Hotel", "stayed in HamptonInn", "pending")
    try:
        employee_serl.serl_submit_reimbursement(reimbursementdata)
        assert False
    except BadReimbursementRequest as e:
        assert str(e) == "Please enter a amount less than 1000"

def test_serl_reimbursement_amount_below_the_limit():
    reimbursementdata = ReimbursementData(0, 1, -100, "Hotel", "stayed in HamptonInn", "pending")
    try:
        employee_serl.serl_submit_reimbursement(reimbursementdata)
        assert False
    except BadReimbursementRequest as e:
        assert str(e) == "Please enter a amount greater than 1"

def test_serl_reimbursement_amount_decimal_digits():
    reimbursementdata = ReimbursementData(0, 2, 27.892, "Gas", "Filled gas to travel to Newyork", "Approved")
    try:
        employee_serl.serl_submit_reimbursement(reimbursementdata)
        assert False
    except BadReimbursementRequest as e:
        assert str(e) == "Please enter amount with 2 decimal values"

def test_serl_length_of_comments():
    reimburesementdata = ReimbursementData(0, 1, 100.00, "Hotel", "I went to meet the customer on Monday March 21st. We went out for dinner. It was too late. While driving back I got struck in traffic and I was very tired too. It was already 11.00PM and looked like the traffic is still not cleared. So I stayed in HamptonInn Hotel that night ", "pending")
    try:
        employee_serl.serl_submit_reimbursement(reimburesementdata)
        assert False
    except BadReimbursementRequest as e:
        assert str(e) == "Please enter a comment less than 100 characters"



