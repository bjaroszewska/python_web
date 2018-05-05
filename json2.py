import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_95517.json"
html = urllib.request.urlopen(url, context=ctx).read()
info = json.loads(html)
sumEntire = 0
for el in info['comments']:
	sumEntire+=int(el['count'])
print(sumEntire)
	



