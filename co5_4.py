import csv
f=open("data.csv","r")
content=csv.reader(f)
index=int(input("Enter a Number:"))
for i in content:
    print(i[index])
