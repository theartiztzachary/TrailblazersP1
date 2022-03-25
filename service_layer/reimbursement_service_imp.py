from data_access_layer.reimbursement_dao_imp import ReimbursementDAOImp
from service_layer.reimbursement_service_interface import ReimbursementServiceInterface


class ReimbursementServiceImp(ReimbursementServiceInterface):
    def __init__(self, reimbursement_obj: ReimbursementDAOImp):
        self.reimbursement_obj = reimbursement_obj

    #  check to make sure request_number is in database; if true, return true, else return false
    def service_cancel_reimbursement_request(self, request_number: int) -> bool:
        pass

# taking in reimbursement ID
    # send reimbursement ID down to data layer
    # data layer will send back a 1 or a 0
    # what do we do with a 1
    # what do we do with a 0 
# sending back a bool


