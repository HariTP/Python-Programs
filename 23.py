def occurence(string):
    lower=string.lower()
    spl=lower.split()
    count=0
    word=[]
    for i in range(len(spl)-1):
        count_m=0
        for j in range(i+1,len(spl)):
            if spl[i]==spl[j]:
                count_m+=1        
        if count_m>count:
            count=count_m
            word.clear()
            word.append(spl[i])
        elif count_m==count:
            word.append(spl[i])  
    if count!=0:
        print("The most occuring word(s) is/are: ",end=': ')       
        for i in range(len(word)-1):
            print(word[i],end=',')
        print(word[-1],end=' = ')    
        print(count+1,"times")
    else:
        print("Every Word has equal occurence")
file=open("23.txt",'r')
lines=file.readlines()
print(lines[0])
occurence(lines[0])
file.close()
                
