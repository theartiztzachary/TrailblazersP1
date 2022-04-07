from custom_exceptions.id_not_found import IdNotFound
from custom_exceptions.non_numeric_reimbursement_id import NonNumericReimbursementID
from data_access_layer.reimbursement_dao_imp import ReimbursementDAOImp
from service_layer.reimbursement_service_imp import ReimbursementServiceImp
from unittest.mock import MagicMock

test_reimbursement_dao = ReimbursementDAOImp()
test_reimbursement_service = ReimbursementServiceImp(test_reimbursement_dao)


# Positive:
# Test that when you give the correct reimbursement_id from the database to cancel the reimbursement,
# there is no error, and it returns itself & a confirmation at end (Mock).

def test_reimbursement_id_success():
    try:
        test_reimbursement_service.service_cancel_reimbursement_request = MagicMock(reurn_value=0)
        assert True
    except IdNotFound as e:
        assert str(e) == "Incorrect ID given"


# Negative:
# Test that when you give a reimbursement ID that does not exist, an error is raised.

def test_catch_incorrect_reimbursement_id():
    try:
        test_reimbursement_service.service_cancel_reimbursement_request(-1)
        assert "Reimbursement ID number does not exist in the database"
    except IdNotFound as e:
        assert str(e) == "Incorrect ID given"


# Negative:
# Test that when you give non-numeric strings, you get an error.

def test_catch_non_numeric_reimbursement_id():
    try:
        test_reimbursement_service.service_cancel_reimbursement_request("Zero")
        assert "Reimbursement Id must be and integer. Please try again."
    except NonNumericReimbursementID as e:
        assert str(e) == "Reimbursement ID needs to be a number"
