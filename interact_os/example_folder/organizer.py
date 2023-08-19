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
    
def extract_ext():
    empty = []
    for k in os.listdir():
        empty.append(check_ext(k))
    return empty

def search_matches(from_cwd, list_of_extensions):
    matches = []
    for item in from_cwd:
        ext_not_found = True
        for key, value in list_of_extensions.items():
            if item in value:
                ext_not_found=False
                break
        if ext_not_found:
            matches.append((item, 'Not a category'))
            
    for item in from_cwd:
        ext_found = True
        for key, value in list_of_extensions.items():
            if item in value:
                ext_found=False
                break
        if not ext_found:
            matches.append((item, key))
    return matches
def run():
    extensions = {'Multimedia' : ['.mp3', '.mp4', '.png', '.bmp'], 
                  'Office': ['.docx', '.xslx', '.ppt', '.txt', '.csv'],
                  'Code': ['.py', '.js', '.php']
                  }

    from_cwd = set(extract_ext())
    print(search_matches(from_cwd, extensions))

if __name__ == '__main__':
    run()