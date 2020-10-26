class BankAccount:
    def __init__(self, name, accountnum, balance):
        self.name = name
        self.accountnum = accountnum
        self.balance = balance
    
    def __str__(self):
        msg = 'Your balance is $' + str(self.balance)
        return msg

    def deposit(self, amount):
        if amount >= 0:
            self.balance = self.balance + amount
        else:
            print('You cannot deposit that number.')

    def withdrawl(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance = self.balance - amount
            else:
                print('You do not have that much money.')
        else:
            print('You must withdrawl a positive number smaller, or equal to your balance.')
class InterestAccount(BankAccount):
    def __init__(self, name, accountnum, balance, interest):
        BankAccount.__init__(self, name, accountnum, balance)
        self.interest = interest
    def addInterest(self):
        self.balance = self.balance + self.balance * self.interest
thename = input('What is your name?')
theaccountnum = input('What is your account number?')
thebalance = float(input('What is your balance?'))
theBankAccount = BankAccount(thename, theaccountnum, thebalance)
print(theBankAccount)
deinterest = float(input('What would you want the interest to be? Give your answer in decimal form. (0.1, 0.2, 0.6, 0.03)'))
theinterest = 0
if deinterest > 0.5:
    theinterest -=0.3
elif deinterest > 0.2:
    theinterest -= 0.1
elif 0.1 >= theinterest >0.01:
    theinterest += 0.02
else:
    theinterest += 0.5
theInterestAccount = InterestAccount(thename, theaccountnum, thebalance, theinterest)
theInterestAccount.addInterest()
print(theInterestAccount)