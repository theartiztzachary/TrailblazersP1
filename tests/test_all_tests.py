from unittest.mock import MagicMock
from decimal import Decimal

from data_access_layer.dal_login_implementation import LogInDataAccessLayerImplementation
from service_layer.serl_login_implementation import LogInServiceLayerImplementation
from data_access_layer.employee_dao_imp import EmployeeDAOImp
from service_layer.employee_serl_imp import EmployeeServiceLayerImp
from data_access_layer.dal_reimbursement_total import ReimbursementTotalsDataImplementation
from service_layer.serl_reimbursement_total import ReimbursementTotalsServiceImplementation
from data_access_layer.reimbursement_dao_imp import ReimbursementDAOImp
from service_layer.reimbursement_service_imp import ReimbursementServiceImp

from utilities.custom_exceptions.employee_not_found import EmployeeNotFound
from utilities.custom_exceptions.incorrect_password import IncorrectPassword
from utilities.custom_exceptions.total_is_zero import TotalIsZero
from utilities.custom_exceptions.no_history import NoHistory
from utilities.custom_exceptions.bad_reimbursement_request import BadReimbursementRequest
from custom_exceptions.id_not_found import IdNotFound
from custom_exceptions.non_numeric_reimbursement_id import NonNumericReimbursementID

from entities.reimbursement_data import ReimbursementData

login_data_access_object = LogInDataAccessLayerImplementation()
login_service_object = LogInServiceLayerImplementation(login_data_access_object)
test_totals_data_implementation = ReimbursementTotalsDataImplementation()
test_totals_service_implementation = ReimbursementTotalsServiceImplementation(test_totals_data_implementation)
employee_dao = EmployeeDAOImp()
employee_serl = EmployeeServiceLayerImp(employee_dao)
test_reimbursement_dao = ReimbursementDAOImp()
test_reimbursement_service = ReimbursementServiceImp(test_reimbursement_dao)

mocking_object = ReimbursementData("0", "1", "100.00", "Hotel", "stayed in HamptonInn", "pending")
mocking_object2 = ReimbursementData(0, 1, 100.00, "Hotel", "stayed in HamptonInn", "pending")


def test_dal_select_employee_information_success():
    result = login_data_access_object.select_employee_information("AGator")
    assert result == [('Password',)]

def test_select_employee_information_incorrect_username_return_empty():

    result = login_data_access_object.select_employee_information("WGator")
    assert result == [None]

def test_select_employee_id_success():
    result = login_data_access_object.select_employee_id("AGator")
    assert result == [(1,)]

def test_select_employee_information_success(): #MOCKED
    login_service_object.login_data_access_object.select_employee_information = MagicMock(return_value=[('Password',)])
    result = login_service_object.service_select_employee_information("AGator", "Password")
    assert result == 1

def test_select_employee_information_incorrect_username(): #MOCKED
    try:
        login_service_object.login_data_access_object.select_employee_information = MagicMock(
        return_value=[None])
        login_service_object.service_select_employee_information("WGator", "Password")
        assert False
    except EmployeeNotFound as e:
        assert str(e) == "The employee username could not be found within the database. Please try again."

def test_select_employee_information_incorrect_password(): #MOCKED
    try:
        login_service_object.login_data_access_object.select_employee_information = MagicMock(return_value=[('Password',)])
        login_service_object.service_select_employee_information("AGator", "WrongPassword")
        assert False
    except IncorrectPassword as e:
        assert str(e) == "The password you have given is incorrect. Please try again."

def test_success_data_completed_total(): # Double check after final lockdown.
    money_total = test_totals_data_implementation.get_completed_reimbursement_total(1)
    assert money_total == (Decimal('140.00'),)

def test_success_data_pending_total(): # Double check after final lockdown.
    money_total = test_totals_data_implementation.get_pending_reimbursement_total(2)
    assert money_total == (Decimal('1172.49'),)

