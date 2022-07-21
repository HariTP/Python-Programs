## Write a python program to remove all the lines that contain the character ‘x’ in a file and write it to another file
file_r=open("12_read.txt",'r')
file_w=open("12_write.txt",'a')
lines=file_r.readlines()
for line in lines:
    if ('x' or 'X') not in line:
        file_w.write(line)
    else:
        continue
file_r.close()
file_w.close()
        
    
                
        

