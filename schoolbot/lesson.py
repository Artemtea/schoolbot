import openpyxl

book = openpyxl.reader.excel.load_workbook(filename="D:\Programing\Python\schoolbot\lessons.xlsx", read_only=True)



print(book.sheetnames)