def test_success_service_completed_total():
    test_totals_service_implementation.data_implementation.get_completed_reimbursement_total = MagicMock(return_value=(Decimal('500'),))
    money_total = test_totals_service_implementation.check_completed_reimbursement_total("5")
    test_totals_service_implementation.data_implementation.get_completed_reimbursement_total.assert_called_with(5)
    assert money_total == 500

def test_success_service_pending_total():
    test_totals_service_implementation.data_implementation.get_pending_reimbursement_total = MagicMock(return_value=(Decimal('500'),))
    money_total = test_totals_service_implementation.check_pending_reimbursement_total("5")
    test_totals_service_implementation.data_implementation.get_pending_reimbursement_total.assert_called_with(5)
    assert money_total == 500

def test_failure_service_no_completed_total():
    test_totals_service_implementation.data_implementation.get_completed_reimbursement_total = MagicMock(return_value=(None))
    try:
        money_total = test_totals_service_implementation.check_completed_reimbursement_total("5")
        assert False
    except TotalIsZero as exception:
        assert str(exception) == "You have no completed reimbursements."

def test_failure_service_no_pending_total():
    test_totals_service_implementation.data_implementation.get_pending_reimbursement_total = MagicMock(return_value=(None))
    try:
        money_total = test_totals_service_implementation.check_pending_reimbursement_total("5")
        assert False
    except TotalIsZero as exception:
        assert str(exception) == "You have no pending reimbursements."

def test_success_data_complete_reimbursement_history(): # Double check after final lockdown.
    list_result = test_totals_data_implementation.get_all_reimbursements(1)
    assert list_result == [(3, 1, Decimal('140.00'), 'flying', 'flew to the next game', 'approved'),
 (12, 1, Decimal('100.00'), 'hotel', 'stayed in HamptonInn', 'pending'),
 (13, 1, Decimal('100.00'), 'hotel', 'stayed in HamptonInn', 'pending'),
 (14, 1, Decimal('100.00'), 'Hotel', 'stayed in HamptonInn', 'pending'),
 (15, 1, Decimal('100.00'), 'Hotel', 'stayed in HamptonInn', 'pending'),
 (17, 1, Decimal('100.00'), 'Hotel', 'stayed in HamptonInn', 'pending'),
 (22, 1, Decimal('12.22'), 'gas', 'dfdsdfd', 'pending'),
 (2, 1, Decimal('75.00'), 'hotel', 'stayed night at Hilton', 'canceled'),
 (43, 1, Decimal('100.23'), 'dining', 'Had dinner with Customer', 'pending'),
 (44, 1, Decimal('100.23'), 'dining', 'Had dinner with Customer', 'pending'),
 (45, 1, Decimal('100.23'), 'dining', 'Had dinner with Customer', 'pending'),
 (46, 1, Decimal('100.23'), 'dining', 'Had dinner with Customer', 'pending'),
 (47, 1, Decimal('100.23'), 'dining', 'Had dinner with Customer', 'pending'),
 (52, 1, Decimal('100.23'), 'dining', 'Had dinner with Customer', 'pending'),
 (53, 1, Decimal('100.23'), 'dining', 'Had dinner with Customer', 'pending'),
 (54, 1, Decimal('100.23'), 'dining', 'Had dinner with Customer', 'pending'),
 (55, 1, Decimal('100.23'), 'dining', 'Had dinner with Customer', 'pending'),
 (56, 1, Decimal('100.23'), 'dining', 'Had dinner with Customer', 'pending'),
 (57, 1, Decimal('100.23'), 'dining', 'Had dinner with Customer', 'pending'),
 (58, 1, Decimal('100.23'), 'dining', 'Had dinner with Customer', 'pending'),
 (59, 1, Decimal('100.23'), 'dining', 'Had dinner with Customer', 'pending'),
 (60, 1, Decimal('100.23'), 'dining', 'Had dinner with Customer', 'pending'),
 (61, 1, Decimal('100.23'), 'dining', 'Had dinner with Customer', 'pending'),
 (62, 1, Decimal('100.23'), 'dining', 'Had dinner with Customer', 'pending'),
 (38, 1, Decimal('18.23'), 'gas', 'Meet Client', 'pending'),
 (39, 1, Decimal('18.23'), 'gas', 'Meet Client', 'pending'),
 (41, 1, Decimal('18.23'), 'gas', 'Meet Client', 'pending'),
 (71, 1, Decimal('100.00'), 'Hotel', 'stayed in HamptonInn', 'pending'),
 (87, 1, Decimal('100.00'), 'Hotel', 'stayed in HamptonInn', 'pending'),
 (85, 1, Decimal('100.00'), 'Hotel', 'stayed in HamptonInn', 'pending'),
 (89, 1, Decimal('100.00'), 'Hotel', 'stayed in HamptonInn', 'pending'),
 (88, 1, Decimal('100.00'), 'Hotel', 'stayed in HamptonInn', 'pending'),
 (84, 1, Decimal('100.00'), 'Hotel', 'stayed in HamptonInn', 'pending'),
 (86, 1, Decimal('100.00'), 'Hotel', 'stayed in HamptonInn', 'pending')]

