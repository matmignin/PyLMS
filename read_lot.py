import json

with open('/Volumes/SHARED/PyLMS/codes.json') as f:
	lot = json.load(f)['products'][0]['batches'][0]['lot'][0]
try:
	print(lot)
except:
	print('')




















