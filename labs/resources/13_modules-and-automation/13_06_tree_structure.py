# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.
import pathlib
from pathlib import Path

#the path with the file structure we want to sweep through
path_to_resources_folder = pathlib.Path('/Users/francescapanteli/Desktop/CodingNomads-python-101/codingnomads/resources')

for folder in path_to_resources_folder.iterdir(): #we are iterating through the folders in the resources folder
    if folder.is_dir(): #if the we are iterating through a folder
        print(" ")
        print(f"The .py files in the {folder.name} folder are (if any): ")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        for file in folder.iterdir():
            if file.name[-3:] == ".py":
                print(file.name)
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print(" ")