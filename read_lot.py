import json

with open('/Users/matbook/Desktop/PyLMS/codes.json') as f:
	lot = json.load(f)['lot']

if lot == None:
	print('')
else:
	print(lot)















