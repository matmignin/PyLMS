#!/Users/matbook/.pyenv/versions/3.8.3/envs/VQenv/bin/python
import json, sys

code = sys.argv[1]


with open('/Users/matbook/Desktop/PyLMS/codes.json') as f:
	code = json.load(f)[code]
if code == None:
	print('')
else:
	print(code)

















