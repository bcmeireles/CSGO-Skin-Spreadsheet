from openpyxl import Workbook
import openpyxl
from openpyxl.drawing.image import Image
import PIL
import io
import urllib3


alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def create_workbook():
    workbook = Workbook()
    return workbook

def save_workbook(workbook, path):
    workbook.save(path)

def write_cell_text(workbook, col, row, text):
    sheet = workbook.active
    sheet[col + row] = text

def write_cell_img(workbook, col, row, img_path):
    sheet = workbook.active
    http = urllib3.PoolManager()
    r = http.request('GET', img_path + '.png')
    image_file = io.BytesIO(r.data)
    img = Image(image_file)

    img.anchor = col + row
    img.width = 113.3858
    img.height = 75.59
    sheet.add_image(img)