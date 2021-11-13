from fpdf import FPDF
import os
import glob
from PIL import Image


arr_jpg = [f for f in glob.glob("*.jpg")]

imagelist = sorted(arr_jpg)
print(imagelist)

# time_txt = open(r"C:\Users\Adm\PycharmProjects\create_pdf", "r") запуск с правами админа
time_txt = open("text.txt", "r")
data = time_txt.read()
time_txt.close()



pdf = FPDF(orientation='l')
pdf.add_page()
for imageFile in imagelist:
    cover = Image.open(imageFile)
    width, height = cover.size
    pdf.image(imageFile, 0, 0, width, height)

    width, height = float(width * 0.264583), float(height * 0.264583)
pdf.set_font("Arial", size=25)
# pdf.ln(85)  # ниже на 85
#pdf.cell(100, 10, txt=data.format("pic1.jpg"), ln=1)
pdf_size = {'P': {'w': 210, 'h': 297}, 'L': {'w': 297, 'h': 210}}

pdf.output("add_image.pdf")





