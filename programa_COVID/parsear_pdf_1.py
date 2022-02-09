# Vamos a tratar de parsear los pdf
import PyPDF2 as PDF2

file = '5-03-2020-nuevo-coronavirus-covid-19-reporte-diario_1.pdf'

with open(file, 'rb') as f:
    pdf = PDF2.PdfFileReader(f)

    page = pdf.getPage(0)
    parsed_page = page.extractText()
print(parsed_page)
