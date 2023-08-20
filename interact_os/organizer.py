#!/usr/bin/env python3

import os
import re
import subprocess

#this function has to extract extensions in a given directory
def return_extension(path):
    command = f"find {path} -maxdepth 1 -name '*'"
    result = subprocess.run(command, shell=True, capture_output=True)
    return set(re.findall(r"\.\w+", result.stdout.decode()))
 
#this function creates directories based on the file category    
def create_directory(category):
    new_dir = f'{category.replace(".", "")}'
    os.makedirs(f'./{new_dir}', exist_ok=True)
    return f'./{new_dir}'

def search_matches(from_cwd, list_of_extensions):
    matches = {}
    for item in from_cwd:
        ext_not_found = True
        for key, value in list_of_extensions.items():
            if item in value:
                ext_not_found=False
                break
        if ext_not_found:
            a, b = (item, 'Miscellaneous')
            matches[a] = b
            
    for item in from_cwd:
        ext_found = True
        for key, value in list_of_extensions.items():
            if item in value:
                ext_found=False
                break
        if not ext_found:
            a,b = (item, key)
            matches[a] = b
    return matches

def chdir(path, ext_dict):
    for filename in os.listdir(path):
        for ext, dir in ext_dict.items():
            if filename.lower().endswith(ext):
                print(filename, dir)
                
        
def run():
    extensions = {'Multimedia' : ['.mp3', '.mp4', '.png', '.bmp'], 
                  'Office': ['.docx', '.xslx', '.ppt', '.txt', '.csv'],
                  'Code': ['.py', '.js', '.php']
                  }
    print(return_extension('./example_folder'))
    print(return_extension('./'))
if __name__ == '__main__':
    run()