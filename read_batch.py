import json

with open('/Volumes/SHARED/PyLMS/codes.json') as f:
	batch = json.load(f)['products'][0]['batches'][0]['batch']
try:
	print(batch)
except:
	print('')





















