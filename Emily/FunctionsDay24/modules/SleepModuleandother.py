""" import time
print('How ', end='')
time.sleep(2)
print('are ', end='')
time.sleep(2)
print('you ', end='')
time.sleep(2)
print('today?') """

""" from time import sleep
print('Hello, talk to you again in 5 seconds...')
sleep(5)
print('Hi again.') """

from time import sleep
print('Welcome to the self-Timer!')
long = input('First, would you rather set your timer in seconds, minutes, or hours?(seconds/minutes/hours)')
longs = long
thetime = int(input('Okay, how long would you like the timer to be? Put it in  your earlier preferred units.'))
if long == 'seconds':
    thetime = thetime
elif long == 'minutes':
    thetime = thetime*60
elif long == 'hours':
    thetime = thetime*60*60
else:
    print("Sorry, that isn't an option.")
for i in range(thetime, 0, -1):
    print(i)
    sleep(1)
print("Timer's up!")