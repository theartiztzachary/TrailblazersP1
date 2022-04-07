from unittest.mock import MagicMock

from data_access_layer.employee_dao_imp import EmployeeDAOImp
from entities.reimbursement_data import ReimbursementData
from service_layer.employee_serl_imp import EmployeeServiceLayerImp
from utilities.custom_exceptions.bad_reimbursement_request import BadReimbursementRequest

employee_dao = EmployeeDAOImp()
employee_serl = EmployeeServiceLayerImp(employee_dao)

mocking_object = ReimbursementData("0", "1", "100.00", "Hotel", "stayed in HamptonInn", "pending")
mocking_object2 = ReimbursementData(0, 1, 100.00, "Hotel", "stayed in HamptonInn", "pending")


def test_serl_submit_reimbursement():
    employee_serl.dao_imp.submit_reimbursement = MagicMock(return_value=mocking_object2)
    result_data = employee_serl.serl_submit_reimbursement(mocking_object)
    assert result_data.reimbursement_id == 0
    employee_serl.dao_imp.submit_reimbursement.assert_called_with(mocking_object)


def test_serl_untypecastable_reimbursment_id():
    reimbursementdata = ReimbursementData("this is not a number", 1, 37.60, "gas", "Went to see the client", "approved")
    try:
        employee_serl.serl_submit_reimbursement(reimbursementdata)
        assert False
    except BadReimbursementRequest as e:
        assert str(e) == "Please enter numeric value for reimbursement_id,employee_id and float value for amount"


def test_serl_untypecastable_employee_id():
    reimbursementdata = ReimbursementData(1, "This is not a number", 37.60, "gas", "Went to see the client", "approved")
    try:
        employee_serl.serl_submit_reimbursement(reimbursementdata)
        assert False
    except BadReimbursementRequest as e:
        assert str(e) == "Please enter numeric value for reimbursement_id,employee_id and float value for amount"


def test_serl_untypecastable_amount():
    reimbursementdata = ReimbursementData(1, 2, "This is not float", "gas", "Went to see the client", "approved")
    try:
        employee_serl.serl_submit_reimbursement(reimbursementdata)
        assert False
    except BadReimbursementRequest as e:
        assert str(e) == "Please enter numeric value for reimbursement_id,employee_id and float value for amount"



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
    reimburesementdata = ReimbursementData(0, 1, 100.00, "Hotel",
                                           "I went to meet the customer on Monday March 21st. We went out for dinner. It was too late. While driving back I got struck in traffic and I was very tired too. It was already 11.00PM and looked like the traffic is still not cleared. So I stayed in HamptonInn Hotel that night ",
                                           "pending")
    try:
        employee_serl.serl_submit_reimbursement(reimburesementdata)
        assert False
    except BadReimbursementRequest as e:
        assert str(e) == "Please enter a comment less than 100 characters"
