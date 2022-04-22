#!/Users/matbook/.pyenv/versions/3.8.3/envs/VQenv/bin/python
import re, pyperclip, os, json

clipboard = pyperclip.paste()

pattern_product = re.compile(r'(?<=\w{3})?(?P<product>[abdefghijkl]\d{3})(?=\w{4})?',re.IGNORECASE)
pattern_batch = re.compile(r'(?<!([ct#|ct]).)\b(?P<batch>\d{3}-\d{4})',re.IGNORECASE)
pattern_lot = re.compile(r'(?P<lot>\b\d{4}\w\d\w?|\bBulk\b|G\d{7}\w?\b|VC\d{6}[ABCDEFGH]?|V[A-Z]\d{5}[A-Z]\d?|\d{5}\[A-Z]{3}\d)',re.IGNORECASE)
pattern_coated = re.compile(r'(?:\d{4}\w\d\w?.|\bBulk\b|G\d{7}\w?\b|VC\d{6}[ABCDEFGH]?|V[A-Z]\d{5}[A-Z]\d?|\d{5}\[A-Z]{3}\d\s|coated:?\s?|ct\#?\s?)(?P<coated>\d{3}-\d{4})',re.IGNORECASE)

match_product = pattern_product.search(clipboard)
match_batch = pattern_batch.search(clipboard)
match_lot = pattern_lot.search(clipboard)
match_coated = pattern_coated.search(clipboard)

code=''
data=[]
with open(os.path.expanduser('~/PyLMS/codes.json'), 'r+') as f:
	data = json.load(f)
	# if not product and not batch and not lot and not coated:
	if match_product:
		data['product'] = match_product.group('product').upper()
		code += match_product.group('product').upper()
		product = match_product.group('product').upper()
	if match_batch and not match_lot and not match_coated:
		data['lot'] = None
		data['coated'] = None
	if match_lot:
		data['lot'] = match_lot.group('lot').upper()
		code += ' ' + match_lot.group('lot').upper()
	if match_coated:
		data['coated'] = match_coated.group('coated')
		code += ' ' + match_coated.group('coated')
	if match_batch:
		data['batch'] = match_batch.group('batch')
		code += ' ' + match_batch.group('batch')

with open(os.path.expanduser('~/PyLMS/codes.json'), 'w') as nf:
	nf.seek(0)
	json.dump(data, nf, indent=4)

print(code)




