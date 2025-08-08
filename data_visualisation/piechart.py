####################################################
###########pie chart example 
import matplotlib.pyplot as plt
""""labels=['apples','oanges','kiwi','watermelon']
prizes=[30,25,35,10]
explode=(0,0,0,0.2)
colors=['red','orange','green','yellow','blue']
plt.pie(prizes,labels=labels,colors=colors,startangle=90,explode=explode,shadow=True,autopct='%1.1f%%')
plt.title("fruits prizes")
plt.axis('equal')
plt.legend()
plt.show()"""

###################################################3
####customise pie charts
"""labels=['c','c++','JAVA','python','Datascience']
prizes=[400,450,1100,700,1350]
colors=['blue','orange','brown','magenta','green']
explode=[0,0,0.2,0,0]
def label_prizes(pct,all_vals):
    absolute=int(round(pct/100.*sum(all_vals)))
    return f'Rs.{absolute}'
plt.figure(figsize=(8,8))
wedges,texts,autotexts=plt.pie(prizes,labels=labels,colors=colors,explode=explode,
                               autopct=lambda pct:label_prizes(pct,prizes),pctdistance=0.6,shadow=True,
                               startangle=90,textprops={'fontsize':12,'fontweight':'bold','color':'black'})
plt.title("Book prizes",fontweight='bold',fontsize=16)
plt.axis('Equal')
plt.legend()
plt.gcf().set_facecolor(color='violet')
plt.show()"""

#################################################
#####pie chart 3D
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Wedge
from matplotlib.collections import PatchCollection

labels=['C','C++','Java','Python','Datascience']
prizes=[400,450,1100,700,1350]
colors=['red','yellow','pink','green','blue']

total=sum(prizes)
fracs=[p/total for p in prizes]
angles=[frac*360 for frac in fracs]

fig=plt.figure(figzise=(8,8))
ax=fig.add_subplot(111,projection='3d')

radius=1
height=0.3
start_angle=0
for i,angle in enumerate(angles):
    theta=np.linspace(np.deg2rad(start_angle),np.deg2rad(start_angle+angle),30)
    x=np.append([0],radius*np.cos(theta))
    y=np.append([0],radius*np.sin(theta))
    ax.plot_trisurf(x,y,height,color=colors[i],alpha=0.8)
    ax.plot_trisurf(x,y,0,color=colors[i],alpha=0.8)

    for j in range(len(theta-1)):
        xs=[radius*np.cos(theta[j]),radius*np.cos(theta[j+1])]
        ys=[radius*np.cos(theta[j]),radius*np.sin(theta[j+1])]
        zs=[0,0,height,height]
        verts=[list(zip(xs,ys,zs))]
ax.add_collection3d(plt.Poly)
