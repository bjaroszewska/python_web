import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET 
data = '''
<person>
<name>Betty</name>
<phone type="intl">
+ 48 669 621 519 </phone>
<email hide="yes"/>
<users>
<user>Some</user>
<user>Some</user>
</users>
</person>
'''
tree = ET.fromstring(data)
print('Name: ', tree.find('name').text)
print("atrr: ", tree.find('email').get(('hide')))
lst = tree.findall('users/user')
print("count users: ", len(lst))

