import pandas as pd
"""data={'name':['mark','steve','jenny'],'age':[22,21,22],'branch':['EEE','CSE','Mech']}---->static input for dataframe
dframe=pd.DataFrame(data)
print(dframe)"""
#dynamic input for dataframe

n=int(input("enter no.of profiles:"))
names=[]
ages=[]
branches=[]
for i in range(n):
    print(f"enter {i+1}---")
    name=input("enter name:")
    age=input("enter age:")
    branch=input("enter branch:")
    names.append(name)
    ages.append(age)
    branches.append(branch)
data={'name':names,'age':ages,'branch':branches}
dataframe=pd.DataFrame(data)
print("\n dataframe created")
print(dataframe)
#dataframe operations
#print(dataframe[['name','branch']])--->particular cols
#print(dataframe.iloc[1])--->particular row
#dataframe['stipend']=[10000,110000]-------->add dataframe
dataframe.insert(1,'age','stipend')
print(dataframe)
