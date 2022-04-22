#!/Users/matbook/.pyenv/versions/3.8.3/envs/VQenv/bin/python
import json, sys, os

a_code = sys.argv[1]

try:
	clear_code = sys.argv[2]
except:
	clear_code = None


with open(os.path.expanduser('~/PyLMS/codes.json'), 'r+') as f:
	data = json.load(f)
	code = data[a_code]
if clear_code:
	with open(os.path.expanduser('~/PyLMS/codes.json'), 'w') as nf:
		data[a_code] = None
		nf.seek(0)
		json.dump(data, nf, indent=4)
if code == None:
	print('')
else:
	print(code)




















