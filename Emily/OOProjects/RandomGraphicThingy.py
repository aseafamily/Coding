restart = 'y'
while restart == 'y':
    num_budget = float(input('What is your budget?'))
    print('These are the options:')
    print('''AllEats - A national grocery chain, costs 14.87 per share. Going up by 1.47%
Microwares - A relatively new technology company, costs 67.13 per share. Going up by 3.21%
Diacloth - A international clothing store, costs 193.02 per share. Going down by 0.21%
Budgetco - A national bank holding company, stocks cost 132.43 per share. Going up by 0.09%
Yurto - A international retail store line, stocks cost 21.56 per share. Going down by 2.63%
Airin - A international airline company, stocks cost 42.06 per share. Going up by 0.13%
Karakha - A film-making company, costs 137.23 per share. Going down by 1.03%
Timtit - A network company, costs 267.07 per share. Going up by 1.03%
BurgerTone - A national restaurant chain, costs 142.02 per share. Going up by 4.27%
Marakoi - A game-making company, costs 314.20 per share. Going up by 0.23%
(A/M/D/B/Y/a/K/T/b/m)
''')
    num_stocks = int(input('Now how many stocks would you like to buy?'))
    
    for kk in range(1, num_stocks+1):
        stock_name = input('Which stock would you like to buy?')
        if stock_name == 'A':
            num_budget = num_budget - 14.87
        elif stock_name == 'M':
            num_budget = num_budget - 67.13
        elif stock_name == 'D':
            num_budget = num_budget - 193.02
        elif stock_name == 'B':
            num_budget = num_budget - 132.43
        elif stock_name == 'Y':
            num_budget = num_budget - 21.56
        elif stock_name == 'a':
            num_budget = num_budget - 42.06
        elif stock_name == 'K':
            num_budget = num_budget - 137.23
        elif stock_name == 'T':
            num_budget = num_budget - 267.07
        elif stock_name == 'b':
            num_budget = num_budget - 142.02
        elif stock_name == 'm':
            num_budget = num_budget - 314.20
        else:
            print('That is not an option.')
    print('Now your budget is ' + str(num_budget) + '.')
    restart = input('Would you like to redo this?(y/n)')
    if restart == 'y':
        num_budget == 0