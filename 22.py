## Integrate SQL with Python by importing the MySQL module to search a student using rollno, delete the record.
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",database="programs")
cursor=db.cursor()
while True:
    ch=int(input("\n1. Search student \n2. Delete record \n3. Exit \nEnter your choice: "))
    if ch==1:
        while True:
            cursor.execute("select * from student_data")
            stud_data=cursor.fetchall()
            rollno=int(input("Enter roll no to search: "))
            for i in stud_data:
                if i[0]==rollno:
                    print("Name: ",i[1])
                    print("Class: ",i[2])
                    break
            else:
                print(rollno,"not found in student database!!")
            ch=input("Want to search more(y/n): ")
            if ch!='y':
                break
    elif ch==2:
        while True:
            rollno=int(input("Enter roll no to be deleted: "))
            cursor.execute("delete from student_data where Rollno={}".format(rollno))
            db.commit()
            print(rollno,"deleted from database")
            want=input("Want to delete more(y/n): ")
            if want!='y':
                break
    elif ch==3:
        print("Exiting Program!")
        break
    else:
        print("Inavlid choice!!!")
    
    
    
    
