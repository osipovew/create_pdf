from fpdf import FPDF

# time_txt = open(r"C:\Users\Adm\PycharmProjects\create_pdf", "r") запуск с правами админа
time_txt = open("text.txt", "r")
data = time_txt.read()
time_txt.close()


def add_image(image_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.image(image_path, x=10, y=8, w=100)
    pdf.set_font("Arial", size=12)
    pdf.ln(85)  # ниже на 85
    pdf.cell(200, 10, txt=data.format(image_path), ln=1)
    pdf.output("add_image.pdf")


if __name__ == '__main__':
    add_image('pic1.jpg')