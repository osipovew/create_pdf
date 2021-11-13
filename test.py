from fpdf import FPDF
from PIL import Image
import glob
import os
from fpdf import FPDF
from PIL import Image
import glob
import os


arr_jpg = [f for f in glob.glob("*.jpg")]

pictures = sorted(arr_jpg)
print(pictures)


image_directory = 'C:\\Users\\vtelv\\PycharmProjects\\create_pdf'
extensions = ('*.jpg','*.png','*.gif')
pdf = FPDF()
imagelist=[]
for ext in extensions:imagelist.extend(glob.glob(os.path.join(image_directory,ext)))

for imageFile in imagelist:
    cover = Image.open(imageFile)
    width, height = cover.size

    # convert pixel in mm with 1px=0.264583 mm
    width, height = float(width * 0.264583), float(height * 0.264583)

    # given we are working with A4 format size
    pdf_size = {'P': {'w': 210, 'h': 297}, 'L': {'w': 297, 'h': 210}}


    pdf.image(imageFile, 0, 0, width, height)
pdf.output("add_image.pdf")