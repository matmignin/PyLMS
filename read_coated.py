import json

with open('/Users/matbook/Desktop/PyLMS/codes.json') as f:
	coated = json.load(f)['coated']
if coated == None:
	print('')
else:
	print(coated)

















