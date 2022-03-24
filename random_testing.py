from utilities.connection_manager import connection

sql = "select * from reimbursements where employee_id = %s"
cursor = connection.cursor()
cursor.execute(sql, [5])
total = cursor.fetchall()
print(total)