#(a+b) * c exp evaluate lambda and returns to another lambda
"""p=(lambda a:lambda b,c:(a+b)*c)(5)(3,2)
print(p)"""
#(a+b) *(c+d) evaluate
"""p=(lambda a:lambda b:lambda c,d:(a+b)*(c+d))(5)(2)(3,4)
print(p)"""
##############
"""p=(lambda a,b:(a+b))(5,2)------------>another way
r=(lambda p,q:p*q)(p,q)
print(r)
"""
###############
#(a-b)/(c-d) evaluate
"""o=(lambda a,b:(lambda c,d:(lambda p,q:p/q)(a-b,c-d)))(1,2)(3,4)
print(o)"""

#################
"""num=int(input("a:"))
n=int(input("x:"))
oper=lambda a:lambda x:(x+a)**2
numsq=oper(num)
print(numsq(n))"""

##########evaluate exp (a-b)/(c-d)
"""try:
    o=(lambda a:lambda b:lambda c,d:(a-b)/(c-d))("10")(4)(8,8)
    print(o)
except ZeroDivisionError:
    print("division by zero error!!")
except TypeError:
    print("invalid datatype!!")

"""
"""o=(lambda a:lambda b:lambda c,d:a+'-'+b+'-'+c+'-'+d)('hi')("nriians")("gud","mrg")
print(o)"""

#given attributes a,b,c,d are hi,!,students,!!! writee a program of nested lambda to concatinate the abcd,by converting a and c to uppercase
#OUTPUT:HI!STUDENTS!!!
"""o=(lambda a:lambda b:lambda c,d:a.upper()+b+c.upper()+d)('hi')('!')('students','!!!')
print(o)"""
######
#given attributes a,b,c,d are hi,!,students,!!! writee a program of nested lambda to concatinate the abcd,by reversing with sep " "
#OUTPUT:IH!STNEDUTS!!!
"""o=(lambda a:lambda b:lambda c,d:[a[::-1]+","+b+","+c[::-1]+","+d])('hi')('!')('students','!!!')
print(o)"""

###num=[4,6,3,8] clist=[12,12,9,16] implement in nested lambda

x=(lambda x:lambda i:i*3 if i<5 else i*2)
above_5=x(5)
num=[4,6,3,8]
o=list(map(above_5,num))
print(o)




