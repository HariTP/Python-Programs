#Write a python program to pass list to a function and double the odd values and half even values of a list and display list element after changing.
def value_changer(lst):
    for i in range(len(lst)):
        if lst[i]%2==0:
            lst[i]=int(lst[i]/2)
        elif lst[i]%2!=0:
            lst[i]=int(lst[i]*2)
    print(lst)
lst=[1,2,3,4,5,6,7,8,9]
print("Original list is:",lst)
print("New list is ",end=':')
value_changer(lst)
