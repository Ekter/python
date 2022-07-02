from PyPDF4 import PdfFileMerger
from PyPDF4 import PdfFileReader
from PyPDF4 import PdfFileWriter
import os
import argparse


def modify_pdf(input_file: str, to_modify: str, modify_by: str, output_file: str):
    """
    Modify a PDF file and save the result into the `output_file`.
    """
    # strict = False -> To ignore PdfReadError - Illegal Character error
    pdfObj = open(input_file, 'rb')
    reader = PdfFileReader(pdfObj,strict=False)
    writer = PdfFileWriter()
    print(reader)
    print(reader.documentInfo)




    # bookmark_name = os.path.splitext(os.path.basename(input_file))[0]
    # reader.
    # merger.append(fileobj=open(input_file, 'rb'), pages=page_range,import_bookmarks=False, bookmark=bookmark_name)
    # # Insert the pdf at specific page
    # merger.write(fileobj=open(output_file, 'wb'))
    # merger.close()


def parse_args():
    """Get user command line parameters"""
    parser = argparse.ArgumentParser(description="Available Options")
    parser.add_argument('-i', '--input_file', dest='input_file', 
                        type=str, required=True, help="Enter the path of the file to process")
    parser.add_argument('-t', '--to_modify', dest='to_modify', 
                        type=str, required=True, help="sting to search and remplace")
    parser.add_argument('-m', '--modify_by', dest='modify_by', 
                        type=str, required=True, help="string to replace")

    parser.add_argument('-o', '--output_file', dest='output_file',
                        required=True, type=str, help="Enter a valid output file")
    # To Porse The Command Line Arguments
    args = vars(parser.parse_args())
    # To Display The Command Line Arguments
    print("## Command Arguments #################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in args.items()))
    print("######################################################################")
    return args


if __name__ == "__main__":
    # Parsing command line arguments entered by user
    args = parse_args()
    # call the main function
    modify_pdf(**parse_args())
