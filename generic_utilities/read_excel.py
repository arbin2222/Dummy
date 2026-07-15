import os
from xlrd import open_workbook

def read():
    path = os.path.join(
        os.getcwd(),
        "generic_utilities",
        "excel.xlsx"
    )

    wb = open_workbook(path)
    sheet = wb.sheet_by_name("Sheet1")

    row = sheet.row_values(1)

    username = row[0]
    email = row[1]
    pwd = row[2]

    return username, email, pwd