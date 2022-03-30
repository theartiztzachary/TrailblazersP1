from custom_exceptions.id_not_found import IdNotFound
from data_access_layer.reimbursement_dao_interface import ReimbursementDAOInterface
from entities.reimbursement_data import ReimbursementData
from utilities.connection_manager import connection


# Send a sql query to update a reimbursement's status code.
# Return and send how many rows were updated.
# If one row is affected, return reimbursement id with updated status code

class ReimbursementDAOImp(ReimbursementDAOInterface):

    # def __init__(self, reimbursement_dao: ReimbursementData):
    #     self.reimbursement_dao = reimbursement_dao

    def cancel_reimbursement_request(self, reimbursement_id: int):
        # Look through the database; make sure id matches to the one inputted; update status code; return True/canceled
        sql = "update reimbursements set status_code = 'canceled' where reimbursement_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement_id])
        connection.commit()
        # ????? Below this belongs in the service layer because it's validating. ?????
        if cursor.rowcount != 0:  # rowcount tells us how many rows were changed
            return 'canceled'
        else:
            raise IdNotFound("Invalid ID")
