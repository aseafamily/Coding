print('Welcome to the Rock, Paper, Scissors Game.')
player1name = input("What is Player1's name?")
player2name = input("What is Player2's name?")
print("Alright then, let's get started.")
player1choice = input("What is " + player1name + "'s choice? (r/p/s)")
player2choice = input('Now what is ' + player2name + "'s choice? (r/p/s)")

if player1choice == 'r' and player2choice == 'r':
    print('It is a tie.')
elif player1choice == 'r' and player2choice == 'p':
    print(str(player2name) + " wins.")
elif player1choice == 'r' and player2choice == 's':
    print(str(player2name) + ' wins.')
elif player1choice == 'p' and player2choice == 'r':
    print(str(player1name) + ' wins.')
elif player1choice == 'p' and player2choice == 'p':
    print('It is a tie.')
elif player1choice == 'p' and player2choice == 's':
    print(str(player2name) + " wins.")
elif player1choice == 's' and player2choice == 'r':
    print(str(player2name) + ' wins.')
elif player1choice == 's' and player2choice == 'p':
    print(str(player1name) + ' wins.')
elif player1choice == 's' and player2choice == 's':
    print('It is a tie.')
else:
    print('Sorry, that is not an option.')
