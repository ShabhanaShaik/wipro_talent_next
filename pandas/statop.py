
"""code to show the computation of statistics and access series attributes 
100 200 150 300 250
print original data,which is serialised
statistics:
mean
sum
max
min
attributes:
index=['a'....'e']
values=[100.0..250.0]"""
import pandas as pd
"""print("enter 5 random nums,space separated:")
nums=input().strip().split()
nums=[float(num) for num in nums]
try:
    if len(nums)!=5:
        raise ValueError ("please enter 5 nums only")
    series=pd.Series(nums,index=['a','b','c','d','e'])
    print("\n original series")
    print(series)
#statistics
    print("\n statistics")
    print(f"mean:{series.mean()}")
    print(f"sum:{series.sum()}")
    print(f"max:{series.max()}")
    print(f"min:{series.min()}")
    #Attributes
    print("\n attributes")
    print(f"index:{series.index.tolist()}")
    print(f"values:{series.values.tolist()}")
    print(f"datatype:{series.dtype}")
except ValueError as e:
    print(f"error:{e}")"""

#######################################################
##vectoring####
print("enter 4 nums,space separated")
nums=input().strip().split()
nums=[float(num) for num in nums]
try:
    if len(nums)!=4:
        raise ValueError("give 4 nums only!")
    series=pd.Series(nums,index=['a','b','c','d'])
    print("\n original seires")
    print(series)
#doubling values vector operation
    doubled=series*2
    print("\n doubled series")
    print(doubled)
#adding 100 to values vector operations
    added=series+100
    print("\n series after vector operations")
    print(added)
except ValueError as e:
    print(f"error{e}")