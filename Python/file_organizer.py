import os
import shutil

def organize_files(folder_path):
    # Get all files in the folder
    files = os.listdir(folder_path)

    for file in files:
        # Get the full path of the file
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            # Get the file extension
            _, ext = os.path.splitext(file)

            # Create a directory for the file extension if it doesn't exist
            if not os.path.exists(os.path.join(folder_path, ext[1:])):
                os.mkdir(os.path.join(folder_path, ext[1:]))

            # Move the file to the appropriate directory
            destination = os.path.join(folder_path, ext[1:], file)
            shutil.move(file_path, destination)
            print(f"Moved {file} to {destination}")

# Provide the folder path to organize
folder_path = "./OS"
organize_files(folder_path)
