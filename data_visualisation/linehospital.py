###################################################
###########plotting a csv file data or csv file


import pandas as pd
import matplotlib.pyplot as plt
try:
    df=pd.read_csv('hospital_data.csv')
    cost_series=df['bill_no']
    date_series=df['admission_date']
    print("\n original series")
    print(cost_series)
    print("\n original Date series:")
    print(date_series)
#user input for cleaning and plotting
    print("fill the missing bill value from median value?(yes/no)")
    fill_confirm=input().strip().lower()
    print("convert admission date to DD/MM/YYYY for display?(yes/no)")
    date_format_confirm=input().strip().lower()
#perform clean bill missing values
    if fill_confirm=='yes':
        median_cost=cost_series.median()
        cleaned_cost_series=cost_series.fillna(median_cost)
        print(cleaned_cost_series)
    else:
        print("\n no changes to medical cost")
#convert admission date to datetime
    cleaned_date_series=pd.to_datetime(date_series,format='%Y-%m-%d',errors='coerce')
    if date_format_confirm=='yes':
        display_dates=cleaned_date_series.dt.strftime('%d-%m-%Y')
        print(cleaned_date_series)
    else:
        display_dates=cleaned_date_series
#plot
    plt.figure(figsize=(10,6))
    plt.plot(cleaned_date_series,cleaned_cost_series,marker='o',ls='-',color='blue')
    plt.title("Medical Cost over admission dates")
    plt.xlabel("admission date")
    plt.ylabel("medical cost($)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
except FileNotFoundError:
    print("error:'hospita_data.csv'doesnt exists")