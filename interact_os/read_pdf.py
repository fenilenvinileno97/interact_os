#!/usr/bin/env python3

import sys
import os
# from pypdf import PdfReader

def files_to_convert():
    filepath = sys.argv[1]
    return filepath

def get_output_filename():
    filename = str(input('Please enter a filename: \n'))
    return filename

def change_filename_ext(filename, ext):
    root, _ = os.path.splitext(filename)
    new_filename = root + ext
    os.rename(filename, new_filename)

def create_text(file, filename):
    try:
        reader = PdfReader(file)
        pages = [x for x in reader.pages]
        with open(filename, 'w', encoding='utf-8') as f:
            for key in pages:
                f.writelines(key.extract_text(0))
    except Exception as PDFormatError:
        print(f'{PDFormatError}: Please use a valid .PDF file!')
            
def run():
    filepath = files_to_convert()
    # filename = get_output_filename()
    # create_text(filepath, filename)
    # change_filename_ext(filename, '.txt')
    print(filepath)
            
if __name__ == '__main__':
    run()