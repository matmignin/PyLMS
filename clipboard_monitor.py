import time, re, pyperclip, json, os, sys


pattern_product = re.compile(r'(?P<product>[abdefghijkl]\b\d{3})(?=\w{4})?',re.IGNORECASE)
pattern_batch = re.compile(r'(?<!([ct#|ct]).)\b(?P<batch>\d{3}-\d{4})',re.IGNORECASE)
pattern_lot = re.compile(r'(?P<lot>\b\d{4}\w\d\w?|\bBulk\b|G\d{7}\w?\b|VC\d{6}[ABCDEFGH]?|V[A-Z]\d{5}[A-Z]\d?|\d{5}\[A-Z]{3}\d)',re.IGNORECASE)
pattern_coated = re.compile(r'(?:\d{4}\w\d\w?.|\bBulk\b|G\d{7}\w?\b|VC\d{6}[ABCDEFGH]?|V[A-Z]\d{5}[A-Z]\d?|\d{5}\[A-Z]{3}\d\s|coated:?\s?|ct\#?\s?)(?P<coated>\d{3}-\d{4})',re.IGNORECASE)




def save_json(input):
    with open(os.path.expanduser('~/PyLMS/codes.json'), 'w') as nf:
        nf.seek(0)
        json.dump(input, nf, indent=4)

recent_value = ""

while True:
    tmp_value = pyperclip.paste()
    if tmp_value != recent_value:
        recent_value = tmp_value
        # print("Value changed: %s" % str(recent_value)[:20])
        match_product = pattern_product.search(recent_value)
        match_batch = pattern_batch.search(recent_value)
        match_lot = pattern_lot.search(recent_value)
        match_coated = pattern_coated.search(recent_value)
        code=''
        data=[]
        with open(os.path.expanduser('~/PyLMS/codes.json'), 'r+') as f:
            data = json.load(f)
            if match_product:
                data['product'] = match_product.group('product').upper()
                code += match_product.group('product').upper()
                product = match_product.group('product').upper()
            if match_batch and not match_lot or not match_coated:
                data['batch'] = match_batch.group('batch')
                data['lot'] = None
                data['coated'] = None
                code += ' ' + match_batch.group('batch')
            if match_lot:
                data['lot'] = match_lot.group('lot').upper()
                code += ' ' + match_lot.group('lot').upper()
            if match_coated:
                data['coated'] = match_coated.group('coated')
                code += ' ' + match_coated.group('coated')
            if match_batch:
                data['batch'] = match_batch.group('batch')
                code += ' ' + match_batch.group('batch')
        if code:
          print(code)
          save_json(data)
    time.sleep(0.5)




