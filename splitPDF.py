# programa limitado para dividir pdf

from PyPDF2 import PdfFileReader, PdfFileWriter

def split(path, name_of_split):
    pdf = PdfFileReader(path)
    pdf_writer = PdfFileWriter()
    for page in range(pdf.getNumPages()):
        if(page>=348 and page<=369):
         pdf_writer.addPage(pdf.getPage(page))

    output = f'{name_of_split}.pdf'
    with open(output, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

if __name__ == '__main__':
    path = '/storage/emulated/0/Download/IS_ES9.pdf'
    split(path, 'cap18')
