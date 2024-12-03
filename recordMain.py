# def check_employee(employee_id):
#     sql = 'SELECT * FROM employees WHERE id=%s'
# 
# cursor = con.cursor(buffered=True)
# data = (employee_id, )
# 
# cursor.execute = cursor.fetchone()
# 
# employee = cursor.fetchone()
# 
# cursor.close()
# 
# return employee is not None
# 
# def add_employee():
#     Id = input("Enter employee ID: ")
#     if check_employee(Id):
#         print("Employee already exists. Please try again.")
#         return 
#     
#     else:
#         Name = input ("Enter employee name: ")
#         Position= input("Enter employee position: ")
#         Salary = input ("Enter employee salary: ")
#         
#         sql = "INSERT INTO  employees (id, name, position, salary) VALUES (%s, %s, %s, %s)"
#         data = (Id, Name, Position, Salary)
#         
#         try: 
#             cursor.execute(sql,data)
#             
#             con.commit()
#             print("Employee added successfully.")
#             
#         except mysql.connector.Error as err:
#             print(f"Error : {err}")
#             con. rollback()
#             
#         finally:
#             cursor.close()
# 
# def add_employee():
#     Id = input("Enter employee ID: ")
#     if check_employee(Id):
#         print("Employee already exists. Please try again.")
#         return
# 
#     else:
#         Name = input ("Enter employee name: ")
#         Position= input("Enter employee position: ")
#         Salary = input ("Enter employee salary: ")
# 
#         sql = "INSERT INTO  employees (id, name, position, salary) VALUES (%s, %s, %s, %s)"
#         data = (Id, Name, Position, Salary)
# 
#         try:
#             cursor.execute(sql,data)
# 
#             con.commit()
#             print("Employee added successfully.")
# 
#         except mysql.connector.Error as err:
#             print(f"Error : {err}")
#             con. rollback()
# 
#         finally:
#             cursor.close()
# 
# def remove_employee():
#     Id = input("Enter employee ID: ")
# 
#     if not check_employee(Id):
#         print("Employee does not exist. Please try again.")
#         return
# 
#     else:
#         sql = "DELETE FROM employees WHERE id=%s"
#         data = (Id,)
#         cursor = con.cursor()
# 
#         try:
#             cursor.execute(sql, data)
#             con.commit()
#             print("Employee removed successfully.")
# 
#         except mysql.connector.Error as err:
#             print(f"Error: {err}")
#             con.rollback()
# 
#         finally:
#             cursor.close()
# 
# def promote_employee():
#     Id = input("Enter employee ID: ")
#     if not check_employee(Id):
#         print("Employee does not exist. Please try again.")
#         return
# 
#     else:
#         try:
#             Amount = float(input("Enter increase in salary: "))
# 
#             sql_select = 'SELECT salary FROM employees WHERE id=%s'
#             data = (Id, )
#             cursor = con.cursor()
#             cursor.execute(sql_select, data)
#             current_salary = cursor.fetchone()[0]
#             new_salary = current + Amount
#             sql_update = 'UPDATE employees SET salary =%s WHERE id=%s'
#             data_update = (new_salary, Id)
#             cursor.execute(sql_update, data_update)
#             con.commit ()
#             print("Employee salary updated successfully.")
# 
#         except (ValueError, mysql.connector.Error) as e:
#             print(f"Error: {e}")
#             con.rollback()
# 
#         finally:
#             cursor.close()
# 
# def display_employees():
#     try:
#         sql = 'SELECT * FROM employees'
#         cursor = con.cursor()
#         cursor.execute(sql)
#         employees = cursor = cursor.fetchall()
#         for employee in employees:
#            print("Employee ID: ", employee[0])
#            print("Employee name: ", employee[1])
#            print("Employee position: ", employee[2])
#            print("Employee salary: ", employee[3])
#            print("------------------------------------------------")
# 
#     except mysql.connector.Error as err:
#         print(f"Error: {err}")
# 
#     finally:
#         cursor.close()
# 
# def menu ():
#     while True:
#         print("\nWelcome to Employee Management Record")
#         print("Press:")
#         print("1 to add employee")
#         print("2 to remove employee")
#         print("3 to increase employee salary")
#         print("4 to display employees")
#         print("5 to exit")
# 
#         opt = input("Enter option: ")
# 
#         if opt == "1":
#             add_employee()
#         elif opt =="2":
#             remove_employee()
#         elif opt == "3":
#             promote_employee()
#         elif opt == "4":
#             display_employees()
#         elif  opt =="5":
#             print("Exiting the system.")
#             break
#         else:
#             print("Invalid option.  Try again.")
#           
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_enough(order_ingredients):
    """returns the amount of resources needed to make each drink"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]
            print(f"Sorry there is not enough water {item}.")
            is_enough = False
    return is_enough

def process_coins():
    """returns total calculated from amount of coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?:  ")) * .25
    total += int(input("How many dimes?:  ")) * .10
    total += int(input("How many nickels?:  ")) * .05
    total += int(input("How many pennies?:  ")) * .01

 def is_transaction_successful(money_recieved, drink_cost):
     """return Truewhen payment accepted, FALSE if not"""
     if money_received >= drink_cost:
         change = round(money_received - drink_cost, 2)
         global profit
         profit += drink_cost
         return True
     else:
         print("Not enough momey.  Money refunded.")
         return False



is_on = True
while is_on:
    choice = input("What drink would you like? espresso, latte, or cappuccino?")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f'Water: {resources['water']}ml')
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_enough(drink["ingredients"]):
            payment = process_coins()


