#prompt the user for a list of integers.For all values greaterthan 100 store write'over'instead of that number.
l=int(input("Enter the limit:"))
list=[]
for i in range(l):
    no=int(input("Enter the number:"))
    if (no>100):
        list.append('over')
    else:
        list.append(no)
print(list)        
    
