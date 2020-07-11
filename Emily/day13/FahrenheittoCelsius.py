import easygui

easygui.msgbox('Hello and welcome to the Fahrenheit and Celsius convertor.')
easygui.enterbox('Do you want to convert Fahrenheit to Celsius, or Celsius to Fahrenheit? (fc/cf)')
convert = easygui.enterbox()
if convert == 'fc':
    easygui.enterbox('Please enter the degree of Fahrenheit you want me to convert to Celsius.')
    degreetype = easygui.enterbox()
    C = 5/9*(float(degreetype) - 32)
    easygui.msgbox(degreetype + ' in celsius is ' + str(C) + ' in Fahrenheit.')
elif convert == 'cf':
    easygui.enterbox('Please enter the degree of Celsius you want me to convert to Fahrenheit.')
    otherdegree = easygui.enterbox()
    F = (float(otherdegree)*1.8+32)
    easygui.msgbox(otherdegree + ' in Fahrenheit is ' + str(F) + ' in celsius.')
