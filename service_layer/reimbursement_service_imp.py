from custom_exceptions.id_not_found import IdNotFound
from custom_exceptions.non_numeric_reimbursement_id import NonNumericReimbursementID
from custom_exceptions.status_code_update_failure import StatusCodeUpdateFailure
from data_access_layer.reimbursement_dao_imp import ReimbursementDAOImp
from entities.reimbursement_data import ReimbursementData
from service_layer.reimbursement_service_interface import ReimbursementServiceInterface


class ReimbursementServiceImp(ReimbursementServiceInterface):

    def __init__(self, reimbursement_dao: ReimbursementDAOImp):
        self.reimbursement_dao = reimbursement_dao

    #  check to make sure reimbursement_id is in database; if true, return true, else return false
    # catch reimbursement id DNE, reimbursement id != int, status code is already canceled,
    def service_cancel_reimbursement_request(self, reimbursement_id):
        try:
            result1 = int(reimbursement_id)  # changes string int to int int (ex changes "one" to 1
        except ValueError:  # if it cannot change from string to int then it's an error -> raise error
            raise NonNumericReimbursementID("Non-numeric ID")
        result = self.reimbursement_dao.cancel_reimbursement_request(result1)  # if try is successful or correct int was provided, programs jumps to line below
        if result is 1:
            return result
        else:
            raise IdNotFound("Incorrect ID")

