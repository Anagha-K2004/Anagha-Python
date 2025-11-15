dic={}
limit=int(input("Enter the limit:"))
for i in range(limit):
    k=input("Enter the key:")
    val=input("Enter the value:")
    dic[k]=val
print("In ascending order")
print(dict(sorted(dic.items())))
print("In Descending order")
print(dict(sorted(dic.items(),reverse=True)))

    
