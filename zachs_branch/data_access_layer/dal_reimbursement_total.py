from zachs_branch.entities.reimbursement_totals_interfaces import ReimbursementTotalsDataInterface
from zachs_branch.utilities.connection_manager import connection

class ReimbursementTotalsDataImplementation(ReimbursementTotalsDataInterface):
    def get_completed_reimbursement_total(self, employee_id: int) -> tuple:
        sql_query = "select sum(amount) from reimbursements where employee_id = %s and status_code = 'approved'"
        cursor = connection.cursor()
        cursor.execute(sql_query, [employee_id])
        total = cursor.fetchone()
        return total

    def get_pending_reimbursement_total(self, employee_id: int) -> tuple:
        sql_query = "select sum(amount) from reimbursements where employee_id = %s and status_code = 'pending'"
        cursor = connection.cursor()
        cursor.execute(sql_query, [employee_id])
        total = cursor.fetchone()
        return total

    def get_all_reimbursements(self, employee_id: int) -> list:
        sql_query = "select * from reimbursements where employee_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql_query, [employee_id])
        history = cursor.fetchall()
        return history