import matplotlib.pyplot as plt
"""x=[5,7,8,7,6,9,5,3,4,8]
y=[99,86,88,100,92,95,84,103,78,94]
plt.scatter(x,y)
plt.xlabel("X-axis")
plt.ylabel("Y axis")
plt.title("Scatterplot")
plt.grid()
plt.show()"""

########################################################
#########scatterplot with numpy####
import numpy as np
"""np.random.seed(10)
x=np.random.randint(1,100,300)
y=np.random.randint(1,100,300)
plt.scatter(x,y,color='white',marker='*',alpha=0.6)
plt.xlabel("X-axis")
plt.ylabel("y-axis")
plt.title("Random scatter plot")
plt.grid()
plt.gca().set_facecolor("#ca0d5c")
plt.show()"""

#########################################################
###############scatetrplot with random nums and random colors 2D
"""np.random.seed(20)
x=np.random.rand(50) * 100
y=np.random.rand(50) * 100
colors=np.random.rand(50)
sizes=np.random.randint(50,500,50)
scatter=plt.scatter(x,y,c=colors,s=sizes,cmap='cool',edgecolors='black',alpha=0.6)
plt.colorbar(scatter,label="color Scale")
plt.xlabel("X-axis")
plt.ylabel("y-axis")
plt.title("Random scatter plot")
plt.grid()
plt.show()"""

########################################################
#############scatterplot with randm colors and random nums 3D
from mpl_toolkits.mplot3d import Axes3D
"""np.random.seed(20)
x=np.random.rand(50) * 100
y=np.random.rand(50) * 100
z=np.random.rand(50) * 100
colors=np.random.rand(50)
sizes=np.random.randint(50,500,50)
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
scatter=ax.scatter(x,y,z,c=colors,s=sizes,cmap='plasma',edgecolors='black',alpha=0.7)
fig.colorbar(scatter,ax=ax,label="color Scale")
ax.set_xlabel("X-axis")
ax.set_ylabel("y-axis")
ax.set_zlabel("z-axis")
plt.title("Random scatter plot")
plt.grid()
plt.show()"""
############################################################33
############multiple 3D scatterplots############3
np.random.seed(42)
x1=np.random.rand(40) * 100
y1=np.random.rand(40) * 100
z1=np.random.rand(40) * 100
colors1=np.random.rand(40)
sizes1=np.random.randint(50,500,40)

x2=np.random.rand(40) * 100
y2=np.random.rand(40) * 100
z2=np.random.rand(40) * 100
colors2=np.random.rand(40)
sizes2=np.random.randint(50,500,40)

fig=plt.figure( figsize=(12,8))
ax=fig.add_subplot(111,projection='3d')
scatter1=ax.scatter(x1,y1,z1,c=colors1,s=sizes1,cmap='viridis',edgecolors='black',marker='H',alpha=0.7,label='Dataset 1')
scatter2=ax.scatter(x2,y2,z2,c=colors2,s=sizes2,cmap='hot',edgecolors='black',marker='P',alpha=0.7,label='Dataset 2')
cbar1=fig.colorbar(scatter1,ax=ax,shrink=0.5,pad=0.1)
cbar1.set_label('plasma')
cbar2=fig.colorbar(scatter2,ax=ax,shrink=0.5,pad=0.09)
cbar2.set_label('viridis')
ax.set_xlabel("X-axis")
ax.set_ylabel("y-axis")
ax.set_zlabel("z-axis")
plt.title("Random scatter plot with 2 datasets")
plt.legend()
plt.grid()
plt.show()