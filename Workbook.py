import pandas as pd
import warnings
import re

# read row B8 of sheet named K852
warnings.simplefilter("ignore")
df = pd.read_excel('C:\\Users\\mmignin\\Documents\\PyLMS\\Formulations_Workbook.xlsm', sheet_name='K852')
print(df.iat[7,1])

# get current clipboard
clipdf = pd.read_clipboard()
print(clipdf)

## regex search
StringToSearch = 'K741 107-0431 0278H1'
p = re.compile(r'(?<=\w{3})?(?P<Product>[abcdefghijkl]\d{3}\b)', re.I)
b = re.compile(r'(?<!Ct#)(?P<Batch>\d{3}-\d{4}\b)',re.I)
l = re.compile(r'(?P<Lot>\b\d{4}\w\d\w?|\bBulk\b|G\d{7}\w?\b|VC\d{6}[ABCDEFGH]?|V[A-Z]\d{5}[A-Z]\d?|\d{5}\[A-Z]{3}\d)',re.I)
c = re.compile(r'(coated: |ct#?|ct\s?|coated\s?)(?P<Coated>\d{3}-\d{4})',re.I)
print(p.search(StringToSearch).group('Product'))
print(b.search(StringToSearch).group('Batch'))



