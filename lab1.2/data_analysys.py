from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']

column_years = sheet['A'][1:]
column_temp = sheet['C'][1:]
column_sun = sheet['D'][1:]
def  get_value(x):
    return x.value

list_y = list(map(get_value,  column_years))
list_t  =list(map(get_value,  column_temp))
list_s  =list(map(get_value,  column_sun))

#print (list_y)

pyplot.plot(list_y, list_t)
pyplot.plot(list_y, list_s)
pyplot.show()

