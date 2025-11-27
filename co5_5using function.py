import csv
#input dictionary using user input method
data={}
n=int(input("Enter the limit:"))
for i in range(n):
    k=input("Enter the key:")
    v=input("Enter the value:")
    data[k]=v
print(data)

def cwrite():
#csv writing
    f=open("dictdata.csv","a",newline='')
    content=csv.writer(f)
    content.writerow(data.keys())
    content.writerow(data.values())
    f.close()
cwrite()

def cread():
#csv reading
    f1=open("dictdata.csv","r")
    c=csv.reader(f1)
    for i in c:
        print(i)
    f1.close()
cread()

