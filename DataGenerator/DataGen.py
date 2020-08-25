import openpyxl

def dataGenerator():
    vk=openpyxl.load_workbook("D:/Workspace/EndToEnd/file/TD10.xlsx")
    sh=vk['Sheet1']
