from data_access_layer.reimbursement_dao_imp import ReimbursementDAOImp
from service_layer.reimbursement_service_interface import ReimbursementServiceInterface


class ReimbursementServiceImp(ReimbursementServiceInterface):
    def __init__(self, reimbursement_dao: ReimbursementDAOImp):
        self.reimbursement_dao = reimbursement_dao

# not sure if to implement the bool or string
    #  check to make sure request_number is in database; if true, return true, else return false
    def service_cancel_reimbursement_request(self, reimbursement_id: int) -> str:
        result = self.reimbursement_dao.cancel_reimbursement_request(reimbursement_id)
        if result == "Canceled":
            return "Canceled"
        elif result == "":
            return "Null"
        else:
            return "Pending"

    # def service_cancel_reimbursement_request(self, reimbursement_id: int):
    #     result = self.reimbursement_dao.cancel_reimbursement_request(reimbursement_id)
    #     if result == "canceled":
    #         return "canceled"
    #     else:
    #         return "pending"





