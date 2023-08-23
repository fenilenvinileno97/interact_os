#!/usr/bin/env python3

import re

def rearrange_name(name):
    #Kennedy, John F.
    pattern = r"(^[\w ?.]*), ([\w ?.]*)$"
    result = re.search(pattern, name)
    if result is None:
        return name
    return f"{result[2]} {result[1]}"

def run():
    name = input('Enter a name: ')
    print(rearrange_name(name))
    
if __name__ == '__main__':
    run()