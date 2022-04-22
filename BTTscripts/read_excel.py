#!/Users/matbook/.pyenv/versions/3.8.3/envs/VQenv/bin/python
import sys, os, openpyxl, warnings, json, re
warnings.simplefilter("ignore")

# pattern_product = re.compile(r'(?<=\w{3})?(?P<product>[abdefghijkl]\d{3})(?=\w{4})?',re.IGNORECASE)
# pattern_batch = re.compile(r'[^(ct\#?)](?P<batch>\b\d{3}-\d{4})')
# pattern_lot = re.compile(r'(?P<lot>\b\d{4}\w\d\w?|\bBulk\b|G\d{7}\w?\b|VC\d{6}[ABCDEFGH]?|V[A-Z]\d{5}[A-Z]\d?|\d{5}\[A-Z]{3}\d)',re.IGNORECASE)
# pattern_coated = re.compile(r'(?:\d{4}\w\d\w?.|\bBulk\b|G\d{7}\w?\b|VC\d{6}[ABCDEFGH]?|V[A-Z]\d{5}[A-Z]\d?|\d{5}\[A-Z]{3}\d\s|coated:?\s?|ct\#?\s?)(?P<coated>\d{3}-\d{4})',re.IGNORECASE)
workbook_path = "/Users/matbook/Library/CloudStorage/OneDrive-VitaquestInternational/Mats LMS Workbook7.xlsm"

# try:
	# sheet_product = sys.argv[1]
# except:
wb = openpyxl.load_workbook(workbook_path, read_only=True)
sheet = wb.active
sheet_product = sheet.title

# try:
# if sys.argv[2]:
# 	sheet_codes = sys.argv[2]
# 	match_batch = pattern_batch.search(sys.argv[2])
# 	match_lot = pattern_lot.search(sys.argv[2])
# 	match_coated = pattern_coated.search(sys.argv[2])
# else:
# 	sheet_codes = sys.argv[2]
# 	match_batch = pattern_batch.search(sys.argv[2])
# 	match_lot = pattern_lot.search(sys.argv[2])
# 	match_coated = pattern_coated.search(sys.argv[2])

# except:
	# sheet_codes = sys.argv[2]
	# match_product = pattern_product.search(sheet_codes)


def save_json(input):
    with open(os.path.expanduser('~/PyLMS/codes.json'), 'w') as nf:
        nf.seek(0)
        json.dump(input, nf, indent=4)



with open(os.path.expanduser('~/PyLMS/codes.json'), 'r+') as f:
	data = json.load(f)
	data['product'] = sheet_product.upper()
	# data['batch'] = match_batch.group('batch')
	# data['lot'] = match_lot.group('lot').upper()
	# data['coated'] = match_coated.group('coated')
	save_json(data)


print(data['product'])









