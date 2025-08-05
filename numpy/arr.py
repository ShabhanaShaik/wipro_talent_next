import numpy as np
x=np.array([1,2,3,4,5])
#print("array 1-D",x)
###############################################
y=np.array([[1,2],[2,4]])
#print("Array 2-D\n",y)
#############################################
o=np.ones((3,6))
#print("ones\n",o)
#############################################
o=np.zeros((3,6))
#print("zeros\n",o)
##########################################
i=np.eye(3)
#print("Identical coordinates:\n",i)
########################################
r=np.arange(0,11,2)
#print("array",r)
########################################
separate=np.linspace(0,1,5)
#print("linspace",separate)


a=np.arange(1,10)
print(a)
resh=a.reshape((3,3))
print(resh)
print("element at (1,1):",resh[1,1])
linear=resh.flatten()
#print(linear)
#print("greater than 5:",linear[linear>5])
#print("less than 5:",linear[linear<5])

#print("random numbers between 0 to 3:",np.random.rand(3))
#print("random interger:\n",np.random.randint(1,100,(2,3)))

#code to print 3x3 matrix which is filled with boolean value True using numpy
a=np.full((3,3),True)----->gives value of user in userdefined times
print(a)
