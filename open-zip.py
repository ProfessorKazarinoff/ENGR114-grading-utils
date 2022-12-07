# open-zip.py
"""
a simple Python script to open and extract a Zip file.
"""

from zipfile import ZipFile
from pathlib import Path
  
# file to unzip
zip_file_path_str = "/Users/peter.kazarinoff/Downloads/Lab 7 Download Dec 6, 2022 500 PM.zip"
zip_file_path = Path(zip_file_path_str)

# directory to unzip into
out_dir_path = Path(zip_file_path_str.strip(".zip"))
out_dir_path.mkdir(parents=True, exist_ok=True)

# opening the zip file in READ mode
with ZipFile(zip_file_path, 'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()
  
    # extract all the files
    print('Extracting all the files now...')
    zip.extractall(out_dir_path)
    print('Done!')
