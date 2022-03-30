from data_access_layer.reimbursement_dao_imp import ReimbursementDAOImp
from service_layer.reimbursement_service_imp import ReimbursementServiceImp

reimbursement_dao = ReimbursementDAOImp()
reimbursement_service = ReimbursementServiceImp()

"""
********************************** Positive Tests **********************************
"""


# Positive:
# Test that when you give a reimbursement ID that exists, returns True

def test_reimbursement_id_exist():
    result = reimbursement_dao.cancel_reimbursement_request(0)
    assert result.reimbursement_id != 0  # result should give back a correct id value (id # > 0 b/c 0 is uninitialized)


# Positive
# Test that the status code is updated in the database by reimbursement id
def test_status_code_update_success():
    result = reimbursement_dao.cancel_reimbursement_request(0)
    assert result.status_code == "canceled"
    # CAN WE DO BELOW INSTEAD?
    # if result.status_code == "canceled":
    #     return True
    # else:
    #     return False


# Positive
# Test if returned rowcount == 1 or > 0 (positive)
# HOW TO DO THIS? SHOULD I DO IT THIS WAY?

"""
********************************** Negative Tests **********************************
"""


# Negative
# Test that when you give a reimbursement ID that does not exist, an empty return is passed up to the service layer.

def test_non_existent_id():
    result = reimbursement_dao.cancel_reimbursement_request(-1)
    assert result.reimbursement_id != 0
    # CAN WE DO BELOW INSTEAD?
    # if result.reimbursement_id != 0:
    #     return False


# Negative
# Test if returned rowcount == 0 or < 1 (negative)
def test_status_code_update_failure():
    result = reimbursement_dao.cancel_reimbursement_request(-1)
    assert result.status_code != "canceled"
    # if result.status_code != "canceled":
    #     return False
