from fpdf import FPDF


def create_pdf_a4():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="text.txt", ln=1, align="C")
    pdf.output("demo.pdf")


def open_txt():
    global data
    # time_txt = open(r"C:\Users\Adm\PycharmProjects\create_pdf", "r") запуск с правами админа
    time_txt = open("text.txt", "r")
    data = time_txt.read()
    time_txt.close()
