#raise exception[,args[,tracebac]]]
"""try:
    num=1
    print(num)
    raise ValueError
except:
    raise ValueError
    print("error!!")"""
###AssertionError
"""c=int(input("enter temp in c"))
f=(c*9/5)+32
assert(f<=32), "Its cold"
print("fahrenheit",f)"""
'''write a program whic infinitely prints natural num'''
#StopIteration error example
"""def display(n):
  while True:
   try:
    n+=1
    if n==21:
     raise StopIteration
   except StopIteration:
      break
   else:
    print(n,end=' ')
i=0
display(i)"""
## RandomError
"""import random
class RandomError(Exception):
    pass
try:
    num=random.random()
    if num<0.1:
        raise RandomError
except RandomError as e:
    print("random error generated")
else:
    print("%.4f"%num)
"""

