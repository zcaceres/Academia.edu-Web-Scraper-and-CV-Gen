import pdfkit
import os

"""
Uses pdfkit (Python wrapper on webkit framework) to generate a PDF from the results.html file
"""

# My local path to executable wkhtmltopdf. PUT YOURS HERE.
path_wkthmltopdf = '/usr/local/bin/wkhtmltopdf'


# Must use bytes not str/textIO to avoid a pdfkit encoding error
config = pdfkit.configuration(wkhtmltopdf=bytes(path_wkthmltopdf, 'utf-8'))


def generate_pdf(professor_name):
    print(os.path.abspath('results.html'))
    with open('results.html', 'r+') as f:
        cv = pdfkit.from_file(f, '{0}.pdf'.format(professor_name), configuration=config)
        if cv:
            print("PDF Generated")
            return cv
        else:
            print("Could not generate PDF with PDFkit")
