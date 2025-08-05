"code to take two arrays a and b ,integrate a and b vertically and horizontally"
import numpy as np
"""
# Input for array a
a = list(map(int, input("Enter 3 numbers for array a (space separated): ").split()))
# Input for array b
b = list(map(int, input("Enter 3 numbers for array b (space separated): ").split()))

# Convert to numpy arrays
a = np.array(a)
b = np.array(b)
v=np.vstack((a,b))
# Vertical and Horizontal stacking
print("Vertical stack:\n", np.vstack((a, b)))
print("Horizontal stack:\n", np.hstack((a, b)))
print("element 5 access:",v[1,1])"""

#code to extract all the odd numbers from user input and print them in a list using array of numpy
#input:1 2 3 4 5 9 8 7 6
#output:[1,3,5,9,7]-->only odd nums
#output=[true,2,true, 4,true,true,8,true,6]----->odd nums as true
"""a=list(map(int,input("enter 9 numbers separated by space:").split()))
a=np.array(a,dtype=object)
a[a%2==1]=True----------> replace odd nums as true
a[a%2==1]=1----->replace odd nums with -1
a[a%2==0]="Even"-------->if want to replce even nums as 'even'
print(a)"""
"""l=[]
for i in a:
    if i%2!=0:
        #i=-1---->odd num then replace it with -1
        i="True"
        l.append(i)
    else:
        l.append(i)
print(np.array(l))"""

"""#code to print 3 multiples as true and remain as false
#input=[2,3,5,6,7]
#output=[false,true,false,true,false]
a=list(map(int,input("enter 5 space sep nums:").split()))
a=np.array(a,dtype=object)
a[a%3==0]=True
a[a!=True]=False
print(a)"""

#array  slicing
"""a=np.array([[1,2,3],[4,5,6]])
print("elemnts at [0:1]",a[0,1])
print("first row",a[0,:]) 
print("remove first element at rows",a[:,1:])
a[0,0]=100
print("modify",a)
"""
#nan------>handle
#statastical func on array
a=np.array([1,2,3,np.nan,5])
print("Ignoring naN:",np.nanmean(a))
print("sum:",np.nansum(a))
#standard deviation formula Sqrt1.N Ei=1 to N(x~i=u)**2
print("std Ignoring naN:",np.std(a[~np.isnan(a)]))

#Replace naN
a=np.array([1,np.nan,3,4,5])
print(a)
a[np.isnan(a)]=0
print(a)
print(np.where(np.isnan(a),0,a))#using np.where to replace nan with 0

#universal functions
a=np.array([1.5,2.9,9.8])
print(a.astype(np.int32))#convert float to int
a=np.array([1,5,2,4,9,8])
print(a.astype(np.float64))#conert int to float
a=np.array([1.5,2.9,9.8])
print(a.astype(str))#convert float to str
a=np.array([0,1,7,0])
print(a.astype(bool))#convert num to bool
a=np.array([True,True,False,True])
print(a.astype(np.int32))#convert bool to int
a=np.array([1.5,2.9,9.8])
print(a.astype(np.complex128))#convert float to comlex
a=np.array([1,2,3,4])
print(a.astype(np.int8)) #convert int to unsigned int
a=np.array([2050101,19990101])
print(a.astype('datetime64[D]'))#convert int to datetime
a=np.array(['1','2','9'])
print(a.astype(np.int32))#convert string to int