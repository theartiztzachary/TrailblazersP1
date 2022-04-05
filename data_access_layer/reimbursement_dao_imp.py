from custom_exceptions.id_not_found import IdNotFound
from data_access_layer.reimbursement_dao_interface import ReimbursementDAOInterface
from utilities.connection_manager import connection


# Send a sql query to update a reimbursement's status code.
# Return and send how many rows were updated.
# If one row is affected, return reimbursement id with updated status code

class ReimbursementDAOImp(ReimbursementDAOInterface):

    def cancel_reimbursement_request(self, reimbursement_id: int):
        # Look through the database; make sure id matches to the one inputted; update status code; return True/canceled
        sql = "update reimbursements set status_code = 'canceled' where reimbursement_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement_id])
        connection.commit()
        if cursor.rowcount != 0:  # rowcount tells us how many rows were changed
            return "Canceled"
        else:
            raise IdNotFound("Invalid ID")

