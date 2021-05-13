from util import random_string

import os
import shutil

remove_file=False

source=input('Enter a source directory: ')
if (os.path.exists(source)==False):
    print("Source directory not find, exiting app. Bye")
    exit()    
    
destination=input('Enter a target directory: ')

if not destination:
    question=input("Do you want to copy the files in the same folder? (Y/N)")
    if question=='N':    
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
        

remove_and_delete=input('Do you want to remove the original file after renaming? (Y/N)')

if remove_and_delete == 'Y':
    remove_file=True

with os.scandir(source) as entries:
    for entry in entries:
        str_random=random_string.id_generator(12)
        if entry.is_file():
            renamed_file = str_random + '__' + entry.name
            shutil.copy(source + "/" + entry.name, destination + "/" +renamed_file)
            if remove_file==True and os.path.isfile(source + "/" + entry.name):
                os.remove(source + "/" + entry.name)
                                    

