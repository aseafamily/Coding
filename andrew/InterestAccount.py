class Bankaccount:
    def __init__(self, name, num, bal):
        self.name = name
        self.num = num
        self.bal = bal

    def __str__(self):
        data = "This is your balance " + str(self.bal)
        return data

    def deposit(self, num):
        if num > 0:
            self.bal = self.bal + num
        else:
            print("That is not a valid number.")
    def withdraw(self, num):
        if num > 0:
            if num <= self.bal:
                self.bal = self.bal - num
            else:
                print('You cannot withdrawl that much money.')
        else:
            print('You cannot withdrawl negative numbers.')
class InterestAccount(Bankaccount):
    def __init__(self, name, num, bal, interest):
        Bankaccount.__init__(self, name, num, bal)
        self.interest = interest

    def addInterest(self):
        self.bal = self.bal + self.bal * self.interest
name = input("What is your name? ")
accountnumber = input("What is your account number? ")
inter = float(input("What is you interest rate? "))
myaccount = Bankaccount(name, accountnumber, 0)
myaccountIn = InterestAccount(name, accountnumber, 0, inter)
myaccount.deposit(100)
myaccountIn.deposit(100)
print(myaccount)
print(myaccountIn)
myaccountIn.addInterest()
print(myaccountIn)