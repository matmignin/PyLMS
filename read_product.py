import json

# with open('/Volumes/SHARED/PyLMS/codes.json') as f:
f = open('/Volumes/SHARED/PyLMS/codes.json')
code = json.load(f)['products'][0]
product = code.get('product')
batch = code['batches'][0].get('batch')
lot = code['batches'][0].get('lot')[0]
coated = code['batches'][0].get('coated')


try:
	# print(product['batches'][0]['batch'] + " " + product['batches'][0]['lot'][0])

	print(product)
	print(batch)
	print(lot)
	print(coated)
except:
	print('')



























