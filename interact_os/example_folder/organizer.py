#!/usr/bin/env python3

import os
import re
import subprocess

def check_files(ext):
    command = f'find *{ext}'
    result = subprocess.run(command, capture_output=True, shell=True)
    return re.search(r"\.\w+", result.stdout.decode())[0]
    # return result.stdout.decode()
    
def create_directory(ext_name):
    new_dir = f'{ext_name.replace(".", "")}'
    os.makedirs(f'./{new_dir}', exist_ok=True)
    
def extract_ext(ext_list):
    empty = []
    for items in ext_list.values():
        for values in items:
            empty.append(check_files(values))
    return empty

def run():
    extensions = {'Multimedia' : ['.mp3', '.mp4', '.png', '.bmp'], 
                  'Office': ['.docx', '.xslx', '.ppt', '.txt', '.csv'],
                  'Code': ['.py', '.js', '.php']
                  }
    # ext_file = input('Enter a file extension: ')
    # extension_fits = False
    # for key in extensions:
    #     if ext_file in extensions[key]:
    #         create_directory(key)
    #         extension_fits = True
    # if not extension_fits:
    #     create_directory('Miscellaneous')
    
    # for i in extract_ext(extensions):
    #     extension_fits = False
    #     for key in extensions:
    #         if i in extensions[key]:
    #             create_directory(key)
    #             extension_fits=True
    #     if not extension_fits:
    #         print('This does not belong')
    
    print(extract_ext())
            
if __name__ == '__main__':
    run()