# Write a Python program to function with key and value, and update value at that key in dictionary entered by user.
def value_changer(d):
    key=input("Enter the key: ")
    val=input("Enter the new value :") 
    for x in (d.keys()):
        if x==key:
            d[x]=val
    print(d)
d={"Name":"Arjun","Roll":"123","Class":"12"}
value_changer(d)

    
