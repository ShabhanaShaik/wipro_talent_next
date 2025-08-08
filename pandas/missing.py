"missing operations on nan"
import pandas as pd
import numpy as np
series=pd.Series([10,np.nan,30,np.nan,50],index=['a','b','c','d','e'])
print("\n original series:")
print(series)
#check missing values
print("\n missing values")
print(series.isna())
#replace nan with 0
filled_series=series.fillna(0)
print("\n series after filling nan with 0:")
print(filled_series)
#missing value deletion
dropped_series=series.dropna()
print("\n series after droppng  missing values")
print(dropped_series)