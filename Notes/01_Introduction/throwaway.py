import urllib.request
u = urllib.request.urlopen('http://www.python.org/')
data = u.read()
print(data)