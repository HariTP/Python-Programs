def bsearch(alst,element):
    beg=0
    last=len(alst)-1
    start=0
    end=-1
    while(beg<=last):
        mid=(beg+last)//2
        if element==alst[mid]:    #element found in the list
            mid=mid
            for i in range(mid,-1,-1):     #travesing backward indexes
                if alst[i]==alst[mid]:
                    start=i             #first index of element stored in start variable
                else:
                    break
            for j in range(mid,len(alst)):  #traversing forward indexes
                if alst[j]==alst[mid]:
                    end=j               #last index of element stored in last variable
                else:
                    break
            print(element,"is present at indexes: ",end="")    
            for x in range(start,end):
                print(x,end=",")
            print(end)
            break                     #breaking out from the outermost while loop
        elif element>alst[mid]:
            beg=mid+1
        else:
                last=mid-1
    else:                    
        print(element,"is not found in the given list!!!")
lst=eval(input("Enter a list: "))
ele=int(input("Enter no to be searched: "))
bsearch(lst,ele)
