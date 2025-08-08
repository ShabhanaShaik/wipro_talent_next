####################################
###simle Histogram
import numpy as np
import matplotlib.pyplot as plt
"""np.random.seed(5)
data=np.random.randint(1,100,50)
plt.hist(data,bins=10,color='green',edgecolor='white')
plt.xlabel('Values range ')
plt.ylabel('Equality share')
plt.title("Histogram")
#plt.grid()
plt.show()"""

#########################################
##########multiple histograms
"""np.random.seed(42)
data1=np.random.randint(1,100,50)
data2=np.random.randint(1,100,50)
data3=np.random.randint(1,100,50)
plt.hist(data1,bins=10,alpha=0.5,label='Dataset-1',color='orange',edgecolor='black')
plt.hist(data2,bins=10,alpha=0.5,label='Dataset-2',color='yellow',edgecolor='black')
plt.hist(data3,bins=10,alpha=0.5,label='Dataset-3',color='red',edgecolor='black')
plt.xlabel("Values")
plt.ylabel("frequency")
plt.title("multiple histograms overlapping")
plt.legend()
plt.show()"""

######################################################
##############multiple 3D histogrms
from mpl_toolkits.mplot3d import Axes3D
np.random.seed(42)
data1=np.random.randint(1,100,50)
data2=np.random.randint(1,100,50)
data3=np.random.randint(1,100,50)

bins=10

count1,bin_edges=np.histogram(data1,bins=bins,range=(0,100))
count2,bin_edges=np.histogram(data1,bins=bins,range=(0,100))
count3,bin_edges=np.histogram(data1,bins=bins,range=(0,100))

bin_centers=0.5*(bin_edges[:-1]+ bin_edges[1:])
fig=plt.figure(figsize=(12,8))
ax=fig.add_subplot(111,projection='3d')

dx=dy=(bin_edges[1]-bin_edges[0]) * 0.5

x1=bin_centers-dx
x2=bin_centers
x3=bin_centers+dx

y1=np.zeros_like(x1)
y2=np.zeros_like(x2)*1.5
y3=np.zeros_like(x3)*3

ax.bar3d(x1,y1,np.zeros_like(count1),dx,dy,count1,color='red',alpha=0.8,label='Dataset-1')
ax.bar3d(x2,y2,np.zeros_like(count2),dx,dy,count2,color='green',alpha=0.8,label='Dataset-2')
ax.bar3d(x3,y3,np.zeros_like(count3),dx,dy,count3,color='blue',alpha=0.8,label='Dataset-3')

ax.set_xlabel("values")
ax.set_ylabel("frequency")
ax.set_title("Multiple histograms overlapping")
ax.set_yticks([0,1.5,3])
ax.set_yticklabels(['Dataset1','Dataset2','Dataset3'])
plt.legend()
plt.show()