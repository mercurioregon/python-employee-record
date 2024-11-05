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

def remove_employee():
    Id = input("Enter employee ID: ")

    if not check_employee(Id):
        print("Employee does not exist. Please try again.")
        return

    else:
        sql = "DELETE FROM employees WHERE id=%s"
        data = (Id,)
        cursor = con.cursor()

        try:
            cursor.execute(sql, data)
            con.commit()
            print("Employee removed successfully.")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            con.rollback()

        finally:
            cursor.close()

def promote_employee():
    Id = input("Enter employee ID: ")
    if not check_employee(Id):
        print("Employee does not exist. Please try again.")
        return

    else:
        try:
            Amount = float(input("Enter increase in salary: "))

            sql_select = 'SELECT salary FROM employees WHERE id=%s'
            data = (Id, )
            cursor = con.cursor()
            cursor.execute(sql_select, data)
            current_salary = cursor.fetchone()[0]
            new_salary = current + Amount
            sql_update = 'UPDATE employees SET salary =%s WHERE id=%s'
            data_update = (new_salary, Id)
            cursor.execute(sql_update, data_update)
            con.commit ()
            print("Employee salary updated successfully.")

        except (ValueError, mysql.connector.Error) as e:
            print(f"Error: {e}")
            con.rollback()

        finally:
            cursor.close()

def display_employees():
    try:
        sql = 'SELECT * FROM employees'
        cursor = con.cursor()
        cursor.execute(sql)
        employees = cursor = cursor.fetchall()
        for employee in employees:
           print("Employee ID: ", employee[0])
           print("Employee name: ", employee[1])
           print("Employee position: ", employee[2])
           print("Employee salary: ", employee[3])
           print("------------------------------------------------")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()

           
