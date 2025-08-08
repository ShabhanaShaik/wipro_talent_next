import matplotlib.pyplot as plt
import numpy as np

"""x=np.linspace(0,10,100)
y1=np.sin(x)
y2=np.cos(x)
y3=np.tan(x)
plt.plot(x,y1,label='sin(x)',color='blue')
plt.plot(x,y2,label='cos(x)',color='green')
plt.plot(x,y3,label='tan(x)',color='red')

plt.xlabel('x')
plt.ylabel('y')
plt.title("Multiple lines in a plot",ha='left',va='top')
plt.legend()
plt.grid()

plt.show()"""

#########################################
########singlelinecall plot

"""x=np.linspace(0,10,100)
y1=np.sin(x)
y2=np.cos(x)
plt.plot(x,y1,'b--',x,y2,'r--')
plt.xlabel('x')
plt.ylabel('y')
plt.title("multiple lines in single plot call")
plt.legend()
plt.grid()
plt.show()"""

##################################
##########multiple lines using loop
"""x=np.linspace(0,10,100)
functions=[(np.sin(x),'sinx','blue',':'),(np.cos(x),'cos(x)','green','-.'),(x**2,'x^2','red','--')]
for fun,label,color,ls in functions:
    plt.plot(x,fun,label=label,color=color,ls=ls)
plt.xlabel('x')
plt.ylabel('y')
plt.title("multiple lines using loop")
plt.legend()
plt.grid()
plt.show()"""


##################################################
#########subplots########### 3 rows 1 column
"""x=[1,2,3,4]
y1=[10,20,30,40]
y2=[30,25,20,10]
y3=[2,4,6,8]
plt.subplot(3,1,1)
plt.plot(x,y1)
plt.title("first plot")
plt.subplot(3,1,2)
plt.plot(x,y2)
plt.title("second plot")
plt.subplot(3,1,3)
plt.plot(x,y3)
plt.title("third plot")
plt.show()"""
##################################
########## 
# 1 row,3 colmns
x=[1,2,3,4]
y1=[10,20,30,40]
y2=[30,25,20,10]
y3=[2,4,6,8]
plt.subplot(1,3,1)
plt.plot(x,y1)
plt.title("first plot")
plt.subplot(1,3,2)
plt.plot(x,y2)
plt.title("second plot")
plt.subplot(1,3,3)
plt.plot(x,y3)
plt.title("third plot")
plt.show()