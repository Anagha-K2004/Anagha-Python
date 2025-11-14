#enter two list of integers check weather the two list have same length and sum are same value or weather any value occur in both?
limit1=int(input("Enter the limit of 1st list:"))
list1=[]
for i in range(limit1):
    num1=int(input("Enter the numbers of 1st list:"))
    list1.append(num1)
    
limit2=int(input("Enter the limit of 2nd list:"))
list2=[]
for i in range(limit2):
    num2=int(input("Enter the numbers of 2nd list:"))
    list2.append(num2)

if len(list1)==len(list2):
    print("Both lists have same length.")
else:
    print("List have different length.")

if sum(list1)==sum(list2):
    print("List have same sum.")
else:
    print("List have different sum.")

status=False
c=0
for j in list1:
    if j in list2:
        status=True
        c=c+1

if status==True:
    print("both list have common",c,"VALUES")
else:
    print("both list have NOT common VALUES")
        
        
          


    


