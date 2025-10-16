class bankaccount():
    def __init__(self,accno,accname,acctype,balance):
        self.accno=accno
        self.accname=accname
        self.acctype=acctype
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("Current Balance is",self.balance)
        print("Deposited Amount is",amount)
    def accountinfo(self):
        print("Account Number=",self.accno)
        print("Account Name=",self.accname)
        print("Account Type=",self.acctype)
        print("Account Balance=",self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient Balance!")
        else:
            self.balance -= amount
            print("withdrawn:",amount,"|Remaining Balance:",self.balance)
   

acno=int(input("Enter your Account Number:"))
name=input("Enter the Account Name:")
actype=input("Enter The Account type:")
bal=float(input("Enter the Balance:"))
obj=bankaccount(acno,name,actype,bal)
print("Account Information=",obj.accountinfo())

depamount=int(input("Enter the Amount to be Deposited:"))
obj.deposit(depamount)

wid=int(input("Enter the Withdrawal Amount:"))
obj.withdraw(wid)




        
