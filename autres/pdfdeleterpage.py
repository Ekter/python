from PyPDF2 import PdfFileWriter, PdfFileReader
pages_to_keep = [1, 7, 14,17,22,24,28,30,33,37,40,41,42,45,46,47,48,49,50,53,58,61,64,70,71,74,75,79,84,87,88,91,92,97,98,99,100,101] # page numbering starts from 0
filename="3-SystClassic.pdf"
infile = PdfFileReader(f'../{filename}', 'rb')
output = PdfFileWriter()

for i in range(infile.getNumPages()):
    if i+1 in pages_to_keep:
        p = infile.getPage(i)
        output.addPage(p)

with open(filename.split(".")[0]+"--cut.pdf", 'wb') as f:
    output.write(f)
