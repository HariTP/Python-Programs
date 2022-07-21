## Integrate SQL with Python by importing the MySQL module record of employee and display the record.
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",database="programs")
cursor=db.cursor()
cursor.execute("select * from employee_data")
emp_data=cursor.fetchall()
print("EmpID   Name     Salary")
for i in emp_data:
    print(i[0],"  ",i[1],"     ",i[2])
