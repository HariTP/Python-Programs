import mymodule
lst=[2,5,6,3,4,4,3,5,5,7,9,0]
print("First function of module:")
mymodule.odd(lst)
print("\nSecond function of module:")
mymodule.even(lst)
print("\nThird function of module:")
mymodule.count(lst,5)

from mymodule import odd,even,count
lst=[2,5,6,3,4,4,3,5,5,7,9,0]
print("Odd numbers in the list are as below:--")
odd(lst)
print("\nEven numbers in the list are as below:--")
even(lst)
print("\nCount function gives the following result:--")
count(lst,5)

