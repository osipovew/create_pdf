from fpdf import FPDF
import glob


arr_jpg = [f for f in glob.glob("*.jpg")]
imageList = sorted(arr_jpg)


pdf = FPDF(orientation='l')


for imageFile in imageList:
    pdf.add_page()
    pdf.image(imageFile, 10, 30, 277, 170)



pdf.output("add_image.pdf")