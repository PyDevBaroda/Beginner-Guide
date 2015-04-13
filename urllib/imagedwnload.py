import urllib
f = open('logo.png','wb')
f.write(urllib.urlopen('http://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/2000px-Python-logo-notext.svg.png').read())
f.close()
