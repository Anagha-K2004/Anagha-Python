import csv
f=open("stud1.csv","w",newline="")
content=csv.writer(f)
for i in range(2):
    name=input("Enter Your Name:")
    age=int(input("Enter Your Age:"))
    grade=input("Enter Your Garde:")
    mark=float(input("Enter Your Mark:"))
    l=[name,age,grade,mark]
    content.writerow(l)
f.close()

f1=open("stud1.csv","r")
content=csv.reader(f1)
for i in content:
    
    print(i)

#create a base class student with attributes name,age,mark and a
#derived classsem1(mark)and derive another class
#final(grade)and display all the details using method overloading
    
