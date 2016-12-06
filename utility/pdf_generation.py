import pdfkit

"""
Uses pdfkit (Python wrapper on webkit framework) to generate a PDF from the results.html file
"""

# My local path to executable wkhtmltopdf
path_wkthmltopdf = '/usr/local/bin/wkhtmltopdf'
# Must use bytes not str/textIO to avoid a pdfkit encoding error
config = pdfkit.configuration(wkhtmltopdf=bytes(path_wkthmltopdf, 'utf-8'))


def generate_pdf(professor_name):
    with open('results.html') as f:
        pdfkit.from_file(f, '{0}.pdf'.format(professor_name), configuration=config)
