def check_employee(employee_id):
    sql = 'SELECT * FROM employees WHERE id=%s'

cursor = con.cursor(buffered=True)
data = (employee_id, )

cursor.execute = cursor.fetchone()

employee = cursor.fetchone()

cursor.close()

return employee is not None

def add_employee():
    Id = input("Enter employee ID: ")
    if check_employee(Id):
        print("Employee already exists. Please try again.")
        return 
    
    else:
        Name = input ("Enter employee name: ")
        Position= input("Enter employee position: ")
        Salary = input ("Enter employee salary: ")
        
        sql = "INSERT INTO  employees (id, name, position, salary) VALUES (%s, %s, %s, %s)"
        data = (Id, Name, Position, Salary)
        
        try: 
            cursor.execute(sql,data)
            
            con.commit()
            print("Employee added successfully.")
            
        except mysql.connector.Error as err:
            print(f"Error : {err}")
            con. rollback()
            
        finally:
            cursor.close()

