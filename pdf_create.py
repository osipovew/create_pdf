from fpdf import FPDF
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

for imageFile in imagelist:
    cover = Image.open(imageFile)
    width, height = cover.size
    pdf.add_page()
    pdf.image(imageFile, 0, 0)
    pdf.cell(100, 10, txt=data.format(imageFile), ln=1) #пошел говорит в жопу


pdf.set_font("Arial", size=25)
pdf.ln(100)  # ниже на 85
pdf.output("add_image.pdf")