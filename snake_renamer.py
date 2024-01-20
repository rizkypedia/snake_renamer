import os
import shutil
from datetime import datetime, timezone, timedelta
from time import time
from util import random_string



source=input('Enter a source directory: ') or 'N/A'

if (source == 'N/A'):
    print('No directory provided, exiting programm')
    exit()
   
if (os.path.exists(source)==False):
    print("Source directory not find, exiting app. Bye")
    exit()    
    
destination=input('Enter a target directory: ')

if not destination:
    question=input("Do you want to move the files in the same folder? (y) ") or 'y'
    if question=='n':    
        destination=input('Plaese enter a target directory: ')
        if (os.path.exists(destination)==False):
            print("destination directory not find, exiting app. Bye")
            exit()        
    else:
        destination = source
        print("Source will be used as target directory")
else:
    if (os.path.exists(destination)==False):
        print("destination directory not find, exiting app. Bye")
        exit()  
        

keep_original_name=input('Do you want to keep the original name as suffix? (y) ') or 'y'

prefix = input('Define a file prefix for the filename e. g. MyFotos: ') or 'MyFotos'

with os.scandir(source) as entries:
    for entry in entries:
        if entry.name == '.DS_Store':
            continue
        if entry.is_file():
            suffix = (datetime.now(timezone.utc) + timedelta(days=3)).timestamp() * 1e3
            renamed_file = prefix + '__' + str(suffix).replace('.','') + '__' + entry.name
            if keep_original_name =='n':
                filename, filextension = os.path.splitext(entry.name)
                renamed_file = prefix + '__' + str(suffix).replace('.','') + filextension
            shutil.move(source + "/" + entry.name, destination + "/" + renamed_file)

