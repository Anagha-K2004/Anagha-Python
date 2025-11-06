#co3_A Generate positive list of numbers from a given list of integers
limit=int(input("Enter the limit:"))
list=[]
for i in range(limit):
    num=int(input("Enter the number:"))
    if (num>0):
        list.append(num)
print(list)
