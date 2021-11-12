from fpdf import FPDF
import os

# time_txt = open(r"C:\Users\Adm\PycharmProjects\create_pdf", "r") запуск с правами админа
time_txt = open("text.txt", "r")
data = time_txt.read()
time_txt.close()

pdf = FPDF()
pdf.add_page()
pdf.image("pic1.jpg")
pdf.image("pic2.jpg")
pdf.image("pic3.jpg")
pdf.set_font("Arial", size=12)
pdf.ln(85)  # ниже на 85
pdf.cell(200, 10, txt=data.format("pic1.jpg"), ln=1)
pdf.output("add_image.pdf")

arr = os.listdir()
print(arr)
