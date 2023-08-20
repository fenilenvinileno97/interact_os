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
def create_directory(path, category):
    new_dir = f'{category.replace(".", "")}'
    new_dir_path = os.path.join(path, new_dir)
    os.makedirs(new_dir_path, exist_ok=True)
    return f'./{new_dir}'

#this function matches files found in return_extension with a known file category 
def set_dir_matches(from_cwd, list_of_extensions):
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

#this function moves files into recently created directories
def chdir(path, ext_dict):
    path = os.path.abspath(path)
    for filename in os.listdir(path):
        for ext, dir in ext_dict.items():
            if filename.lower().endswith(ext):
                create_directory(path, dir)
                current_path = os.path.join(path, filename)
                new_path = os.path.join(os.path.dirname(current_path), dir+'/'+filename)
                os.rename(current_path, new_path)
               
def run():
    extensions = {'Multimedia' : ['.mp3', '.mp4', '.png', '.bmp'], 
                  'Office': ['.docx', '.xslx', '.ppt', '.txt', '.csv'],
                  'Code': ['.py', '.js', '.php']
                  }
    pathway = './example_folder'
    from_cwd = return_extension(pathway)
    found_matches = set_dir_matches(from_cwd, extensions)
    chdir(pathway, found_matches)

    
if __name__ == '__main__':
    run()