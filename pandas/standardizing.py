import pandas as pd
import numpy as np
"""try:
    df=pd.read_csv('hospital_data.csv')
    series=df['patient_name']
    print("original  name series:\n")
    print(series)
    clean_series=series.str.title().str.strip()----->name first letter capital
    print("name series after standardization with(tite case,stripped space):")
    print(clean_series)
#saving to csv dataframe
    df['patient_name']=clean_series
    df.to_csv('hospital_data.csv',index=False)
    print("DATA saved to csv file")
except FileNotFoundError:
    print("error:'hospital_data.csv' doesnt exists")"""

"""try:
    df=pd.read_csv('hospital_data.csv')
    series=df['age']
    print("\original age series:")
    print(series)
#replace invalid ages ,< 0 or >120 with nan
    clean_series=series.where((series>=0) & (series<=120),np.nan)
    print("\n age series after replacing invalid ages with naN:")
    print(clean_series)
except FileNotFoundError:
    print("error:'hospital_data_csv'doesnt exists")"""

try:
    df=pd.read_csv('hospital._data.csv')
    series=df['admission_date']
    print("\n original admission_date")
    print(series)
    print("\n convert admisiion dateformat from y/m/d to d/m/y:")
    confirm=input().strip().lower()
    if confirm=='yes':
        date_series=pd.to_datetime(series,format='%y-%m-%d')
        f_series=date_series.dt.strftime('%d-%m-%y')
        print(" \n after conversion")
        print(f_series)
    
    #update dataframe
        df['admission_date']=f_series
        df.to_csv('hospital_dat.csv',index=False)
        print("\n updated with dates")
except FileNotFoundError:
    print("error")