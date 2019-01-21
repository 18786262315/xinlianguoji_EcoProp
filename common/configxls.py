import xlrd
import xlwt

class readExcle():
    '''
        处理xls
    '''
    def __init__(self):
        pass
    def read_row(self,pwd,value):
        # 读取行
        data = xlrd.open_workbook(pwd,'rb')
        table = data.sheets()[0]
        return table.row_values(value)

    def read_col(self,pwd,name):
        # 读取列
        data = xlrd.open_workbook(pwd,'rb')
        table = data.sheets()[0]
        for i,value in enumerate(table.row(0)):
            if value == name:
                return i
        return table.col_values(i)


# print('表名：'+data.sheet_names()[0])

# table = data.sheets()[0]
# nrows = table.nrows
# ncols = table.ncols
# print('表格行数为%d,列数为%d'%(nrows,ncols))
# #输出每一行的值
# for item in range(table.ncols):
#      print(table.col_values(item))

# print(table.col_values(0))

# #获取单元格的值
# cell_A1 = table.row(0)[5].value
# cell_A2 = table.cell(0,0).value
# cell_A3 = table.col(0)[0].value
# print(cell_A1)
# print(cell_A2)
# print(cell_A3)