#!/Users/matbook/.pyenv/versions/3.8.3/envs/VQenv/bin/python
import json




with open('/Users/matbook/Desktop/PyLMS/codes.json') as f:
	product = json.load(f)['product']
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


















