import json

with open('/Volumes/SHARED/PyLMS/codes.json') as f:
	product = json.load(f)['products'][0]
	# batch = json.load(f)['products'][0]['batches'][0]
	# lot = json.load(f)['products'][0]['batches'][0]['lot'][0]
	# coated = json.load(f)['products'][0]['batches'][0]['coated']
try:
	print(product)
	# print(batch)
	# print(lot)
	# print(coated)
except:
	print('')




















