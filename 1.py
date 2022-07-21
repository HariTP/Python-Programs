# Write a python program to search an element in a list and display the frequency of element present in list and their location using Linear search by using user defined function. [List and search element should be entered by user]
def search(lst,ele):
    count=0
    lst_pos=[]
    for i in range(len(lst)):
        if lst[i]==ele:
            count+=1
            lst_pos.append(i)
    print(ele,"is found",count,"times at positions",end=' ')
    for i in range(len(lst_pos)-1):
        print(lst_pos[i],end=',')
    print(lst_pos[-1],end='.')
lst=eval(input("Enter a list: "))
ele=int(input("Enter the elements to be searched: "))
search(lst,ele)
    
