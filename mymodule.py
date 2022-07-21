def odd(lst):    #function prints odd values from a list
    for x in lst:
        if x%2==1:
            print(x,end='  ')
            
def even(lst):   #function prints even values from a list
    for x in lst:
        if x%2==0:
            print(x,end='  ')

def count(lst,ele):  #functiom prints frequency of an element in a list
    count=0
    for x in lst:
        if x==ele:
            count+=1
    print(ele,"is present",count,"times.")
    

        
