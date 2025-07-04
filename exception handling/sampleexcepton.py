"""num=int(input("enter numerator"))
dno=int(input("enter denominator"))
try:
    quo=num/dno
    print("quotient",quo)
except ZeroDivisionError:
    print("denominator cant be zero")"""
"""try:
    n=int(input("enter num:"))
    print(n*4)
except KeyboardInterrupt:
    print("\n num should be entered")
except ValueError:
    print("pls check before you enter data type")
print("bye")"""
"""try:
    n=int(input("enter num:"))
    print(n*4)
except (KeyboardInterrupt,ValueError,TypeError) as e:
    print("\n num should be entered..\n ",type(e).__name__)"""
"""try:
    file=open('file.txt')
    str=file.readline()
    print(str)
    
except IOError:
    print("error occured during input take")

else:
    print("succssfully fetched data")"""


    