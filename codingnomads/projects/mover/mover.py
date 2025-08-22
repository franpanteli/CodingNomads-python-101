# Write a script that moves all files with the .png extension
# from one folder to another

# Import pathlib
import pathlib
from pathlib import Path

# The path where we want to create the new folder
folder_directory = pathlib.Path('/Users/francescapanteli/Desktop/CodingNomads-python-101/codingnomads/projects/not_done/mover/moving_files')

# Create a new folder
new_folder = folder_directory / "png_files" #the directory of the folder we want to create - we
                                            #are adding a new section to the previous directory
new_folder.mkdir(exist_ok=True) #create the new folder - allow it to exist
    #we first have the directory of the new folder, and then we create it

"""Now we have
        -> a folder with another folder inside it - with a standardised name
        -> the larger folder has .png files in it
        -> we want to iterate through the files in the larger folder and find the ones with .png
    """

# Filter for screenshots only
"""-> we are looking through folder_directory and iterating for the files whose suffix is .png
    """

for file in folder_directory.iterdir():
    if file.suffix == ".png":
        # Create a new path for each file
        new_file_path = new_folder / file.name
        # Move the screenshot there
        file.rename(new_file_path)





