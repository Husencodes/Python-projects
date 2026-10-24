
import PyPDF2

pdffiles = ["1.pdf", "2.pdf"]
merger = PyPDF2.PdfMerger()

for filename in pdffiles:
    with open(filename, "rb") as pdfFile:
        merger.append(pdfFile)

merger.write("merged.pdf")
merger.close()

print("PDF files merged successfully!")
