import json

with open('/Users/matbook/Desktop/PyLMS/codes.json') as f:
	product = json.load(f)['product']
if product == None:
	print('')
else:
	print(product)



























