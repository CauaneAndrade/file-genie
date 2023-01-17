import os
import shutil

def rename_and_organize(directory):
    # Get a list of all files in the directory
    files = os.listdir(directory)
    
    # Iterate through each file
    for file in files:
        # Get the file name and extension
        file_name, file_ext = os.path.splitext(file)
        
        # Rename the file using a specified naming convention
        new_file_name = file_name.replace(" ", "_") + file_ext
        os.rename(os.path.join(directory, file), os.path.join(directory, new_file_name))
        
        # Move the file to a specified subfolder based on file extension
        if file_ext in [".jpg", ".jpeg", ".png"]:
            shutil.move(os.path.join(directory, new_file_name), os.path.join(directory, "images"))
        elif file_ext in [".doc", ".docx"]:
            shutil.move(os.path.join(directory, new_file_name), os.path.join(directory, "documents"))
        elif file_ext in [".mp3", ".wav"]:
            shutil.move(os.path.join(directory, new_file_name), os.path.join(directory, "audio"))
        else:
            shutil.move(os.path.join(directory, new_file_name), os.path.join(directory, "other"))

if __name__ == "__main__":
    # Prompt user for directory to organize
    directory = input("Enter directory path to organize: ")
    rename_and_organize(directory)
    print("Files in the directory have been successfully renamed and organized.")
