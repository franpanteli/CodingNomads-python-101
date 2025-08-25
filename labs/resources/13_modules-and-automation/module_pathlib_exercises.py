# Import pathlib
import pathlib

# Find the path to my Desktop
path = pathlib.Path.cwd()  # Returns the path of your current working directory, can be converted to a string

# List all the files on there
print("FILES IN CWD: %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
for filepath in path.iterdir(): #prints the directories of the files which are in the current working directory
    print(filepath.name) #unless the .name method is added - and then it's the filename
        #this is an attribute, not a method
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

path_to_desktop = pathlib.Path("/Users/francescapanteli/Desktop/").name #.name only shows the path to the folder
print("Path to Desktop:",path_to_desktop)
#listing all the files on the Desktop

path_to_desktop = pathlib.Path("/Users/francescapanteli/Desktop/")
print("DESKTOP FILES: %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
for filepath in path_to_desktop.iterdir():
    print("1", filepath.name) #the name of the file
    print("2", filepath.suffix) #the name of the file extension, e.g txt
    print("3", filepath.is_dir()) #if it's a directory
    print("4", filepath.parent) #the path of the directory above the current one
    print("5", filepath.stem) #the name of the directory (not the path) where the file is coming from
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

# Filter for screenshots only

# Create a new folder

# Move the screenshots in there



