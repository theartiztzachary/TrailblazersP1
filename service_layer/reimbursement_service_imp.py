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
        if type(reimbursement_id) != int(reimbursement_id):  # incorrect id type
            try:
                int(reimbursement_id)
            except ValueError:
                raise NonNumericReimbursementID("Reimbursement Id must be and integer. Please try again.")
        elif reimbursement_id <= 0:  # negative id
            raise IdNotFound("ID number must be positive.")
        elif self.reimbursement_dao.get_status_code_update:  # status code already updated
            raise StatusCodeUpdateFailure("This cancel reimbursement request was already processed.")
        elif self.reimbursement_dao.get_reimbursement_id_number != reimbursement_id:  # id DNE
            raise IdNotFound("Reimbursement ID number does not exist in the database")


