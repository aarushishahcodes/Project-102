import os
import shutil

from_dir = "users/neha/downloads/assets"
to_dir = "users/neha/downloads/document_files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

list ['.txt', '.doc', '.docx', '.pdf']

if os.path.exists(path2):
    print("Moving " + file_name + ".....")

else:
    os.makedirs(path2)
    print("Moving " + file_name + ".....")
    shutil.move(path1, path3)