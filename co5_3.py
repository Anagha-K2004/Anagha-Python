import csv
f=open("data.csv","r")
content=csv.reader(f)

for i in content:
    print(i)
