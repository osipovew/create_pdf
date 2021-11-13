from fpdf import FPDF
import glob
from PIL import Image

arr_jpg = [f for f in glob.glob("*.jpg")]

imagelist = sorted(arr_jpg)
print(imagelist)


pdf = FPDF(orientation='l')
pdf.set_auto_page_break( False )
pdf.set_font('Arial', 'B', 16)
pdf.add_page()


counter = 0
y =10
x =10


for imageFile in imagelist:
    counter = counter + 1
    y = y + 10
    x = x + 10

    txt_filename = imageFile + ".txt"
    txt_format = "PHOTO #" + str(counter) + " | " + open(txt_filename, "r").read()

    cover = Image.open(imageFile)
    width, height = cover.size

    pdf.image(imageFile, x, y)
    #pdf.set_xy(0, y)

    print("=====================")
    print('image: ' + imageFile)
    print("x:" + str(pdf.get_x()))
    print("y:" + str(pdf.get_y()))
    print("=====================")
    #pdf.cell(100, 10, txt_format)



pdf.ln(100)  # ниже на 85
pdf.output("add_image2.pdf")