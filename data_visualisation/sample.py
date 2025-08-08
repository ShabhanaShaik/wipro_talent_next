import matplotlib.pyplot as plt
import numpy as np
x=[1,2,3,4,5]
y=[10,20,30,40,50]
plt.figure(figsize=(10,6),dpi=100)
plt.plot(x,y,color='blue',ls=':',lw=4,marker='*',markerfacecolor='green',markersize=8,markeredgecolor='black')
plt.title("Line plot",fontsize=18,ha='left',va='top',fontweight='bold',color='orange')
plt.xlabel("years of working",fontsize=12)
plt.ylabel("profit in millions",fontsize=12)
plt.gca().set_facecolor("#d580ff")
plt.gcf().set_facecolor("#ffccee")
plt.grid(True,ls='--',lw=1.5,alpha=0.7,color='yellow')
plt.show()