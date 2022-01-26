# from openpyxl import load_workbook, Workbook
import pandas as pd
import warnings


# Warning.simplefilter("ignore")
warnings.simplefilter("ignore")
# wb = load_workbook(filename = 'C:\\Users\\mmignin\\Documents\\PyLMS\\Formulations_Workbook.xlsm', read_only=True, data_only = True)
df = pd.read_excel('C:\\Users\\mmignin\\Documents\\PyLMS\\Formulations_Workbook.xlsm', sheet_name='K852')
# wb = Workbook()

# ws = wb['K830']
# ws = wb.get_sheet_by_name('K830')
# print(wb['B8'].value)
print(df.iat[7,1])
