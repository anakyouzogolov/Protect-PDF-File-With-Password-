import PyPDF2 as pdf

out_put = pdf.PdfFileWriter()

read_pdf = pdf.PdfFileReader(open("mypdf.pdf", "rb")) # mypdf is the pdf file you want to protect with password


for p in range(read_pdf.getNumPages()):
    out_put.addPage(read_pdf.getPage(p))


out_put_stream = open("encrypted_pdf.pdf", "wb") # encrypted_pdf.pdf is output pdf file with password 

out_put.encrypt("1234", use_128bit=True)
out_put.write(out_put_stream)
out_put_stream.close()
