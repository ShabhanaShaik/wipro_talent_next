#read 5 numbers from list both _+ve and -ve and make a count of nums of +ve and -ve num "0" is considered as +ve
l=[]
pos_count=0
neg_count=0
for i in range (5):
    a=int(input(f"enter number{i+1}:"))
    l.append(a)
for j in l:
    if j>=0:
        pos_count+=1
    else:
        neg_count+=1
print("positive nums count",pos_count)
print("negative nums count",neg_count)
