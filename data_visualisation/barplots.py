"""import matplotlib.pyplot as plt
stud=['A','B','C','D','E']
marks=[77,45,56,80,95]
colors=['red','grey','brown','orange','yellow']
bars=plt.bar(stud,marks,color=colors,edgecolor='black',lw=2,width=0.5,align='center',hatch='//')
for bar in bars:
    height=bar.get_height()
    plt.text(bar.get_x()+bar.get_width()/2,height+0.5,str(height),ha='center',fontsize=10)
#plt.bar(stud,marks) #vertical
#plt.barh(stud,marks,color=colors,edgecolor='black',lw=2,height=0.5,hatch='')#horizontal
plt.title("performance bar chart",loc='left',color="green")
plt.xlabel("students")
plt.ylabel("marks/100")
plt.legend()
plt.grid(ls=':',lw=0.6)
plt.gca().set_facecolor('pink')
plt.tight_layout()
plt.show()
"""

####################################################
###########colo mapping with 

"""import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import numpy as np
stud=['ram','ravi','rahul','ritesh']
marks=[10,50,30,40]
norm=mcolors.Normalize(vmin=min(marks),vmax=max(marks))
cmap=cm.plasma#plasma colors
cmap=cm
colors=cmap(norm(marks))
fig,ax=plt.subplots()
bars=ax.bar(stud,marks,color=colors,edgecolor='black')
sm=cm.ScalarMappable(cmap=cmap,norm=norm)
sm.set_array([])
cbar=plt.colorbar(sm,ax=ax)
cbar.set_label('Marks')
ax.set_title("Bar chart with plasma")
ax.set_xlabel('students')
ax.set_ylabel('Marks')
plt.tight_layout()
plt.show()"""
#############################################
######3d barplot######################
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
"""fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(111,projection='3d')
x=np.array([10,20,30])
y=np.array([10,20,30])
z=np.zeros(3)
dx=dy=np.ones(3)*0.4
dz=np.array([[5,10,15],[10,5,20],[15,20,5]])
np.random.seed(42)
colors=plt.cm.tab10(np.random.rand(len(x)*len(y)))
color_index=0
for i in range(len(x)):
    for j in range(len(y)):
        ax.bar3d(x[i],y[j],z[i],dx[i],dy[j],dz[i,j],color=colors[color_index],edgecolor='black')
        color_index +=1
ax.set_xlabel("X-axis")
ax.set_ylabel("y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("3D plot")
ax.view_init(elev=15,azim=60)
plt.grid()
plt.show()"""

###########################################
###multiple bars##########
"""data=['A','B','C','D']
x=np.arange(len(data))
v1=[5,10,15,20]
v2=[8,12,10,18]
v3=[3,7,13,17]
width=0.25
x1=x-width
x2=x
x3=x+width
np.random.seed(42)
colors=plt.cm.tab10(np.random.rand(3))
fig,ax=plt.subplots(figsize=(8,6))

ax.bar(x1,v1,width,label='Dataset 1',color=colors[0],edgecolor='black',alpha=0.4)
ax.bar(x2,v2,width,label='Dataset 2',color=colors[1],edgecolor='black',alpha=0.4)
ax.bar(x3,v3,width,label='Dataset 3',color=colors[2],edgecolor='black',alpha=0.4)
ax.set_xlabel('data',fontsize=12,color='darkblue')
ax.set_ylabel('values',fontsize=12,color='darkblue')
ax.set_title("multiple bar graphs")
ax.legend(fontsize=10)
plt.tight_layout()
plt.show()"""

data=['A','B','C','D']
x=np.arange(len(data))
v1=[5,10,15,20]
v2=[8,12,10,18]
np.random.seed(42)
colors=plt.cm.tab10
z
(np.random.rand(2))
fig,ax=plt.subplots(figsize=(6,4))
ax.bar(x,v1,label='Dataset 1',color=colors[0],edgecolor='black',alpha=0.8)
ax.bar(x,v2,label='Dataset 2',color=colors[1],edgecolor='black',alpha=0.8)
ax.set_xlabel('Data')
ax.set_ylabel('values')
ax.set_title("stacked bar graphs")
ax.legend()
plt.tight_layout()
plt.show()

