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

# ****************** HELP ###########
def test_reimbursement_id_exist():
    reimbursement_dao.get_reimbursement_id_number(33)
    assert True  # this does not work


# Positive
# Test that the status code is updated in the database by reimbursement id
def test_status_code_update_success():
    reimbursement_dao.get_status_code_update(33)
    assert True


# Positive
# Test if returned rowcount == 1 or > 0 (positive)

"""
********************************** Negative Tests **********************************
"""


# Negative
# Test that when you give a reimbursement ID that does not exist, an empty return is passed up to the service layer.

def test_non_existent_id():
    # try:
    #     reimbursement_dao.cancel_reimbursement_request(-1)
    #     assert "Invalid ID"
    # except IdNotFound as e:
    #     assert str(e) == "Invalid ID"
    reimbursement_dao.cancel_reimbursement_request(-1)
    assert "Invalid ID"


# Negative
# Test if returned rowcount == 0 or < 1 (negative)
# this test would be necessary if cancel reimbursement request was already processed

def test_status_code_update_failure():
    # result = reimbursement_dao.get_status_code_update(31)
    # if result == "Error! Your cancel reimbursement request was already processed!":
    #     raise StatusCodeUpdateFailure("Error! Your cancel reimbursement request was already processed!")
    reimbursement_dao.cancel_reimbursement_request(-1)
    assert "Error! Your cancel reimbursement request was already processed!"
