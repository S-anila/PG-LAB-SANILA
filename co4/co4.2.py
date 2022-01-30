classBank;
def__init__(self);
self.bal=0
defcreate(self) ;
print("enter The Details")
self.no=int(input("enter the account Number"))
self.name=input("enter the name")
self.type=input("Entr the account type")
defdeposit(self);
self.amount=int(input("enter the amount to deposit"))
self.bal=self.bal+self.amount
print("BALANCE",self.bal)
defwithdraw(self);
self.amount=int(input("enter the amount to withdraw"))
self.bal=self.bal-self.amount
print("BALANCE",self.bal)
defdisplay(self);
print("ACCOUNT NUMBER:",self.no)
print("ACCOUNT HOLDER NAME:",self.name)
print("ACCOUNT TYPE:",self.type)
print("ACCOUNT BALANCE:",self.bal)

B=Bank()
B.create()
x=1
whilex!=0;
print("MENU")
x=int((input("1.DEPOSIT 2.WITHDRAW 3.BALANCE")))
if x==1:
        B.deposit()
elif x==2:
        B.withdraw()
elif x==3:
        B.display()
else:
        print("invalid selection")
