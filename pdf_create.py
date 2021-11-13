from fpdf import FPDF
import glob


arr_jpg = [f for f in glob.glob("*.jpg")]
imageList = sorted(arr_jpg)


waveFile = 'wave.png'


pdf = FPDF(orientation='l')
pdf.set_font('Arial', 'B', 16)


counter = 1


for imageFile in imageList:
    counter = counter + 1
    pdf.add_page()
    pdf.image(waveFile, 0, 0, 297, 20)

    txt_content = "PHOTO #" + str(counter) + " | " + open(imageFile + ".txt", "r").read()

    pdf.image(imageFile, 10, 30, 277, 170)
    pdf.cell(20, 20, txt_content, 10)



pdf.output("add_image.pdf")