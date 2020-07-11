import easygui
flavor = easygui.enterbox("What is your favorite ice cream flavor?",
                          default = "what ever")
easygui.msgbox("You picked " + flavor + '.')
