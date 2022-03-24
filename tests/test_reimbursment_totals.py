from decimal import Decimal
from data_access_layer.dal_reimbursement_total import ReimbursementTotalsDataImplementation
from service_layer.serl_reimbursement_total import ReimbursementTotalsServiceImplementation

from unittest.mock import MagicMock

from utilities.custom_exceptions.total_is_zero import TotalIsZero

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
    assert money_total == 500

def test_success_service_pending_total():
    test_totals_service_implementation.data_implementation.get_pending_reimbursement_total = MagicMock(return_value=(Decimal('500'),))
    money_total = test_totals_service_implementation.check_pending_reimbursement_total("5")
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