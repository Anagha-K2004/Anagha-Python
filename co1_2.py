#dispaly future leap year from current year to final year.(2028)
from datetime import date
current=date.today().year
final=int(input("Enter the Final year:"))
for i in range(current,final+1):
    if (i%4==0 and i%100!=0 or i%400==0):
        print(i)
    
