from custom_exceptions.id_not_found import IdNotFound
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
    result = reimbursement_dao.cancel_reimbursement_request(6)
    assert result == "Canceled"  # result should give back a correct id value (id # > 0 b/c 0 is uninitialized)


# Positive
# Test that the status code is updated in the database by reimbursement id
def test_status_code_update_success():
    result = reimbursement_dao.cancel_reimbursement_request(6)
    assert result == "Canceled"
    # WE CAN ALSO DO BELOW
    # if result == "canceled":
    #     return True
    # else:
    #     return False


# Positive
# Test if returned rowcount == 1 or > 0 (positive)

"""
********************************** Negative Tests **********************************
"""


# Negative
# Test that when you give a reimbursement ID that does not exist, an empty return is passed up to the service layer.

def test_non_existent_id():
    try:
        result = reimbursement_dao.cancel_reimbursement_request(-1)
        assert False
    except IdNotFound as e:
        assert str(e) == "Invalid ID"


# Negative
# Test if returned rowcount == 0 or < 1 (negative)

