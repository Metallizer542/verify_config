import xlwt
import xlrd
from xlutils.copy import copy as xlcopy

def GenerateXLSHead(filename):

    font0 = xlwt.Font()
    font0.name = 'Times New Roman'
    font0.colour_index = 0
    font0.bold = True

    style0 = xlwt.XFStyle()
    style0.font = font0

    font1 = xlwt.Font()
    font1.name = 'Times New Roman'
    font1.colour_index = 0
    font1.bold = False

    style1 = xlwt.XFStyle()
    style1.font = font1

    wb = xlwt.Workbook()
    ws = wb.add_sheet('Server 1')

    ws.write(0, 0, 'Имя файла', style0)
    ws.write(0, 1, 'Имя параметра', style0)
    ws.write(0, 2, 'Полученое значение', style0)
    ws.write(0, 3, 'Рекомендуемое значение', style0)

    ws.write(2, 1, '/opt/cm-data/attachments', style1)

    wb.save(filename)


#GenerateXLSHead(r'C:\Users\dkutyrev\Desktop\python_xls\test.xls')


