#
# Converts PDF and PPTX files to XML.
#
# Author: Gabriel Ghiuzan
#

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import XMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io
import os


def convert_to_pdf(path_to_file, filename):
    rsrcmgr = PDFResourceManager()
    output = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = XMLConverter(rsrcmgr, output, codec=codec, laparams=laparams)
    file = open(path_to_file, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(file, pagenos, maxpages=maxpages, password=password, caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)

    xml_output = output.getvalue()

    # Creates and array in which the first index is the name of the file
    # and the second index is the extension of the file
    filename_and_extension = filename.split('.')

    # Takes only the name of the file and adds the .txt extension
    output_filename = filename_and_extension[0] + '.xml'

    # Stores the path of the file which will contain the converted file
    output_path = "information_retrieval_system/xml_files/" + output_filename

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    output_file = open(output_path, "w")
    output_file.write(xml_output)

    file.close()
    device.close()
    output.close()
    output_file.close()