# Write a Python program to pass a string to a function and count how many vowels present in the string.
def vow_count(str):
    count=0
    for x in str:
        if x in "AEIOUaeiou":
            count+=1
    print("Number of vowels in the gven string is: ",count)
str=input("Enter a string: ")
vow_count(str)
