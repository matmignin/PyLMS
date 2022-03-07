import json

with open('/Volumes/SHARED/PyLMS/codes.json') as f:
	coated = json.load(f)['products'][0]['batches'][0]['coated']
try:
	print(coated)
except:
	print('')




















