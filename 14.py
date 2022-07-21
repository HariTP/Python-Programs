## Write a python program to create a binary file with name and roll number.Search for a given roll number and display name, if not found display appropriate message.
import pickle
ch=int(input("1. Add sudent \n2. Search roll no \nEnter your choice: "))
if ch==1:
    file1=open("student.dat","wb")
    dict_stud={}
    while True:
        roll_no=int(input("Enter roll no: "))
        name=input("Enter student name: ")
        dict_stud[roll_no]=name
        print("Student data added")
        want=input("Want to enter more?(Y/N): ")
        if want==('y' or 'Y'):
            continue
        else:
            break
    pickle.dump(dict_stud,file1)
    file1.close()
elif ch==2:
    file2=open("student.dat","rb")
    stud_data=pickle.load(file2)
    while True:
        roll=int(input("Enter roll no of student: "))
        print("Student is: ",stud_data[roll])
        choice=input("Want to search more?(Y/N): ")
        if choice==('y' or 'Y'):
            continue
        else:
            break
    file2.close()
else:
    print("Invalid choice!!!")


