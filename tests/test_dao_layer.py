from data_access_layer.reimbursement_dao_imp import ReimbursementDAOImp
from service_layer.reimbursement_service_imp import ReimbursementServiceImp

reimbursement_dao = ReimbursementDAOImp()
reimbursement_service = ReimbursementServiceImp()


# Positive:
# Test that when you give a reimbursement ID that exists, returns True or returns object?

def test_reimbursement_id_exist():
    result = reimbursement_dao.cancel_reimbursement_request(0)
    assert result.reimbursement_id != 0  # result should give back a correct id value (id # > 0)


# Positive
# Test that when a reimbursement request is updated, its status code is updated in the database.
def test_status_code_update():
    result = reimbursement_dao.cancel_reimbursement_request(0)
    if result.status_code == "canceled":
        return True
    else:
        return False

# test if returned rowcount == 1 or > 0 (positive)
# test if returned rowcount == 0 or < 1 (negative)


# Negative
# Test that when you give a reimbursement ID that does not exist, an empty return is passed up to the service layer.

def test_non_existent_id():
    result = reimbursement_dao.cancel_reimbursement_request(-1)
        if result.reimbursement_id != 0: 


