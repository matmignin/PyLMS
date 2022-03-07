import json

with open('/Volumes/SHARED/PyLMS/codes.json') as f:
	product = json.load(f)['products'][0]['product']
try:
	print(product)
except:
	print('')





















