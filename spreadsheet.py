from openpyxl import Workbook
import openpyxl

alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def create_workbook():
    workbook = Workbook()
    return workbook

def save_workbook(workbook, path):
    workbook.save(path)

def write_cell_text(workbook, col, row, text)
    sheet = workbook.active
    sheet[col + row] = text

def write_cell_img(workbook, col, row, img_path):
    sheet = workbook.active
    img = openpyxl.drawing.image.Image(img_path)
    img.anchor = col + row
    img.width = 64
    img.height = 64
    sheet.add_image(img)