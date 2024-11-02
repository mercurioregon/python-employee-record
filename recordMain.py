def check_employee(employee_id):
    sql = 'SELECT * FROM employees WHERE id=%s'

cursor = con.cursor(buffered=True)
data = (employee_id, )

cursor.execute = cursor.fetchone()

employee = cursor.fetchone()

cursor.close()

return employee is not None