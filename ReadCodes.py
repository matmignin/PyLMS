import json

try:
	with open('/Volumes/SHARED/PyLMS/codes.json') as f:
		# data = json.load(f)['code'][0]['product']
		data = json.load(f)['code'][1]['product']
	print(data)
except:
	print('')












