import os
import shutil

from_dir = "C:/Users/ramam/Downloads"
to_dir = "C:/Users/ramam/Downloads/Document_Files"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:
    name,ext = os.path.splitext(file_name)

    if ext == "":
        continue
    if ext in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir + "/" + file_name
        path2 = to_dir + "/" + "Document_Files"
        path3 = path2 + "/" + file_name

        if os.path.exists(path2):
            print("Moving " + file_name + "...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving " + file_name + "...")
            shutil.move(path1,path3)