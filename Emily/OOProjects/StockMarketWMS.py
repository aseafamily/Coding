num_budget = float(input('What is your budget?')) #Asks the budget
if_budget = num_budget #An extra budget, in case I don't want to change num_budget
restart = 'y' #If the user wants to continue rebuying stocks
while restart == 'y': #While the user wants to keep conntinuing
    print('These are the options:') #These are the stock options
    print('''AllEats - A national grocery chain, costs 14.87 per share. Going up by 1.47% 
    Microwares - A relatively new technology company, costs 95.13 per share. Going up by 2.21%
    Diacloth - A international clothing store, costs 193.02 per share. Going down by 0.21%
    Budgetco - A national bank holding company, stocks cost 132.43 per share. Going up by 0.09%
    Yurto - A international retail store line, stocks cost 21.56 per share. Going down by 2.63%
    Airin - A international airline company, stocks cost 42.06 per share. Going up by 0.13%
    Karakha - A film-making company, costs 137.23 per share. Going down by 1.03%
    Timtit - A network company, costs 267.07 per share. Going up by 1.03%
    BurgerTone - A national restaurant chain, costs 142.02 per share. Going up by 2.27%
    Marakoi - A game-making company, costs 314.20 per share. Going up by 0.23%
    ''') #Those were all the stock options, there are 10
    which_stocks = (input('Now that you know your options, which stock would you like to buy first?(AllEats/Microwares/Diacloth/Budgetco/Yurto/Airin/Karaka/Timtit/BurgerTone/Marakoi)')) #Which stock the user wants to buy first
    if which_stocks == 'AllEats' or which_stocks == 'Microwares' or which_stocks == 'Diacloth' or which_stocks == 'Budgetco' or which_stocks == 'Yurto' or which_stocks == 'Airin' or which_stocks == 'Karakha' or which_stocks == 'Timtit' or which_stocks == 'BurgerTone' or which_stocks == 'Marakoi': #If the user wanted to buy a stock that exists
        if which_stocks == 'AllEats': #What the stockprice is, depending on which stock the user wants to buy
            thestockprice = 14.87
        elif which_stocks == 'Microwares':
            thestockprice = 95.13
        elif which_stocks == 'Diacloth':
            thestockprice = 193.02
        elif which_stocks == 'Budgetco':
            thestockprice = 132.43
        elif which_stocks == 'Yurto':
            thestockprice = 21.56
        elif which_stocks == 'Airin':
            thestockprice = 42.06
        elif which_stocks == 'Karakha':
            thestockprice = 137.23
        elif which_stocks == 'Timtit':
            thestockprice = 267.07
        elif which_stocks == 'BurgerTone':
            thestockprice = 142.02
        elif which_stocks == 'Marakoi':
            thestockprice = 314.20
        else: #If the user entered something that isn't an option, what the stockprice is
            thestockprice = 0
        how_many_stock = int(input('How many ' + which_stocks + ' shares would you like to buy?')) #How many shares of that stock the user wants to buy
        
        if num_budget - (thestockprice * how_many_stock) >= 0: #To make sure the user can afford the stocks he/she wants to buy
            num_budget = num_budget - (thestockprice * how_many_stock) #This is how much money the user has left
            print('You have $' + str(num_budget) + ' left.') #This tells the user how much
            if float(num_budget) > 14.87: #If the user can buy more stocks
                restart = input('Do you want to buy more stocks?(y/n)') #If the user wants to buy more stops
            else:
                print('You do not have enough money to buy more stocks.') #If the user doesn't have enough money to buy more stocks
    else: #If the user enters somethign that isn'ta  stock option
        print("That's not an option.")