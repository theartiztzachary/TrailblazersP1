from data_access_layer.reimbursement_dao_imp import ReimbursementDAOImp
from service_layer.reimbursement_service_interface import ReimbursementServiceInterface


class ReimbursementServiceImp(ReimbursementServiceInterface):
    def __init__(self, reimbursement_dao: ReimbursementDAOImp):
        self.reimbursement_dao = reimbursement_dao

    #  check to make sure request_number is in database; if true, return true, else return false
    def service_cancel_reimbursement_request(self, reimbursement_id: int) -> bool:
        result = self.reimbursement_dao.cancel_reimbursement_request(reimbursement_id)
        if result == "canceled":
            return True
        else:
            return False





