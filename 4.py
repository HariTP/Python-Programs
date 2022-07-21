#Write a Python program input n numbers in tuple and pass it to function to count how many even and odd numbers are entered.
def count_oe(tup):
    count_odd=0
    count_even=0
    for x in tup:
        if x%2==0:
            count_even+=1
        else:
            count_odd+=1
    print("Number of even values is: ",count_even)        
    print("Number of odd values is: ",count_odd)
tup=eval(input("Enter a tuple: "))
count_oe(tup)
