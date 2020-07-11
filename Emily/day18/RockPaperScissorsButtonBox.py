import easygui

easygui.msgbox('Welcome to the Rock, Paper, Scissors Game.')
player1name = easygui.enterbox("What is Player1's name?")
player2name = easygui.enterbox("What is Player2's name?")
easygui.msgbox("Alright then, let's get started.")
player1choice = easygui.enterbox("What is " + player1name + "'s choice? (r/p/s)")
player2choice = easygui.enterbox('Now what is ' + player2name + "'s choice? (r/p/s)")

if player1choice == 'r' and player2choice == 'r':
    easygui.msgbox('It is a tie.')
elif player1choice == 'r' and player2choice == 'p':
    easygui.msgbox(str(player2name) + " wins.")
elif player1choice == 'r' and player2choice == 's':
    easygui.msgbox(str(player2name) + ' wins.')
elif player1choice == 'p' and player2choice == 'r':
    easygui.msgbox(str(player1name) + ' wins.')
elif player1choice == 'p' and player2choice == 'p':
    easygui.msgbox('It is a tie.')
elif player1choice == 'p' and player2choice == 's':
    easygui.msgbox(str(player2name) + " wins.")
elif player1choice == 's' and player2choice == 'r':
    easygui.msgbox(str(player2name) + ' wins.')
elif player1choice == 's' and player2choice == 'p':
    easygui.msgbox(str(player1name) + ' wins.')
elif player1choice == 's' and player2choice == 's':
    easygui.msgbox('It is a tie.')
else:
    easygui.msgbox('Sorry, that is not an option.')
