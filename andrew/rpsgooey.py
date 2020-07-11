import easygui

fst = easygui.enterbox("Please put in a rock, paper, and scissors, r for rock, p for paper, s for scissors.")
snd = easygui.enterbox("Please put in a rock, paper, and scissors, r for rock, p for paper, s for scissors.")
if fst == 'r' and snd == 'r':
    easygui.msgbox("This is a tie because you both did rock.")
elif fst == 'r' and snd == 'p':
    easygui.msgbox("The second user won because the 1st one did rock and the second one did paper.")
elif fst == 'r' and snd == 's':
    easygui.msgbox("The first user won because the first person did rock and the second person did scissors.")
elif fst == 'p' and snd == 'p':
    easygui.msgbox("Tie is tie because you both did paper.")
elif fst == 'p' and snd == 's':
    easygui.msgbox("The second player won because the second player did scissors and the first player did paper.")
elif fst == 'p' and snd == 'r':
    easygui.msgbox("The first player won because the first player did paper and the second player did rock.")
elif fst == 's' and snd == 's':
    easygui.msgbox("This is a tie because you both did scissors.")
elif fst == 's' and snd == 'p':
    easygui.msgbox("The first player won because the first player did scissors and th second player did paper.")
elif fst =='s' and snd == 'r':
    easygui.msgbox("The second player won because the first player did scissors and the second player did rock.")
else:
    easygui.msgbox("I could not uderstand one of you.")
    



