#!/usr/bin/env python3

import os
import re
import subprocess

def check_ext(ext):
    command = f'find *{ext}'
    result = subprocess.run(command, capture_output=True, shell=True)
    return re.search(r"\.\w+", result.stdout.decode())[0]

def create_directory(ext_name):
    new_dir = f'{ext_name.replace(".", "")}'
    os.makedirs(f'./{new_dir}', exist_ok=True)
    return f'./{new_dir}'

def extract_ext(path):
    empty = []
    for k in os.listdir(path):
        empty.append(check_ext(k))
    return empty

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
                new_dir = create_directory(dir)
                os.rename(filename, new_dir)
                
        
def run():
    extensions = {'Multimedia' : ['.mp3', '.mp4', '.png', '.bmp'], 
                  'Office': ['.docx', '.xslx', '.ppt', '.txt', '.csv'],
                  'Code': ['.py', '.js', '.php']
                  }

    ext_list_in_cwd = set(extract_ext('./'))
    searched_matches = search_matches(ext_list_in_cwd, extensions)
    chdir('./', searched_matches)
    # print(list(searched_matches.values()))

if __name__ == '__main__':
    run()