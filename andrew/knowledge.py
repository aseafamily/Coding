first = input("Enter 5 names:")
sec = input()
th = input()
f = input()
fi = input()
thing = [first, sec, th, f, fi]
print("These are the names ", thing, ' ')
thing1 = int(input("Replace one of the names, (1, 5):"))
newname = input("New name")
thing2 = thing1 - 1
thing[thing2] = newname
print("This is your new list ", thing)
if thing1 >= 6:
    print("How dare you!!!!!!!!!!!!!!!!!!!")
if thing1 <= 0:
    print("HOWJDFJDKAFJDKFDSJfDJFKSDJFKJDFKDJfkadhfdgxnvhjfdhfxnjcjkdshxcfcuidjskhxfuijckdshxnfjcdhfiskdfhcn")
#first = input("Enter 5 names:")
#sec = input()
#th = input()
#f = input()
#fi = input()
#thing = [first, sec, th, f, fi]
#print("This is the thind name ", thing[2], '.')
#first = input("Enter 5 names:")
##sec = input()
#th = input()
##f = input()
#fi = input()
#thing = [first, sec, th, f, fi]
#thing1 = thing[:]
#thing1.sort()
#print("These are the names ", thing, ' ', 'And here is the list when sorted ', thing1, '.')
#first = input("Enter 5 names:")
#sec = input()
#th = input()
#f = input()
#fi = input()
#thing = [first, sec, th, f, fi]
#print("These are the names ", thing, ' ')
#import time
#number = int(input("Which multiplication table would you like?"))
#high = int(input("How high do you want to go?"))
#print("Here's your table:")
#for i in  range(1, high + 1):
#    print(str(i) + ' x ' + str(number) + " = " + str(i * number))
#    time.sleep(1)
#for i in range(8):
#    print(i)
#for i in range(2, 9, 2):
#    print(i)
#userinput = input("Please enter a number.")
#number = float(userinput)
#print(type(number))
