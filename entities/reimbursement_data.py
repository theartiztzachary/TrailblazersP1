class ReimbursementData:
    def __init__(self, reimbursement_id: int, employee_id: int, amount: float, reason: str, reimbursement_comment: str,
                 status_code: str):
        self.reimbursement_id = reimbursement_id
        self.employee_id = employee_id
        self.amount = amount
        self.reason = reason
        self.reimbursement_comment = reimbursement_comment
        self.status_code = status_code

    def reimbursementdata_to_dictionary(self):
        return {
            "reimbursementId": self.reimbursement_id,
            "employeeId": self.employee_id,
            "amount": self.amount,
            "reason": self.reason,
            "reimbursementComment": self.reimbursement_comment,
            "statusCode": self.status_code
        }
