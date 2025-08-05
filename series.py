import pandas as pd
"""print("enter 3 names separated with space:")
names=input().strip().split()------------->basic code for series dataframe creation
print("enter 3 index labels:")
indices=input().strip().split()
try:
    if len(names)!=3 or len(indices)!=3:
        raise ValueError("please provide exact names with indices")
    series=pd.Series(data=names,index=indices)
    print("created a new series:")
    print(series)
except ValueError as e:
    print(f"error:{e}")"""


#code elaborate how to filter numerical data in series based on condition(eg:values > thresold)
"""print("enter 4 randoom nums ,space separate")
nums=input().strip().split()
nums=[float(num) for num in nums]
try:
    if len(nums)!=4:
        raise ValueError("please provide exactly 4 nums:")
    total_data=pd.Series(nums)
    print(total_data)

    filtered=total_data[total_data>10]--->threshold set
    print("values greter than 10:")
    print(filtered)
except ValueError as e:
    print(f'error{e}')"""

#code elaborate how to filter numerical data in series based on conditioin insentivity
"""import pandas as pd

print("Enter 5 random strings, space separated:")
strings = input().strip().split()

print("Enter substring:")
substring = input().strip()

try:
    if len(strings) != 5:
        raise ValueError("Please provide exactly 5 strings.")

    series = pd.Series(data=strings)
    print("\nOriginal Series:")
    print(series)

    filtered_series = series[series.str.lower().str.contains(substring.lower(), na=False)]

    print(f"\nStrings containing '{substring}' (case-insensitive):")
    print(filtered_series if not filtered_series.empty else "No match found.")

except ValueError as e:
    print(f"Error: {e}")"""






