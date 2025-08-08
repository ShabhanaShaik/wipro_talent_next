import pandas as pd
"""import numpy as np
data={'patient_id':['p1','p2','p3','p4','p5'],'patient_name':['vijay','ajay','suresh','amit',None],'age':[34,42,None,33,44],'dept':['neurology','cancer','icu','cardiology','pulmonory'],
      'bill_no':[7000.50,60000.0,43200.0,None,87000.0],'admission_date':['2025-02-12','2024-09-09','2025-01-22','2024-12-12','2024-05-08']}
df=pd.DataFrame(data)
df.to_csv('hospital_data.csv',index=False)
print("created csv file succesfully")"""

#########################################################
"""try:
    df=pd.read_csv('hospital_data.csv')
    print("\n Hospital Dataframe")
    print(df)
    #display basic info
    print("\n dataframe INFO")
    print(df.info())------------->csv file information
    print("\n summary statistics")
    print(df.describe())
except FileNotFoundError:
    print("error:'hospital_data.csv not found")"""

##############find missing values
"""try:
    df=pd.read_csv('hospital_data.csv')
    print("\noriginal hospital Dataframe")
    print(df)
#check missing values
    print("\n Missing values:")
    print(df.isna())
#filling name by unkonwn,value by 0
    df_filled=df.copy() 
    df_filled['patient_name']=df_filled['patient_name'].fillna('unknown')
    df_filled['age']=df_filled['age'].fillna(df_filled['age'].mean())
    df_filled['bill_no']=df_filled['bill_no'].fillna(0)
    print("\n after filling by default")
    print(df_filled)
except FileNotFoundError:
    print("error:'hospital_data.csv not found")"""

"""names=pd.Series(['apple','oranges','kiwi'])
df=names.to_frame(name='Name')--------->series to frame
#add new colmn
df['price']=[50,30,80]------>adding new colmn to dataframe
print(df)"""

######################################################
###########grouping of data in csv file########
"""try:
    df=pd.read_csv('hospital_data.csv')
    print("\n Original Dataframe")
    print(df)
#grouping by dept
    grouped=df.groupby('dept')['bill_no'].mean()
    print("\n avg medical cost by dept")
    print(grouped)
except FileNotFoundError:
    print("error:'hospital_data.csv doesnt exists")"""


###################################################
###########apply discount t bill amount
"""try:
    df=pd.read_csv('hospital_data.csv')
    print("\n original data of hospital")
    print(df)
#add discount_cost colmn(10%discount)
    df['discount']=df['bill_no']*0.9---------->add discount colmn
#sorting by bill
    sorted_df=df.sort_values('bill_no',ascending=False)--------->sort colmns by bill amount
    print("\n sorted by medical bills(descending order):")
    print(sorted_df)
except FileNotFoundError:
    print("error:hospital_data.csv doesnt exists")"""


####################################################
#############add a status colmn based on age
"""try:
    df=pd.read_csv('hospital_data.csv')
    print("\n original hospital dataframe")
    print(df)
#add a status colmn,baed on age
    df['status']=df['age'].apply(lambda x:'senior' if x>=45 else 'adult' if x>=18 and x<45 else 'teenager')
    print("\n dataframe with status colmn:")
    print(df)
#saving to csv
    df.to_csv('hospital_data_updated.csv',index=False)
    print("\n modified dataframe saved ")
except FileNotFoundError:
    print("error:'hospital_data.csv' dosent exists")"""

#########################################################
#########edit bill by manuallyyyyyyyyy
"""try:
    df=pd.read_csv('hospital_data.csv')
    series=df['bill_no']
    print("\n original hospital dataframe")
    print(series)
#user manual input
    print("\n enter patient id to update:")
    newpatient_id=input().strip()
    print(f"enter new bill for {newpatient_id}:")
    new_cost=float(input())
#update bill series and save
    if newpatient_id in df['patient_id'].values:
        index=df[df['patient_id']==newpatient_id].index[0]
        series[index]=new_cost
        print("\n updates medical bill series")
        print(series)
#update dataframe and save
        df['bill_no']=series
        df.to_csv('hospital_data.csv',index=False)
        print("\n updated hospital data after bill amount updated ")
        #print(df.isna())
        df_filled=df.copy()
        df_filled['patient_name']=df_filled['patient_name'].fillna('unknown')
        df_filled['age']=df_filled['age'].fillna('unknown')
        print(df_filled)
    else:
        print(f"error:patient_id{newpatient_id}not found.")
except  FileNotFoundError:
    print("error:'hospital_data.csv' doesnt exists")     """


