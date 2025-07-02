'''class abc():
    def __init__(self,val):
        print("class method")
        self.val=val
        print("value is:",val)
obj=abc(10)'''
class abc():
    cv=0
    def __init__(self,var):
        abc.cv+=1
        self.var=var
        print("object var:",var )
        print("cls variable:",abc.cv)
    def __del__(self):
        abc.cv-=1
        print("obj with %d is going out of scope"%self.var)
obj1=abc(10)
obj2=abc(20)
del obj1
del obj2



