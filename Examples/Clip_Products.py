
import re, pyperclip, os, json

# def get_codes():
# data = json.load('codes.json')


clipboard = '''
2/28/22
F
Skinny Coffee 360g Bag
J984
111-0330
Appitivi llc
0334A2B
2/28/22
F
Skinny Coffee 360g Bag
J555
555-0331
Appitivi llc
0334A2C
2/28/22
F
Blue Raspberry 4g Stick
K656
106-1272
Branded Acquico
0225L1
2/28/22
F
Electrolyte Lemonade Power 378g
K607
201-0027
Branded Acquico
0106A2
2/28/22
F
'''
pattern_product = re.compile(r'(?<=\w{3})?(?P<product>[abdefghijkl]\d{3})(?=\w{4})?',re.IGNORECASE|re.DOTALL)
pattern_batch = re.compile(r'[^(ct\#?)](?P<batch>\d{3}-\d{4}\b)',re.IGNORECASE|re.DOTALL)
pattern_lot = re.compile(r'(?P<lot>\b\d{4}\w\d\w?|\bBulk\b|G\d{7}\w?\b|VC\d{6}[ABCDEFGH]?|V[A-Z]\d{5}[A-Z]\d?|\d{5}\[A-Z]{3}\d)',re.IGNORECASE|re.DOTALL)
pattern_coated = re.compile(r'(?:\d{4}\w\d\w?.|\bBulk\b|G\d{7}\w?\b|VC\d{6}[ABCDEFGH]?|V[A-Z]\d{5}[A-Z]\d?|\d{5}\[A-Z]{3}\d\s|coated:?\s?|ct\#?\s?)(?P<coated>\d{3}-\d{4})',re.IGNORECASE|re.DOTALL)

####for clipping line by line
# for line in clipboard.splitlines():
# 	match_product = pattern_product.search(line)
# 	if match_product:
# 		print('product: ', match_product[0].upper())
# 	match_batch = pattern_batch.search(line)
# 	if match_batch:
# 		print('batch: ', match_batch[0])
# 	match_lot = pattern_lot.search(line)
# 	if match_lot:
# 		print('lot: ', match_lot[0].upper())
# 	match_coated = pattern_coated.search(line)
# 	if match_coated:
# 		print('coated: ', match_coated[0])
# 	print()

match_product = pattern_product.search(clipboard)
if match_product:
	product = match_product.group('product').upper()
match_batch = pattern_batch.search(clipboard)
if match_batch:
	batch = match_batch.group('batch')
match_lot = pattern_lot.search(clipboard)
if match_lot:
	lot = match_lot.group('lot').upper()
match_coated = pattern_coated.search(clipboard)
if match_coated:
	coated = match_coated.group('coated')

print(product, batch, lot, coated)













