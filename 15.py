## Write a python program to create a binary file with roll number, name and marks, input a roll number and update the marks.
import pickle
file1=open("15_student.dat","wb+")
dict_stud={1:["Arjun",40],2:["Ram",34],3:["Raju",38],4:["Anmol",25],5:["Krishna",30]}
pickle.dump(dict_stud,file1)
file1.close()

##file2=open("15_student.dat","rb+")
##stud_data=pickle.load(file2)
##print(stud_data)
##roll=int(input("Enter roll no of student: "))
##mark=int(input("Enter new marks of student:"))
##str_name=stud_data[roll][0]
##old_mark=stud_data[roll][1]
##stud_data[roll][1]=mark
##file2.truncate(0)
##pickle.dump(stud_data,file2)
##print("Mark of",str_name,"updated from",old_mark,"to",mark)
##file2.close()
