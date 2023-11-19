import os
import shutil

def organize_files(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_extension = filename.split('.')[-1]
            folder_path = os.path.join(directory, file_extension)

            # Create folder if it doesn't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Move the file to the corresponding folder
            shutil.move(os.path.join(directory, filename), os.path.join(folder_path, filename))

if __name__ == "__main__":
    folder_path = input("Enter the path of the directory to organize: ")

    if os.path.exists(folder_path):
        organize_files(folder_path)
        print("Files organized successfully.")
    else:
        print("Invalid directory path. Please provide a valid path.")
