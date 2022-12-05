import os
import zipfile

filenames = ["__init__.py"]

ignorelist = ["__pycache__"]


def get_all_files_in_folder(path):
    retval = []

    for folder_name, sub_folders, file_names in os.walk(path):
        for file_name in file_names:
            path = folder_name + "/" + file_name

            ignored = False
            for string in ignorelist:
                if string in path:
                    ignored = True

            if not ignored:
                retval.append(path)

    return retval


archive = zipfile.ZipFile("multiedit.zip", mode="w")
archive.write("icon_hr.png", "resources/icon.png")
archive.write("__init__.py", "plugins/__init__.py")
archive.write("multiedit.py", "plugins/multiedit.py")
archive.write("icon.png", "plugins/icon.png")
archive.write("metadata.json", "metadata.json")

for path in get_all_files_in_folder("src"):
    archive.write(path, "plugins/" + path)

for path in get_all_files_in_folder("resources"):
    archive.write(path, "plugins/" + path)
    


