list1=[]
limit=int(input("Enter the limit:"))
for i in range(limit):
    element=input("Enter the color:")
    list1.append(element)
print(list1)
list2=[]
limit=int(input("Enter the limit:"))
for i in range(limit):
    element2=input("Enter the color:")
    list2.append(element2)
print(list2)
for i in list1:
    if i not in list2:
        print(i)
        
