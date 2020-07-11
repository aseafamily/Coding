import urllib.request
file = urllib.request.urlopen('http://google.com')
message = file.read()
print(message)
