import xlrd
import os

keyFilePath = u'./resource/搜索词.xlsx'


def main():
    if not os.path.exists(keyFilePath):
        print('搜索词excel文件不存在！')
        return

    workbook = xlrd.open_workbook(keyFilePath)

    sheet_names = workbook.sheet_names()

    for sheet_name in sheet_names:
        sheet = workbook.sheet_by_name(sheet_name)
        # rows = sheet.row_values(0)  # 获取第1行内容
        # print('rows: ', rows)
        cols = sheet.col_values(0)  # 获取第1列内容
        print('cols: ', cols)

    return cols