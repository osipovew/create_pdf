import os

from fpdf import FPDF
import glob

arr_jpg = [f for f in glob.glob("pic*.jpg")]
imageList = sorted(arr_jpg)

waveFile = 'wave.png'

pdf = FPDF(orientation='l')

pdf.set_font('Arial', 'B', 16)

counter = 0
name_pict = "pic"
name_form = ".jpg.txt"
for imageFile in imageList:
    counter = counter + 1
    pdf.add_page()

    pdf.image(waveFile, 0, 0, 297, 20)
    where_is_config = os.path.exists(name_pict + str(counter) + name_form)
    print(where_is_config)
    print((name_pict + str(counter) + name_form))
    if where_is_config:
        txt_content = "PHOTO #" + str(counter) + " | " + open(imageFile + ".txt", "r").read()
    else:
        txt_content = "PHOTO #" + str(counter)
    pdf.cell(20, 20, txt_content, 10)
    pdf.image(imageFile, 10, 30, 277, 170)
pdf.output("add_image.pdf")
