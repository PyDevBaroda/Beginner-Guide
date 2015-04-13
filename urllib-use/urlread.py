import urllib2
url = "http://www.google.com/"
# get response from url
response = urllib2.urlopen(url)
fh = open('downloaded_file.html', "w")
fh.write(response.read())
fh.close()

