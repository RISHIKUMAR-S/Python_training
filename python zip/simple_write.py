# importing required modules
from zipfile import ZipFile
import os

# writing files to a zipfile
with ZipFile('my_python_files.zip','w') as zip:
    zip.write('hi.txt')
