import re
import shutil
import os

def move_files(source_folder, destination_folder):
    pattern = r"^score_\d+\.svg$"
    for file in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file)
        if os.path.isfile(file_path) and re.match(pattern, file):
            destination_path = os.path.join(destination_folder, file)
            shutil.move(file_path, destination_path)

    # Rename the destination folder
    folder_name = os.path.basename(source_folder)
    new_folder_path = os.path.join(os.path.dirname(destination_folder), folder_name)
    os.rename(destination_folder, new_folder_path)


# Specify the destination folder path
base_path = r"D:\user\Ioakeim Sogiakas\Music\MusicCrack\Scores"
destination_folder = os.path.join(base_path, "svg_files")

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Assuming the program is located in the 'src' folder
program_path = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(program_path, "src")

for folder_name in os.listdir(src_path):
    folder_path = os.path.join(src_path, folder_name)
    if os.path.isdir(folder_path):
        move_files(folder_path, destination_folder)

# Delete the contents of the src folder and its subdirectories
for root, dirs, files in os.walk(src_path, topdown=False):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        os.remove(file_path)
    for dir_name in dirs:
        dir_path = os.path.join(root, dir_name)
        os.rmdir(dir_path)

print("Files moved, folders renamed, and src folder contents deleted successfully.")