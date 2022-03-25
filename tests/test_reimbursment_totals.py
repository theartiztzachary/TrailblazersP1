from decimal import Decimal
from data_access_layer.dal_reimbursement_total import ReimbursementTotalsDataImplementation
from service_layer.serl_reimbursement_total import ReimbursementTotalsServiceImplementation
from entities.reimbursement_data import ReimbursementData

from unittest.mock import MagicMock

from utilities.custom_exceptions.total_is_zero import TotalIsZero
from utilities.custom_exceptions.no_history import NoHistory

test_totals_data_implementation = ReimbursementTotalsDataImplementation()
test_totals_service_implementation = ReimbursementTotalsServiceImplementation(test_totals_data_implementation)

def test_success_data_completed_total():
    money_total = test_totals_data_implementation.get_completed_reimbursement_total(1)
    assert money_total == (Decimal('215'),)

def test_success_data_pending_total():
    money_total = test_totals_data_implementation.get_pending_reimbursement_total(2)
    assert money_total == (Decimal('1009.18'),)

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

def test_success_data_complete_reimbursement_history():
    list_result = test_totals_data_implementation.get_all_reimbursements(1)
    assert list_result == [(2, 1, Decimal('75.00'), 'hotel', 'stayed night at Hilton', 'approved'), (3, 1, Decimal('140.00'), 'flying', 'flew to the next game', 'approved'), (12, 1, Decimal('100.00'), 'hotel', 'stayed in HamptonInn', 'pending'), (13, 1, Decimal('100.00'), 'hotel', 'stayed in HamptonInn', 'pending')]

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