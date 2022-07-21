## Integrate SQL with Python by importing the MySQL module to search an employee using empno and if present in table display the record, if not display appropriate method.
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",database="programs")
cursor=db.cursor()
cursor.execute("select * from employee_data")
emp_data=cursor.fetchall()
while True:
    empid=int(input("Enter employee ID to search: "))
    for i in emp_data:
        if i[0]==empid:
            print("Name: ",i[1])
            print("Salary: ",i[2])
            break
    else:
        print(empid,"not found in employee database!!")
    ch=input("Want to search more(y/n): ")
    if ch!='y':
        break
