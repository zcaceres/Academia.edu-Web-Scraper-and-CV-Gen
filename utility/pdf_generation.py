import pdfkit

"""
Uses pdfkit (Python wrapper on webkit framework) to generate a PDF from the results.html file
"""

def generate_pdf(professor_name):
    with open('results.html') as f:
        pdfkit.from_file(f, '{0}.pdf'.format(professor_name))