def test_success_service_complete_reimbursement_history():
    test_totals_service_implementation.data_implementation.get_all_reimbursements = MagicMock(return_value=[(2, 1, 75, 'hotel', 'stayed night at the Hilton', 'approved'), (3, 1, 140, 'flying', 'flew to next game', 'approved')])
    result_list = test_totals_service_implementation.check_full_history("1")
    test_totals_service_implementation.data_implementation.get_all_reimbursements.assert_called_with(1)
    assert result_list[0].reimbursement_id == 2
    assert result_list[1].reimbursement_id == 3

def test_failure_service_no_history():
    test_totals_service_implementation.data_implementation.get_all_reimbursements = MagicMock(return_value=tuple())
    try:
        full_history = test_totals_service_implementation.check_full_history("5")
        assert False
    except NoHistory as exception:
        assert str(exception) == "You have no reimbursement history."

def test_dao_submit_reimbursement():
    reimbursements = ReimbursementData(0, 6, 100.00, "Hotel", "stayed in HamptonInn", "pending")
    result = employee_dao.submit_reimbursement(reimbursements)
    assert result.reimbursement_id != 0

def test_dao_get_reimbursement_info_by_id_success():
    result = employee_dao.get_reimbursement_info_by_id(2)
    assert result.reimbursement_id == 2

def test_dao_get_reimbursement_info_by_non_existant_id():
    result = employee_dao.get_reimbursement_info_by_id(-100)
    assert result is None

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

def test_reimbursement_id_exist():
    result = test_reimbursement_dao.cancel_reimbursement_request(33)
    assert result is 1

def test_non_existent_id():
    result = test_reimbursement_dao.cancel_reimbursement_request(-1)
    assert result == 0

def test_status_code_update_failure():
    result = test_reimbursement_dao.cancel_reimbursement_request(33)
    assert result == 0

def test_reimbursement_id_success():
    test_reimbursement_service.reimbursement_dao.cancel_reimbursement_request = MagicMock(return_value=1)
    result = test_reimbursement_service.service_cancel_reimbursement_request(3)
    assert result == 1

def test_catch_incorrect_reimbursement_id():
    try:
        test_reimbursement_service.reimbursement_dao.cancel_reimbursement_request = MagicMock(return_value=0)
        test_reimbursement_service.service_cancel_reimbursement_request(-1)
        assert False
    except IdNotFound as e:
        assert str(e) == "Incorrect ID"

def test_catch_non_numeric_reimbursement_id():
    try:
        result = test_reimbursement_service.service_cancel_reimbursement_request("Zero")
        assert result is False
    except NonNumericReimbursementID as e:
        assert str(e) == "Non-numeric ID"