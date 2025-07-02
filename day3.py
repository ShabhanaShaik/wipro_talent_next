'''def hi(name):
    return f"Hello,{name}!"
print(hi("students"))'''
#def a(x,y=1):
    #return x*y
#print(a(5))
 #print(a(5,4))
#def num1(*args):
 #   avg=sum(args)/len(args)
  #  return f"max_val:{max(args)},min_val:{min(args)},avg_val:{avg}"
#print(num1(1,2,3,4,5))
#def info(**kwargs):
   # for key,value in kwargs.items():
        #print(f"{key}:{value}")
#info(name="shabbu",age=20,city="hyd")
#sq=lambda a:a*a 
#print(sq(5))
#add=lambda x,y:x+y
#print(add(5,2))   
#def fact(n):
 #   if n==0 or n==1:
 #       return 1
 #   else:
 #       return n*fact(n-1) 
#print(fact(5))
'''def is_even(n):
    if n==0:
        return True
    return is_odd(n-1)
def is_odd(n):
    if n==0:
        return False
    return is_even(n-1)
print(is_even(4))
print(is_odd(7))'''
'''def is_p(s):
    if len(s)<=1:
        return True
    return check_p(s,0,len(s)-1)
def check_p(s,start,end):
    if start>=end:
        return True
    if s[start]!=s[end]:
      return False
    return is_p(s[start+1:end])
print(is_p("racecar"))
print(is_p("fun"))'''
'''def ftail(n,acc=1):
    if n==0 or n==1:
        return acc
    return ftail(n-1,n*acc)
print(ftail(5))'''
'''def sfact(n):
    if n<=0:
        return 1
    return fact(n)*sfact(n-1)
def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)
print(sfact(4))'''
def pt(a,n):
    if n==1:
        return a
    return a**pt(a,n-1)
print(pt(2,3))
