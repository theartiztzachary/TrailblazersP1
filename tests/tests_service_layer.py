from custom_exceptions.non_numeric_reimbursement_id import NonNumericReimbursementID
from data_access_layer.reimbursement_dao_imp import ReimbursementDAOImp
from service_layer.reimbursement_service_imp import ReimbursementServiceImp

reimbursement_dao = ReimbursementDAOImp()
reimbursement_service = ReimbursementServiceImp(reimbursement_dao)


# Positive:
# Test that when you give the correct reimbursement_id from the database to cancel the reimbursement,
# there is no error, and it returns itself & a confirmation at end (Mock).

def test_reimbursement_id_success():
    pass


# Negative:
# Test that when you give a reimbursement ID that does not exist, an error is raised. (Mocked)

def test_catch_incorrect_reimbursement_id():
    pass


# Negative:
# Test that when you give non-numeric strings, you get an error.

def test_catch_non_numeric_reimbursement_id():
    try:
        # reimbursement_id, employee_id, amount, reason, reimbursement_comment, status_code
        # reimbursement_example = ReimbursementData("Zero", 1, 100, "Gas", "Traveled", "Pending")
        reimbursement_service.service_cancel_reimbursement_request(reimbursement_example)
    except NonNumericReimbursementID as e:
        assert str(e) == "Reimbursement ID needs to be a number"
