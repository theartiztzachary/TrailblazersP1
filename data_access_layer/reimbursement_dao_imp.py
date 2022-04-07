from custom_exceptions.id_not_found import IdNotFound
from data_access_layer.reimbursement_dao_interface import ReimbursementDAOInterface
from utilities.connection_manager import connection


# Send a sql query to update a reimbursement's status code.
# Return and send how many rows were updated.
# If one row is affected, return reimbursement id with updated status code

class ReimbursementDAOImp(ReimbursementDAOInterface):

    def cancel_reimbursement_request(self, reimbursement_id: int):
        # Look through the database; make sure id matches to the one inputted; update status code; return True/canceled
        # sql = "update reimbursements set status_code = 'canceled' where reimbursement_id = %s"
        sql = "update reimbursements set status_code = 'canceled' where reimbursement_id = %s and status_code " \
              "= 'pending'"
        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement_id])
        connection.commit()
        if cursor.rowcount != 0:  # rowcount tells us how many rows were changed
            return "canceled"
        elif cursor.rowcount == 0:  # rowcount = 0 tells us nothing was changed
            return "Error! Your cancel reimbursement request was already processed!"
        else:
            raise IdNotFound("Invalid ID")

    def get_status_code_update(self, reimbursement_id):
        sql = "select status_code from reimbursements where reimbursement_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement_id])
        status_code_result = cursor.fetchone()[0]
        if status_code_result == 'canceled':
            return True
        elif status_code_result == 'pending' or status_code_result == 'approved':
            return False
        else:
            raise IdNotFound("Invalid ID")

    def get_reimbursement_id_number(self, reimbursement_id: int):
        sql = "select reimbursement_id from reimbursements where reimbursement_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement_id])
        reimbursement_id_result = cursor.fetchone()[0]
        if reimbursement_id_result == reimbursement_id:
            return True
        else:
            return False
