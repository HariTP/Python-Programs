## Write a python program to create a CSV file with empid, name and mobile no. and search empid, update the record and display the records.
import csv
with open("16.csv",'r') as file_check:
    check=csv.reader(file_check)     ## to check if file is empty
    lst_check=[]
    for i in check:
        lst_check.append(i)
if lst_check==[]:                          ## if file is empty do not write 
    file1=open("16.csv",'w')
    fields=['empid','name','mobile']
    rows=[['100','Raghav','1234567890'],['101','Rajeev','1122334455'],['102','Anuj','9876543210'],['103','Vineet','9988776655'],['104','Harry','1020304050']]
    file_write=csv.writer(file1,delimiter=',')
    file_write.writerow(fields)
    for x in rows:
        file_write.writerow(x)
    file1.close()
else:
    pass

ch=int(input("1. Search by Emp ID \n2. Update record \n3. Display records \nEnter your choice: "))
if ch==1:
    with open("16.csv",'r') as file_search:
        search=csv.reader(file_search)
        while True:
            empid=int(input("Enter Emp ID: "))
            str_empid=str(empid)
            for i in search:
                if i[0]==str_empid:
                    print("Name:",i[1],"\nMobile no:",i[2])
                    file_search.seek(0)    ## to return cursor to strarting of file
                    break  
            else:
                print("Emp ID not found in the record")
                file_search.seek(0)     ## to return cursor to strarting of file
            want=input("Want to search more(y/n): ")
            if want!='y':
                break
elif ch==2:
    with open("16.csv",'r') as file_output:
        output=csv.reader(file_output)
        lst=[]
        for i in output:
            lst.append(i)
    while True:
        empid=int(input("Enter Emp ID of: "))
        name=input("Enter new name: ")
        mobile=int(input("Enter new mobile no: "))
        str_empid=str(empid)
        for j in lst:
            if j[0]==str_empid:
                j[1]=name
                j[2]=mobile
                print("Record updated")
                with open("16.csv",'w') as file_input:
                    input_data=csv.writer(file_input,delimiter=',')
                    for a in lst:
                        input_data.writerow(a)
                break           ## to beak inner for loop
        else:
            print(empid,"not found in record!!")
        want=input("want to update more(y/n)")    
        if want!='y':
            break         ## break to exit outermost while loop
elif ch==3:
    with open("16.csv",'r') as file_display:
        display=csv.reader(file_display)
        lst=[]
        for i in display:
            lst.append(i)
    for x in lst:
        print(x[0],x[1],x[2])
            
        
