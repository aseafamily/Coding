import easygui
ForC = easygui.buttonbox("Please put in C which is = to Celsius to Fahrenhiet. F = Fahrenhiet to Celsuis.",
                         choices = ['F', 'C'])
number = easygui.textbox("Please enter a number.")
if ForC == "F":
    C=(float(number)- 32)/1.8
    easygui.msgbox(C)
elif ForC == "C":
    F=float(number)*1.8+32
    easygui.msgbox(F)
else:
    easygui.msgbox("How dare you.")
