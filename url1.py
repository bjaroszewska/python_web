import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Siddhant.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for x in range(0, 6):
	url = tags[17].get('href', None)
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	if(x ==5):
		print(tags[17].text)