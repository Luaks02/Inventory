from openpyxl import workbook, load_workbook
from openpyxl.utils import get_column_letter

wb = load_workbook('Estoque.xlsx')
ws = wb.active

for row in range(1,11):
    ws['A' + str(row)] = row

wb.save('Estoque.xlsx')