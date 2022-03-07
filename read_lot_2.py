import json

with open('/Volumes/SHARED/PyLMS/codes.json') as f:
	lot_2 = json.load(f)['products'][0]['batches'][0]['lot'][1]
try:
	print(lot_2)
except:
	print('')





















