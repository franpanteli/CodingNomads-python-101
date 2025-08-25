# Write a script that searches a folder you specify (as well as its subfolders, up
# to two levels deep) and compiles a list of all `.jpg` files contained in there.
# The list should include the complete path of each `.jpg` file.
# 
# You should train:
# 
# - Using `for` loops
# - Using conditional statements
# - Working with `pathlib`
# - Thinking about nested loops
#
# If you are feeling bold, create a list containing each type of file extension
# you find in the folder.
# Start with a small folder to make it easy to check whether your program is
# working correctly. Then search a bigger folder.
# This program should work for any specified folder on your computer.

#FOR THIS SCRIP TO WORK, YOU HAVE TO BE CD'D INTO THE TEST FOLDER IN THE TERMINAL
#module imports
import pathlib
from pathlib import Path

#the path with the file structure we want to sweep through
test_folder = pathlib.Path('/Users/francescapanteli/Desktop/CodingNomads-python-101/codingnomads/projects/filesearch/test_folder')

#iterate through the folders in the test folder
file_extensions = "" #a list of file extensions
for folder in test_folder.iterdir(): #we are iterating through the folders in the test folder
    #we don't hit a folder
    if folder.is_dir() == False:
        if folder.is_dir() == False:
            file_extensions += folder.suffix

    if folder.is_dir(): #if the we are iterating through a folder
        print(f"The .jpg files in the {test_folder.name} folder on the first and second levels are (if any): ")
        for file in folder.iterdir(): #a folder can be a part of this
            if file.name[-4:] == ".jpg":
                print(file.name)

            if file.is_dir():
                nested_folder = file
                for nested_file in nested_folder.iterdir():
                    if nested_file.name[-4:] == ".jpg":
                        print(nested_file.name)
                    if nested_file.is_dir() == False:
                        file_extensions += nested_file.suffix

            if file.is_dir() == False:
                file_extensions += file.suffix

print(" ")
print(file_extensions)
print(file_extensions)
file_extension_return = ""

if ".pdf" in file_extensions:
    file_extension_return += ", .pdf"

if ".xml" in file_extensions:
    file_extension_return += ", .xml"

if ".jpg" in file_extensions:
    file_extension_return += ", .jpg"

if ".png" in file_extensions:
    file_extension_return += ", .png"

if ".txt" in file_extensions:
    file_extension_return += ", .txt"

print("This is a list of file extensions which are contained in the folder and nested folder - up to two levels down in the file tree:", file_extension_return[2:])
