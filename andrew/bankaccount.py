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

names = input("What is your name? ")
accountnumber = input("What is your account number? ")
dorw = int(input("How much money do you want to deposit aka add: "))
dorw1 = int(input("How much do you want to withdraw? "))
myaccount = Bankaccount(names, accountnumber, dorw)
print(myaccount)
myaccount.deposit(dorw)
print(myaccount)
myaccount.withdraw(dorw1)
print(myaccount)