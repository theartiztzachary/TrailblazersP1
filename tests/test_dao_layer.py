from custom_exceptions.id_not_found import IdNotFound
from custom_exceptions.status_code_update_failure import StatusCodeUpdateFailure
from data_access_layer.reimbursement_dao_imp import ReimbursementDAOImp
from service_layer.reimbursement_service_imp import ReimbursementServiceImp

reimbursement_dao = ReimbursementDAOImp()
reimbursement_service = ReimbursementServiceImp(reimbursement_dao)

"""
********************************** Positive Tests **********************************
"""


# Positive:
# Test that when you give a reimbursement ID that exists, returns True

def test_reimbursement_id_exist():
    result = reimbursement_dao.cancel_reimbursement_request(33)
    assert result is 1


# Positive
# Test if returned rowcount == 1 or > 0 (positive)

"""
********************************** Negative Tests **********************************
"""


# Negative
# Test that when you give a reimbursement ID that does not exist, an empty return is passed up to the service layer.

def test_non_existent_id():
    result = reimbursement_dao.cancel_reimbursement_request(-1)
    assert result == 0


# Negative
# Test if returned rowcount == 0 or < 1 (negative)
# this test would be necessary if cancel reimbursement request was already processed

def test_status_code_update_failure():
    result = reimbursement_dao.cancel_reimbursement_request(33)
    assert result == 0
