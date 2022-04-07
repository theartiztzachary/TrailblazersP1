from utilities.connection_manager import connection

# sql = "select reimbursement_id from reimbursements where reimbursement_id = %s"
# cursor = connection.cursor()
# cursor.execute(sql, [150])
# result = cursor.fetchone()
# print(type(result))

# sql = "update reimbursements set status_code = 'canceled' where reimbursement_id = %s and status_code = 'pending' and employee_id = %s"
# cursor = connection.cursor()
# cursor.execute(sql, (83, 6))
# connection.commit()
# result = cursor.rowcount
# print(result)

def interrupt():
    print("one")
    try:
        int("whoops")
    except ValueError:
        raise ValueError

    print("two")

interrupt()
