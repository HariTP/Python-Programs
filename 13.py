file_lower=open("LOWER.txt",'a')
file_upper=open("UPPER.txt",'a')
file_others=open("OTHERS.txt",'a')
user_input=input("Enter any keybord keys: ")
for i in user_input:
    if i.isupper():
        file_upper.write(i)
    elif i.islower():
        file_lower.write(i)
    else:
        file_others.write(i)
file_lower.close()
file_upper.close()
file_others.close()

