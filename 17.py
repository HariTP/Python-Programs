## Write a Python program to create Lpush( ) and Lpop( ) function to do push and pop operation on a stack using a list.
##stk=[]
def Lpush(stk,lst):
    stk.append(lst)
def Lpop(stk):
    if stk==[]:
        return "underflow"
    else:    
        stud=stk.pop()
        return stud
def display(stk):
    if stk==[]:
        print("Stack is empty")
    else:    
        print(stk[-1],"<---- TOP")
        for i in range(-2,-len(stk)-1,-1):
            print(stk[i])
stk=[]            
while True:
    choice=int(input("\n1. Push to stack \n2. Pop from stack \n3. Display stack \n4. Quit \nEnter your choice: "))
    if choice==1:
        while True:
            roll_no=int(input("Enter roll no of student: "))
            name=input("Enter student's name: ")
            clas=int(input("Enter class of student: "))
            lst=[roll_no,name,clas]
            Lpush(stk,lst)
            print("Entry pushed to stack.")
            ch=input("Want to push more(y/n): ")
            if ch!='y':
                break    
    elif choice==2:
        while True:
            stat=Lpop(stk)
            if stat=="underflow":
                print("Empty stack!! Underflow!!")
                break
            else:
                print(stat,"popped out of stack.")
                want=input("Want to pop more(y/n): ")
                if want!='y':
                    break
    elif choice==3:
        display(stk)
    elif choice==4:
        print("Exiting out!!")
        break
    else:
        print("Invalid choice!! \nEnter a valid choice again")
        








            
