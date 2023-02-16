import os
import glob

# get the directory path from user input
dir_path = input("Enter the directory path: ")

# create a list of all .xls and .xlsx files in the directory
file_list = glob.glob(os.path.join(dir_path, '*.xls')) + glob.glob(os.path.join(dir_path, '*.xlsx'))

# loop through the file list and delete each file
for file_path in file_list:
    os.remove(file_path)