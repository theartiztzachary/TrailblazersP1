from data_access_layer.employee_dao_interface import EmployeeDAOInterface
from entities.reimbursement_data import ReimbursementData
from utilities.connection_manager import connection


class EmployeeDAOImp(EmployeeDAOInterface):
    def submit_reimbursement(self, reimbursements: ReimbursementData) -> ReimbursementData:
        sql = "insert into reimbursements values(default, %s, %s, %s, %s, %s) returning reimbursement_id"
        cursor = connection.cursor()
        cursor.execute(sql, (reimbursements.employee_id, reimbursements.amount, reimbursements.reason, reimbursements.reimbursement_comment, reimbursements.status_code))
        connection.commit()
        returned_id = cursor.fetchone()[0]
        reimbursements.reimbursement_id = returned_id
        return reimbursements


    def get_reimbursement_info_by_id(self, reimbursement_id: int) -> ReimbursementData | None:
        sql = "select * from reimbursements where reimbursement_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement_id])
        record = cursor.fetchone()
        if record is not None:
            reimbursements = ReimbursementData(*record)
            return reimbursements
        else:
            return record
