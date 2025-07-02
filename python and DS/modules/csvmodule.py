import csv
with open ("people.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(['name','age'])
    for _ in range(2):
        name=input("enter name")
        age=int(input("enter age"))
        writer.writerow([name,age])
print("data written on csv file")