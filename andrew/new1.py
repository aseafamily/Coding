dic = {}
loa = input("Add or look up a word (a/l)")
while loa == 'a' or loa == 'l':
    loa = input("Add or look up a word (a/l)")
    if loa == 'a':
        word = input("Type the word: ")
        definition = input("Type the definition: ")
        print("Word added!")
        dic [word] = definition
    if loa == 'l':
        askforword = input("What is the word that you want to search up?")
        if askforword in dic:
            print(definition)
        
