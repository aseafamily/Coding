def mon(q, d, n, p):
    total = ((q * 25) + (d * 10) + (n * 5) + (p * 1))
    return total

q = int(input("quarters: "))
d = int(input("dimes: "))
n = int(input("nickels: "))
p = int(input("pennies: "))
dk = mon(q, d, n, p)
print(dk / 100)

"""def ting(name, address, street, city, state, zipcode, con):
    print(name)
    print(address, ', ', street)
    print(city, ', ', state, ', ', con)
    print(zipcode)
name = input("What is your name: ")
address = input("What is your address: ")
street = input("what street do you live on: ")
city = input("What city do you live in: ")
state = input("What state or province do you live in: ")
zipcode = input("What is you zip or postal code: ")
con = input("What country do you live in: ")
ting(name, address, street, city, state, zipcode, con)
'''def printmyname():
    print("Andrew")
printmyname()
""def caltax(pri, tax):
    tat = pri + (pri * tax)
    my = 1000
    print("My_price (inside function)", my)
    return tat

my = float(input("Enter a price: "))
tata = caltax(my, 0.1)
print("Price = ", my, "Tatal print = ", tata)
print("My_price (inside function)", my)
def caltax(pri, tax):
    tat = pri + (pri * tax)
    print(pri)
    return tat

my = float(input("Enter a price: "))
tata = caltax(my, 0.1)
print("Price = ", my, "Tatal print = ", tata)
def caltax(pri, taxpri):
    taxta = pri + (pri * taxpri)
    return taxta
totalpri = caltax(7.99, 0.06)
print(totalpri)
tat = caltax(7.99, 0.06) + caltax(6.59, 0.08)
print(tat)
def printmyaddress(myname, house):
    print(myname)
    print(house, "ne 110th way")
    print("Redmond, Washinton, U.S.A")
    print("98052")
    print()
printmyaddress("Andrew Ma", '??')
printmyaddress("Alex Ma", "Secert")
def printmyaddress():
    print("Andrew Ma")
    print("18105 ne 110th way")
    print("Redmond, Washinton, U.S.A")
    print("98052")
    print()
printmyaddress()
printmyaddress()
printmyaddress()
printmyaddress()
printmyaddress()"""
