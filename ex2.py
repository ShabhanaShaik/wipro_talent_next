'''s={'a':1,'b':2}
s['a'],s['b']=s['b'],s['a']
#s['b']=s['a']
print(s)
import itertools
gen=iter([1,2,3])
l=list(gen)
l[0],l[1]=l[1],l[0]
print(l)

n=10
print([(i**2) for i in range(1,n+1) if i%2==0])
num=int(input())
copy=num
sum=0
while(num>0):
 rem=num%10
 fact=1
 for i in range(1,rem+1):
  fact*=i
 sum=sum + fact
 num//=10
if sum==num:
 print(copy,"strong")
else:
 print(copy,"not strong")
num=int(input("enter"))
sum=0
while(num!=0):
    rem=num%10
    sum=rem+sum
    num=num//10
if(num%sum)==0:
    print("nivens")
else:
    print("not")
num=int(input("enter"))
visit=set()
while num!=1 and num not in visit:
    visit.add(num)
    sum=0
    temp=num
    while temp>0:
        d=temp%10
        sum=sum+ d**2
        temp//=10
    num=sum
if num==1:
    print("happy")
else:
    print("not")
term=int(input("enter"))
value=0
for i in range(1,term+1):
    if i%2==0:
        value=                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              ((i//2)-1) * 7
    else:
        value=(i//2)*6
print("the",term,"th value is",value)
#1 1 2 3  4 9 8 
num=int(input("enter the term"))
if num%2==1:
    print(2**(num//2))
else:
    print(3**(num//2-1))
 #pattern
n=int(input("enter"))
for i in range(n):
  for j in range(n):
        if (i==j or i+j==n-1 or i==0 or i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
  print()
n=int(input("enter rows"))
totalrows=2*n-1
for i in range(1,totalrows+1):
    if i<=n:
        spaces=i-1
        stars=2*(n-i)+1
    else:
        spaces=totalrows-i
        stars=2*(i-n)+1
    print(" "*spaces+"*"*
    stars)'''


















