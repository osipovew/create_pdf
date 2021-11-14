from fpdf import FPDF
pdf = FPDF()
imagelist = "lg.png"
# imagelist is the list with all image filenames
for image in imagelist:
    pdf.add_page()
    pdf.image(imagelist, 10, 10, 10, 10)
pdf.output("yourfile.pdf", "F")