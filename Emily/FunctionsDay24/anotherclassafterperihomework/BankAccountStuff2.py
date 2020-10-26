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
keepgoingas = input('Welcome to your Virtual Bank Account. Would you like to continue? (y/n)')
if keepgoingas == 'y':
    thename = input('What is your name?')
    theaccountnum = input('What is your account number?')
elif keepgoingas == 'n':
    print('Alright then.')
else:
    print("THAT'S NOT AN OPTION YOU IDIOT!")
nonBankAccount = BankAccount(thename, theaccountnum, 0)
while keepgoingas == 'y':
    print(nonBankAccount)
    depositammount = int(input('How much would you like to deposit?'))
    nonBankAccount.deposit(depositammount)
    print(nonBankAccount)
    withdrawlammount = int(input('How much would you like to withdrawl?'))
    nonBankAccount.withdrawl(withdrawlammount)
    print(nonBankAccount)
    keepgoingas = input('Would you like to continue? (y/n)')