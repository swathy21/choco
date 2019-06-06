from statistics import median
from fractions import Fraction as fr 
mylist=[]
n=int(input("enter the number of elements"))
for i in range(0,n):
    x=int(input("enter the number"))
    mylist.insert(i,x)
print(median(mylist)) 
