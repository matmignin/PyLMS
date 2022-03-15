import json

with open('/Users/matbook/Desktop/PyLMS/codes.json') as f:
	batch = json.load(f)['batch']
if batch == None:
	print('')
else:
	print(batch)





















