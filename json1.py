import json
data = ''' 
[{
	"id": "1",
	"x":"2",
	"name": "bj"
},
{"id":"2",
"x":"22",
"name":"other"}
]
'''

info = json.loads(data)
print('user: ', len(info))
for item in info: 
	print('Name: ', item['name'])