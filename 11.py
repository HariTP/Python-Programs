## Write a python program to read and display file content line by line with each word separated by '#'

file=open("11.txt",'r')
line=file.readlines()   ## line=list, each line as string
for sent in line:       ## sent=string having a line
    word=sent.split()   ## word=list, each word as string 
    length=len(word)    
    for i in range(length-1):  
        print(word[i],end='#')  ## printing each word sep by '#'
    print(word[length-1])        
file.close()
    
