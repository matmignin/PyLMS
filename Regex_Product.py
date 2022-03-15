
import re, pyperclip, os, json

# def get_codes():
# data = json.load('codes.json')
clipboard = '''
J984 111-0330 0334A2B
J550 111-0331 0334A2C ct#222-2222
'''
find_product = re.compile(r'((?<=\w{3})?(?P<product>[abdefghijkl]\d{3}))(?=\w{4})?-',re.IGNORECASE|re.DOTALL)
# found_product = find_product.search(Clipboard)

find_batch = re.compile(r'(?<!Ct#)\d{3}-\d{4}\b',re.IGNORECASE|re.DOTALL)
# found_batch = find_batch.search(Clipboard)

find_name = re.compile(r'((?:2016\.\n*(?P<name>[\w \S]*))(?!Dietary Supplement))',re.IGNORECASE)

find_lot = re.compile(r'(?P<lot>\b\d{4}\w\d\w?|\bBulk\b|G\d{7}\w?\b|VC\d{6}[ABCDEFGH]?|V[A-Z]\d{5}[A-Z]\d?|\d{5}\[A-Z]{3}\d)',re.IGNORECASE|re.DOTALL)
find_coated = re.compile(r'(\d{4}\w\d\w?.|\bBulk\b|G\d{7}\w?\b|VC\d{6}[ABCDEFGH]?|V[A-Z]\d{5}[A-Z]\d?|\d{5}\[A-Z]{3}\d\s|coated: |ct#?|ct\s?|coated\s?)(?P<coated>\d{3}-\d{4})',re.IGNORECASE|re.DOTALL)
# Clipboard = pyperclip.paste()
# found_name = find_name.search(Clipboard)
# print(found_name.group(1))

# print(found_product.group('product'))
try:
	# batch = re.findall(find_batch,Clipboard)
	lot = re.findall(find_lot,clipboard)
	print(lot[1])
	# print('----')
	# print(os.environ.get('VAR1'))
	# os.environ['VAR_Batch1'] = Batch[1]
	# print(os.environ['VAR_Batch1'])
except:
	print('')
# print(found_product[1])
# print(re.findall(find_product,Clipboard))
# print(re.findall(find_batch,Clipboard)[1])
# print(re.finditer(found_batch[2],Clipboard))
# print(re.findall(found_name.group('name'),Clipboard))















