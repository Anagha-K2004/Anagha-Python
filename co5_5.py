import csv
#input dictionary using user input method
data={}
n=int(input("Enter the limit:"))
for i in range(n):
    k=input("Enter the key:")
    v=input("Enter the value:")
    data[k]=v
print(data)
#csv writing
f=open("dictdata.csv","w",newline='')
content=csv.writer(f)
content.writerow(data.keys())
content.writerow(data.values())
f.close()
#csv reading
f1=open("dictdata.csv","r")
c=csv.reader(f1)
for i in c:
    print(i)
f1.close()
